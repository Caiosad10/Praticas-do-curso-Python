#if else - desafio - ponto do steak

temperatura = int(input('Qual a temperatura da carne? '))

if temperatura < 48:
  print('A carne está crua') 
elif temperatura < 54:
  print('A carne está mal passada')
elif temperatura < 60:
  print('A carne está ao ponto')
elif temperatura < 65:
  print('A carne está bem passada')
elif temperatura >= 71:
  print('A carne está assada')

print('')

#Funções - Calculadora para pintura

rendimento_tinta = int(input('Qual o rendimento da tinta por metros? '))
altura_parede = int(input('Qual a altura da parede em que voce quer utilizar a tinta? '))
largura_parede = int(input('Qual a largura da parede em que voce quer utilizar a tinta? '))

def calculo_tinta():
  area = altura_parede * largura_parede
  rendimento = area / rendimento_tinta
  if rendimento == 1:
    print(f'Você precisa de {rendimento} lata de tinta') 
  else: 
    print(f'Você precisa de {rendimento} latas de tintas')

calculo_tinta()

print('')
#Sets - Filtrando funcionarios em uma empresa

funcionarios = ['Ana', 'Fernando', 'Victoria', 'Sergio', 'Lasanha', 'Fricasse']
turno_dia = ['Sergio', 'Lasanha', 'Fricasse']
turno_noite = ['Ana', 'Fernando', 'Victoria']
tem_carro = ['Sergio', 'Victoria', 'Lasanha']

TemCarro_noite = set(tem_carro) & set(turno_noite)
TemCarro_dia = set(tem_carro) & set(turno_dia)
NaoTemCarro = set(funcionarios) - set(tem_carro)

print(f'Os funcionarios que trabalham de noite e tem carro são: {TemCarro_noite}')
print('')

print(f'Os funcionarios que trabalham de dia e tem carro são: {TemCarro_dia}')
print('')

print(f'Os funcionarios que não tem carro são: {NaoTemCarro}')
print('')

#If elif - Calculo de IMC

alturaP = float(input('Digite sua altura em metros com centimetros: '))
pesoP = float(input('Digite seu peso em KG: '))

imc = pesoP / (alturaP/100) ** 2
if imc < 18.5:
  print(f'Seu IMC é {imc}')
  print('Magreza')
elif imc >= 18.6  and imc < 24.9:
  print(f'Seu IMC é {imc}')
  print('Normal')
elif imc >= 25.0  and imc < 29.9:
  print(f'Seu IMC é {imc}')
  print('Sobrepeso')
elif imc >= 30.0 and imc < 39.9:
  print(f'Seu IMC é {imc}')
  print('Obesidade')
elif imc >= 40:
  print(f'Seu IMC é {imc}')
  print('Obesidade Grave')