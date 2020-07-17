# Imports
import time
import webbrowser 
import random
import OfficialWordList
import requests 
import os

# Introduction 
print('''Welcome to CyberFisher(CF)! Where you can fish yourself a random site on the World Wide Web! 
Note: If the console goes blank for a while just close out and ReExecute CyberFisher''')
time.sleep(7)

# loadingScreen 
done = False
while True:
    while done == False:
        print("Fishing.")
        time.sleep(random.choice(OfficialWordList.times))
        os.system('cls')
        print("Fishing..")
        time.sleep(random.choice(OfficialWordList.times))
        os.system('cls')
        print("Fishing...")
        time.sleep(random.choice(OfficialWordList.times))
        os.system('cls')

        # Formatting the random link 
        try:
            ttp_or_ttps = random.choice(OfficialWordList.ttp_ttps)
            random_domain_name = random.choice(OfficialWordList.wordList)
            random_domain_extension = random.choice(OfficialWordList.top_level_domain)
            random_link = ttp_or_ttps + random_domain_name + random_domain_extension

            # Validating the random link
            requests = requests.get(random_link)
            if requests.status_code == 200:
                done = True
                print("You have caught the " + random_link + " fish. Nice Catch! :)")
                time.sleep(3)
                # Launching WebBrowser for the Validated Link
                webbrowser.open(random_link, new=2)
                break

        # Creating a new link if the link isn't valid 
        except:
            print("Fishing.")
            time.sleep(0.01)
            os.system('cls')
            print("Fishing..")
            time.sleep(0.01)
            os.system('cls')
            print("Fishing...")
            time.sleep(0.01)
            os.system('cls')
            done = False

    



