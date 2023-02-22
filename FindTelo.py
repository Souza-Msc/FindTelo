#Last Updated: 22 Feb 2023
#Author: Pedro Mendes de Souza; pedromsouza0@gmail.com
#Usage: python FindTelo.py
#Options: python FindTelo.py --help

from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from argparse import RawTextHelpFormatter,SUPPRESS
import argparse, re, os, sys


# Guide Msg

def guide_msg():
    return "\n\nExemple of usage: pyhton FindTelo.py -i example.fasta"

# Author info

def author_info(param):

	valid = 0

	author = ('\n\n\t Any comments or questions? Please email Pedro Souza (author) at'\
	' pedromsouza0@gmail.com\n\n')

	if param.author == True:
		print (author)
		valid += 1
	
	return valid

## Parses and Check 

def get_parameters():

    parser = argparse.ArgumentParser(description=
	'\n\n\nThis script will get the first and the last X number of nucleotides in each read/sequence from your file and compile a new file containing this information.'+guide_msg(), 
	usage=SUPPRESS,formatter_class=RawTextHelpFormatter)

    required_param_group = parser.add_argument_group('Required Options')

    required_param_group.add_argument('--input_file','-i', action='store',
	help="\n Sequences in a SeqRecord parseble format. More info https://biopython.org/wiki/SeqIO \n\n")

    optional_arg_group = parser.add_argument_group('Options')

    optional_arg_group.add_argument('--number','-n', default = '50',
	help="\n User-defined number of nucleotides to be collected from each read/sequence. Default= 50.\n\n")

    optional_arg_group.add_argument('-author', action='store_true',
	help=' \n Print author contact information \n\n')

    optional_arg_group.add_argument('--out_file', '-o', action='store', default= "FindTelo_out.fasta", help='\n User-defined out file name and format. Default: FindTelo_out.fasta\n')


    if len(sys.argv[1:]) == 0:
        print (parser.description)
        print ('\n')
        sys.exit()

    param = parser.parse_args()
	
    quit_eval = author_info(param)
    if quit_eval > 0:
        sys.exit()

    param = parser.parse_args()

    return param

def extract_ends(param):
    
    iDot = param.input_file.find('.')
    iType = param.input_file[(iDot+1):]

    oDot = param.out_file.find('.')
    oType = param.out_file[(oDot+1):]
    
    
    data = list(SeqIO.parse(param.input_file, iType))
    
    sequences = []

    for i in data:
        fw = i.seq[:int(param.number)]
        rv = i.seq[int(f"-{param.number}"):]
        full = fw + rv
        frag = SeqRecord(full)
        frag.id = i.id
        sequences.append(frag)

    SeqIO.write(sequences, param.out_file, oType)
    



def run():
    param = get_parameters()
    extract_ends(param)

run()
