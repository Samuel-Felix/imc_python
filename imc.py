# módulo imc
import estado_imc as calcular

peso = 0
altura = 0.0
nome = ""

nome = input("Informe o Nome do paciente: ")

erro = True
while erro:
    try:
        peso = int(input("Informe o peso do paciente: "))
        erro = False
    except:
        print("Valor Indesejado")

erro = True
while erro:
    try:
        altura = float(input("Informe a altura do paciente: "))
        erro = False
    except:
        print("Valor Invalido!")

calcular.calcular_imc(peso, altura)