friendcounts <- read.table("C:/Users/bitto/Documents/GitHub/cs532-s17/assignments/a4-solution/twitterCounts.txt")

orderedfriendcounts <- sort(friendcounts$V2)
mn <- mean(orderedfriendcounts)
nelson <- 622
cols <- c("aquamarine3", "brown4" )[(orderedfriendcounts == nelson) +1]

mp <- barplot(orderedfriendcounts, col= cols, border = cols, main="Friendship Paradox", xlab="Friend", ylab = "Num Friends", log = "y")
par(new =TRUE)
valueclosestindex <- which.min(abs(orderedfriendcounts - mn))
abline(v = mp[valueclosestindex], col = "aquamarine4")

std = sd(orderedfriendcounts)