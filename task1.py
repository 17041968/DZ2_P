#Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
a = int(input('Введите число '))
for i in range(a, a + 1):
	c = [i]
	for item in c:
		fact = 1
		for number in range(1, item + 1):
			fact = fact * number
			print("{} ! = {}".format(item, fact))