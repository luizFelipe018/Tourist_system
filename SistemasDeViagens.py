

class Pais:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome


class Cidade:
    def __init__(self, codigo, nome, UF, codigo_pais):
        self.codigo = codigo
        self.nome = nome
        self.UF = UF
        self.codigo_pais = codigo_pais


class Guia:
    def __init__(self, codigo, nome, endereco, telefone, codigo_cidade):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.codigo_cidade = codigo_cidade


class Cliente:
    def __init__(self, CPF, nome, endereco, codigo_cidade):
        self.CPF = CPF
        self.nome = nome
        self.endereco = endereco
        self.codigo_cidade = codigo_cidade


class Pacote:
    def __init__(self, codigo, descricao, codigo_guia, valor_por_pessoa, total_participantes, quant_max_participantes):
        self.codigo = codigo
        self.descricao = descricao
        self.codigo_guia = codigo_guia
        self.valor_por_pessoa = valor_por_pessoa
        self.total_participantes = total_participantes
        self.quant_max_participantes = quant_max_participantes


class Venda:
    def __init__(self, codigo, CPF_cliente, codigo_pacote, quantidade_pessoas, valor_total):
        self.codigo = codigo
        self.CPF_cliente = CPF_cliente
        self.codigo_pacote = codigo_pacote
        self.quantidade_pessoas = quantidade_pessoas
        self.valor_total = valor_total


def ler_paises():
    paises = []
    while True:
        codigo = int(input("Digite o código do país: "))
        nome = input("Digite o nome do país: ")
        pais = Pais(codigo, nome)
        paises.append(pais)
        continuar = input("Deseja cadastrar outro país? (s/n): ")
        if continuar.lower() != 's':
            break
    return paises


def ler_cidades():
    cidades = []
    while True:
        codigo = int(input("Digite o código da cidade: "))
        nome = input("Digite o nome da cidade: ")
        UF = input("Digite o UF da cidade: ")
        codigo_pais = int(input("Digite o código do país: "))
        cidade = Cidade(codigo, nome, UF, codigo_pais)
        cidades.append(cidade)
        continuar = input("Deseja cadastrar outra cidade? (s/n): ")
        if continuar.lower() != 's':
            break
    return cidades


def incluir_guia(guias, cidades, paises):
    while True:
        codigo = int(input("Digite o código do guia a ser inserido: "))
        
        codigo_existente = False
        for guia in guias:
            if guia.codigo == codigo:
                print(f"O código {codigo} já existe na tabela de Guias. Insira um código diferente.")
                codigo_existente = True
                break
        
        if not codigo_existente:
            nome = input("Digite o nome do guia: ")
            endereco = input("Digite o endereço do guia: ")
            telefone = input("Digite o telefone do guia: ")
            codigo_cidade = int(input("Digite o código da cidade: "))
            
            cidade_encontrada = None
            for cidade in cidades:
                if cidade.codigo == codigo_cidade:
                    cidade_encontrada = cidade
                    break
            
            if cidade_encontrada:
                pais_encontrado = None
                for pais in paises:
                    if pais.codigo == cidade_encontrada.codigo_pais:
                        pais_encontrado = pais
                        break
                
                print(f"Cidade: {cidade_encontrada.nome}, UF: {cidade_encontrada.UF}")
                if pais_encontrado:
                    print(f"País: {pais_encontrado.nome}")
            
            novo_guia = Guia(codigo, nome, endereco, telefone, codigo_cidade)
            guias.append(novo_guia)
            print(f"Guia {nome} inserido com sucesso!")
        
        continuar = input("Deseja cadastrar outro guia? (s/n): ")
        if continuar.lower() != 's':
            break
    
    return guias


