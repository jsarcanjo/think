entrada_usuario = input("Digite uma sequencia de notas separado por virgula:")
notas = []
for nota_texto in entrada_usuario.split(","):
 notas.append(int(nota_texto))

total = 0
for nota in notas:
 total += nota
media = 0
media = total /len(notas)
print(f"A média das notas é  {media}")

 
 


            