#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо
a = int(input('введите число:'))
z = list(range(- a, a + 1))
print(z)
k = - 2
z = z[k:] + z[:k]
print(z)