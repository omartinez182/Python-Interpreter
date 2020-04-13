def main():
	print("Ingrese primer numero: ")
	num1 = 0.0
	num1 = input()
	print("Ingrese segundo numero: ")
	num2 = 0.0
	num2 = input()
	print("Ingrese tercer numero: ")
	num3 = 0.0
	num3 = input()
	if ((num1  >=  num2) and (num1  >=  num3)):
		print(num1)
		if (num2 >= num3):
			print(num2)
			print(num3)
		else:
			print(num3)
			print(num2)
	else:
		if ((num2  >=  num1) and (num2  >=  num3)):
			print(num2)
			if (num1 >= num3):
				print(num1)
				print(num3)
			else:
				print(num3)
				print(num1)
		else:
			if ((num3  >=  num1) and (num3  >=  num2)):
				print(num3)
				if (num1 >= num2):
					print(num1)
					print(num2)
				else:
					print(num2)
					print(num1)

	print("Ingrese numero: ")
	numero = 0
	numero = input()
	contador = 0
	while (int(contador) != int(numero)):
		contador = contador+1
		print(contador)
main()
