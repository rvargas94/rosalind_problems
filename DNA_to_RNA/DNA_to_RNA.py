######################################
#This script will solve the problem  #
#Transcribing DNA INTO RNA           #
#From http://rosalind.info/problems  #
######################################

def convert_to_RNA(DNA_string):
    char_array = list(DNA_string)
    for x in range(len(char_array)):
        if char_array[x] == 'T':
            char_array[x] = 'U'
            print "Changed"
    RNA_str = ''.join(char_array)
    return RNA_str

def main():
    file_to_open = "DNA.txt"
    open_file_buffer = open(file_to_open,"r")
    DNA_string = open_file_buffer.read()
    RNA_string = convert_to_RNA(DNA_string)
    print RNA_string

    file_to_open = "RNA.txt"
    open_file_buffer = open(file_to_open,"w")
    open_file_buffer.write(RNA_string)

if __name__=='__main__':
    main()
