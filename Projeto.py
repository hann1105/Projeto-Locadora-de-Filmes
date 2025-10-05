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
                return current
            current=current.next
        print("Filme não encontrado")
        return None
    
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
        trocou=True #bubble short para a ordenação
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
        print("\nFilmes ordenados por gênero:")
        current=self.head
        while current is not None: # para mostrar a lista ordenada
            print(f"{current.genero}: {current.titulo}")
            current=current.next

class NodePilha:
    def __init__(self,filme):
        self.filme=filme
        self.next=None

class Pilha:
    def __init__(self):
        self.topo=None
        self.tamanho=0

    def push(self,filme):
        new_node=NodePilha(filme)
        new_node.next=self.topo
        self.topo=new_node
        self.tamanho+=1

    def is_empty(self):
        return self.tamanho==0

    def mostrar_cinco_ultimos(self):
        if self.is_empty():
            print("Nenhum filme foi alugado recentemente")
        print("Os 5 último filmes alugados foram:")
        current=self.topo
        contador=0
        while current is not None and contador<5:
            print(f"{current.filme.titulo} - {current.filme.genero}")
            current=current.next
            contador+=1
        return

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
        print(self.front.cliente) 
        return

    def size(self):
        return self._size
    
    def is_empty(self):
        return self._size==0
               

    def mostrar_filmes_reservas(self):
        clientes_fila=[]
        current=self.front
        while current is not None:
            clientes_fila.append(current.cliente)
            current=current.next
        return clientes_fila

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
            return cliente
        else:
            print("Cliente não encontrado")
            return
    
    def alugar_filme(self,lista_filmes,cpf,titulo,codigo,pilha_alugueis): #lista_filmes é o objeto que será criado da classe ListaDeFilmes
        cliente=self.buscar_cliente(cpf)
        if not cliente:
            #print("Cliente não encontrado")
            return
        current=lista_filmes.head
        while current is not None:
            if current.titulo==titulo:
                if cliente.idade>=current.classificacao_indicativa:
                    if current.situacao=="Disponivel":
                        current.situacao= "Alugado"
                        cliente.filmes_alugados.append(current) #adicionando a lista de filmes alugados do cliente
                        pilha_alugueis.push(current)
                        print(f"{cliente.nome} alugou o filme '{current.titulo}'-({current.codigo}) com sucesso!")
                    else:
                        print(f"{current.titulo} não está disponível")
                        print(f"Adicionando o cliente {cliente.nome} para a lista de reservas do filme '{current.titulo}'")
                        current.fila_reservas.adicionar_na_fila(cliente) #adicionando o cliente na fila de reservas
                else:
                    print("Você não possui idade para a classificação indicativa desse filme. Aluguel cancelado")
                return
            current=current.next
        print("Filme não encontrado")
    
    def devolver_filme(self,lista_filmes,cpf,titulo,codigo):
        cliente=self.buscar_cliente(cpf)
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
                        current.situacao="Disponivel"
                        print(f"{cliente.nome} devolveu '{current.titulo}'. Agora está disponível para aluguel.")
                else:
                    print(f"O cliente {cliente.nome} não possui este filme alugado.")
                return
            current=current.next
        print("Filme não encontrado")

