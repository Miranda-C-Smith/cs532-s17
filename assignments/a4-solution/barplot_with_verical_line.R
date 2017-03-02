friendcounts <- read.table("C:/Users/bitto/Documents/GitHub/cs532-s17/assignments/a4-solution/facebookFriendCount.txt")

orderedfriendcounts <- sort(friendcounts$V1)
mn <- mean(orderedfriendcounts)
nelson <- 154
cols <- c("aquamarine3", "brown4" )[(orderedfriendcounts == nelson) +1]

mp <- barplot(orderedfriendcounts, col= cols, border = cols, main="Friendship Paradox", xlab="Friend", ylab = "Num Friends")
par(new =TRUE)
valueclosestindex <- which.min(abs(orderedfriendcounts - mn))
abline(v = mp[valueclosestindex], col = "aquamarine4")