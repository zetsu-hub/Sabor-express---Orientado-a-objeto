
from modelos.avaliacao import Avaliacao
import os

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria): #Faz com que, quando vamos criar um novo restaurante, coloquemos o seu nome e sua categoria, para salvar de uma vez

        self.nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
        

    def __str__(self): #Apresenta o nome, categoria e etc... do restaurante em forma de texto
        return f'{self.nome} | {self.categoria}'
    
    @classmethod #Ele motra que o 'Listar_restaurantes' é um método da classe 

    def listar_restaurantes(cls): #Faz uma lista de todos os restaurantes criandos
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliações'.ljust(25)} |{'Status'.ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Funcionando' if self._ativo else 'Não está funcionando'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacoes(self, cliente, nota = ''):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        


    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_nota = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_nota, 1)
        return media

    



