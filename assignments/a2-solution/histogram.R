library(plotrix)
mementos <- read.table("C:/Users/bitto/Documents/GitHub/cs532-s17/assignments/a2-solution/timeMapCount_uniqueUrls_1000")
num_memento <- table(mementos)
max_num <- 20
xgap <- ifelse(num_memento > 900, num_memento-890, num_memento)
xat <- pretty(xgap)
xlab <- ifelse(xat > 10, xat+890, xat)
hist(xgap, axes=FALSE, breaks=max_num, main="Mementos Histogram", xlab="Instances", col="coral")

axis(1,at=xat,labels=xlab)
axis(2)
axis.break(1,11,style="slash")
