class Node:
    def __init__(self,titulo,genero,diretor,classificacao_indicativa,ano,codigo,situacao):
        self.titulo=titulo
        self.genero=genero
        self.diretor=diretor
        self.classificacao_indicativa=classificacao_indicativa
        self.ano=ano
        self.codigo=codigo
        self.situacao=situacao
        self.fila_reservas=FilaDeReservas()
        self.next=None

class ListaDeFilmes:
    def __init__(self):
        self.head=None
    
    def inserir_filme(self,titulo,genero,diretor,classificacao_indicativa,ano,codigo,situacao):
        new_filme=Node(titulo,genero,diretor,classificacao_indicativa,ano,codigo,situacao)
        if self.head is None:
            self.head=new_filme
            print("Filme adicionado com sucesso!")
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=new_filme
            print("Filme adicionado com sucesso!")

    def buscar_filme(self,titulo,genero):
        current=self.head
        while current is not None:
            if current.titulo == titulo and current.genero==genero:
                print(f"Titulo: {current.titulo} ")
                print(f"Gênero: {current.genero}")
                print(f"Diretor: {current.diretor}")
                print(f"Classificação Indicativa:{current.classificacao_indicativa}")
                print(f"Ano de Publicação: {current.ano}")
                print(f"Código do Filme: {current.codigo}")
                print(f"Situação: {current.situacao}")
                return
            current=current.next
        print("Filme não encontrado")
        return
    
    def mostrar(self):
        current=self.head
        while current is not None:
            print(f"{current.genero}: {current.titulo}")
            current=current.next

    def listar_por_genero(self):
        genero=str(input("Digite o gênero para listar os filmes disponíveis: "))
        print(f"Filmes - {genero}")
        current=self.head
        while current is not None:
            if current.genero==genero:
                print(f"{current.titulo}")
                return 
            current=current.next
        print("Não há filmes para esse gênero")
        return

    def remover_filme(self,codigo):
        codigo=str(input("Digite o código do filme que deseja remover: "))
        if self.head is None:
            print("Lista vazia")
            return
        if self.head.codigo==codigo:
            self.head=self.head.next
            print("Filme removido com sucesso")
            return
        current=self.head
        while current.next is not None and current.next.codigo!=codigo:
            current=current.next
            print("Filme removido com sucesso!")
        if current.next is not None:
            current.next=current.next.next
    
    def ordenar_por_genero(self):
        if self.head is None or self.head.next is None:
            return
        trocou=True
        while trocou:
            trocou=False
            current=self.head
            while current.next:
                if current.genero>current.next.genero:
                    current.titulo,current.next.titulo=current.next.titulo,current.titulo
                    current.genero,current.next.genero=current.next.genero,current.genero
                    current.diretor,current.next.diretor=current.next.diretor,current.diretor
                    current.classificacao_indicativa,current.next.classificacao_indicativa=current.next.classificacao_indicativa,current.classificacao_indicativa
                    current.ano,current.next.ano=current.next.ano,current.ano
                    current.codigo,current.next.codigo=current.next.codigo,current.codigo
                    current.situacao,current.next.situacao=current.next.situacao,current.situacao
                    trocou=True       
                current=current.next

class NodeFila:
    def __init__(self,cliente):
        self.cliente=cliente
        self.next=None

class FilaDeReservas: #em adicionar, vai chamar cliente, pois ele que vai ficar na fila de reserva e não o filme
    def __init__(self): #ja que cada filme ja terá sua própria lista de reservas
        self.front=None
        self._size=0
    
    def adicionar_na_fila(self,cliente):
        new_fila=NodeFila(cliente)
        if self.front is None:
            self.front=new_fila
        else:
            current=self.front
            while current.next is not None:
                current=current.next
            current.next=new_fila
        self._size+=1

    def retirar_da_fila(self):
        if self.is_empty():
            print("Fila de reserva vazia")
            return
        cliente=self.front.cliente
        self.front=self.front.next
        self._size-=1
        return cliente

    def peek(self):
        if self.is_empty():
            print("Fila de reserva vazia")
            return
        print(self.front.filme) 
        return

    def size(self):
        return self._size
    
    def is_empty(self):
        self._size==0
        return        

    def mostrar_filmes_reservas(self):
        filmes=[]
        current=self.front
        while current is not None:
            filmes.append(current.filme)
            current=current.next
        return filmes

