import itertools as it
import time

## ## ## STEP 1: Get Inputs ## ## ## -----------------------------------------------
inputFileName = input("which .txt file to read word lists from? : ")

# this section just checks you've put the .txt at the end of the filename as its a common habit to forget
nameCheck = inputFileName[-4:]      # take the last 4 char of the string
if nameCheck != ".txt":             # check the 4 chars are .txt, otherwise it has not been input
    inputFileName = inputFileName + ".txt"      # add the .txt if it has been forgotten

print (" \n ", "   opening ", inputFileName, " \n ")

permuteLengthMin = input(" What is the minimum permutation length you seek eg 12 permutations (not combinations!) : \n ")
# permuteLengthMax = input("what is the maximum length you seek eg 50 permutations : ")

outputFileName = input("which .txt file to save permutations to? ")
# this section just checks you've put the .txt at the end of the filename as its a common habit to forget
nameCheck = outputFileName[-4:]      # take the last 4 char of the string
if nameCheck != ".txt":             # check the 4 chars are .txt, otherwise it has not been input
    outputFileName = outputFileName + ".txt"      # add the .txt if it has been forgotten
open(outputFileName, 'a').close()           # create the blank file for writing later

# open the list from file specified and ignore the \n at the end
with open(inputFileName) as f:          # open the list from file specified and ignore the \n at the end
    wordz = f.read().splitlines()
# Note, if the text file has 2 words on one line it will treat it as one, eg "hello world" is 1 item as on 1 line "hello", "world" is 2 items.
f.close()   ## Save RAM, close the file!

# print(wordz) ... this was just checking its a list, it should be a tuple (faster)... to revert later

## ## ## STEP 2: PERMUTE the Variables ## ## ## -----------------------------------------------


tic = time.perf_counter()                                           # ** Start the timer
combo_list = list(it.permutations(wordz, int(permuteLengthMin)))
toc = time.perf_counter()                                           # ** Stop the timer
print(f"  \n Calculated in {toc - tic:0.2f} seconds \n")   # the 0.2f means 2 decimal places

#print(my_combos)
first_3_strings = str(combo_list[:3])
print("The first five strings appear like this; "+ first_3_strings + " ... etc ---> see the saved text file for full output")

## ## ## STEP 3: Save Permutations to a file ## ## ## -----------------------------------------------


with open(outputFileName, 'a') as f: 
   f.write(str(combo_list))                 # note we turn combo_list into a string, otherwise it doesnt write
   f.close() 

print ("\n" + " >-- Finished --< "+ "\n")
      
    
    #### FOR LATER when speed needs tuning
    # This will yield an "array" of lines from the file.
#      lines = tuple(open(filename, 'r'))


