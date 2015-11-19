imposto = float(input("Imposto: "))
if imposto < 10:
	print("Médio")
elif imposto < 27.5:
	print("Alto")
else:
	print("Muito alto")

imposto = 0.3
print("Alto" if imposto > 0.27 else "Baixo")

imposto = 0.10
print("Alto" if imposto > 0.27 else "Baixo")

imposto = 0.4
valor_imposto = "Alto" if imposto > 0.27 else "Baixo"
print (valor_imposto)
