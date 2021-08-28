from atm_card import AtmCard
from customer import Customer
import random
import datetime

atm = Customer(id)

while True:
    id = int(input('Masukkan PIN awal: '))
    trial = 0

    while id != int(atm.checkPin()) and trial<3:
        id = int(input('PIN yang Anda masukkan salah, coba lagi!: '))
        trial+=1

    if trial >= 3:
        print('ERROR: PIN yang Anda masukkan salah')
        exit()