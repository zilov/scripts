#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @created: 17.03.2021
# @author: Danil Zilov
# @contact: zilov.d@gmail.com

import argparse
import os.path


def read_fastq(fastq_open):
    head = fastq_open.readline().strip()
    if head == "":
        return False
    seq = fastq_open.readline().strip()
    strain = fastq_open.readline().strip()
    qual = fastq_open.readline().strip()
    head_n = int(head[1:].split()[0].split(".")[-1])
    return head, seq, strain, qual, head_n


def reads_number(fastq_file):
    reads_number = 0
    with open(fastq_file) as fh:
        for line in fh:
            reads_number += 1
    return int(reads_number / 4)


def reads_diff_finder(main_fastq_file, fastq_file_to_compare):
    """Returns generator with read ID and trimmed sequence"""

    main_file_len = reads_number(main_fastq_file)
    print(f"{main_file_len} reads in base fastq file!")

    proscock = False

    with open(main_fastq_file) as fh1:
        with open(fastq_file_to_compare) as fh2:
            for read in range(main_file_len):
                if not proscock:
                    head1, seq1, strain1, qual1, head1_n = read_fastq(fh1)
                    if head1 == False:
                        break
                    head2, seq2, strain2, qual2, head2_n = read_fastq(fh2)
                    if head2_n > head1_n:  # if read was filtered it won't looking forwrd
                        proscock = True
                        continue
                    elif head2_n == head1_n and seq1 != seq2:
                        diff = [head2, seq1.replace(seq2, "")]
                        yield diff
                        continue
                else:
                    head1, seq1, strain1, qual1, head1_n = read_fastq(fh1)
                    if head1 == False:
                        break
                    if head2_n > head1_n:  # if read was filtered it won't looking forwrd
                        proscock = True
                        continue
                    elif head2_n == head1_n:
                        if seq1 != seq2:
                            diff = [head2, seq1.replace(seq2, "")]
                            yield diff
                        proscock = False
                        continue


def main(settings):
    n_reads = 0
    with open(output_file, "w") as fw:
        for i in range(len(compared_reads)):
            print(f"Working with {compared_reads[i]}")

            raw_to_tool = reads_diff_finder(base_read, compared_reads[i])

            for header_and_seq in raw_to_tool:
                n_reads += 1
                if n_reads % 10000000 == 0:
                    print(n_reads, end=" ")
                header = header_and_seq[0][1:].split()[0] + f"_{tools_list[i]}"
                sequence = header_and_seq[1]
                fw.write(f">{header}\n{sequence}\n")
    print(f"{n_reads} were trimmed!")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Finds diffs between reads in two files and outputs it in fasta file')
    parser.add_argument('-b', '--base', help='Read file with which you are gonna compare', required=True)
    parser.add_argument('-o', '--output', help='output file in fasta format with trimmed reads', required=False,
                        default="")
    parser.add_argument('-c', '--compared', help='list of compared reads files like "./file1_1.fq ./file2_1.fq ..." ',
                        nargs='*', required=True)
    parser.add_argument('-t', '--toolslist', help='list of compared reads tools like "v2trim trimmomatic fastp ..."',
                        nargs='*', required=True)
    args = vars(parser.parse_args())

    base_read = os.path.abspath(args["base"])
    compared_reads = args["compared"]
    tools_list = args["toolslist"]

    if not args["output"]:
        file_name = os.path.basename(base_read).split(".")[0] + "_trimmed_parts.fasta"
        output_file = os.path.join(os.path.dirname(base_read), file_name)
    else:
        output_file = os.path.abspath(args["output"])

    settings = {
        "base_read": base_read,
        "compared_reads": compared_reads,
        "output_dir": output_file,
    }

    main(settings)
    print("DONE!")
    print(f"Output was written in {output_file}")
