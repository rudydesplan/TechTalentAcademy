#Exercie 1

vector_a <- c(1, 2, 3, 4, 5)
vector_b <- c(6, 7, 8, 9, 10)
vector_c <- c(11, 12, 13, 14, 15)

threevmatrix <- matrix(c(vector_a, vector_b, vector_c), nrow = 5, byrow = FALSE)
#print(threevmatrix)

#2.
name <- c("Francois", "Pierre", "Jean", "Jordan", "Stephen")
age <- c(20, 25, 30, 35, 40)
role <- c("Employee1", "Employee2", "Manager", "Director", "CEO")
length_of_service <- c(1, 2, 3, 4, 5)

employeedf <- data.frame(name, age, role, length_of_service)
#print(employeedf)

#3.
library("ggplot2")

x <- 1:20
y <- x^2
qplot(x, y, xlab = "x", ylab = "x^2", main = "f(x) = x^2")

#4.
barplot(age, xlab = "name", ylab = "age", names.arg = name)

#5.
#6.
sequence <- 20:50
avg <- mean(c(sequence))
#print(avg)
sum <- sum(c(sequence))
#print(sum)
