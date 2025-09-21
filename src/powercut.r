set.seed(599)
big_matrix <-  matrix(runif(10000000), 10000, 1000)

computation <-  tryCatch(
  read.csv("temp.txt", sep="\t", header = FALSE, row.names = 1),
  error = function(e) return(matrix(0, 0, 0)) # return an empty matrix if failed to read the file
)

# Now we have a computation matrix either it is empty or has actual results
for (x in max(1, row(computation) + 1) : ncol(big_matrix)) {
  x_corr <- cor(big_matrix[, x], big_matrix, use = "pair")
  cat(x_corr, sep = "\t", "\n", file = "temp.txt", append = TRUE)
  cat("Computation completed for column: ", x, "\n")
}
