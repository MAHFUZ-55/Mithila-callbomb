logo ="""\033[1;96m
  /$$      /$$  /$$$$$$  /$$   /$$ /$$$$$$$$ /$$   /$$ /$$$$$$$$
| $$$    /$$$ /$$__  $$| $$  | $$| $$_____/| $$  | $$|_____ $$ 
| $$$$  /$$$$| $$  \ $$| $$  | $$| $$      | $$  | $$     /$$/ 
| $$ $$/$$ $$| $$$$$$$$| $$$$$$$$| $$$$$   | $$  | $$    /$$/  
| $$  $$$| $$| $$__  $$| $$__  $$| $$__/   | $$  | $$   /$$/   
| $$\  $ | $$| $$  | $$| $$  | $$| $$      | $$  | $$  /$$/    
| $$ \/  | $$| $$  | $$| $$  | $$| $$      |  $$$$$$/ /$$$$$$$$
|__/     |__/|__/  |__/|__/  |__/|__/       \______/ |________/
                                             
                                             """

import requests
number = input("Enter Your Number: ")
amount = int(input ("Enter Your Amount: "))
for i in range (amount):
 r= requests.get("http://pikachu-call-bomber.ezyro.com/babyyy.php?phone="+number)
 f= r.content
 print(f)