def incluir_cliente(clientes, cidades, paises):
    while True:
        CPF = input("Digite o CPF: ")
        CPF_existente = False
        for cliente in clientes:
            if cliente.CPF == CPF:
                print(f"O CPF {CPF} já está cadastrado. Insira um CPF válido.")
                CPF_existente = True
                break
        if not CPF_existente:
            nome = input("Digite o nome do cliente: ")
            endereco = input("Digite o endereço: ")
            codigo_cidade = int(input("Digite o código da cidade: "))
            
            cidade_encontrada = None
            for cidade in cidades:
                if cidade.codigo == codigo_cidade:
                    cidade_encontrada = cidade
                    break
            
            if cidade_encontrada:
                pais_encontrado = None
                for pais in paises:
                    if pais.codigo == cidade_encontrada.codigo_pais:
                        pais_encontrado = pais
                        break
                
                print(f"Cidade: {cidade_encontrada.nome}, UF: {cidade_encontrada.UF}")
                if pais_encontrado:
                    print(f"País: {pais_encontrado.nome}")

            cliente = Cliente(CPF, nome, endereco, codigo_cidade)
            clientes.append(cliente)
            print(f"Cliente {nome} inserido com sucesso!")
        continuar = input("Deseja cadastrar outro cliente? (s/n): ")
        if continuar.lower() != 's':
            break

    return clientes    


def excluir_cliente(clientes):
    CPF = input("Digite o CPF do cliente que deseja excluir: ")
    cliente_encontrado = None
    
    for cliente in clientes:
        if cliente.CPF == CPF:
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado:
        clientes.remove(cliente_encontrado)
        print(f"Cliente {cliente_encontrado.nome} com CPF {CPF} removido com sucesso!")
    else:
        print(f"Cliente com CPF {CPF} não encontrado na lista de clientes.")

    return clientes


def incluir_pacotes(guias, cidades, paises):
    pacotes = []
    while True:
        codigo = int(input("Digite o código do pacote: "))
        descricao = input("Digite a descrição do pacote: ")
        codigo_guia = int(input("Digite o código do guia: "))
        
        guia_encontrado = None
        for guia in guias:
            if guia.codigo == codigo_guia:
                guia_encontrado = guia
                break
        
        if guia_encontrado:
            print(f"Nome do guia: {guia_encontrado.nome}")
            
            valor_por_pessoa = float(input("Digite o valor por pessoa: "))
            
            while True:
                total_participantes = int(input("Digite o total de participantes: "))
                quant_max_participantes = int(input("Digite a quantidade máxima de participantes: "))
                
                if total_participantes <= quant_max_participantes:
                    break
                else:
                    print("O total de participantes não pode ser maior que a quantidade máxima de participantes.")
            
            cidade_encontrada = None
            for cidade in cidades:
                if cidade.codigo == guia_encontrado.codigo_cidade:
                    cidade_encontrada = cidade
                    break
            
            pais_encontrado = None
            if cidade_encontrada:
                for pais in paises:
                    if pais.codigo == cidade_encontrada.codigo_pais:
                        pais_encontrado = pais
                        break
            
            if cidade_encontrada:
                print(f"Cidade do guia: {cidade_encontrada.nome}, UF: {cidade_encontrada.UF}")
            if pais_encontrado:
                print(f"País do guia: {pais_encontrado.nome}")
            
            pacote = Pacote(codigo, descricao, codigo_guia, valor_por_pessoa, total_participantes, quant_max_participantes)
            pacotes.append(pacote)
        else:
            print(f"Código do guia {codigo_guia} não encontrado. Pacote não adicionado.")
        
        continuar = input("Deseja cadastrar outro pacote? (s/n): ")
        if continuar.lower() != 's':
            break
    return pacotes


