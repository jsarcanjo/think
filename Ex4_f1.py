fatorial = int(input("Digite um número:"))
resultado = 1
for numero in range(fatorial, 1, -1):
  resultado *= numero
print(f"O fatorial de {fatorial} e {resultado}")
 
