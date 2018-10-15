setwd("/Users/john/Projects/Notes-Intro-to-Stat-Learning/")

# Header file with abstract
top <- "/Users/john/Projects/Intro to Stat Learning/header.tex"

# Document text
doc <-  "/Users/john/Projects/Intro to Stat Learning/notes.txt"

# Merge config file
system("cat header.tex notes.txt > Notes-Intro-to-Stat-Learning.tex")

write(paste0("\\end{document}"), "Notes-Intro-to-Stat-Learning.tex", append = TRUE)

# Compile pdf
system("pdflatex Notes-Intro-to-Stat-Learning.tex")

# Remove Latex Files
system("rm Notes-Intro-to-Stat-Learning.tex")
system("rm Notes-Intro-to-Stat-Learning.log")
system("rm Notes-Intro-to-Stat-Learning.aux")

