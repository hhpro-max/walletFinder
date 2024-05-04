import requests
from bitcoin import *
magicbyteNums = []

for i in range(256) :
    print("current magicbye : ",i)
    private_key = random_key()
    print("Private Key:", private_key)
    public_key = privtopub(private_key)
    print("Public Key:", public_key)
    address = pubtoaddr(public_key,magicbyte=i)
    print("Bitcoin Address:", address)
    url = "https://bitcoinexplorer.org/api/address/" + address
    while True:
        try :
            tryCounts = 0
            response = requests.get(url,timeout=10)
            data = response.json()
            if response.status_code == 200 and data["txHistory"] :
                print("found " , i )
                magicbyteNums.append(i)
                break
            else : 
                tryCounts += 1
                if tryCounts > 10 :
                    print("FATAL ERR")
                    err = True
                    break
        except requests.exceptions.Timeout:
            print("The request timed out")
            print("TRYING AGAIN ... (counts = " + str(tryCounts) + " )")
            tryCounts += 1
            if tryCounts > 10 :
                    print("FATAL ERR")
                    err = True
                    break       
        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)
            print("TRYING AGAIN ... (counts = " + str(tryCounts) + " )")
            tryCounts += 1  
            if tryCounts > 10 :
                    print("FATAL ERR")
                    err = True
                    break 
        except KeyError as e:
            print("An error occurred:", e)
            break 
print(magicbyteNums)                