import glob
import shlex
import subprocess
import pprint
from multiprocessing import Pool
import sys
import time

pp = pprint.PrettyPrinter(indent=4)
# arg 1 : ouput dir
# arg 2 : max concurrency (48)


def run_blast(file):
    seq_path = file[0:-6]
    # print(seq_path)
    seq_name = seq_path.split("/")[-1]
    exe = "/usr/bin/time /usr/local/bin/psiblast"
    # db = "/data/uniref/uniref90.fasta"
    db = "/data/uniref/uniref90.fasta"

    cmd = exe+" -query "+file+" -out "+sys.argv[1]+seq_name+".bls -db " + \
        db+" -num_threads 1"
    p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    p.wait()
    print(seq_name+","+str(i)+","+p.stderr.read().decode())
    sys.stdout.flush()


seq = "/home/dbuchan/blast_benchmark/example_sequences/iga1C.fasta"
process_list = []

start_time = time.time()
print("seq,cores/concurrency,time_output,type")
# fasta= open("pdb_2015.fasta", "w")
for i in range(5, int(sys.argv[2])+1):
    start_time = time.time()
    process_list += i * [seq]
    p = Pool(i)
    p.map(run_blast, process_list)

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))
