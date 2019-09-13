import random
import sys

def frog(final_dist=100,max=6):

    # I wrote this quickly in a pub
    # Don't judge me
    
    total_dist = 1
    
    while total_dist <= final_dist:
        
        cap = 10**max
        
        trials = 0
        total_leaps = 0
        
        while trials <= cap:
            
            dist = total_dist
            leaps = 0
            
            while dist > 0:
                this_jump = int(random.random()*(dist)+1)
                dist -= this_jump
                leaps += 1
                
            total_leaps += leaps
            
            trials += 1
            
        print "{0}\t{1}".format(total_dist,(total_leaps*1.0)/trials)
    
        total_dist += 1
    
    return "DONE"

def main(args):
    """
    Read the first command line as 'final_dist'
    Read the second command line as 'max'
    """
    frog(*[int(a) for a in args[1:3]])

if __name__ == '__main__': 
    main(sys.argv)