def incluir_vendas(pacotes, clientes, cidades, guias):
    vendas = []
    while True:
        codigo = int(input("Digite o código da venda: "))
        CPF_cliente = input("Digite o CPF do cliente: ")
        cliente_encontrado = None
        
        for cliente in clientes:
            if cliente.CPF == CPF_cliente:
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            cidade_cliente = None
            for cidade in cidades:
                if cidade.codigo == cliente_encontrado.codigo_cidade:
                    cidade_cliente = cidade
                    break
            
            if cidade_cliente:
                print(f"Cliente: {cliente_encontrado.nome}, Cidade: {cidade_cliente.nome}")
            else:
                print(f"Cliente: {cliente_encontrado.nome}, Cidade não encontrada")
        else:
            print(f"O CPF {CPF_cliente} não existe em nosso banco de dados")
            continue

        codigo_pacote = int(input("Digite o código do pacote: "))
        
        pacote_encontrado = None
        for pacote in pacotes:
            if pacote.codigo == codigo_pacote:
                pacote_encontrado = pacote
                break
        
        if pacote_encontrado:
            guia_associado = None
            for guia in guias:
                if guia.codigo == pacote_encontrado.codigo_guia:
                    guia_associado = guia
                    break
            
            if guia_associado:
                print(f"Descrição do Pacote: {pacote_encontrado.descricao}")
                print(f"Nome do Guia: {guia_associado.nome}")
                print(f"Valor por Pessoa: R$ {pacote_encontrado.valor_por_pessoa:.2f}")
            else:
                print(f"Guia associado ao pacote não encontrado.")
            
            while True:
                quantidade_pessoas = int(input("Digite a quantidade de pessoas: "))
                
                if quantidade_pessoas <= pacote_encontrado.quant_max_participantes:
                    break
                else:
                    print(f"A quantidade de pessoas excede o limite máximo permitido ({pacote_encontrado.quant_max_participantes}). Tente novamente.")
            
            valor_total = quantidade_pessoas * pacote_encontrado.valor_por_pessoa
            
            venda = Venda(codigo, CPF_cliente, codigo_pacote, quantidade_pessoas, valor_total)
            vendas.append(venda)
        else:
            print(f"Código do pacote {codigo_pacote} não encontrado. Venda não registrada.")
        
        continuar = input("Deseja cadastrar outra venda? (s/n): ")
        if continuar.lower() != 's':
            break
    return vendas

def consultar_pacote(pacotes, guias, cidades, paises):
    codigo_pacote = int(input("Digite o código do pacote que deseja consultar: "))
    
    pacote_encontrado = None
    for pacote in pacotes:
        if pacote.codigo == codigo_pacote:
            pacote_encontrado = pacote
            break
    
    if pacote_encontrado:
        guia_associado = None
        for guia in guias:
            if guia.codigo == pacote_encontrado.codigo_guia:
                guia_associado = guia
                break
        
        cidade_guia = None
        if guia_associado:
            for cidade in cidades:
                if cidade.codigo == guia_associado.codigo_cidade:
                    cidade_guia = cidade
                    break
        
        pais_guia = None
        if cidade_guia:
            for pais in paises:
                if pais.codigo == cidade_guia.codigo_pais:
                    pais_guia = pais
                    break
        
        valor_total_arrecadado = pacote_encontrado.valor_por_pessoa * pacote_encontrado.total_participantes
        
        print("\n### Informações do Pacote ###")
        print(f"Código: {pacote_encontrado.codigo}")
        print(f"Descrição: {pacote_encontrado.descricao}")
        print(f"Valor por Pessoa: R$ {pacote_encontrado.valor_por_pessoa:.2f}")
        print(f"Total de Participantes: {pacote_encontrado.total_participantes}")
        print(f"Quantidade Máxima de Participantes: {pacote_encontrado.quant_max_participantes}")
        print(f"Valor Total Arrecadado: R$ {valor_total_arrecadado:.2f}")
        
        if guia_associado:
            print("\n### Informações do Guia ###")
            print(f"Código do Guia: {guia_associado.codigo}")
            print(f"Nome do Guia: {guia_associado.nome}")
            print(f"Endereço do Guia: {guia_associado.endereco}")
            print(f"Telefone do Guia: {guia_associado.telefone}")
            if cidade_guia:
                print(f"Cidade do Guia: {cidade_guia.nome}, UF: {cidade_guia.UF}")
                if pais_guia:
                    print(f"País do Guia: {pais_guia.nome}")
            else:
                print("Cidade do Guia não encontrada")
        else:
            print("\nGuia associado não encontrado.")
    else:
        print(f"Pacote com código {codigo_pacote} não encontrado.")

def pacotes_completamente_vendidos(pacotes, guias):
    pacotes_vendidos = []
    
    for pacote in pacotes:
        if pacote.total_participantes == pacote.quant_max_participantes:
            pacotes_vendidos.append(pacote)
    
    if pacotes_vendidos:
        print("\n### Pacotes Completamente Vendidos ###")
        for pacote in pacotes_vendidos:
            nome_guia = None
            for guia in guias:
                if guia.codigo == pacote.codigo_guia:
                    nome_guia = guia.nome
                    break
            
            valor_total_arrecadado = pacote.valor_por_pessoa * pacote.total_participantes

            print(f"Código: {pacote.codigo}")
            print(f"Descrição: {pacote.descricao}")
            print(f"Nome do Guia: {nome_guia}")
            print(f"Valor Total Arrecadado: R$ {valor_total_arrecadado:.2f}")
            print("----------------------")
    else:
        print("Não há pacotes completamente vendidos.")

