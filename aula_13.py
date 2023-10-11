cidade = 'são carlos'
endereco = 'Rua Candido Padim, 25 - Vila Prado'
completo = cidade + endereco
print(cidade.startswitch('São'))
print(cidade.endswitch('Los'))
print('Rua' in completo)
print('Avenida' not in endereco)

n = 'text'
a = n.ljust(90)
print(a)



nomes = "joão paulo /maria paula/ana beatriz/jose pedro"
print(nomes.split('/))'))

nomes = "joão paulo \nmaria paula\nana beatriz\njose pedro"
print(nomes.splitlines())


n = float(input())
c = str(n)
print(c)
print(c.split('.'))

f = 'ai dios mio'

f1 = f.replace('dios', 'ai')
f2 = f.replace('','#')
print(f1)
print(f2)

print("-"*30)

for x in str(input("Digite seu nome: ")):
   print(x)
for x in input("Digite seu nome: "):
   print(x)