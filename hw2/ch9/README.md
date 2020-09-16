**Filters**

- head [-numbr of lines to print] [path] is a program that prints the first so 
  many lines of its input. By default it will print 10.

- tail [-number of lines to print] [path] is the opposite of head in that it 
  will print the last lines.

- sort [-options] [path] will sort out it's input. by default, alphabetically.

- nl [-options] [path] numbers lines

- wc [-options] [path] gives a word count. by default it will give a count of 3
   -l will give us lines
   -w will give us words
   -m will give us characters

- cut [-options] [path] helps if your program is separated in to fields and you   only want certain fields.

- sed <expression> [path] stands for **Stream Editor** and it allows us to do
  search and replace on our data

  	s/search/replace/g

- uniq [options] [path] stands for unique and will remove duplicate lines from 
  data. The lines must be adjacent

- tac [path] opposite of cat and it will print last to first

