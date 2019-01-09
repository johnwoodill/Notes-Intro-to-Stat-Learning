pwd <- getwd()
setwd(pwd)

# Header file with abstract
top <- paste0(pwd, "/header.tex")

# Document text
doc <-  paste0(pwd, "/notes.txt")

# Merge config file
system("cat header.tex notes.txt > Notes-Hands-On-ML-with-scikit-learn-and-TF.tex")

write(paste0("\\end{document}"), "Notes-Hands-On-ML-with-scikit-learn-and-TF.tex", append = TRUE)

# Compile pdf
system("pdflatex Notes-Hands-On-ML-with-scikit-learn-and-TF.tex")

# Remove Latex Files
system("rm Notes-Hands-On-ML-with-scikit-learn-and-TF.tex")
system("rm Notes-Hands-On-ML-with-scikit-learn-and-TF.log")
system("rm Notes-Hands-On-ML-with-scikit-learn-and-TF.aux")
