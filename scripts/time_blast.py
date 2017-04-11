import glob
from subprocess import call
import pprint
from multiprocessing import Pool
import sys

pp = pprint.PrettyPrinter(indent=4)
# arg 1 : pool size
# arg 2 : directory
# arg 3 : ouput dir
print(sys.argv[1])
exit(1)


def run_blast(file):
    seq_name = file[0:-6]
    print(seq_name)
    # exe = "/usr/local/bin/psiblast"
    # db = "/data/uniref/uniref90.fasta"
    # call([exe, "-query", file, "-out", sys.argv[3]+"/"+seq_name+".bls", "-db", db])


fasta_dir = "/cs/research/bioinf/home1/green/dbuchan/archive0/eigen_thread" \
            "/eigenthreader/seq_files/"
# fasta= open("pdb_2015.fasta", "w")
p = Pool(sys.argv[1])
p.map(run_blast, glob.glob(sys.argv[2]+"*.fasta"))
