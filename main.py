import threading
from addressGen import AddressGen
from checkAddress import checkAddress
checkAdd = checkAddress()
addGen = AddressGen()
api_url= "https://bitcoinexplorer.org/api/address/"
#here we wanted to use threads instead but we would get 503 error too much which i think its bicause of requests payload

#def checkPPKH():
#    while True:
#        private_key,public_key,address = addGen.btcPPKH()
#        url = api_url + address
#        checkAdd.checkAddress(private_key=private_key,public_key=public_key,url=url,fileName="ppkh_address.txt")
#def checkPSH():
#    while True:
#        private_key,public_key,address = addGen.btcPSH()
#        url = api_url + address
#        checkAdd.checkAddress(private_key=private_key,public_key=public_key,url=url,fileName="psh_address.txt")      
#ppkh_thread = threading.Thread(target=checkPPKH)
#ppkh_thread.start()
#
#psh_thread = threading.Thread(target=checkPSH)
#psh_thread.start()
def checkPPKH(): 
    private_key,public_key,address = addGen.btcPPKH()
    url = api_url + address
    checkAdd.checkAddress(private_key=private_key,public_key=public_key,url=url,fileName="ppkh_address.txt")
def checkPSH():
    private_key,public_key,address = addGen.btcPSH()
    url = api_url + address
    checkAdd.checkAddress(private_key=private_key,public_key=public_key,url=url,fileName="psh_address.txt")  
while True :
    checkPPKH()
    checkPSH()
