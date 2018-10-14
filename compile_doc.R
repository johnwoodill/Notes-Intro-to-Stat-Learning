setwd("/Users/john/Projects/Intro to Stat Learning/")

# Header file with abstract
top <- "/Users/john/Projects/Intro to Stat Learning/header.tex"

# Document text
doc <-  "/Users/john/Projects/Intro to Stat Learning/notes.txt"

# Merge config file
system("cat header.tex document.txt > output.tex")

write(paste0("\\end{document}"), "output.tex", append = TRUE)

# Compile pdf
system("pdflatex output.tex")
