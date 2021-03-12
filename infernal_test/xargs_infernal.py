#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#@created: <26.10.20>
#@author: <Danil Zilov/Alexey Komissarov>
#@contact: <zilov@scamt-itmo.ru/akomissarov@scamt-itmo.ru>

import sys
import argparse
import os
import os.path

def main():
    ''' Function description.
    '''
   
    models_dir = "/media/eternus1/nfs/projects/shared/rybozymes_models/"
    N = 0
    for cid, cm in enumerate(os.listdir(models_dir)):
        N += 1
        
    for cid, cm in enumerate(os.listdir(models_dir)):
        model = models_dir + cm
        command = 'ls /mnt/data/ncbi/refseq/bacteria_single/parsed_fa/ | grep fna | xargs -P 120 -I {} sh -c "cmsearch %s /mnt/data/ncbi/refseq/bacteria_single/parsed_fa/{} | /home/dzilov/infernal_test/infernal_to_gff.py"' % model
        print(cid,N,command)
        os.system(command)
    print("DONE!")              

if __name__ == '__main__':
  
    main()

    