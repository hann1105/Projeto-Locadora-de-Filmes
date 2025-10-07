class Node: #classe Node para a lista encadeada dos filmes
    def __init__(self,titulo,genero,diretor,classificacao_indicativa,ano,codigo,situacao): # cada filme é constituído por esses atributos
        #Atributos dos filmes
        self.titulo=titulo
        self.genero=genero
        self.diretor=diretor
        self.classificacao_indicativa=classificacao_indicativa
        self.ano=ano
        self.codigo=codigo
        self.situacao=situacao
        self.fila_reservas=FilaDeReservas() #cada filme terá sua própria Fila de reservas, para assim ficar organizado no processo de aluguel quando um filme já estiver Alugado
        self.next=None #ponteiro next 

class ListaDeFilmes: #classe para Lista encadeada de filmes
    def __init__(self):
        self.head=None
    
    #Método para inserir filmes na lista
    def inserir_filme(self,titulo,genero,diretor,classificacao_indicativa,ano,codigo,situacao): 
        
        new_filme=Node(titulo,genero,diretor,classificacao_indicativa,ano,codigo,situacao)

        if self.head is None: # se a cabeça for fazia, o novo filme será a cabeça
            self.head=new_filme
            print("Filme adicionado com sucesso!")
        else: # caso não
            current=self.head  #o ponteiro current irá pecorrer toda a lista enquanto não for None, quando chegar a esse nó None, ele irá adicionar o novo filme
            while current.next is not None:
                current=current.next
            current.next=new_filme
            print("Filme adicionado com sucesso!")

    #Método para buscar filme de acordo com o título e o gênero
    def buscar_filme(self,titulo,genero):
        current=self.head #ponteiro começa do primeiro nó da lista
        while current is not None: #percorre toda a lista
            if current.titulo == titulo and current.genero==genero: # compara se o título e o gênero do filme do nó é igual ao filme procurado
                print(f"Titulo: {current.titulo} ")
                print(f"Gênero: {current.genero}")
                print(f"Diretor: {current.diretor}")
                print(f"Classificação Indicativa:{current.classificacao_indicativa}")
                print(f"Ano de Publicação: {current.ano}")
                print(f"Código do Filme: {current.codigo}")
                print(f"Situação: {current.situacao}")
                return current
            current=current.next
        print("Filme não encontrado") #não encontrou 
        return None
    
    #Método mostrar os filmes (menu do funcionário para ter maior controle)
    def mostrar(self):
        current=self.head #começa do primeiro nó
        while current is not None:
            print(f"{current.genero}: {current.titulo}") #Mostra o gênero e o filme
            current=current.next

    #Método listar, vai listar os filmes por determinado gênero escolhido
    def listar_por_genero(self):
        genero=str(input("Digite o gênero para listar os filmes disponíveis: "))
        print(f"Filmes - {genero}")
        current=self.head
        while current is not None: #percorre a lista toda
            if current.genero==genero: #compara se o gênero do nó corresponde ao nó escolhido pelo usuário
                print(f"{current.titulo}")
                encontrou=True
            current=current.next
        if not encontrou:
            print("Não há filmes para esse gênero")
        return

    #Método para remover filmes (menu do funcionário)
    def remover_filme(self,codigo): #vai remover o filme de acordo com o código dele
        if self.head is None:
            print("Lista vazia")
            return
        if self.head.codigo==codigo: #se o filme a ser removido for o da cabeça
            self.head=self.head.next #vai pular a cabeça e a nova cabeça vai ser o next 
            print("Filme removido com sucesso")
            return
        current=self.head #caso não seja o filme da cabeça, o current vai percorrer a lista enquanto não for None
        while current.next is not None and current.next.codigo!=codigo: # e enquanto o código for diferente do código inserido pelo usuário
            current=current.next
            print("Filme removido com sucesso!")
        if current.next is not None: #se tiver mais filmes depois do removido, ele irá pular para o próximo nó
            current.next=current.next.next
    
    # Método de Ordenação por gênero com base no Insertion Sort
    def ordenar_por_genero(self):
        if self.head is None or self.head.next is None: #se a lista estiver vazia ou só tem um filme não há o que ordenar
            return

        # Novo início da lista ordenada
        lista_ordenada = None  
        current = self.head

        while current is not None:# enquanto o current não chega ao fim da lista
            proximo = current.next  # guarda o próximo nó antes de desconectar
            # Inserção na lista ordenada
            if (lista_ordenada is None or 
            current.genero.lower() < lista_ordenada.genero.lower() or
            (current.genero.lower() == lista_ordenada.genero.lower() and 
             current.titulo.lower() < lista_ordenada.titulo.lower())): #vai comparar os gêneros do nó do current para o nó da lista ordenada
                # insere no início
                current.next = lista_ordenada #o nó atual aponta para o antigo inicio
                lista_ordenada = current #atualiza o novo início
            else: #inserção no meio ou final
                # percorre a lista ordenada até achar o ponto de inserção
                temporario = lista_ordenada #temporario é um ponteiro temporario para auxiliar e aponta para o primeiro nó da lista ja organizada
                while (temporario.next is not None and 
                  (temporario.next.genero.lower() < current.genero.lower() or
                   (temporario.next.genero.lower() == current.genero.lower() and 
                    temporario.next.titulo.lower() < current.titulo.lower()))):#vai percorrer a lista enquanto o proximo nó tiver um genero menor(ordem alfabetica) do que o do nó atual
                    temporario = temporario.next #e se masi de um filme tiver o mesmo gênero, ele ordenará o título dos gêneros
                current.next = temporario.next
                temporario.next = current #o current é encaixado logo depois do temporário, em ordem
            current = proximo  # avança para o próximo da lista original

        # Atualiza o head da lista
        self.head = lista_ordenada

        # Exibe os filmes ordenados
        print("\nFilmes ordenados por gêneros:")
        current = self.head
        while current:
            print(f"{current.genero}: {current.titulo}")
            current = current.next

