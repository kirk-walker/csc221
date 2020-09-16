**Piping and Redirection**

- Every program run on the command line has 3 data streams.
	
	STDIN(0) - Standard input
	STDOUT(1) - Standard output
	STDERR(2) - Standard error

- > is used to redirect data. It will make a new file if one does not exist and
  put the data in it. If we are putting data in to a file that does exist then
  it will erase what is in the file.

- >> will append the data to the existing file.

- < will send the data the other way.

- 2> using the number associated with the stream allows us to redirect errors

- 2>&1 allows us to redirect stderr in to the stdout stream and then sends both
  to a location

- ( | ) allows us to pipe data from one program to another
  add pipes incrementally and test as you go so you make less errors.

- Pipes and Redirection can be combined as well.


