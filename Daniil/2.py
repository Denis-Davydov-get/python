import random  # импорт модуля random
messages_count = random.randint(1, 3)
UU = random.randint(1, 7)
RR = random.randint(5, 30)
TT = random.randint(5, 30)
if UU >= 11 and UU <= 19:
    word = "подтягиваний"
else:
    if UU % 10 == 1:
        print word = "подтягивание"
elif UU % 10 in (2,3,4):
    word = "подтягивания"
else 
    print(f'Сделай {UU} подтягиваний')