#class Node para a Pilha com lista encadeada
class NodePilha:
    def __init__(self,filme):
        self.filme=filme
        self.next=None #ponteiro next para percorrer os nós

#class Pilha
class Pilha:
    def __init__(self):
        self.topo=None
        self.tamanho=0

    #Método para inserir o filme na pilha
    def push(self,filme):
        new_node=NodePilha(filme) 
        new_node.next=self.topo
        self.topo=new_node #o topo vai ser o novo filme adicionado ()LIFO
        self.tamanho+=1
 
    #Método para ver se a pilha está vazia
    def is_empty(self):
        return self.tamanho==0

    #Método para mostrar os cinco filmes alugados recentemente
    def mostrar_cinco_ultimos(self):
        if self.is_empty(): #Se a pilha está vazia, nenhum filme foi alugado 
            print("Nenhum filme foi alugado recentemente")
        print("Os 5 último filmes alugados foram:")
        current=self.topo #começa no primeiro nó
        contador=0 #contador para ser até 5
        while current is not None and contador<5: #enquanto current não for None e contador for menor que 5
            print(f"{current.filme.titulo} - {current.filme.genero}") #vai mostrar o título e o gênero
            current=current.next
            contador+=1
        return

#classe Node para a fila encadeada de reserva
class NodeFila:
    def __init__(self,cliente):
        self.cliente=cliente
        self.next=None

#classe para a fila de reserva dos filmes
class FilaDeReservas: #em adicionar, vai chamar cliente, pois ele que vai ficar na fila de reserva e não o filme
    def __init__(self): #ja que cada filme ja terá sua própria lista de reservas
        self.front=None
        self._size=0
    
    #Método para adicionar o cliente na fila de reserva de determinado filme, quando este estiver já em situação de alugado
    def adicionar_na_fila(self,cliente):
        new_fila=NodeFila(cliente)
        if self.front is None: #se a fila está vazia, o novo nó será a 'cabeça'
            self.front=new_fila
        else: #caso não
            current=self.front 
            while current.next is not None: #vai percorrer toda a fila
                current=current.next
            current.next=new_fila #e adicionar no final 
        self._size+=1

    #Método para retirar da fila de reserva do filme, irá ser utilizado quando o livro for devolvido e o cliente que está a espera do filme, receberá o livro e sairá da fila
    def retirar_da_fila(self):
        if self.is_empty():
            print("Fila de reserva vazia")
            return
        cliente=self.front.cliente #vai guardar o cliente no front
        self.front=self.front.next #vai pular e remover esse cliente e o próximo será o novo front, na ordem (FIFO)
        self._size-=1
        return cliente

    #Método para retornar o primeiro da fila
    def peek(self):
        if self.is_empty():
            print("Fila de reserva vazia")
            return
        print(self.front.cliente) 
        return

    #Método para mostrar o tamanho
    def size(self):
        return self._size

    #Método para ver se a fila está vazia    
    def is_empty(self):
        return self._size==0
               
    #Método para mostrar a fila de clientes para determinado filme
    def mostrar_filmes_reservas(self):
        clientes_fila=[] #lista para colocar os clientes da fila
        current=self.front
        while current is not None:
            clientes_fila.append(current.cliente)
            current=current.next
        return clientes_fila

