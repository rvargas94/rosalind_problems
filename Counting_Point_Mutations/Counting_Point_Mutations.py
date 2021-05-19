######################################
#This script will solve the problem  #
#Counting Point Mutations            #
#From http://rosalind.info/problems  #
######################################

def hammingDistance(s,t):
    distance = 0
    for i in range(len(s)-1):
        if s[i] != t[i]:
            distance += 1
    return distance
    
def main():
    file_to_open = "Counting_Point_Mutations\\rosalind_hamm.txt"
    open_file_buffer = open(file_to_open,"r")
    
    dnaStrings = open_file_buffer.readlines()

    distance = hammingDistance(dnaStrings[0],dnaStrings[1])
    print("Hamming distance is:",distance)

if __name__ == '__main__':
    main()
