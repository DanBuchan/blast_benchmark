import glob
import shlex
import subprocess
import pprint
from multiprocessing import Pool
import sys

pp = pprint.PrettyPrinter(indent=4)
# arg 1 : pool size
# arg 2 : directory
# arg 3 : ouput dir


def run_blast(file):
    seq_path = file[0:-6]
    print(seq_path)
    seq_name = seq_path.split("/")[-1]
    exe = "/usr/bin/time /usr/local/bin/psiblast"
    db = "/data/uniref/uniref90.fasta"
    for i in range(1, 11):
        cmd = exe+" -query "+file+" -out "+sys.argv[3]+seq_name+".bls -db " + \
              db+" -num_threads "+str(i)
        print("threads : "+str(i))
        p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        p.wait()
        print(seq_name+" : "+p.stderr.read().decode())


# fasta= open("pdb_2015.fasta", "w")
p = Pool(int(sys.argv[1]))
p.map(run_blast, glob.glob(sys.argv[2]+"*.fasta"))
