# Bitcoin_address_balance_checker
check a bitcoin account balance using python3 

There is one key dependency, blockcypher, which you should check out for the many other tricks it has (https://pypi.org/project/blockcypher/)

STEP 1)
pip install -r requirements.txt 
    OR 
pip3 install -r requirements.txt

STEP 2) 
python checker.py
    OR 
python3 checker.py

STEP 3) paste in the bitcoin public key when requested, if not found it will say so

More advanced.... 

PART B)
If you want to check balances of many wallets, then 
save your Target accounts to a file called wallet_list.txt
then run: 
python3 multichecker.py     (OR python checker.py, but seriously get over python2)

All wallets With a balance will be output to: wallets_output.txt
But all acounts will be printed to terminal, even the duff ones


( Blcokcyhper allows 200 account checks, or 3 per second, for free tier users, if you want more, see their plans, https://accounts.blockcypher.com/plans/details/free)


