Pseudocode of the algorithm:
  
  the1.py
1. define the fileName that want to read
2. assign the probeLen
readFile(fileName):
1. define the list1 to which we will add the genome sequences
2. open the file that want to read
3. for line in file:
 IF line contains “N”
 For loop continues without taking this line
 add the line to list1
4. close the file