#Classe dos clientes
class Cliente:
    def __init__(self,nome,idade,telefone,cpf):
        #Atributos de cada cliente
        self.nome=nome
        self.idade=idade #a idade é um atributo a ser pedido pois, se determinado cliente não tiver a idade mínima
        self.telefone=telefone  #para alugar o filme, de acordo com a classificação indicativa dele, o aluguel não é permitido
        self.cpf=cpf
        self.filmes_alugados=[] #lista para mostrar os filmes alugados do cliente

#Classe para as operações que o cliente pode ter
class SistemaClientes:
    def __init__(self):
        self.clientes={} #dicionário para clientes, para facilitar a procura, inserção e remoção

    #Método para adicionar o cliente para o sistema da locadora
    def adicionar_cliente(self,nome,idade,telefone,cpf):
        if cpf in self.clientes: #procura se o cliente já é cadastrado
            print("Usuário já cadastrado")
        else: #caso não, adiciona o cliente no dicionário
            self.clientes[cpf]=Cliente(nome,idade,telefone,cpf)
            print("Cliente adicionado com sucesso")

    #Método para buscar clientes pelo cpf
    def buscar_cliente(self,cpf):
        if cpf in self.clientes: #compara o cpf
            cliente=self.clientes[cpf]
            print(f"Nome: {cliente.nome}/idade:{cliente.idade}/telefone:{cliente.telefone}") #vai mostrar os dados desse cliente
            print("Filmes alugados:") #vai mostrar os filmes alugados por esse cliente específico
            if cliente.filmes_alugados:
                for filme in cliente.filmes_alugados:#for para mostrar a lista dos filmes alugados
                    print(f"  - {filme.titulo}")
            else:
                print("  Nenhum filme alugado no momento.")
            return cliente
        else:
            print("Cliente não encontrado")
            return
    
    #Método para o cliente alugar o filme
    def alugar_filme(self,lista_filmes,cpf,titulo,codigo,pilha_alugueis): #lista_filmes é o objeto que será criado da classe ListaDeFilmes
        cliente=self.buscar_cliente(cpf) #confirma se é cliente para poder alugar
        if not cliente:
            return
        current=lista_filmes.head
        while current is not None: #vai percorrer toda a lista
            if current.titulo==titulo: #se o titulo do filme escolhido pelo cliente for encontrado (comparação dos títulos)
                if cliente.idade>=current.classificacao_indicativa: #e se o cliente tem idade para alugar esse filme
                    if current.situacao=="Disponivel": #e se a situação do filme está como 'Disponivel'
                        current.situacao= "Alugado" #vai mudar a situação para 'Alugado'
                        cliente.filmes_alugados.append(current) #adicionando a lista de filmes alugados do cliente
                        pilha_alugueis.push(current) #adiciona na pilha dos filmes alugados recentemente
                        print(f"{cliente.nome} alugou o filme '{current.titulo}'-({current.codigo}) com sucesso!")
                    else:
                        print(f"{current.titulo} não está disponível") #o filme está alugado
                        print(f"Adicionando o cliente {cliente.nome} para a lista de reservas do filme '{current.titulo}'")
                        current.fila_reservas.adicionar_na_fila(cliente) #adicionando o cliente na fila de reservas
                else:
                    print("Você não possui idade para a classificação indicativa desse filme. Aluguel cancelado") #a idade do cliente é menor que a classificação indicativa
                return
            current=current.next #percorrer os nós
        print("Filme não encontrado")
    
    #Método para devolução do filme
    def devolver_filme(self,lista_filmes,cpf,titulo,codigo):
        cliente=self.buscar_cliente(cpf) #vai buscar o cliente
        current=lista_filmes.head
        while current is not None:
            if current.titulo==titulo and current.codigo==codigo: #vai comparar os títulos e os códigos
                if current in cliente.filmes_alugados: 
                    cliente.filmes_alugados.remove(current) #vai remover o filme da lista dos filmes alugados do cliente

                    if not current.fila_reservas.is_empty(): #se a fila de reservas para esse filme não estiver vazia
                        proximo_cliente=current.fila_reservas.retirar_da_fila() #o próximo cliente, por ordem de pedido, ficará com o filme
                        proximo_cliente.filmes_alugados.append(current) #coloca na lista dos filmes alugados do próximo cliente
                        print(f"{cliente.nome} devolveu '{current.titulo}'.")
                        print(f"O filme foi reservado automaticamente para {proximo_cliente.nome}.")
                    else: #caso não tenha nenhuma reserva
                        current.situacao="Disponivel" #a situação do filme volta a ficar disponível
                        print(f"{cliente.nome} devolveu '{current.titulo}'. Agora está disponível para aluguel.")
                else: #o cliente não tem esse filme para devolver pois nçao está na sua lista de filmes alugados
                    print(f"O cliente {cliente.nome} não possui este filme alugado.")
                return
            current=current.next
        print("Filme não encontrado")

