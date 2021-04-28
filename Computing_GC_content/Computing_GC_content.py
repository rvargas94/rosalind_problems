######################################
#This script will solve the problem  #
#Computing GC Content                #
#From http://rosalind.info/problems  #
######################################
import re
from collections import defaultdict

def calculateGCContent(DNA_string):
    substrList = ["G","C"]
    occurances = 0
    for c in substrList:
        occurances += DNA_string.count(c)
    occurances /= len(DNA_string)
    return round(100*occurances,6)

def main():
    file_to_open = "Computing_GC_content\\rosalind_gc.txt"
    open_file_buffer = open(file_to_open,"r")
    file_text = open_file_buffer.read().replace('\n','')
    open_file_buffer.close()
    prog = re.compile("(?P<ID>Rosalind_\d{4})(?P<DNA>[ACGT]+)")

    gcContent = defaultdict(float)

    for item in prog.findall(file_text):
        id = item[0][0:]
        gcContent[id] = calculateGCContent(item[1])

    maxKey = max(gcContent,key=gcContent.get)
    
    file_to_open = "Computing_GC_content\\solution.txt"
    open_file_buffer = open(file_to_open,"w")
    open_file_buffer.write(maxKey+"\n")
    open_file_buffer.write(str(gcContent[maxKey]))
    open_file_buffer.close()
    

if __name__ == '__main__':
    main()
