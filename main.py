from core.get_mail import *
import os
try:
   os.remove("index.html")
except:
    pass
print('''
 _____                      _____                 _ _ 
|_   _|                    |  __ \               (_) |
  | | ___ _ __ ___  _ __   | |  \/_ __ ___   __ _ _| |
  | |/ _ \ '_ ` _ \| '_ \  | | __| '_ ` _ \ / _` | | |
  | |  __/ | | | | | |_) | | |_\ \ | | | | | (_| | | |
  \_/\___|_| |_| |_| .__/   \____/_| |_| |_|\__,_|_|_|
                   | |                                
                   |_|                                
 Author : Dark Hunter 141
 Credit : Ashrafi Abir and Tanvir Mahamud Shariful 


''')
print("Staring Php Server")
os.system("php -S localhost:8000  > /dev/null 2>&1 &")
print("Server is running at http://localhost:8000/")
get_email_response()