def exibir_registros_vendas(vendas, pacotes, clientes):
    if not vendas:
        print("Não há registros de vendas.")
        return
    
    total_vendido = 0.0  
    
    print("\n### Registros de Vendas ###")
    for venda in vendas:
        cliente_nome = None
        pacote_descricao = None
        
        for cliente in clientes:
            if cliente.CPF == venda.CPF_cliente:
                cliente_nome = cliente.nome
                break
        
        for pacote in pacotes:
            if pacote.codigo == venda.codigo_pacote:
                pacote_descricao = pacote.descricao
                break
        
        valor_total_venda = venda.valor_total
        total_vendido += valor_total_venda
        
        print(f"Código da Venda: {venda.codigo}")
        if cliente_nome:
            print(f"Nome do Cliente: {cliente_nome}")
        if pacote_descricao:
            print(f"Descrição do Pacote: {pacote_descricao}")
        print(f"Quantidade de Pessoas: {venda.quantidade_pessoas}")
        print(f"Valor Total: R$ {valor_total_venda:.2f}")
        print("----------------------")
    

    print(f"\nValor Total Vendido: R$ {total_vendido:.2f}")

def visualizar_paises_cidades(paises, cidades):
    print("\n### Países e Cidades ###")
    if not paises:
        print("Não há países cadastrados.")
    else:
        for pais in paises:
            print(f"Código: {pais.codigo}, Nome: {pais.nome}")
            print("Cidades:")
            pais_cidades = [cidade for cidade in cidades if cidade.codigo_pais == pais.codigo]
            if pais_cidades:
                for cidade in pais_cidades:
                    print(f"  - Código: {cidade.codigo}, Nome: {cidade.nome}, UF: {cidade.UF}")
            else:
                print("  - Nenhuma cidade cadastrada para este país.")

def visualizar_guias(guias, cidades, paises):
    print("\n### Guias ###")
    if not guias:
        print("Não há guias cadastrados.")
    else:
        for guia in guias:
            cidade = next((cidade for cidade in cidades if cidade.codigo == guia.codigo_cidade), None)
            pais = next((pais for pais in paises if pais.codigo == cidade.codigo_pais), None)
            print(f"Nome: {guia.nome}, Cidade: {cidade.nome}, País: {pais.nome}")


def visualizar_clientes(clientes, cidades, paises):
    print("\n### Clientes ###")
    if not clientes:
        print("Não há clientes cadastrados.")
    else:
        for cliente in clientes:
            cidade = next((cidade for cidade in cidades if cidade.codigo == cliente.codigo_cidade), None)
            pais = next((pais for pais in paises if pais.codigo == cidade.codigo_pais), None)
            print(f"Nome: {cliente.nome}, Cidade: {cidade.nome}, País: {pais.nome}")

def visualizar_pacotes(pacotes, guias, cidades, paises):
    print("\n### Pacotes ###")
    if not pacotes:
        print("Não há pacotes cadastrados.")
    else:
        for pacote in pacotes:
            guia = next((guia for guia in guias if guia.codigo == pacote.codigo_guia), None)
            cidade = next((cidade for cidade in cidades if cidade.codigo == guia.codigo_cidade), None)
            pais = next((pais for pais in paises if pais.codigo == cidade.codigo_pais), None)
            print(f"Destino: {cidade.nome}, País: {pais.nome}, Guia: {guia.nome}, Descrição: {pacote.descricao}")

def visualizar_vendas(vendas, pacotes, clientes):
    print("\n### Vendas ###")
    if not vendas:
        print("Não há vendas cadastradas.")
    else:
        for venda in vendas:
            pacote = next((pacote for pacote in pacotes if pacote.codigo == venda.codigo_pacote), None)
            cliente = next((cliente for cliente in clientes if cliente.codigo == venda.codigo_cliente), None)
            print(f"Cliente: {cliente.nome}, Pacote: {pacote.descricao}, Data: {venda.data}, Valor: {venda.valor}")

