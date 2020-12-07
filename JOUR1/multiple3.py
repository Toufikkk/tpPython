#coding:utf8
N=int(input("tapez un nombre"))

if (N%2)==0:
	if N%3==0:
		print("Ce nombre est pair et il est multiple de 3")
	else:
		print("Ce nombre est pair et pas multiple de 3")
if (N%2)!=0:
	if N%3==0:
			print("Ce nombre est impaire et il est multiple de 3")
	else:
			print("Ce nombre est ni pair ni multiple de 3")