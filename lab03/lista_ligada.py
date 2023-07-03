from estrutura_elementar import estrutura_elementar


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def set_proximo(self, no):
        self.proximo = no

    def get_proximo(self):
        return self.proximo


class LinkedList(estrutura_elementar):
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            novoNo.set_proximo(self.inicio)
            self.inicio = novoNo

    def inserir_fim(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            aux = self.inicio
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
            aux.set_proximo(novoNo)
#---------------------------------------------------
    def esta_vazio(self) -> bool:
        if self.inicio is None:
            return True
        else:
            return False
#---------------------------------------------------
    def remove(self, item):
        tep = self.inicio
        if tep is not None:
            if tep.valor == item:
                self.inicio = tep.proximo
                tep = None
                return
            
            while tep is not None:
                if tep.valor == item:
                    break
                prev = tep
                tep = tep.proximo
                
            if tep == None:
                return
            prev.proximo = tep.proximo
            tep = None
                  
#---------------------------------------------------    
    def tamanho(self) -> int:
        if self.inicio is None:
            return 0
        else:
            cont = 1
            aux = self.inicio
            while aux.get_proximo() is not None:
                cont = cont+1
                aux = aux.get_proximo()
                
            return cont

#
    def limpa(self):
        pass
                
#--------------------
    def procura(self, item) -> bool:
        if item > self.tamanho():
            return False
        if item <= self.tamanho():
            cont = 1
            aux = self.inicio
            while aux.get_proximo() is not None:
                cont = cont+1
                aux = aux.get_proximo()        
            return True
        
        return False
#-------
    def indice_de(self, item):
        if item <= self.tamanho():
            cont = 1
            aux = self.inicio
            while aux.get_proximo() is not None:
                if aux == item:
                    return cont
                else:
                    cont=cont+1
                    aux = aux.get_proximo()        
            
        if item > self.tamanho():
            return -1 
#-------
    def recupera_indice(self, index):
        if index > self.tamanho():
            return None
        
            
        if index < self.tamanho():
            cont = 0
            aux = self.inicio
            while aux.get_proximo() is not None:
                
                    if cont == index:
                        return #aux.valor
                    else:
                        cont=cont+1
                        aux = aux.get_proximo()
                
            return  
        
