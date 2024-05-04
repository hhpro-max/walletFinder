from bitcoin import *
import requests
import random
err = False
while True:
    if err :
        break
    private_key = random_key()
    print("Private Key:", private_key)
    public_key = privtopub(private_key)
    print("Public Key:", public_key)
    randomMagicNumber = random.choice([0, 5])
    address = pubtoaddr(public_key,magicbyte=randomMagicNumber)
    print("Bitcoin Address:", address)
    url = "https://bitcoinexplorer.org/api/address/" + address
    while True:
        tryCounts = 0
        try :
            response = requests.get(url,timeout=10)
            if response.status_code == 200 :
                data = response.json()
                balanceSatL = data["txHistory"]["txCount"]
                txCountL = data["txHistory"]["balanceSat"]
                print("transaction counts :",txCountL)
                print("balance :" , balanceSatL)
                if balanceSatL > 0 or txCountL > 0 :
                    print("wallet found!")
                    with open('example.txt', 'a') as file:
                        walletData = '\n pv-key: ' + private_key + "\n pub-key: " + public_key + "\n address: " + address + "\n balance: " + str(balanceSatL)
                        file.write(walletData)
                        file.close()
                break        
            else:
                print("Failed to retrieve data (the status code is not 200) status code is : " + str(response.status_code))
                print("TRYING AGAIN ... (counts = " + str(tryCounts) + " )")
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
