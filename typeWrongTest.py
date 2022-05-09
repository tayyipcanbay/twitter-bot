import random
import string
import time
from turtle import pos


def writeSome(str, count):
    print("-------------------------------------------------------------------")
    maxWrong = int(len(str) / 3)  # maksimum kaç harf yanlış olacak
    print(maxWrong)
    countWrong = random.randrange(
        1, maxWrong
    )  # random ile yanlış olacak harf sayısını belirler
    position = []

    for i in range(countWrong):
        position.append(
            random.randrange(0, len(str))
        )  # yanlış yazılacak pozisyonu belirler
    # position arrayi sort edilmeli
    position.sort()
    print(position)
    position = list(dict.fromkeys(position))
    print(position)
    time.sleep(3)
    j = 0
    for i in range(len(str)):
        if position[j] == i:  # Burası ile alakalı bir problem
            rnd = random.choice(string.ascii_letters.casefold())
            print(rnd)
            time.sleep(random.random())
            print("Delete")
            time.sleep(random.random())
            print(str[i])
        else:
            time.sleep(random.random())
            print(str[i])

    print("-------------------------------------------------------------------")
    count += 1


count = 0
for i in range(100):
    writeSome("Deneme yazısı Yazıyorum", count=count)
