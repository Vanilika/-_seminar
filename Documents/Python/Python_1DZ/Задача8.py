#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

#*Пример:*

#3 2 4 -> yes
#3 2 1 -> no

length = int(input("длина шоколадки: "))
width = int(input("ширина шоколадки: "))
slices = int(input("cколько долек отломить?: "))
if slices % length == 0 or slices % width == 0:
    print("шоколад можно разломить")

else:
    print("Так не делится")
    