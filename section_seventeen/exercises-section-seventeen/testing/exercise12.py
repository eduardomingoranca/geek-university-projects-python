"""
Baseando-se no exercicio 11 adicione os atributos menorMarcha e maiorMarcha,
onde o atributo menorMarcha indica qual sera a menor marcha possivel para a
moto e o atributo maiorMarcha indica qual sera a maior marcha possivel. Desta
forma os metodos marchaAcima e marchaAbaixo devem ser reescritos de forma
a nao permitirem a troca de marchas para valores abaixo da menorMarcha e
acima da maiorMarcha. O metodo imprimir deve ser modificado de forma a
mostrar na tela os valores de todos os atributos.
"""
from classes.vehicle import Motorcycle

m1 = Motorcycle('Harley Davidson', 'Nighster', 'Blue', 3, 'null')

print(m1.__gear_up__(3))
print(m1.__gear_down__(2))

