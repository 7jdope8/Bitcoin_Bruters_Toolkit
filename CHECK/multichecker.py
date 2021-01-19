import blockcypher
import time

def balance(publicKey1):
    try:
        total = blockcypher.get_total_balance('publicKey1')
        bitcoinBalance = int(total)/100000000       # because the library keeps giving satoshi results even though the docs dont say that
        time.sleep(0.35)
        print('Balance is '+ str(total) + '  Satoshis, or in Bitcoin: ' +str(bitcoinBalance) + ', in account: '+ publicKey1)
        
        if bitcoinBalance>0.000000001:
            # Open a file with access mode 'a'
                file_object = open('wallets_output.txt', 'a')     # open a file to save results to
                L = [publicKey1, " ", bitcoinBalance]    # the results will be the amount of bitcoin and the public hash of the wallet
                file_object.writelines(L)   # write the results to a new line (presumably not overwriting previous results!)
                file_object.close() # always close the file, for some reason important!
        else: 
            print("")           # not sure WTF I'm doing here, just had to make the IF work
    except:
        print('Account is not found')

#def main(publicKey1):
#	publicKey1 = input("Enter an Address :  ")
#	balance(publicKey1)

read_for = open('wallet_list.txt')  # open text file with wallets saved
for publicKey1 in read_for:     # loop through the list
    balance(publicKey1)
    #print(publicKey1)
    #time.sleep(0.2)
    
read_for.close()


