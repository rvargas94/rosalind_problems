######################################
#This script will solve the problem  #
#Complementing a Strand of DNA       #
#From http://rosalind.info/problems  #
######################################

def reverse_compliment(DNA_string):
    DNA_string = DNA_string[::-1]
    char_array = list(DNA_string)
    for x in range(len(char_array)):
                if char_array[x] == 'A':
                   char_array[x] = 'T'
                elif char_array[x] == 'T':
                   char_array[x] = 'A'
                elif char_array[x] == 'C':
                   char_array[x] = 'G'
                elif char_array[x] == 'G':
                   char_array[x] = 'C'
    new_string = ''.join(char_array)
    return new_string

def main():
    file_to_open = "DNA.txt"
    open_file_buffer = open(file_to_open,"r")
    DNA_string = open_file_buffer.read()
    DNA_comp = reverse_compliment(DNA_string)
    print DNA_comp

    file_to_open = "DNA_rev_comp.txt"
    open_file_buffer = open(file_to_open,"w")
    open_file_buffer.write(DNA_comp)

    

if __name__ == '__main__':
    main()
