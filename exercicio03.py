from tkinter import N


primeiroNome = input('Digite seu primeiro nome: ')
print('Digite agora seu salário \N')
salarioReais = input('Reais: ')
salarioCentavos = input('Centavos')
salarioFormatado = salarioReais + ',' + salarioCentavos
mensagem = "o salario de " + primeiroNome + "no mês de abril foi de R$ "+ salarioFormatado + ""
print(mensagem)
