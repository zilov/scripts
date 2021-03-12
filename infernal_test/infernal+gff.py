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


def infernal_runner(infernal_output, input_model, input_fasta):
    command = "cmsearch -o %s --cpu 1 %s %s" % (infernal_output, input_model, input_fasta)
    if not os.path.exists(infernal_output):
        os.system(command)
        print(command)
    else: print(infernal_output + " exists! Extracting GFF!")

        
def infernal_to_gff_runner(infernal_to_gff_path, infernal_output, output_gff):
    command = "%s -i %s -o %s" % (infernal_to_gff_path, infernal_output, output_gff)
    os.system(command)
    print(command)
    print("Done!")
   

def main(models, path)
    
    for model in models:
        model_prefix = model.split(".")[0]
        model = models_path + model
        for file in path:
            input_fasta = fasta_path + file
            input_fasta_prefix = file.split(".")[0]
            input_model = model
            output_path = "/home/dzilov/infernal_test/test_run/%s" % input_fasta_prefix
            if not os.path.exists(output_path):
                os.mkdir(output_path)
            output_gff = output_path + "/%s_%s.gff" % (input_fasta_prefix, model_prefix)
            infernal_output = output_gff.split(".gff")[0]

            infernal_runner(infernal_output, model, input_fasta)
            infernal_to_gff_runner(infernal_to_gff_path, infernal_output, output_gff)
        
                        

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Program description.')
    parser.add_argument('-i','--input', help='Output file of infernal cmsearch', required=True)
    parser.add_argument('-o','--output', help='Ouput gff file with rybozymes', required=True)
    args = vars(parser.parse_args())
    
    infernal_output = args["input"]
    gff_output = os.path.abspath(args["output"])


    settings = {
        "infernal_output": infernal_output,
        "gff_output": gff_output,
    }

    main(settings)
