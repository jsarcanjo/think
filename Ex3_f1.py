numeros_inteiros = [5, 2, 3, 20]
soma_par = 0
soma_impar = 0

for numero in numeros_inteiros:
  resto_divisao = numero % 2            
  if resto_divisao == 0:
    soma_par += numero
  else:
    soma_impar += numero

print(f"Soma par: {soma_par}\nSoma impar: {soma_impar}")         
