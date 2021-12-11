# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 16:52:15 2021

@author: Elessar
"""

import time

startTime = time.time()

fileName = "turkey.txt"
probeLen = 100

def readFile(fileName):

    list1 = []
    
     
    file = open(fileName, "r")

    for line in file:
        if "N" in line:     
            continue
        
        list1.append(line)
        
    file.close()

    return list1


def writeToFile(dict,valid_seq): 
    
    string = ""
    probe_len = 0
    
    max_keys = [key for key, value in dict.items()          
                        if value == max(dict.values())]
    
    max_value = max(dict, key=dict.get)
    
    for index in max_keys:
        string = string + index + "\n"
        probe_len += 1
 
    with open("didemKahyaoglu.txt", 'w') as file:
        file.write(str(valid_seq)+" " + str(dict.get(max_value)) + "\n")
        file.write(str(probe_len)+ "\n")
        file.write(string)
        
    file.close()

def findSeq(seq,probeLen): 
   
    dict={}
    
    
    for i in range(0,len(seq)-probeLen):
        sub = seq[i:i+probeLen]
        cnt = seq.count(sub)

        if sub not in dict:
            dict[sub] = cnt
          
    return dict

def probes(fileName, probeLen):
    
    valid_seq = 10
    list1 = readFile(fileName)
   
    seq_len = 0
    valid_seq_cnt=0
   
    string1 = ""
  
    for gens in list1 :
       
        seq_len = len(gens)-1
        valid_seq_cnt = valid_seq_cnt + 1
     
        if valid_seq_cnt <= valid_seq:
           
            if seq_len >= 27000 :
                for nucl in gens:
                    string1 =  string1 + nucl
      
    dict=findSeq(string1,probeLen)
    writeToFile(dict,valid_seq)
  
probes(fileName,probeLen)

endTime = time.time()
elapsedTime = endTime - startTime


print(elapsedTime)