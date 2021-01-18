import itertools as it
import time

## ## ## STEP 1: Get Inputs ## ## ## -----------------------------------------------
inputFileName = input("which .txt file to read word lists from? : ")

# this section just checks you've put the .txt at the end of the filename as its a common habit to forget
nameCheck = inputFileName[-4:]      # take the last 4 char of the string
if nameCheck != ".txt":             # check the 4 chars are .txt, otherwise it has not been input
    inputFileName = inputFileName + ".txt"      # add the .txt if it has been forgotten

print (" \n ", "   opening ", inputFileName, "\n")

lineNos=0
with open(inputFileName, 'r') as f:
    for line in f:
        lineNos += 1
print("> Total number of items to scramble is ----> ", lineNos, "\n", "\n")

permuteLengthMin = int(input("What is the minimum permutation length you seek eg 12 permutations (not combinations!) :\n "))
# permuteLengthMax = input("what is the maximum length you seek eg 50 permutations : ")
permuteLengthMax = int(input("\nWhat is the Max permutation length you seek eg 20 permutations: \n"))
# permuteLengthMax = input("what is the maximum length you seek eg 50 permutations : ")

outputFileName = input("which .txt file to save permutations to? ")
# this section just checks you've put the .txt at the end of the filename as its a common habit to forget
nameCheck = outputFileName[-4:]      # take the last 4 char of the string
if nameCheck != ".txt":             # check the 4 chars are .txt, otherwise it has not been input
    outputFileName = outputFileName + ".txt"      # add the .txt if it has been forgotten
open(outputFileName, 'a+').close()           # create the blank file for writing later

# open the list from file specified and ignore the \n at the end
with open(inputFileName) as f:          # open the list from file specified and ignore the \n at the end
    wordlist = f.read().splitlines()
# Note, if the text file has 2 words on one line it will treat it as one, eg "hello world" is 1 item, but with a delimiter (,) as on 1 line "hello", "world" is 2 items.
f.close()   ## Save RAM, close the file!

## ## ## STEP 2: PERMUTE the wordlist ## ## ## -----------------------------------------------
print ("\n", "     calculating....","\n")
loopz = 0
combo_list = []
while int(permuteLengthMin+loopz)<= int(permuteLengthMax):
    tic = time.perf_counter()                                           # ** Start the timer                                    
    combo_list = list(it.permutations(wordlist, int(permuteLengthMin+loopz)))
    n=len(combo_list)
    with open(outputFileName, 'a+') as f:           # save the string, as an append to the file
        f.write(str(combo_list))                 # note we turn combo_list into a string, otherwise it doesnt write
        f.close() 
    toc = time.perf_counter()                                           # ** Stop the timer
                                         
    print("calculation of permutation of length ",int(permuteLengthMin+loopz) ,", which is ", n , " total permutations")  
    loopz = int(loopz + 1)       
    print(f"  >    \n Calculated in {toc - tic:0.4f} seconds \n")   # the 0.4f means 4 decimal places

#print(my_combos)
first_2_strings = str(combo_list[:2])
print("\n","The first few strings appear like this; "+ first_2_strings + "\n" ,"\n")
#
print ("\n","\n" + " ,.-~*´¨¯¨`*·~-.¸-(_FINISHED_)-,.-~*´¨¯¨`*·~-.¸ "+ "\n","\n")
#
print ("           results in " + outputFileName + "\n","\n")
      
    



