library(ggplot2)

shm_timings <- read.csv(file="/home/dbuchan/projects/blast_benchmark_results/shm_example_times.csv", header=TRUE, check.names=FALSE, strip.white = TRUE, sep=",",na.strings= c("999", "NA", " ", ""))
nvme_timings <- read.csv(file="/home/dbuchan/projects/blast_benchmark_results/example_times.csv", header=TRUE, check.names=FALSE, strip.white = TRUE, sep=",",na.strings= c("999", "NA", " ", ""))
example_timings <- rbind(shm_timings, nvme_timings)

ggplot(subset(example_timings, !(protein=='titin')), aes(x=cores, y=time, group=protein, colour=protein))+geom_line(size=1.5)+facet_wrap(~location, scales="free")

concurrent_timings <- read.csv(file="/home/dbuchan/projects/blast_benchmark_results/igal_concurrent_timing.csv", header=TRUE, check.names=FALSE, strip.white = TRUE, sep=",",na.strings= c("999", "NA", " ", ""))

batch_timings <- subset(concurrent_timings, (type == 'batch'))
batch_timings$seq<-NULL
colnames(batch_timings)<-c("concurrency", "type", "time")

core_timings <- subset(concurrent_timings, !(type == 'batch'))
colnames(core_timings)<-c("seq", "concurrency", "type", "time")

average_timings<-aggregate(time~concurrency, data=core_timings, mean, na.rm=TRUE)
average_timings$type<-"average"

concurrent_timings<-rbind(batch_timings, average_timings)

ggplot(concurrent_timings, aes(x=concurrency, y=time, group=type, colour=type))+geom_line(size=1.5)+geom_point(size=4)