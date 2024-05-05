import requests
class checkAddress :
    def __init__(self):
        print("check address class has been created!")
    def checkAddress(self,private_key,public_key,url,fileName):
        tryCounts = 0    
        while True:
                try :
                    response = requests.get(url,timeout=10)
                    if response.status_code == 200 :
                        data = response.json()
                        balanceSatL = data["txHistory"]["txCount"]
                        txCountL = data["txHistory"]["balanceSat"]
                        print("address : ",url,"transaction counts :",txCountL ," balance :" , balanceSatL)
                        tryCounts = 0
                        if balanceSatL > 0 or txCountL > 0 :
                            print("wallet found!")
                            with open(fileName, 'a') as file:
                                walletData = '\n pv-key: ' + private_key + "\n pub-key: " + public_key + "\n address: " + url + "\n balance: " + str(balanceSatL)
                                file.write(walletData)
                                file.close()
                                
                        break        
                    else:
                        print("Failed to retrieve data with url " + url + " (the status code is not 200) status code is : " + str(response.status_code) )
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
                        