def menu_principal():
    paises = []
    cidades = []
    guias = []
    clientes = []
    pacotes = []
    vendas = []

    while True:
        print("\n### Menu Principal ###")
        print("1. Gerenciar Países")
        print("2. Gerenciar Cidades")
        print("3. Gerenciar Guias")
        print("4. Gerenciar Clientes")
        print("5. Gerenciar Pacotes")
        print("6. Gerenciar Vendas")
        print("7. Visualizar Dados")
        print("8. Sair do Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_paises(paises)
        elif opcao == '2':
            menu_cidades(cidades, paises)
        elif opcao == '3':
            menu_guias(guias, cidades, paises)
        elif opcao == '4':
            menu_clientes(clientes, cidades, paises)
        elif opcao == '5':
            menu_pacotes(pacotes, guias, cidades, paises)
        elif opcao == '6':
            menu_vendas(vendas, pacotes, clientes)
        elif opcao == '7':
            menu_visualizar_dados(paises, cidades, guias, clientes, pacotes, vendas)
        elif opcao == '8':
            print("Saindo do programa ...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

def menu_paises(paises):
    while True:
        print("\n### Menu de Países ###")
        print("1. Adicionar País")
        print("2. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            paises.extend(ler_paises())
        elif opcao == '2':
            break
        else:
            print("Opção inválida. Escolha novamente.")

def menu_cidades(cidades):
    while True:
        print("\n### Menu de Cidades ###")
        print("1. Adicionar Cidade")
        print("2. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cidades.extend(ler_cidades())
        elif opcao == '2':
            break
        else:
            print("Opção inválida. Escolha novamente.")

def menu_guias(guias, cidades, paises):
    while True:
        print("\n### Menu de Guias ###")
        print("1. Adicionar Guia")
        print("2. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            guias = incluir_guia(guias, cidades, paises)
        elif opcao == '2':
            break
        else:
            print("Opção inválida. Escolha novamente.")

def menu_clientes(clientes, cidades, paises):
    while True:
        print("\n### Menu de Clientes ###")
        print("1. Adicionar Cliente")
        print("2. Excluir Cliente")
        print("3. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            clientes = incluir_cliente(clientes, cidades, paises)
        elif opcao == '2':
            clientes = excluir_cliente(clientes)
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Escolha novamente.")

def menu_pacotes(pacotes, guias, cidades, paises):
    while True:
        print("\n### Menu de Pacotes ###")
        print("1. Adicionar Pacote")
        print("2. Consultar Pacote")
        print("3. Pacotes Completamente Vendidos")
        print("4. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            pacotes = incluir_pacotes(pacotes, guias, cidades, paises)
        elif opcao == '2':
            consultar_pacote(pacotes, guias, cidades, paises)
        elif opcao == '3':
            pacotes_completamente_vendidos(pacotes, guias)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Escolha novamente.")

def menu_vendas(vendas, pacotes, clientes):
    while True:
        print("\n### Menu de Vendas ###")
        print("1. Incluir Venda")
        print("2. Exibir Registros de Vendas")
        print("3. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            vendas = incluir_vendas(pacotes, clientes)
        elif opcao == '2':
            exibir_registros_vendas(vendas, pacotes, clientes)
        elif opcao == '3':
            break
        else:
            print("Opção inválida. Escolha novamente.")

def menu_visualizar_dados(paises, cidades, guias, clientes, pacotes, vendas):
    while True:
        print("\n### Visualizar Dados ###")
        print("1. Visualizar Países e Cidades")
        print("2. Visualizar Guias")
        print("3. Visualizar Clientes")
        print("4. Visualizar Pacotes")
        print("5. Visualizar Vendas")
        print("6. Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            visualizar_paises_cidades(paises, cidades)
        elif opcao == '2':
            visualizar_guias(guias, cidades, paises)
        elif opcao == '3':
            visualizar_clientes(clientes, cidades, paises)
        elif opcao == '4':
            visualizar_pacotes(pacotes, guias, cidades, paises)
        elif opcao == '5':
            visualizar_vendas(vendas, pacotes, clientes)
        elif opcao == '6':
            break
        else:
            print("Opção inválida. Escolha novamente.")


menu_principal()

