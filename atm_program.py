from atm_card import AtmCard
from customer import Customer
from tkinter import *
import random
import datetime

atm = Customer('pdk0T11', 460550, 700000)

while True:
    id = int(input('> Masukkan PIN Anda: '))
    trial = 0

    while id != int(atm.checkPin()) and trial<3:
        print('PIN yang Anda masukkan salah, coba lagi!')
        id = int(input('> Masukan PIN Anda: '))
        trial+=1

    if trial >= 3:
        print('ERROR: PIN yang Anda masukkan salah')
        exit()

    while id == int(atm.checkPin()):
        print('Selamat datang, di aplikasi ATM Machine ini...')
        print('Berikut adalah menu-menu yang dapat Anda pilih:')
        print('\t1: Cek Saldo \n\t2: Debit\n\t3: Simpan\n\t4: Ganti Pin\n\t5: Keluar')
        menu = int(input('> Pilihan:'))