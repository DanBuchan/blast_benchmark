import glob
import subprocess
import pprint
from multiprocessing import Pool
import sys

pp = pprint.PrettyPrinter(indent=4)
# arg 1 : pool size
# arg 2 : directory
# arg 3 : ouput dir


def run_blast(file):
    seq_name = file[0:-6]
    print(seq_name)
    exe = "/usr/bin/time /usr/local/bin/psiblast"
    db = "/data/uniref/uniref90.fasta"
    stdout = subprocess.Popen([exe, "-query", file, "-out",
                              sys.argv[3]+"/"+seq_name+".bls", "-db", db],
                              stdout=subprocess.PIPE)
    print(seq_name+" : "+str(stdout))


# fasta= open("pdb_2015.fasta", "w")
p = Pool(int(sys.argv[1]))
p.map(run_blast, glob.glob(sys.argv[2]+"*.fasta"))
