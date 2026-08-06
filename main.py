'''Sistema de Gerenciamento de Biblioteca
Cadastrar livros (título, autor, ano de publicação, código/ISBN, status: disponível ou emprestado)
Registrar empréstimo de um livro (muda o status para "emprestado")
Registrar devolução de um livro (muda o status de volta para "disponível")
Listar todos os livros cadastrados, com seus status
Buscar um livro por título ou autor
Ordenar a listagem de livros (por título, autor ou ano)
Todos cadastram o mesmo tipo de sistema — a diferença vai estar na qualidade da implementação, na organização do código e em como cada um resolveu os detalhes.
'''

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