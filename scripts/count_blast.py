import glob
import shlex
import subprocess
from multiprocessing import Pool, Lock, Value
import sys
import time
import random


# arg 1 : pool size
# arg 2 : input directory
# arg 3 : ouput directory
# arg 4 : time in hours to run blasts
# arg 5 : sequence 'same' or 'random'

#assign arguments
POOL_SIZE = int(sys.argv[1])
INPUT = sys.argv[2]
OUTPUT = sys.argv[3]
RUN_TIME = float(sys.argv[4])
RAND_SEQ = True if sys.argv[5] == 'random' else False

#initialize job counter and lock
jobs = Value('i', 0)
lock = Lock()


def run_blast(file):
    global jobs
    global lock
    exe = "/usr/local/bin/psiblast"
    db = "/data/uniref/uniref90.fasta"
    cmd = exe+" -query "+file+" -out out.xml -out_pssm out.pssm -db " + \
              db+" -outfmt 5 -inclusion_ethresh 0.001 -num_iterations 3 -num_alignments 1 -num_threads 1"
    p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    with lock:
        jobs.value += 1


#create pool
p = Pool(POOL_SIZE)
#get all fasta files
files = glob.glob(INPUT+"*.fasta")
num_files = len(files)

#execute for given time
timeout = time.time() + RUN_TIME*3600
if RAND_SEQ:   
    while time.time() < timeout:
        try:
            #select a random sample of files to fill the pool
            rand_files = random.sample(files, POOL_SIZE)
            p.map(run_blast, rand_files)
        except ValueError:
            print("Pool size must be less than or equal to number of files")
else:
    while time.time() < timeout:
        p.map(run_blast, [files[0]] * POOL_SIZE)


print("Jobs completed: "+str(jobs.value)+"\nExcess time: "+str(time.time() - timeout))


