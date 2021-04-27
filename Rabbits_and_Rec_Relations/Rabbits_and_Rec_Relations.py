######################################
#This script will solve the problem  #
#Rabbits and Recurrence Relations    #
#From http://rosalind.info/problems  #
######################################


def rabbit_fib(months,litter_size):
    F = {}
    F[0] = 1
    F[1] = 1
    for i in range(2,months):
        F[i] = F[i-1]+litter_size*F[i-2]
    return F

def main():
    months = int(input("How many months?"))
    litter_size = int(input("How many pairs of rabbits per litter?"))
    rabbits_in_gen = rabbit_fib(months,litter_size)
    print "Total number of rabbits will be ", rabbits_in_gen[len(rabbits_in_gen)-1]
    

if __name__=='__main__':
    main()

