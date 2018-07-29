import random
import time

def generate_str(patternlen):
    letters = 'abcdefghijklmnopqrstuvwxyz '
    letterslen = len(letters)
    monkey_type = ""
    for index in range(patternlen):
        monkey_type = monkey_type + letters[random.randrange(letterslen)]
    
    return monkey_type
    
def score(pattern, teststring):
    count = 0
    for index in range(len(pattern)):
        if pattern[index] == teststring[index]:
            count += 1
            
    return count/len(pattern)        
            
    
def main():
    """
    This code is attempting to test the infinite monkey theorem 
    Theorem: Given a string, how many random trials does it take generate a matching string?
    """
    start_time = time.time()
    
    pattern = "methinks it is like a weasel"
    patternlen = len(pattern)
    
    newscore = 0
    bestscore = 0
    beststring = ''
    
    while bestscore < 1:
        teststring = generate_str(patternlen)
        print(teststring)
        newscore = score(pattern, teststring)
        if newscore>bestscore:
            beststring = teststring
            bestscore = newscore
            print('The best so far:', beststring)
        
    print('The Monkey has finally become The Bard!')
    e = time.time - start_time
    print('The Monkey took {0} hours {1} minutes and {2} seconds'.format(e // 3600, e % 3600 // 60, e % 60))    

main()    