class Cliente:
    def __init__(self,nome,idade,telefone,cpf):
        self.nome=nome
        self.idade=idade
        self.telefone=telefone
        self.cpf=cpf
        self.filmes_alugados=[]

class SistemaClientes:
    def __init__(self):
        self.clientes={} #dicionário para clientes

    def adicionar_cliente(self,nome,idade,telefone,cpf):
        if cpf in self.clientes:
            print("Usuário já cadastrado")
        else:
            self.clientes[cpf]=Cliente(nome,idade,telefone,cpf)
            print("Cliente adicionado com sucesso")

    def buscar_cliente(self,cpf):
        if cpf in self.clientes:
            cliente=self.clientes[cpf]
            print(f"Nome: {cliente.nome}/idade:{cliente.idade}/telefone:{cliente.telefone}")
        else:
            print("Cliente não encontrado")
    
    def alugar_filme(self,lista_filmes,cpf,titulo,codigo): #lista_filmes é o objeto que será criado da classe ListaDeFilmes
        cliente=self.buscar_cliente(cpf)
        if not cliente:
            print("Cliente não encontrado")
            return
        current=lista_filmes.head
        while current is not None:
            if current.titulo==titulo:
                if cliente.idade>=current.classificacao_indicativa:
                    if current.situacao=="Disponível":
                        current.situacao= "Alugado"
                        print(f"{cliente.nome} alugou o filme '{current.titulo}'-({current.codigo}) com sucesso!")
                    else:
                        print(f"{current.titulo} não está disponível")
                        print(f"Adicionando para a fila de reservas para o cliente {current.nome}")
                        current.fila_reservas.adicionar_na_fila(cliente)
                else:
                    print("Você não possui idade para a classificação indicativa desse filme. Aluguel cancelado")
                return
            current=current.next
        print("Filme não encontrado")
    
    def devolver_filme(self,lista_filmes,cpf,titulo,codigo):
        cliente=self.buscar_filme(cpf)
        current=lista_filmes.head
        while current is not None:
            if current.titulo==titulo and current.codigo==codigo:
                if current in cliente.filmes_alugados:
                    cliente.filmes_alugados.remove(current)
                    
                    if not current.fila_reservas.is_empty():
                        proximo_cliente=current.fila_reservas.retirar_da_fila()
                        proximo_cliente.filmes_alugados.append(current)
                        print(f"{cliente.nome} devolveu '{current.titulo}'.")
                        print(f"O filme foi reservado automaticamente para {proximo_cliente.nome}.")
                    else:
                        current.situacao=="Disponível"
                        print(f"{cliente.nome} devolveu '{current.titulo}'. Agora está disponível para aluguel.")
                else:
                    print(f"O cliente {cliente.nome} não possui este filme alugado.")
                return
            current=current.next
        print("Filme não encontrado")




        




lista=ListaDeFilmes()
lista.inserir_filme("Paola e as aventuras","romance", "Lucas", 19,2023,"1234", "Disponivel")
lista.inserir_filme("o medo","Terror","Joao", 18,2001,"0987","Disponivel")
lista.inserir_filme("Velozes e Furiosos","Ação","Homem", 16,2010,"6789","Disponivel")
lista.inserir_filme("Amor","Drama","austin",10,2011,"6543","Disponivel")
lista.inserir_filme("socorro","Terror","ain",18,2021,"8726","Reservado")

print("Antes de ordenar por genero")
lista.mostrar()
#lista.listar_por_genero()
#lista.buscar_filme("o medo", "Terror")
#lista.remover_filme(1234)
#lista.listar_por_genero()
lista.ordenar_por_genero()
print("-------------------------------")
print("Depois de ordenar por genero")
lista.mostrar()


