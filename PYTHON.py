import time
import subprocess
import os
import sys
from time import sleep
logo1 = """
      ########   ########  ##           ###             ##     ###     #########
      ##     ##  ##        ##          ## ##            ##    ## ##    ##      ##
      ##     ##  ##        ##         ##   ##           ##   ##   ##   ##      ##
      ########   ########  ##        ##     ##          ##  ##     ##  #########
      ##     ##  ##        ##        #########    ##    ##  #########  ##     ##
      ##     ##  ##        ##        ##     ##    ##    ##  ##     ##  ##      ##
      ########   ########  ########  ##     ##      #####   ##     ##  ##       ##


           ########   ##    ##  ########  ##     ##  ########   ##    ##
           ##     ##   ##  ##      ##     ##     ## ##      ##  ###   ##
           ##     ##    ####       ##     ##     ## ##      ##  ####  ##
           ########      ##        ##     ######### ##      ##  ## ## ##
           ##            ##        ##     ##     ## ##      ##  ##  ####
           ##            ##        ##     ##     ## ##      ##  ##   ###
           ##            ##        ##     ##     ##  ########   ##    ##
"""
time.sleep(2)

logo2 = """  __________________
  |################|
  |################|
  |################|
  |################|
  |################|
 _|################|___
|_____________________|
  |##################|
  |####|''''|##|''|##|
  |####|   _|##|_ |##|
  |####|__|##  ##| ##|
  |_##############___|   
   |  |_|_|_|_|_|_|
   |  |_ _ _ _ _ _
   |  | | | | | | |
    |_############|
      |___________|"""
 
logo3 = """
 ########  ##    ## ######## ##     ##  #######  ##    ##
 ##     ##  ##  ##     ##    ##     ## ##     ## ###   ##
 ##     ##   ####      ##    ##     ## ##     ## ####  ##
 ########     ##       ##    ######### ##     ## ## ## ##
 ##           ##       ##    ##     ## ##     ## ##  ####
 ##           ##       ##    ##     ## ##     ## ##   ###
 ##           ##       ##    ##     ##  #######  ##    ##
 """

logo4 = """
       ######  ##     ## ##      ## ########   ######
       ##    ## ###   ### ##  ##  ## ##     ## ##    ##
       ##       #### #### ##  ##  ## ##     ## ##
       ##       ## ### ## ##  ##  ## ########   ######
       ##       ##     ## ##  ##  ## ##              ##
       ##    ## ##     ## ##  ##  ## ##        ##    ##
       ######  ##     ##  ###  ###  ##         ######
"""

logo5 = """
       ########  ##     ##     #######     ##     ##  ######     ########  ##     ##     #######
       ##     ## ##     ##    ##     ##    ##     ## ##    ##    ##     ## ##     ##    ##     ##
       ##     ## ##     ##           ##    ##     ## ##          ##     ## ##     ##           ##
       ########  ##     ##     #######     ##     ##  ######     ########  ##     ##     #######
       ##         ##   ##     ##            ##   ##        ##    ##         ##   ##            ##
       ##          ## ##      ##             ## ##   ##    ##    ##          ## ##      ##     ##
       ##           ###       #########       ###     ######     ##           ###        #######
"""
def menu2():
	print "[1] Kembali Ke Menu Utama"
	print "[2] Keluar Dari Tools Ini"
	out()
	
def out():
	taktik = raw_input("Masukkan Pilihan Anda : ")
	if taktik == "":
		out()
	elif taktik == "1":
		os.system("clear")
		menu()
	elif taktik == "2":
		os.system("clear")
		print "Terima Kasih Telah Menggunakan Tools Ini"
		sleep(4)
		keluar()
	else:
		print "Masukkan Pilihan Yang Benar"
		sleep(3)
		os.system("clear")
		
def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()
 
def install():
	os.system('clear')
	os.system('pkg update && pkg upgrade')
	os.system('pkg install python')
	os.system('pkg install git')
	os.system('clear')

def menu():
	print logo1
	time.sleep(1)
	print " -----------------Mr XXXTRI3WSL-----------------  "
	print " ---------https://github.com/MrXXXTRI3WSL-------  "
	print " -------   =============================   -------"
	print " |  +  |   SILAHKAN PILIH MENU Tools nya   |  +  |"
	print " -------   =============================   -------"
	time.sleep(2)
	print 44*"="
	print "1). APA ITU PEMOGRAMAN PYTHON..?        "
	print 44*"="
	time.sleep(1)
	print "2). CARA MENAMBAHKAN WARNA PADA SCRIPT  "
	print 44*"="
	time.sleep(1)
	print "3). MENGENAL Mode Interaktif Python     "
	print 44*"="
	time.sleep(1)
	print "4). Python Versi 2 vs Python Versi 3    "
	print 44*"="
	pilih()

def pilih():
	kontol = raw_input("Masukkan Pilihan Anda : ")
	if kontol == "":
		print "[!]Masukkan Pilihan Anda[!]"
		sleep(2)
		pilih()
	elif kontol == "1":
		pengertian()
	elif kontol == "2":
		warna()
	elif kontol == "3":
		interaktif()
	elif kontol == "4":
		vs()
	else:
		print "Masukkan Pilihan Yang Benar"
		pilih()

def pengertian():
	install()
	print logo3
	print logo2
	print "\n\nAPA ITU PEMOGRAMAN PYTHON...?"
	time.sleep(1)
	print "\n\nPython merupakan bahasa pemrograman tingkat tinggi yang diracik oleh Guido van Rossum."
	time.sleep(2)
	print "\nPython banyak digunakan untuk membuat berbagai macam program, seperti: program CLI, Program GUI (desktop) "
	time.sleep(2)
	print "\nPython juga dikenal dengan bahasa pemrograman yang mudah dipelajari, karena struktur sintaknya rapi dan mudah "
	time.sleep(2)
	print "\nPython bagus untuk pemula yang belum pernah coding"
	menu2()
	
def warna():
	install()
	print logo4
	print logo2
	time.sleep(2)
	print "\n\nMenambahkan Warna Script di pemrograman python ada banyak sekali"
	time.sleep(5)
	print "\nMode interaktif merupakan fasilitas/fitur yang disediakan oleh Python sebagai tempat menulis kode secara interaktif."
	time.sleep(4)
	print "\nFitur ini dikenal juga dengan Shell,"
	time.sleep(4)
	print "\nConsole, REPL (Read Eval Print Loop), interpreter, dsb."
	menu2()

def vs():
	install()
	print logo5
	print logo2
	time.sleep(3)
	print "\n\nPython 3 menyimpan string secara default adalah Unicode"
	time.sleep(4)
	print "\nsedangkan toko Python 2 perlu mendefinisikan nilai string Unicode dengan u. Nilai variabel Python 3 tidak pernah berubah"
	time.sleep(4)
	print "\nMode interaktif merupakan fasilitas/fitur yang disediakan oleh Python sebagai tempat menulis kode secara interaktif."
	time.sleep(4)
	print "\nFitur ini dikenal juga dengan Shell,"
	time.sleep(4)
	print "\nConsole, REPL (Read Eval Print Loop), interpreter, dsb."
	menu2()
	
	
	
	
	
	
if __name__ == '__main__':
	menu()
