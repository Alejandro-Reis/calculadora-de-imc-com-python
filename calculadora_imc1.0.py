print('Bem vindo a calculadora de imc...')

nome=input('Qual o seu nome?' ) 

altura=float(input('Qual a sua altura?' ))

peso=float(input('Qual o seu peso?' ))

imc= (peso) / (altura*altura)

print(f'Seu nome é: {nome} \nsua altura é: {altura:.2f} \nseu peso é: {peso} \ne seu imc é: {imc:.2f}')
