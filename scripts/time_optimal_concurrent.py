import glob
import shlex
import subprocess
import pprint
from multiprocessing import Pool
import sys
import time

# Time blast as we increase the number of cores over the core test set


pp = pprint.PrettyPrinter(indent=4)
# arg 1 : pool size
# arg 2 : directory
# arg 3 : ouput dir


def run_blast(file):
    seq_path = file[0:-6]
    # print(seq_path)
    seq_name = seq_path.split("/")[-1]
    exe = "/usr/local/bin/psiblast"
    # db = "/data/uniref/uniref90.fasta"
    db = "/data/uniref/uniref90.fasta"
    cmd = exe+" -query "+file+" -out "+sys.argv[3]+seq_name+".bls -db " + \
        db+" -num_threads 2"
    p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    p.wait()


# fasta= open("pdb_2015.fasta", "w")
p = Pool(int(sys.argv[1]))
print("pool_size,time")
sys.stdout.flush()
for i in range(22, 26):
    start_time = time.time()
    p.map(run_blast, glob.glob(sys.argv[2]+"*.fasta"))
    end_time = time.time()
    batch_time = end_time - start_time
    print(str(i)+","+str(batch_time))
    sys.stdout.flush()
