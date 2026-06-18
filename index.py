import os

# Nome do arquivo onde os dados serão salvos
NOME_ARQUIVO = "dados_usuarios.csv"

def carregar_dados():
    usuarios = []
    # Verificação se o arquivo existe conforme ensinado [3, 4]
    if os.path.exists(NOME_ARQUIVO):
        # Uso da instrução 'with' para leitura [1]
        with open(NOME_ARQUIVO, "r") as arquivo:
            for linha in arquivo:
                # O professor sugeriu formato CSV [6], usamos ';' como separador
                dados = linha.strip().split(";")
                nome = dados
                senha = dados[7]
                fatura = float(dados[8])
                limite = float(dados[9])
                entradas = float(dados[10])
                # Converte a string de compras de volta para lista (eval é prático aqui)
                compras = eval(dados[11])
                usuarios.append([nome, senha, fatura, limite, compras, entradas])
    return usuarios

def salvar_dados(usuarios):
    # Uso do modo "w" para sobrescrever o arquivo com a lista atualizada [2]
    with open(NOME_ARQUIVO, "w") as arquivo:
        for u in usuarios:
            # Estrutura: nome;senha;fatura;limite;entradas;lista_compras
            linha = f"{u};{u[7]};{u[8]};{u[9]};{u[11]};{u[10]}\n"
            arquivo.write(linha)

def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

def main():
    usuarios = carregar_dados()

    while True:
        print("\n--- Dapper Finanças ---")
        print("1 - Cadastrar Conta")
        print("2 - Acessar")
        print("3 - Encerrar")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            nome = input("Usuário: ").strip()
            if any(u == nome for u in usuarios):
                print("Usuário já cadastrado!")
                continue
            senha = input("Senha: ")
            limite = ler_float("Limite de crédito: R$ ")
            # Novo usuário: [nome, senha, fatura, limite, lista_compras, entradas]
            usuarios.append([nome, senha, 0.0, limite, [], 0.0])
            salvar_dados(usuarios)
            print("Conta criada com sucesso!")

        elif escolha == "2":
            tentativas = 0
            while tentativas < 3:
                user = input("\nUsuário: ")
                passw = input("Senha: ")
                
                indice = -1
                for i in range(len(usuarios)):
                    if usuarios[i] == user and usuarios[i][7] == passw:
                        indice = i
                        break
                
                if indice != -1:
                    print(f"\nBem-vindo, {user}!")
                    menu_logado(usuarios, indice)
                    break
                else:
                    tentativas += 1
                    print(f"Dados incorretos! ({3-tentativas} tentativas restantes)")
            
            if tentativas == 3: print("Acesso bloqueado!")

        elif escolha == "3":
            print("Saindo...")
            break

def menu_logado(usuarios, idx):
    while True:
        print("\n--- Menu Principal ---")
        print("1. Consultar Fatura")
        print("2. Realizar Compra (Saída)")
        print("3. Registrar Entrada (Renda)")
        print("4. Relatório de Saldo")
        print("5. Ver Limite")
        print("6. Sair")
        
        op = input("Opção: ")
        
        if op == "1":
            print(f"\nFatura atual: R$ {usuarios[idx][8]:.2f}")
            for c in usuarios[idx][10]:
                print(f"- {c['cat']}: R$ {c['val']:.2f}")
        
        elif op == "2":
            val = ler_float("Valor da compra: R$ ")
            if val <= 0:
                print("Valor inválido!")
            elif usuarios[idx][8] + val > usuarios[idx][9]:
                print("Compra negada: Limite insuficiente!")
            else:
                cat = input("Categoria: ").capitalize()
                usuarios[idx][8] += val
                usuarios[idx][10].append({"cat": cat, "val": val})
                salvar_dados(usuarios)
                print("Compra aprovada!")

        elif op == "3":
            val = ler_float("Valor da entrada: R$ ")
            if val > 0:
                usuarios[idx][11] += val
                salvar_dados(usuarios)
                print("Entrada registrada!")
        
        elif op == "4":
            print("\n--- Relatório Mensal ---")
            print(f"Entradas: R$ {usuarios[idx][11]:.2f}")
            print(f"Saídas: R$ {usuarios[idx][8]:.2f}")
            print(f"Saldo: R$ {usuarios[idx][11] - usuarios[idx][8]:.2f}")

        elif op == "5":
            print(f"Limite total: R$ {usuarios[idx][9]:.2f}")
            print(f"Disponível: R$ {usuarios[idx][9] - usuarios[idx][8]:.2f}")

        elif op == "6":
            break

main()