# Learning

## Python

### Zarchi

## R

### Noorbaksh
#### S10 

```
# open and read data
read.csv(file.choose(),header = T)
# checking class and data dimension
class(a)
dim(a)
# file chekcing
rownames(a) = a[,1]
View(a)
rownames(a) = a[,-1]
a = a[,-1]
at = t(a)
# drawing box plot
at = as.data.frame(at)
boxplot(at)
# trimming data to have better box plot
boxplot(at, col = 3, main = "box plot of microarray", xlab= "list of cases", ylab = "expression levels")
boxplot(at, ylim = c(0,500))
boxplot(at, col = 3, main = "box plot of microarray", xlab= "list of cases", ylab = "expression levels", ylim = c(0,500))
b = log2(at)
boxplot(b)
min(at)
c = at + 1 # if we have zero in our data, log(0) = infinity so we have to add all of our data with one 
c = log2(c)
min(c)
boxplot(c)
heatmap(c)
class(c)
cm = as.matrix(c)
heatmap(cm)
heatmap(t(cm))
heatmap(a)
am = as.matrix(a)
heatmap(am)
heatmap(cm)
# install package
# install from tool menu
# install.packages('pheatmap')
library(pheatmap)
pheatmap(am)
pheatmap(cm)
pheatmap(log2(a+1))
```
##