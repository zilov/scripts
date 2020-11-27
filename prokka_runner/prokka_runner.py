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

def main(input_fasta, outdirectory):
    ''' Function description.
    '''
        
    prefix = input_fasta.split("/")[-1].split(".")[0]
    outdir = outdirectory + "/" + prefix
    
    command = "prokka --quiet --cpus 20 --outdir %s --prefix %s %s" % (outdir, prefix, input_fasta)
    print(command)
    if not dry:
        os.system(command)
    
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Prokka runner')
    parser.add_argument('-i','--input', help='whole path to fasta file', required=True)
    parser.add_argument('-o','--outdir', help='output directory', required=True)
    parser.add_argument('-d','--dry', help='run without running prokka', action='store_true')
    args = vars(parser.parse_args())
    
    input_fasta = os.path.abspath(args["input"])
    outdirectory = os.path.abspath(args["outdir"])
    dry = args["dry"]
    
    main(input_fasta, outdirectory)
    print("DONE for file %s" % input_fasta)
