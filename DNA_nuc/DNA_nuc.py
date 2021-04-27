######################################
#This script will solve the problem  #
#Counting DNA Nucleotides            #
#From http://rosalind.info/problems  #
######################################
import json

def count_DNA_nucs(DNA_string):
    previously_seen = {'A':0,'C':0,'T':0,'G':0}
    freq_values = ""
    for letters in DNA_string:
        if letters in previously_seen:
            previously_seen[letters] += 1

    
    #although order should not matter,
    #Rosalind  wants order in A C G T 
    #for vals in previously_seen:
    #    freq_values += str(previously_seen[vals])
    #    freq_values += " "

    freq_values += str(previously_seen['A'])
    freq_values += " "
    freq_values += str(previously_seen['C'])
    freq_values += " "
    freq_values += str(previously_seen['G'])
    freq_values += " "
    freq_values += str(previously_seen['T'])
    
    
    return freq_values


def main():
    file_to_open = "DNA.txt"
    open_file_buffer = open(file_to_open,"r")
    DNA_string = open_file_buffer.read()
    letter_frequency = count_DNA_nucs(DNA_string)

    
    print letter_frequency

    
    file_to_open = "frequency.txt"
    open_file_buffer = open(file_to_open,"w")
    open_file_buffer.write(letter_frequency)

if __name__== '__main__':
    main()
