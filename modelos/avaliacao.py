class Avaliacao:
    '''Representa a avaliação e suas características
    
    Parâmetros:

    - Cliente (str): O nome do clinte
    - Nota (str): A nota que o cliente dá ao restaurante 
    
    '''

    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota