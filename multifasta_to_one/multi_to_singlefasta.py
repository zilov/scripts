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

def main(input_multifasta):
    ''' Function description.
    '''
    # находим айдишки в мультифасте, записываем в список

    fasta = {}
    header = None
    with open(input_multifasta) as fh:
        for i, line in enumerate(fh):
            line = line.strip()
            if line.startswith(">") and header != line[1:8]:
                if header != None:
                    fasta[header]="\n".join(seq)
                header = line[1:8]
                seq = [line]
            else:
                seq.append(line)
    if header:
        fasta[header] = "\n".join(seq)
    
    for key, value  in fasta.items():
        file_name = os.path.join("/mnt/data/ncbi/refseq/bacteria_single", "%s.fna" % key)
        with open(file_name, "w") as fw:
            fw.write(value)
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Multifasta reader/writer')
    parser.add_argument('-i','--input', help='whole path to multifasta file', required=True)
    args = vars(parser.parse_args())
    
    input_multifasta = os.path.abspath(args["input"])
    
    main(input_multifasta)
    print("DONE for file %s" % input_multifasta)
