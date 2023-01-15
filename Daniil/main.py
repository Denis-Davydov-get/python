import random
import eel
eel.init("web")
eel.start("main.html",size=(700,700))
print("введите число от 1 до 8")
patrons_gun = 8
your_lucky = 0
while 1:
    where_patron = random.randint(1,8)
    print(where_patron)
    fire = int(input())
    if where_patron == fire :
        print("Вы мертвы.")
    else:
        print("Вы выиграли.)
        your_lucky + 1
