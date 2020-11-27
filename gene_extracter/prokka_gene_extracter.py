#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#@created: <data>
#@author: <name>
#@contact: <email>

import sys
import argparse
import os
import os.path

def main(input_dir, outdirectory):
    ''' Function description.
    '''
    
    def fasta_reader(file):
        fasta = {}
        header = None
        with open(file) as fh:
            for i, line in enumerate(fh):
                line = line.strip()
                if line.startswith(">"):
                    if header:
                        fasta[header]="".join(seq)
                    header = line
                    seq = []
                else:
                    seq.append(line)
        if header:
            fasta[header] = "".join(seq)
        return fasta 

    def revcomp(seq):
        new_seq = ""
        for i in seq[::-1]:
            if i == "A":
                new_seq += "T"
            elif i == "T":
                new_seq += "A"
            elif i == "G":
                new_seq += "C"
            else:
                new_seq += "G"
        return new_seq
    
    path = os.path.abspath(input_dir)
    inp_dir_list = os.listdir(path)
    for i in inp_dir_list:
        if ".fna" in i:
            input_fasta = path + "/" + i
            print("INPUT FASTA FILE IS %s" % input_fasta)
        if ".gff" in i:
            input_gff = path + "/" + i
            print("INPUT GFF FILE IS %s" % input_gff)
           
        

    prefix = input_fasta.split("/")[-1].split(".")[0]
    outdir = outdirectory + "/" + prefix
    print("OUTPUT DIRECTORY IS %s" % outdir)
    out_file = outdir + "/" + prefix + "_genes_seq.txt"
    print("OUTPUT FILE IS %s" % out_file)
    
    if os.path.exists(outdir):
        pass
    else:
        os.mkdir(outdir)
    
    fasta = fasta_reader(input_fasta)
    
    #gff_reader
    i = 0
    with open(out_file, "w") as fw: 
        with open(input_gff) as fh:
            for line in fh:
                if line.startswith("#"):
                    continue
                if line.startswith(">"): # to read until fasta part starts
                    break
                line = line.strip().split("\t")
                if not "gene" in line[8]:
                    continue
                gene = line[8].split("gene")[1].split(";")[0][1:]
                contig = line[0]
                start = int(line[3])
                stop = int(line[4])
                strain = line[6]
                product = line[8].split(";")[-1]
                new_header = ">%s:%s:%s:%s:%s:%s" % (gene, prefix, contig, start, stop, product)
                i+=1
                for header, seq in fasta.items():
                    if header == ">" + contig:
                        fw.write(new_header + "\n")
                        if strain == "+":
                            fw.write(seq[start-1:stop] + "\n")
                        elif strain == "-":
                            fw.write(revcomp(seq[start-1:stop]) + "\n") #add reverce compliment
    fw.close()
    
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Prokka runner')
    parser.add_argument('-i','--input', help='path to prokka dir', required=True)
    parser.add_argument('-o','--outdir', help='output directory', required=True)
    parser.add_argument('-d','--dry', help='dry run', action='store_true')
    args = vars(parser.parse_args())
    
    input_dir = os.path.abspath(args["input"])
    outdirectory = os.path.abspath(args["outdir"])
    dry = args["dry"]
    
    if os.path.exists(outdirectory):
        pass
    else:
        os.mkdir(outdirectory)
    
    main(input_dir, outdirectory)
    print("DONE for path %s" % input_dir)
