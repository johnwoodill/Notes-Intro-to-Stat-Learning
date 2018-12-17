pwd <- getwd()
setwd(pwd)
# Header file with abstract
top <- paste0(pwd, "/header.tex")

# Document text
doc <-  paste0(pwd, "/notes.txt")

# Merge config file
system("cat header.tex notes.txt > Notes-Intro-to-Stat-Learning.tex")

write(paste0("\\end{document}"), "Notes-Intro-to-Stat-Learning.tex", append = TRUE)

# Compile pdf
system("pdflatex Notes-Intro-to-Stat-Learning.tex")

# Remove Latex Files
system("rm Notes-Intro-to-Stat-Learning.tex")
system("rm Notes-Intro-to-Stat-Learning.log")
system("rm Notes-Intro-to-Stat-Learning.aux")
# system("rm Notes-Intro-to-Stat-Learning.toc")