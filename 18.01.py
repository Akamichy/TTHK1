﻿#def Loe_failist(fail:str)->list:
#    jarjend = []
#    f = open(fail,'r', encoding = "utf-8-sig")
#    for rida in f:
#        jarjend.append(rida.strip())
#    f.close()
#    return jarjend
from random import * 
from funktsioonid import *
def Kirjuta_failisse(fail:str, jarjend:list):
    f = open(fail, 'w', encoding = "utf-8-sig")
    for item in jarjend:
        f.write(item+'\n')
    f.close()

#paevad = Loe_failist("TextFile1.txt")
#print(paevad)

#list_=[]
#for i in range(5):
#    nimi=input(str(i+1)+ ".slovo ")
#    list_.append(nimi)
#Kirjuta_failisse("est.txt", list_)

def file_read(fail:str) -> list:
    order = []
    ff = open(fail, 'r', encoding = "utf-8-sig")
    for j in ff:
        order.append(j.strip())
    ff.close()
    return order

reading = file_read("rus.txt")
reading2 = file_read("est.txt")
#print(reading, reading2)

#while True:
def spisok():
    print("Словарь:")
    for i, (ru, est) in enumerate(zip(reading, reading2), start=1):
        print(f"{i}.{ru} - {est}")
    print("0 - выход")
spisok()
print("""
1. Добавление нового слова в словарь
2. Удаление имеющегося слова из словаря
3. Исправление ошибки в словаре
4. Проверка знаний
5. TTS 
""")


choice = input("Выберите операцию: ")
if choice == "1":
    newrus = input("Пожалуйста, введите слово: ")
    newest = input("Palun, tõlkige see sõna: ")
    reading.append(newrus)
    reading2.append(newest)
    Kirjuta_failisse("rus.txt", reading)
    Kirjuta_failisse("est.txt", reading2)
spisok()

if choice == "2":
    ch = int(input("Пожалуйста, введите порядковый номер слова, которое хотите удалить: "))
    if ch == 0:
        exit()
    else:
        reading.pop(ch-1)
        reading2.pop(ch-1)
        spisok()

elif choice == "3":
    ch1 = int(input("Пожалуйста, введите порядковый номер слова, которое хотите исправить: "))
    if ch1 == 0:
        exit()
    else:
        #venesona()
        #eestisona()
        newrus = input("Верное написание слова: ")
        newest = input("Uus sõna ilma vigadeta: ")
        reading[ch1-1] = newrus
        reading2[ch1-1] = newest
        Kirjuta_failisse("rus.txt", reading)
        Kirjuta_failisse("est.txt", reading2)
        spisok()



elif choice == "4":
    score = 0
    for i in range(50):
        print( )
    for _ in range(len(reading)):
        randd = randint(1, len(reading))
        word = reading[randd-1]
        word2 = reading2[randd-1]
        ind1 = reading.index(word)
        ind2 = reading2.index(word2)
        ans = input(f'Как переводится слово {word2}?: ').capitalize()
        if ans == word:
            if ind1 == ind2:
                score += 1
        else:
            print(f'Неверно! Правильный ответ: reading2[ind2]!')

    howm = score/len(reading)
    print(f'Вы набрали {(howm)*100}%')

        
    

#with open('Nimed.txt', 'r') as f:
#    print(f.read())

#from os import *
#if path.isfile("Nimed.txt"): 
#    remove("Nimed.txt")
