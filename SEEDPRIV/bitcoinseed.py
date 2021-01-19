# This program takes you mnemomic and gives you the private & public keys, and address.
# a nice way to make a brain wallet, I recommend 24 words!

from bitcoin import sha256,  privtopub, pubtoaddr    

YourSeed = input("Input your mnemonic seed: ")

priv= sha256(YourSeed)
print("PRIVATE key: " + priv)
print ("           °°° never share your private key °°°")

pub = privtopub(priv)
print("public key: " + pub)

address = pubtoaddr(pub)
print("address: " + address)

