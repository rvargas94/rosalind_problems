######################################
#This script will solve the problem  #
#Finding a Motif in DNA              #
#From http://rosalind.info/problems  #
######################################

def findSubstrIndicies(s,t):
    ixList = []
    for i in range(len(s)-len(t)+1):
        if(t == s[i:i+len(t)]):
            ixList.append(i+1)
    return ixList

def main():
    file_to_open = "Finding_a_Motif_in_DNA//rosalind_subs.txt"
    open_file_buffer = open(file_to_open,"r")
    text = open_file_buffer.read().splitlines()

    ix = findSubstrIndicies(text[0],text[1])
    
    file_to_open = "Finding_a_Motif_in_DNA//solution.txt"
    open_file_buffer = open(file_to_open,"w")
    for index in ix:
        open_file_buffer.write(str(index) + " ")
        

if __name__ == '__main__':
    main()
