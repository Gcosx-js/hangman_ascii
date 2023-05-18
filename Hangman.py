import time
import os
import random
sozler = {'soyuducu':'Elektronik məişət əşyasıdır',
           'kitab':'Bilgi vasitəsidir',
           'python':"Proqramlaşdırma dilidir",
           'informatika':'Fənn adıdır',
           'telefon':'Elektronik elaqe vasitesidir',
           'qələm':'Yazı yazmaq üçün istifadə olunan əşya'} #word_db
soz = random.choice(list(sozler.keys()))
ipucu = sozler[soz]
tap = list(["_"] * len(soz))
s = 4
Tr = [] #Islenmis dogru herflerin siyahisi
Yr = [] #Islenmis yalnis herflerin siyahisi
hangman_images = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

while True:
    if '_' not in tap:
        print("---------------------\nTəbriklər,Qazandınız : {0} \n---------------------".format(soz))
        time.sleep(3)
        os.system('cls')
        break
    print("\nSöz : ",' '.join(tap)," >> {0}".format(ipucu))
    print(hangman_images[len(hangman_images) - 1 - s])
    daxil = str(input("Daxil edin : "))
    user = daxil.lower()
    if user in Tr or user in Yr:
        print("Bu seçimi daha öncə etmisiniz!")
        time.sleep(2)
        os.system('cls')
        continue
    if user in soz:
        Tr.append(user)
        for i in range(len(soz)):
            if soz[i] == user:
                tap[i] = user
                os.system('cls')
    else:
        s-=1
        print("Yalnış!,Qalan cəhd sayınız : %s"%s)
        time.sleep(2)
        os.system('cls')
        Yr.append(user)
        if s <= 0:
            print(hangman_images[len(hangman_images) - 1 - s])
            print("Uduzdunuz : {0}".format(soz))
            time.sleep(3)
            os.system('cls')
            break
