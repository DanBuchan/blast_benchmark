Scripts for running benchmark and stress test on our new blastmachine.

example_sequences/ : a set of specific sequences representing some classic example_sequences

random_sequences/ : 1,300 sequences submitted to the PSIPRED webserver since 2008

# Test psiblast
/usr/local/bin/psiblast -query example_sequences/1ga1C.fasta -out tests.bls -db /data/uniref/uniref90.fasta

peak memory: 12859124  ~12/13Gb

128Gb
48 cores


Run set of 1383 with 5 cores per process (10 concurrent)
Run set of 1383 with 1 core per process (10 concurrent)

run set of
