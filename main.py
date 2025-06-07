from atividade1 import Pessoa
from atividade2 import CalculadoraSimples
from atividade3 import Carro
from atividade4 import Cachorro
from atividade5 import Produto



#atividade 1

pessoa1 = Pessoa("Luise", 25)
pessoa1.apresentar()  

pessoa2 = Pessoa("Lucas", 20)
pessoa2.apresentar()  

#atividade 2

calc = CalculadoraSimples()

print("Soma: ", calc.somar(10, 5))
print("Subtração: ", calc.subtrair(10, 5))
print("Multiplicação: ", calc.multiplicar(10, 5))
print("Divisão: ", calc.dividir(10, 5))
print("Divisão por zero: ", calc.dividir(10, 0))

#atividade 3

carro1 = Carro("Fusca")

carro1.mostrar_velocidade()  
carro1.acelerar()
carro1.mostrar_velocidade()  
carro1.acelerar()
carro1.mostrar_velocidade()  
carro1.frear()
carro1.mostrar_velocidade()  
carro1.frear()
carro1.frear()  
carro1.mostrar_velocidade()  

#atividade 4

cachorro1 = Cachorro("Apolo", "Labrador")
cachorro2 = Cachorro("Amora", "Poodle")
cachorro3 = Cachorro("Paçoca", "Pastor Alemão")

cachorro1.latir()
cachorro2.latir()
cachorro3.latir()

#atividade 5

produto1 = Produto("Arroz", 5.99, 10)

produto1.mostrar_estoque()

produto1.comprar(5)
produto1.mostrar_estoque()

produto1.comprar(10)  

produto1.repor(20)
produto1.mostrar_estoque()