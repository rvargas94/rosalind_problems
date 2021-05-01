######################################
#This script will solve the problem  #
#Translating RNA into Protein        #
#From http://rosalind.info/problems  #
######################################

STARTCODON = "AUG"
ENDCODONS = ["UAA","UAG","UGA"]

RNA_CODON_TABLE = {
    "UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
    "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
    "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
    "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
    "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
    "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
    "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
    "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
    "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
    "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
    "CAA" : "Q", "AAA" : "K", "GAA" : "E", "CAG" : "Q",
    "AAG" : "K", "GAG" : "E", "UGU" : "C", "CGU" : "R",
    "AGU" : "S", "GGU" : "G", "UGC" : "C", "CGC" : "R",
    "AGC" : "S", "GGC" : "G", "CGA" : "R", "AGA" : "R",
    "GGA" : "G", "UGG" : "W", "CGG" : "R", "AGG" : "R",
    "GGG" : "G" 
}

def translate(rnaString):
    proteinString = ""
    counter = 0

    while( (counter+3) < len(rnaString) ):
        rnaStringChunk = rnaString[counter:counter+3]
        if rnaStringChunk in ENDCODONS:
            break
        proteinString += RNA_CODON_TABLE[rnaStringChunk]
        counter += 3

    return proteinString



def main():
    file_to_open = "Translating_RNA_into_protein//rosalind_prot.txt"
    open_file_buffer = open(file_to_open,"r")
    rnaString = open_file_buffer.read()
    open_file_buffer.close()

    proteinString = translate(rnaString)

    file_to_write = "Translating_RNA_into_protein//proteinString.txt"
    open_file_buffer = open(file_to_write,"w")
    open_file_buffer.write(proteinString)
    open_file_buffer.close()

if __name__ == '__main__':
    main()
