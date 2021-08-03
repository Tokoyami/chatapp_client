import base64
import requests
import os
if os.name != "posix":
    print("-"*50)
    print("WARNING: This program is only tested on POSIX")
    print("--Installation for windows--")
    print("https://docs.microsoft.com/en-us/windows/wsl/install-win10")
    print("After installing open command prompt in current directory and type")
    print("wsl pkg install python")
    print("After installation, type wsl python3 client.py to start chat app.")
    print("--Installation for android--")
    print("Go to google play store and find app called Termux, then open it and type this:")
    print("git clone https://github.com/Tokoyami/chatapp_client.git && mv ./chatapp_client-master/start.sh . && pkg install python")
    print("After command completes, to start chat app, type")
    print("./start.sh")
    print("-"*50)
    if input("Type anything to still continue or nothing to exit: ") == "":
        exit(0)
print("Getting the code...\r")
server_code = requests.get("https://www.campfiremsg.com/chat_b64code").text
print("Decoding the code...\r")
code = base64.b64decode(server_code)
print("Compiling the code...\r")
compiled = compile(code,"<string>","exec")
print("Executing compiled code...\r")
os.system("clear")
eval(compiled)