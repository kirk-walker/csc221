-**mkdir <directory name>** makes a directory wherever you are.
-Using -p allows us to make parent directories
 Ex. mkdir -p csc221/hw2/ch5
-**rmdir <directory name>** removes directories
  This command supports -p.
  The directory must also be empty before it is removed.
-We can create a blank file if it does not exist with **touch [options] <filename>**
-We can duplicate a file or directory using **cp [options] <source> <destination>**
-**cp -r** lets us copy directories and files within them.
  -r stands for recursive.
-To move a file we use **mv [options] <source> <destination>**
  If we specify the destination to be the same directory as the source, but with a different name
  then we have used mv  to rename a file or directory.
-**rm [options] <file>** is used to remove a file.
  When rm is used with -r it allows us to remove all directories and all files and directories
  contained within it.

