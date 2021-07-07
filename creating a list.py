words = input("Введите что хотите написать:")
quantity = int(input("Введите количество повторений:"))
tring = 0
open = open("list.txt","w",encoding="utf-8")

while tring<=quantity:
    tring = tring + 1
    open.write(words + " \n")