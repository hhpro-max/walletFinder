from bitcoin import *
from bit import Key
#from bitcoinlib.wallets import Wallet,wallet_delete
class AddressGen :
    
    def __init__(self) :

        print("Address generator class has been created!")
    def btcPPKH(self) :
        #MTHOD_1
        # Generate a Legacy address (P2PKH)
        #legacy_address = wallet.get_key().address

        #method 2
        private_key = random_key()
        public_key = privtopub(private_key)
        address = pubtoaddr(public_key)
        return private_key,public_key,address
    def btcPSH(self) :
        #method 1
        '''
        private_key = random_key()
        public_key = privtopub(private_key)
        address = pubkey_to_address(public_key, magicbyte=5)
        '''
        #method 2
        '''
        key = Key()
        private_key = key
        public_key = key.public_key
        address = key.segwit_address 
        '''
        #method 3
        # Generate a SegWit address (P2SH)
        #segwit_address = wallet.get_key(key_type='segwit').address

        #method 4
        private_key = random_key()
        public_key = privtopub(private_key)
        script =  public_key # + 'OP_0' 
        address = scriptaddr(script) 
        return private_key,public_key,address
    def btcPWPKH(self):
        #NOT WORKING YET
        return private_key,public_key,address