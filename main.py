import csv

# Criação do arquivo .csv
with open('cadastros.csv', 'w', newline='') as arquivo:
  campos = ['ID','Aluno', 'Nota']
  escritor = csv.DictWriter(arquivo, fieldnames=campos)
  escritor.writeheader()

# Carregamento dos dados do arquivo .csv para uma lista de dicionários
def carregar_dados():
  with open('cadastros.csv', 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    return list(leitor)


# Menu de opções
def menu():
  print("--------------------")
  print("SIGA UFAPE".center(20))
  print("--------------------" + "\n")
  print("1." + "VISUALIZAR".center(15))
  print("2." + "ADICIONAR".center(15))
  print("3." + "REMOVER".center(14))
  print("4." + "EDITAR NOTA".center(17))
  print("5." + "BUSCAR".center(12))
  print("6." + "SAIR".center(10) + "\n")
  print("--------------------")
  opcao = input("Escolha uma opção\n-> ")
  print("--------------------")
  return opcao


# Visualizar os alunos atualmente cadastrados
def visualizar_alunos(dados):
  if len(dados) == 0:
    print("\n[CADASTROS VAZIOS]")
    return
  print("ALUNOS CADASTRADOS: ")
  for d in dados:
    print(f"\n| ID:       {d['ID']}")
    print(f"| Aluno(a): {d['Aluno']}")
    print(f"| Nota:     {d['Nota']}")

# Adicionar um novo aluno ao cadastro
def adicionar_aluno(dados):
  id = input("ID\n-> ")
  
  if id_existe(dados, id):
    while id_existe(dados, id):
      print("\n[ID JÁ EXISTE, INSIRA UM ID VÁLIDO]")
      id = input("ID\n-> ")
    
  aluno = input("Nome\n-> ")
  nota = float(input("Nota\n-> "))
  dados.append({'ID' : id, 'Aluno': aluno, 'Nota': nota})
  print("\n[ALUNO(A) CADASTRADO(A)]")

# Remover um aluno do cadastro
def remover_aluno(dados):
  id = input("Digite o ID do aluno(a) a ser removido\n-> ")
  if id_existe(dados, id):
    for d in dados:
      if d['ID'] == id:
        aluno_removido = d
        dados[:] = [d for d in dados if d.get('ID') != id]
        print("\nALUNO(A) REMOVIDO(A):")
        print(f"\n| ID:       {aluno_removido['ID']}")
        print(f"| Aluno(a): {aluno_removido['Aluno']}")
        print(f"| Nota:     {aluno_removido['Nota']}")
  else:
    print("[ID NÃO ENCONTRADO]")

# Editar a nota de um aluno
def editar_nota(dados):
  id = input("Digite o ID do aluno\n-> ")
  if id_existe(dados, id):
    for d in dados:
      if d['ID'] == id:
        d['Nota'] = float(input("Digite a nova nota\n-> "))
        print("\n[NOTA ATUALIZADA]")
        print(f"\n| ID:       {d['ID']}")
        print(f"| Aluno(a): {d['Aluno']}")
        print(f"| Nota:     {d['Nota']}")
  else:
    print("[ID NÃO ENCONTRADO]")
      
# Busca filtrada
def buscar_alunos(dados):
  print(">>> TIPO DE BUSCA <<<\n")
  print("1.  BUSCA POR INICIAL DO NOME")
  print("2.  BUSCA POR NOTA\n")
  tipo = input("Escolha uma opção\n-> ")
  
  while tipo != "1" and tipo != "2":
    print("\n[OPÇÃO INVÁLIDA]")
    tipo = input("Escolha uma opção\n-> ")
    
  if tipo == "1":
    inicial = input("\nInicial\n-> ").upper()
    resultados = [d for d in dados if d['Aluno'][0].upper() == inicial]
    if len(resultados) == 0:
      print("\n[NENHUM RESULTADO ENCONTRADO]")
    else:
      print("--------------------")
      print(f"LISTA DE ALUNOS COM A INICIAL ({inicial}):")
      for r in resultados:
        print(f"\n| ID:       {r['ID']}")
        print(f"| Aluno(a): {r['Aluno']}")
        print(f"| Nota:     {r['Nota']}")
        
  elif tipo == "2":
    valor = float(input("\nNota\n-> "))
    resultados = [d for d in dados if abs(float(d['Nota']) - valor) < 0.01]
    if len(resultados) == 0:
      print("\n[NENHUM RESULTADO ENCONTRADO]")
    else:
      print("--------------------")
      print(f"LISTA DE ALUNOS COM NOTA IGUAL A ({valor}):")
      for r in resultados:
        print(f"\n| ID:       {r['ID']}")
        print(f"| Aluno(a): {r['Aluno']}")
        print(f"| Nota:     {r['Nota']}")

# Atualização do arquivo .csv com as modificações
def atualizar_arquivo(dados):
  with open('cadastros.csv', 'w', newline='') as arquivo:
    campos = ['ID', 'Aluno', 'Nota']
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(dados)

# Verifica se o ID já existe
def id_existe(dados, id):
  for d in dados:
    if d['ID'] == id:
      return True
  return False

# Execução do programa
dados = carregar_dados()
opcao = ''
while opcao != '6':
  opcao = menu()
  if opcao == '1':
    visualizar_alunos(dados)
  elif opcao == '2':
    adicionar_aluno(dados)
  elif opcao == '3':
    remover_aluno(dados)
  elif opcao == '4':
    editar_nota(dados)
  elif opcao == '5':
    buscar_alunos(dados)
  elif opcao == '6':
    break
  else:
    print("[OPÇÃO INVÁLIDA. TENTE NOVAMENTE]")
atualizar_arquivo(dados) # Atualiza o arquivo após o término do loop

