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
        print('\t1: Cek Saldo \n\t2: Debet\n\t3: Simpan\n\t4: Ganti Pin\n\t5: Keluar')
        menu = int(input('> Pilihan:'))

        if menu==1:
            print('Saldo Anda saat ini: Rp.'+ str(atm.checkBalance()))
        elif menu==2:
            # meminta nominal yang igin didebet
            nominal = int(input('Nominal debet: '))
            
            # melakukan verifikasi
            verification = input('KONFIRMASI: Anda akan menarik uang sebanyak',str(nominal),'?(y/n)')
            if verification=='y':
                print('Saldo awal Anda: Rp.'+str(atm.checkBalance()))
            else:
                break

            # pengecekan saldo
            if nominal>atm.checkBalance():
                print('Saldo Anda tidak mencukupi')
                continue
            else:
                atm.withdrawBalance(nominal)
                print('Debet saldo berhasil...')
                print('Saldo Anda saat ini: Rp.'+str(atm.checkBalance()))
                continue
        elif menu==3:
            nominal = int(input('Nominal: '))
            
            verification = input('KONFIRMASI: Anda akan menambahkan saldo sebanyak',str(nominal),'?(y/n)')
            if verification=='y':
                print('Saldo awal Anda: Rp.'+str(atm.checkBalance()))
            else:
                break

            atm.depositBalance(nominal)
            print('Saldo Anda saat ini: Rp.'+str(atm.checkBalance()))
        elif menu==4:
            verify_pin = int(input('Masukkan PIN Anda saat ini: '))
            if verify_pin==atm.checkPin():
                newPin = int(input('Masukkan PIN baru Anda: '))
                verification = input('KONFIRMASI: Anda akan mengubah PIN',str(nominal),'?(y/n)')
                
                if verification=='y':
                    atm.changePin(newPin)
                else:
                    break
        elif menu==5:
        else: