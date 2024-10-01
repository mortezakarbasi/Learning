# S01 codes
# part 1
# working directory
getwd()
# changing working directory
# back slash is escape charater
setwd("D:\\selfstudy\\push_Learning")
setwd("D:/selfstudy/push_Learning")
# part 2
# arithmetic operations
1 + 1 
5 * 5
5 ** 2
5 ^ 2
5 / 2
## remainder
5 %% 2 # python 5 % 2
## integer division
5 %/% 2 # python 5 // 2
# logical operators
1 > 2
2 > 1
2 >= 2
2 <= 3
2 == 2
2 != 2
2 > 1 | 3 > 2
2 > 1 | 3 < 2
2 < 1 | 3 < 2
2 > 1 & 3 > 2
2 > 1 & 3 < 2
2 < 1 & 3 < 2
k <- x == 1 & y == 3
isTRUE(k)
# object
x = 1 
x <- 2
y <- 3
# vector (in vector all elements must be a same type)
z <- c(1,3,4,6,8)
zseq <- 1:100
zreverse <- 100:1
# list of objects
ls()
# remove objects
rm(k)
# save or load object

# quit and exit R
q()
#  finding library.Paths
.libPaths()
# part 3
# indexing objects
zreverse[1]
zreverse[2]
zreverse[40]
zreverse[c(40,60)]
# matrix
y = matrix(1:20, nrow=5, ncol=4)
y
dim(y)
y[2,2]
y[2,]
y[,3]
z = c(40,50,60,70)
y[3,] <- c(40,50,60,70)
z = c(40,'ali',50)
z
#  help
?functionname
?matrix
# history
history()
# package
install.packages("package name")
installed.packages()
# S02
