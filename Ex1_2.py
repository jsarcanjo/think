
entrada_usuario = input("Digite os números separado por virgula")
numeros = []

for numero_texto in entrada_usuario.split(","):
            numeros.append(int(numero_texto))

maior_numero = 0 

for numero in numeros:
  if  numero > maior_numero:
maior_numero = numero
print(f"O maior numero é : {maior_numero}")