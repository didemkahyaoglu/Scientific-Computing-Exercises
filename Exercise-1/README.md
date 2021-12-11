# Pseudocode of the algorithm:
  
  # the1.py
1. define the fileName that want to read
2. assign the probeLen
3. call probes(fileName,probeLen) function
4. calculate elapsedTime

# readFile(fileName):
1. define the list1 to which we will add the genome sequences
2. open the file that want to read
3. for line in file:
        
        IF line contains “N”
             For loop continues without taking this line
        add the line to list1
4. close the file

# writeToFile(dict,valid_seq):
1. initialize the string that will hold max_keys of dictionary
2. initialize the probe_len(length of the returning list of the probes function)
3. find the max_keys that have max value of dictionary
4. find the max_value of dictionary
5. for index in max_keys:
      assign the max_keys to string
      probe_len increments by one
      
6. open the “didemKahyaoglu.txt” file that want to write
7. write the valid_seq , max_value , probe_len , string to file.
8. close the file 

# findSeq(seq,probeLen):
1. initialize the dict that holds the subsequences
2. for i in range(0,len(seq)- probeLen):
    
    assign the seq values from range of i to i+ probeLen, to sub
    
    assign the cnt values that holds the maximum number sequences that the probes are found
 IF sub not in dict:
 assign cnt value to dict[sub]
 
# probes(fileName, probeLen):
1. assign valid_seq value
2. assign list1 from readFile(fileName) function
3. initialize the seq_len that will hold length of the sequences(must be greater or equal
than 27000)
4. initialize the valid_seq_cnt that will hold the number of valid sequences
5. initialize the string1 that will hold substrings
6. for gens in list1 :
        
        assign gens length – 1 to seq_len
        valid_seq_cnt increments by one
        IF valid_seq_cnt less than or equal to valid_seq:
           IF seq_len greater or equal than 27000:
               for nucl in gens:
                    append nucleotides to string1
7. assign findSeq(string1, probeLen) to dict
8. write the file with writeToFile(dict,valid_seq) function
