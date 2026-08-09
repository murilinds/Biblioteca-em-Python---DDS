'''Sistema de Gerenciamento de Biblioteca
Cadastrar livros (título, autor, ano de publicação, código/ISBN, status: disponível ou emprestado)
Registrar empréstimo de um livro (muda o status para "emprestado")
Registrar devolução de um livro (muda o status de volta para "disponível")
Listar todos os livros cadastrados, com seus status
Buscar um livro por título ou autor
Ordenar a listagem de livros (por título, autor ou ano)
Todos cadastram o mesmo tipo de sistema — a diferença vai estar na qualidade da implementação, na organização do código e em como cada um resolveu os detalhes.
'''

class Biblioteca: ##Commit Para A Classe
    def __init__(self):
        self.livros = {}

    def cadastrar_livro(self, livro):
        if livro.codigo_isbn in self.livros:
            return False  
        self.livros[livro.codigo_isbn] = livro
        return True
    
    def listar_livros(self):
        return self.livros

    def buscar_livro(self,titulo,autor):
        for livro in self.livros.values():
            if livro.titulo == titulo or livro.autor == autor:
                return livro
        return None
        

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
        return f"{self.titulo} - {self.autor} ({self.ano_publicacao}) - {self.codigo_isbn} - Status: {self.status}"
    
    def __repr__(self):
        return self.__str__()

