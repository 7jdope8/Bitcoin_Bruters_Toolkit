from bitcoin import random_key, privtopub, pubtoaddr

private_key = random_key()
print("Randomly Generated Private Key: " + private_key)

public_key = privtopub(private_key)
print("Derived from Private Key, Public Key: " + public_key)

address = pubtoaddr(public_key)
print("Bitcoin Address: " + address)
