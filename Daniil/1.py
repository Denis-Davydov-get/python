import random  # импорт модуля random

messages_count = random.randint(1, 5)
UU = random.randint(1, 4)
RR = random.randint(5, 30)
TT = random.randint(5, 30)
if messages_count == 1:
    print(f'Сделай {UU} подтягиваний ')
elif messages_count == 2:
    print(f'Сделай {RR} упражений на пресс ')
elif messages_count == 3 :
    print(f'Сделай {TT} отжиманий ')
else:
    print('Сегодня отдыхай')
