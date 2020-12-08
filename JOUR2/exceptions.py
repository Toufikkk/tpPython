#coding:utf8
try:
	a = int(input('Valeur a : '))
	b = int(input('Valeur b : '))
	assert a, b == int
	assert b != 0
	assert (a % 2) == 0
	result = a / b
	print (result)

except ValueError:
	print('Value error')