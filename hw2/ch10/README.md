**Grep and Regular Expressions**

- egrep [command line options] <pattern> [path] is a program that will search a
  given set of data and print every line which contains a given pattern.

  	ex. egrep 'mellon' mysampledata.txt 
	 will print everyline containing 'mellon'
        ex. egrep -n 'mellon'
	 will give the line number
	ex. -c
	 will just show how many lines matched
	ex. '[aeiou]{2,}' 
	 will identify with lines that have two or more vowels in a row
	ex '2.+'
	 any line with a 2 that is not at the end of the line
	ex. '2$'
	 the number 2 is the last character on the line
	ex. 'or|is|go'
	 each line that contains either is, go, or or.
	ex. '^[A-K]' 
	 Name begins with A-K

 
