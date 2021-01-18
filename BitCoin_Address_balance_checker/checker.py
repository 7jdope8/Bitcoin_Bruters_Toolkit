import blockcypher

def balance(publicKey):
    try:
        total = blockcypher.get_total_balance(publicKey)
        bitcoinBalance = int(total)/100000000
        print('Balance is '+ str(total) + ' Satoshis, or in Bitcoin: ' +str(bitcoinBalance) + ', in account: '+ publicKey)
    except:
        print('Account is not found, exiting...')

def main():
	publicKey = input("Enter your Address: ")
	balance(publicKey)

main()