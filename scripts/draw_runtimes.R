library(ggplot2)

shm_timings <- read.csv(file="/scratch0/NOT_BACKED_UP/dbuchan/projects/blast_benchmark_results/shm_example_times.csv", header=TRUE, check.names=FALSE, strip.white = TRUE, sep=",",na.strings= c("999", "NA", " ", ""))
nvme_timings <- read.csv(file="/scratch0/NOT_BACKED_UP/dbuchan/projects/blast_benchmark_results/example_times.csv", header=TRUE, check.names=FALSE, strip.white = TRUE, sep=",",na.strings= c("999", "NA", " ", ""))
example_timings <- rbind(shm_timings, nvme_timings)

ggplot(subset(example_timings, !(protein=='titin')), aes(x=cores, y=time, group=protein, colour=protein))+geom_line(size=1.5)+facet_wrap(~location, scales="free")
ggsave("/scratch0/NOT_BACKED_UP/dbuchan/projects/blast_benchmark_results/runtimes_shm_vs_nvme.png", width=10, height=7, dpi=300)
concurrent_timings <- read.csv(file="/scratch0/NOT_BACKED_UP/dbuchan/projects/blast_benchmark_results/igal_concurrent_timing.csv", header=TRUE, check.names=FALSE, strip.white = TRUE, sep=",",na.strings= c("999", "NA", " ", ""))

batch_timings <- subset(concurrent_timings, (type == 'batch'))
batch_timings$seq<-NULL
colnames(batch_timings)<-c("concurrency", "type", "time")

core_timings <- subset(concurrent_timings, !(type == 'batch'))
colnames(core_timings)<-c("seq", "concurrency", "type", "time")

average_timings<-aggregate(time~concurrency, data=core_timings, mean, na.rm=TRUE)
average_timings$type<-"average"

concurrent_timings<-rbind(batch_timings, average_timings)

ggplot(concurrent_timings, aes(x=concurrency, y=time, group=type, colour=type))+geom_line(size=1.5)+geom_point(size=4)
ggsave("/scratch0/NOT_BACKED_UP/dbuchan/projects/blast_benchmark_results/concurrency_impact.png", width=10, height=7, dpi=300)

optimal_bulk_timings <- read.csv(file="/scratch0/NOT_BACKED_UP/dbuchan/projects/blast_benchmark_results/optimal_high_throughput.csv", header=TRUE, check.names=FALSE, strip.white = TRUE, sep=",",na.strings= c("999", "NA", " ", ""))
optimal_bulk_timings$min<-optimal_bulk_timings$time/60
optimal_bulk_timings$hours<-optimal_bulk_timings$min/60
ggplot(optimal_bulk_timings, aes(x=pool_size, y=hours))+geom_line(size=1.5)
ggsave("/scratch0/NOT_BACKED_UP/dbuchan/projects/blast_benchmark_results/bulk_runtime.png", width=10, height=7, dpi=300)

