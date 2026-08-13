'''Sistema de Gerenciamento de Biblioteca
Cadastrar livros (título, autor, ano de publicação, código/ISBN, status: disponível ou emprestado)
Registrar empréstimo de um livro (muda o status para "emprestado")
Registrar devolução de um livro (muda o status de volta para "disponível")
Listar todos os livros cadastrados, com seus status
Buscar um livro por título ou autor
Ordenar a listagem de livros (por título, autor ou ano)
Todos cadastram o mesmo tipo de sistema — a diferença vai estar na qualidade da implementação, na organização do código e em como cada um resolveu os detalhes.
'''
import csv
import os

class Biblioteca: 
    def __init__(self):
        # Define o caminho absoluto baseado na pasta onde este script está salvo
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        self.arquivo_csv = os.path.join(diretorio_atual, "livros.csv")
        self.livros = {}
        self.carregar_dados()

    def carregar_dados(self):
        if not os.path.exists(self.arquivo_csv):
            return
        
        try:
            with open(self.arquivo_csv, mode="r", encoding="utf-8") as arquivo:
                leitor = csv.DictReader(arquivo)
                for linha in leitor:
                    titulo = linha["titulo"]
                    autor = linha["autor"]
                    ano = int(linha["ano_publicacao"])
                    isbn = int(linha["codigo_isbn"])
                    status = linha["status"]

                    livro = Livro(titulo, autor, ano, isbn)
                    livro.status = status
                    self.livros[isbn] = livro
        except Exception as e:
            print(f"Erro ao carregar os dados do arquivo: {e}")

    def salvar_dados(self):
        try:
            with open(self.arquivo_csv, mode="w", newline="", encoding="utf-8") as arquivo:
                campos = ["titulo", "autor", "ano_publicacao", "codigo_isbn", "status"]
                escritor = csv.DictWriter(arquivo, fieldnames=campos)
                
                escritor.writeheader()
                for livro in self.livros.values():
                    escritor.writerow({
                        "titulo": livro.titulo,
                        "autor": livro.autor,
                        "ano_publicacao": livro.ano_publicacao,
                        "codigo_isbn": livro.codigo_isbn,
                        "status": livro.status
                    })
        except Exception as e:
            print(f"Erro ao salvar os dados no arquivo: {e}")

    def cadastrar_livro(self):
        print("\n--- CADASTRO DE LIVRO ---")
        titulo = input("Digite O Título: ")
        autor = input("Digite O Autor: ")
        try:
            ano = int(input("Digite O Ano de Publicação: "))
            isbn = int(input("Digite O Código ISBN: "))
        except ValueError:
            print("Erro: Ano e ISBN devem ser números inteiros.")
            return False

        if isbn in self.livros:
            print("Erro: Já existe um livro cadastrado com este ISBN.")
            return False
            
        novo_livro = Livro(titulo, autor, ano, isbn)
        self.livros[novo_livro.codigo_isbn] = novo_livro
        
        self.salvar_dados()
        print("Livro cadastrado com sucesso!")
        return True
    
    def listar_livros(self):
        print("\n--- LISTA DE LIVROS ---")
        if not self.livros:
            print("Não Existe Nenhum Livro!")
            return
        
        for livro in self.livros.values():
            print(livro)

    def buscar_livro(self):
        print("\n--- BUSCAR LIVRO ---")
        termo = input("Digite o Título ou o Autor para buscar: ").lower()
        encontrados = []
        
        for livro in self.livros.values():
            if termo in livro.titulo.lower() or termo in livro.autor.lower():
                encontrados.append(livro)
                
        if encontrados:
            print("\nLivro(s) Encontrado(s):")
            for livro in encontrados:
                print(livro)
        else:
            print("\nNenhum livro correspondente foi encontrado.")

    def ordenar_livros(self):
        print("\n--- ORDENAR LIVROS ---")
        if not self.livros:
            print("Não há livros cadastrados para ordenar.")
            return

        criterio = input("Deseja ordenar por 'titulo', 'autor' ou 'ano'? ").lower()
        livros_lista = list(self.livros.values())
        
        if criterio == "titulo":
            livros_ordenados = sorted(livros_lista, key=lambda livro: livro.titulo.lower())
        elif criterio == "autor":
            livros_ordenados = sorted(livros_lista, key=lambda livro: livro.autor.lower())
        elif criterio == "ano":
            livros_ordenados = sorted(livros_lista, key=lambda livro: livro.ano_publicacao)
        else:
            print("Critério inválido. Tente novamente.")
            return
            
        print(f"\nLivros ordenados por {criterio.capitalize()}:")
        for livro in livros_ordenados:
            print(livro)

    def registrar_emprestimo(self):
        print("\n--- REGISTRAR EMPRÉSTIMO ---")
        try:
            isbn = int(input("Digite o ISBN do livro: "))
            if isbn in self.livros:
                if self.livros[isbn].emprestar():
                    self.salvar_dados()  
                    print("Empréstimo realizado com sucesso!")
                else:
                    print("O livro já está emprestado no momento.")
            else:
                print("Livro não encontrado.")
        except ValueError:
            print("ISBN inválido. Digite apenas números.")

    def registrar_devolucao(self):
        print("\n--- REGISTRAR DEVOLUÇÃO ---")
        try:
            isbn = int(input("Digite o ISBN do livro: "))
            if isbn in self.livros:
                if self.livros[isbn].devolver():
                    self.salvar_dados()  
                    print("Devolução realizada com sucesso! O livro agora está disponível.")
                else:
                    print("Este livro já consta como disponível.")
            else:
                print("Livro não encontrado.")
        except ValueError:
            print("ISBN inválido. Digite apenas números.")

    def iniciar_menu(self):
        while True:
            print("\n--Menu--")
            print("[1] - Cadastrar Livro")
            print("[2] - Listar Todos os Livros")
            print("[3] - Buscar Livro (por Título ou Autor)")
            print("[4] - Ordenar Livros")
            print("[5] - Registrar Empréstimo")
            print("[6] - Registrar Devolução")
            print("[0] - Sair")

            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                self.cadastrar_livro()
            elif opcao == "2":
                self.listar_livros()
            elif opcao == "3":
                self.buscar_livro()
            elif opcao == "4":
                self.ordenar_livros()
            elif opcao == "5":
                self.registrar_emprestimo()
            elif opcao == "6":
                self.registrar_devolucao()
            elif opcao == "0":
                print("\nSaindo do sistema... Até a próxima!")
                break
            else:
                print("\nOpção inválida! Por favor, escolha um número entre 0 e 6.")


class Livro:
    def __init__(self, titulo, autor, ano_publicacao, codigo_isbn):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.codigo_isbn = codigo_isbn
        self.status = "disponível"

    def emprestar(self):
        if self.status == "disponível":
            self.status = "emprestado"
            return True
        return False

    def devolver(self):
        if self.status == "emprestado":
            self.status = "disponível"
            return True
        return False

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.ano_publicacao}) [ISBN: {self.codigo_isbn}] - Status: {self.status}"
    
    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.iniciar_menu()