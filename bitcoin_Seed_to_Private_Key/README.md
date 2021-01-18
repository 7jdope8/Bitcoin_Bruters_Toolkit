# Bitcoin Address: Turn seed mnemonics into Private Keys & Addresses
- input a Mnemonic to create new bitcoin address in python (bitcoinseed.py)
- create addresses from random (bitcoinrandom.py)

A good test example is the mnemomic: youaremysunshinemyonlysunshine
- the first time this was stolen in 2013 it took 2 days
- the second time it was stolen in 2019 it took under a minute
https://www.blockchain.com/btc/address/12NEsPS2tPhjXJHd3kGkTvQ7ECGypuxbeo

- To check a long list of mnemomics, paste the lines of words into seedlist.txt and use> python3 bitcoinseed_multi.py
this only prints results to screen

- python fullkit.py will do the lot: take your seedlist.txt file, calculate all the Private Keys and addresses and print them to the terminal, and it will save just the public bitcoin addresses as a list to addresses.txt for quick testing, and it will also save addresses and priv keys to addr_priv.txt so if you do hit an open account you can find the private key

addresses.txt is what we use to compare to our copy of the blockchain to see if there is an address with a positive balance.

THIS IS CURRENTLY STILL A WORK IN PROGRESS... Should be finalised by Feb 1st.
