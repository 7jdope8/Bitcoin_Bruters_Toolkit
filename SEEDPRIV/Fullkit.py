# This program takes a word file of mnemomics and calculates a new priv key and address from each line of the .txt file
# Work in Progress ... do we even need the (uncompressed) public key, just check the address? quicker

# > python fullkit.py   # defaults to seedlist.txt for input

# Printing to screen is time consuming - comment out prints if serious
from bitcoin import privtopub, pubtoaddr, sha256         
     
with open("seedlist.txt", "r") as ourfile, open("addresses.txt", "a+") as adds, open("addr_priv.txt", "a+") as addpriv: # Open our txt file to read from, file to write to, and 3rd file is only used if we hit a match and need to reference the priv key
    for line in ourfile:
        YourSeed = line

        priv= sha256(YourSeed)
        print("PRIVATE key: " + priv)
        print ("           *** never share your private key ***")

        pub = privtopub(priv)
        print("public key: " + pub)

        address = pubtoaddr(pub)
        print("address: " + address)
        adds.write(address + "\n")
        addpriv.write(address+","+priv + "\n") 

        print ("________________________________________________")

ourfile.close()  # Close our txt file