#Classe Principal Locadora
class Locadora: 
    def __init__(self):
        self.lista = ListaDeFilmes()        # a lista única de filmes
        self.sistema = SistemaClientes() # sistema único de clientes
        self.pilha_alugueis=Pilha() #pilha única de filmes recentes

        #Inserindo filmes iniciais 
        self.lista.inserir_filme("O amor não tira férias","Romance", "Nancy Meyers", 12,2006,"001", "Disponivel")
        self.lista.inserir_filme("Matrix","Ficção Científica"," Lana Wachowskie Lilly Wachowski", 14,1999,"002","Disponivel")
        self.lista.inserir_filme("Velozes e Furiosos","Ação","Rob Cohen", 14,2001,"003","Disponivel")
        self.lista.inserir_filme("O Impossível","Drama","Juan Antonio Bayona",14,2012,"004","Disponivel")
        self.lista.inserir_filme("A cinco passos de você","Romance","Justin Baldoni",12,2019,"005","Disponivel")
        self.lista.inserir_filme("Jogo Justo","Romance"," Chloe Domont",18,2023,"006","Disponivel")
        return
    
    #Método para o menu dos clientes
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
            
            #Pedindo para o usuário inserir a opção que deseja
            opcaocliente=str(input("Digite uma opção para ter acesso as funções: "))
            if opcaocliente.lower()=="a": #Alugar filme
                titulo=str(input("Digite o título do filme: "))
                cpf=str(input("Digite seu CPF: "))
                codigo=str(input("Digite o código do filme:"))
                alugar=self.sistema.alugar_filme(self.lista,cpf,titulo,codigo,self.pilha_alugueis)#método alugar sendo utilizado

            elif opcaocliente.lower()=="l": #Listar filmes 
                listar=self.lista.listar_por_genero() #Método listar por gênero, vai pedir para o usuário inserir o gênero

            elif opcaocliente.lower()=="d" : #Devolver filme
                cpf1=str(input("Digite seu CPF: "))
                titulo1=str(input("Digite o título do filme que deseja devolver: "))
                codigo1=str(input("Código do filme: "))
                devolver=self.sistema.devolver_filme(self.lista,cpf1,titulo1,codigo1) #Método devolver

            elif opcaocliente.lower()=="f": #Ver fila de reservas para determinado filme
                    titulo3=str(input("Digite o título do filme: "))
                    genero=str(input("Digite o gênero do filme: "))
                    filme=self.lista.buscar_filme(titulo3,genero)
                    if filme:
                        reservas = filme.fila_reservas.mostrar_filmes_reservas() #método de mostrar a fila de reserva
                        if reservas: #se tiver reservas
                            print( (f"\nFila de reservas para o filme '{filme.titulo}':"))
                            for i, cliente in enumerate(reservas, start=1): #vai mostrar a ordem em que o cliente está na fila
                                print(f"{i}º - {cliente.nome} (CPF: {cliente.cpf})")
                        else:
                            print("Não há reservas para este filme.")
                    else:
                        print("Filme não encontrado.")

            elif opcaocliente.lower()=="b": #Pesquisar determinado filme
                titulo2=str(input("Digite o título do filme que deseja pesquisar: "))
                genero2=str(input("Digite o gênero do filme: "))
                buscarfilme=self.lista.buscar_filme(titulo2,genero2) #Método buscar sendo chamado

            elif opcaocliente.lower()=="i": #vai voltar para a tela inicial para outros clientes utilizarem o sistema
                return self.inicio()
            
            elif opcaocliente.lower()=="s": #vai fechar o sistema
                print("Saindo do sitema...")
                break #vai parar o while

            else:
                print("Opção inválida")

    #Método do menu do funcionário com mais opções
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
        
    #Método do início do sistema, programa principal
    def inicio (self):
        print()
        print(" ----------------------------------------------")
        print("                 LOCADORA PH                   ")
        print("-----------------------------------------------")
        print()
        entrada=str(input("Bem vindo!Já possui cadastro?[S/N]")) #pergunta se tem cadastro na Locadora
        if entrada.lower()=="s":
            usuario=str(input("Digite seu CPF: "))
            if usuario== "139778": #Se tiver esse cpf é funcionário da livraria 
                while True:
                    print()
                    funcionario=self.menu_funcionario() #vai abrir o menu do funcionário
                    opcaofuncionario=str(input(" Escolha uma opção para navegar no Sistema da Locadora: "))
                    print()
                    if opcaofuncionario.lower()=="i": #Inserir novos filmes pedindo todos os atributos
                        print( "           CADASTRO DE FILMES         ")
                        titulo=str(input(" Insira o Título: "))
                        genero=str(input(" Insira o gênero: "))
                        diretor=str(input(" Insira o diretor: "))
                        classificacao_indicativa=int(input(" Insira a classificação Indicativa: "))
                        ano=int(input(" Insira o ano de lançamento: "))
                        codigo=str(input(" Insira o código do filme: "))
                        situacao=str(input(" Situação do filme: "))
                        inserir=self.lista.inserir_filme(titulo,genero,diretor,classificacao_indicativa,ano,codigo,situacao) #Método inserir sendo chamado
                        
                    elif opcaofuncionario.lower()=="r": #Remover o filme da lista da locadora
                        codigo=str(input("Digite o código do filme que deseja remover: "))
                        remover=self.lista.remover_filme(codigo) #método remover sendo chamado

                    elif opcaofuncionario.lower()=="b": #Buscar cliente com base no CPF
                        cpf=str(input("Digite o CPF do cliente que deseja pesquisar: "))
                        buscar=self.sistema.buscar_cliente(cpf) #Método buscar cliente sendo chamado
                        
                    elif opcaofuncionario.lower()=="f": #Ver fila de reserva do filme
                        titulo3=str(input("Digite o título do filme: "))
                        genero=str(input("Digite o gênero do filme: "))
                        filme=self.lista.buscar_filme(titulo3,genero) #Método buscar sendo chamado
                        if filme:
                            reservas = filme.fila_reservas.mostrar_filmes_reservas() #método de mostrar a fila de reserva
                            if reservas: #se tiver reserva
                                print( (f"\nFila de reservas para o filme '{filme.titulo}':")) #mostra os clientes por ordem
                                for i, cliente in enumerate(reservas, start=1):
                                    print(f"{i}º - {cliente.nome} (CPF: {cliente.cpf})")
                            else:
                                print("Não há reservas para este filme.")
                        else:
                            print("Filme não encontrado.")

                    elif opcaofuncionario.lower()=="l": #Buscar livro com base no titulo e gênero
                        titulo1=str(input("Digite o Título do filme:")) 
                        genero=str(input("Digite o gênero do filme: "))
                        buscarlivro=self.lista.buscar_filme(titulo1,genero) #Método buscar filme sendo chamado

                    elif opcaofuncionario.lower()=="li": #vai listar todos os filmes independente de gênero
                        mostrar=self.lista.mostrar() #Método mostrar sendo chamado
                        
                    elif opcaofuncionario.lower()=="o": #Ordenar por gênero
                        ordenar=self.lista.ordenar_por_genero() #Método ordenar sendo chamado

                    elif opcaofuncionario.lower()=="p": #Mostrar os 5 aluguéis recente
                        self.pilha_alugueis.mostrar_cinco_ultimos() #Método sendo chamado
                        
                    elif opcaofuncionario.lower()=="s": #Sair do sistema do funcionário
                        print("Saindo do sistema do funcionário...")
                        return self.inicio() #voltar para a tela inicial
                    else:
                        print("Opção inválida")

            elif usuario in self.sistema.clientes:
                self.menu_cliente() #vai mostrar o menu dos clientes
            else:
                print("Cliente não encontrado, tente novamente")
                self.inicio()
        elif entrada.lower()=="n": #vai fazer o cadastro do usuário
            print()
            print("               CADASTRO DE USUÁRIO           ")
            nome=str(input("Digite seu nome e sobrenome: "))
            idade=int(input("Digite sua idade: "))
            telefone=str(input("Digite seu número de celular para contato: "))
            cpf=str(input("Digite seu CPF: "))
            cliente1=self.sistema.adicionar_cliente(nome,idade,telefone,cpf) #método adicionar cliente sendo chamado
            cliente1=self.menu_cliente() #vai mostrar o menu do cliente
        else:
            print("Opção inválida")


if __name__ == "__main__": #Para rodar o programa
    sistema_locadora = Locadora()
    sistema_locadora.sistema.adicionar_cliente("Paola Coutinho", 19, "998668644", "139778") #Funcionário 
    sistema_locadora.inicio()
    

