# This program takes a word file of mnemomics(seedlist.txt) and calculates a new priv key and address from each line of the .txt file
# Work in Progress ... do we even need the (uncompressed) public key, just check the address? quicker
# Does not output to a txt file, only prints on screen, use fullkit.py to save into a file

from bitcoin import privtopub, pubtoaddr, sha256         
     
with open("seedlist.txt", "r") as ourfile: # Open our txt file
    for line in ourfile:
        YourSeed = line

        priv= sha256(YourSeed)
        print("PRIVATE key: " + priv)
        print ("           °°° never share your private key °°°")

        pub = privtopub(priv)
        print("public key: " + pub)

        address = pubtoaddr(pub)
        print("address: " + address)
        print ("________________________________________________")

ourfile.close()  # Close our txt file