class Locadora: #Classe Principal que chama os métodos para a iteração com o usuário
    def __init__(self):
        self.lista = ListaDeFilmes()        # a lista única de filmes
        self.sistema = SistemaClientes() # sistema único de clientes
        self.pilha_alugueis=Pilha()

        self.lista.inserir_filme("Paola e as aventuras","romance", "Lucas", 19,2023,"1234", "Disponivel")
        self.lista.inserir_filme("o medo","Terror","Joao", 18,2001,"0987","Disponivel")
        self.lista.inserir_filme("Velozes e Furiosos","Ação","Homem", 16,2010,"6789","Disponivel")
        self.lista.inserir_filme("Amor","Drama","austin",10,2011,"6543","Disponivel")
        self.lista.inserir_filme("socorro","Terror","ain",18,2021,"8726","Alugado")
        
           
        return
    def menu_cliente(self):
        while True:
            print("                       *            MENU               *                          ")
            print("A - Alugar filme" \
            "      L - Listar filmes por gênero" \
            "      D - Devolver filme" \
            "      B - Buscar filmes" \
            "      F - Visualizar Fila de Reserva de um filme" \
            "      I - Voltar a Tela inicial" \
            "      S - Sair" \
            "       ")
            
            
            opcaocliente=str(input("Digite uma opção para ter acesso as funções: "))
            if opcaocliente.lower()=="a":
                titulo=str(input("Digite o título do filme: "))
                cpf=str(input("Digite seu CPF: "))
                codigo=str(input("Digite o código do filme:"))
                alugar=self.sistema.alugar_filme(self.lista,cpf,titulo,codigo,self.pilha_alugueis)

            elif opcaocliente.lower()=="l":
                listar=self.lista.listar_por_genero()

            elif opcaocliente.lower()=="d" :
                cpf1=str(input("Digite seu CPF: "))
                titulo1=str(input("Digite o título do filme que deseja devolver: "))
                codigo1=str(input("Código do filme: "))
                devolver=self.sistema.devolver_filme(self.lista,cpf1,titulo1,codigo1) 

            elif opcaocliente.lower()=="f":
                    titulo3=str(input("Digite o título do filme: "))
                    genero=str(input("Digite o gênero do filme: "))
                    filme=self.lista.buscar_filme(titulo3,genero)
                    if filme:
                        reservas = filme.fila_reservas.mostrar_filmes_reservas()
                        if reservas:
                            print( (f"\nFila de reservas para o filme '{filme.titulo}':"))
                            for i, cliente in enumerate(reservas, start=1):
                                print(f"{i}º - {cliente.nome} (CPF: {cliente.cpf})")
                        else:
                            print("Não há reservas para este filme.")
                    else:
                        print("Filme não encontrado.")


            elif opcaocliente.lower()=="b":
                titulo2=str(input("Digite o título do filme que deseja pesquisar: "))
                genero2=str(input("Digite o gênero do filme: "))
                buscarfilme=self.lista.buscar_filme(titulo2,genero2)

            elif opcaocliente.lower()=="i":
                return self.inicio()
            
            elif opcaocliente.lower()=="s":
                print("Saindo do sitema...")
                break

            else:
                print("Opção inválida")

    def menu_funcionario(self):
        print("*                *               *    MENU - SISTEMA INTERNO    *                *              * ")
        print("I - Inserir filme" \
        "      R - Remover filme " \
        "      B - Buscar cliente " \
        "      F - Visualizar Fila de Espera de um filme" \
        "      L - Buscar livros por gênero" \
        "      LI - Listar filmes" \
        "      O - Ordenar por gênero" \
        "      P - Ver últimos 5 filmes alugados" \
        "      S - Sair")
        

    def inicio (self):
        print()
        print(" ----------------------------------------------")
        print("                 LOCADORA PH                   ")
        print("-----------------------------------------------")
        print()
        entrada=str(input("Bem vindo!Já possui cadastro?[S/N]"))
        if entrada.lower()=="s":
            usuario=str(input("Digite seu CPF: "))
            if usuario== "139778": #Se tiver esse cpf é funcionário da livraria
                while True:
                    print()
                    funcionario=self.menu_funcionario()
                    opcaofuncionario=str(input(" Escolha uma opção para navegar no Sistema da Locadora: "))
                    print()
                    if opcaofuncionario.lower()=="i":
                        print( "           CADASTRO DE FILMES         ")
                        titulo=str(input(" Insira o Título: "))
                        genero=str(input(" Insira o gênero: "))
                        diretor=str(input(" Insira o diretor: "))
                        classificacao_indicativa=int(input(" Insira a classificação Indicativa: "))
                        ano=int(input(" Insira o ano de lançamento: "))
                        codigo=str(input(" Insira o código do filme: "))
                        situacao=str(input(" Situação do filme: "))
                        inserir=self.lista.inserir_filme(titulo,genero,diretor,classificacao_indicativa,ano,codigo,situacao)
                        
                    elif opcaofuncionario.lower()=="r":
                        codigo=str(input("Digite o código do filme que deseja remover: "))
                        remover=self.lista.remover_filme(codigo)

                    elif opcaofuncionario.lower()=="b":
                        cpf=str(input("Digite o CPF do cliente que deseja pesquisar: "))
                        buscar=self.sistema.buscar_cliente(cpf)
                        
                    elif opcaofuncionario.lower()=="f":
                        titulo3=str(input("Digite o título do filme: "))
                        genero=str(input("Digite o gênero do filme: "))
                        filme=self.lista.buscar_filme(titulo3,genero)
                        if filme:
                            reservas = filme.fila_reservas.mostrar_filmes_reservas()
                            if reservas:
                                print( (f"\nFila de reservas para o filme '{filme.titulo}':"))
                                for i, cliente in enumerate(reservas, start=1):
                                    print(f"{i}º - {cliente.nome} (CPF: {cliente.cpf})")
                            else:
                                print("Não há reservas para este filme.")
                        else:
                            print("Filme não encontrado.")

                    elif opcaofuncionario.lower()=="l":
                        titulo1=str(input("Digite o Título do filme:"))
                        genero=str(input("Digite o gênero do filme: "))
                        buscarlivro=self.lista.buscar_filme(titulo1,genero)

                    elif opcaofuncionario.lower()=="li":
                        mostrar=self.lista.mostrar()
                        
                    elif opcaofuncionario.lower()=="o":
                        ordenar=self.lista.ordenar_por_genero()

                    elif opcaofuncionario.lower()=="p":
                        self.pilha_alugueis.mostrar_cinco_ultimos()
                        
                    elif opcaofuncionario.lower()=="s":
                        print("Saindo do sistema do funcionário...")
                        return self.inicio()
                    else:
                        print("Opção inválida")

            elif usuario in self.sistema.clientes:
                self.menu_cliente()
        elif entrada.lower()=="n":
            print()
            print("               CADASTRO DE USUÁRIO           ")
            nome=str(input("Digite seu nome e sobrenome: "))
            idade=int(input("Digite sua idade: "))
            telefone=str(input("Digite seu número de celular para contato: "))
            cpf=str(input("Digite seu CPF: "))
            cliente1=self.sistema.adicionar_cliente(nome,idade,telefone,cpf)
            cliente1=self.menu_cliente()
        else:
            print("Opção inválida")


if __name__ == "__main__":
    sistema_locadora = Locadora()
    sistema_locadora.sistema.adicionar_cliente("Paola Coutinho", 19, "998668644", "139778")
    sistema_locadora.inicio()
    



"""print("Antes de ordenar por genero")
lista.mostrar()
#lista.listar_por_genero()
#lista.buscar_filme("o medo", "Terror")
#lista.remover_filme(1234)
#lista.listar_por_genero()
lista.ordenar_por_genero()
print("-------------------------------")
print("Depois de ordenar por genero")
lista.mostrar()"""


