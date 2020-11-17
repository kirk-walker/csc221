- Part 1 -

1.Make all the directories needed for part1
 EX.  mkdir 'word' 'word' 'word'
2. While in ~/part1 use the grep command to get all files that have the word assigning in t  them. 
 EX. grep -lir assigning file(asterisk)
3. Pipe the grep command to xargs to move the files to the directory assigning
 Ex. grep -lir assigning file(asterisk) | xargs mv -t ../assigning
4. Repeat this process for the rest of the directories

- Part 2 -

1. For task one simply use the command 'sort' paired with your file to sort the words in al  alphabetical order. Then take the output and use '>' to put it in a new file. 
 EX. sort shuffled-words.txt > shuffled-words-sorted.txt

2. For task two use the sort command on rand-words.txt but now pipe it to uniq -c to see a 
  list of the words and how many times they are repeated. Then pipe it to sort -n to get it  the list in number order. Lastly use tail to get the last top 10. 
 EX. sort rand-words.txt | uniq -c | sort -n | tail > common words.txt

3. For task three do the exact command but with a new file. 
 EX. sort rand-numbers.txt | uniq -c | sort -n | tail > common-numbers.txt

4. For task four do the exact command but with a new file.
 EX. sort rand-numbers-2.txt | uniq -c | sort -n | tail > common-2.txt

5. For task five do the same command but with rand-numbers-5.txt. I could not figure out
the subselections of columns.
 EX. sort rand-numbers-5.txt | uniq -c | sort -n | tail > common-5.txt
