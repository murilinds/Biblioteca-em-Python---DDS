Sistema de Gerenciamento de Biblioteca -- Murilo Pereira D'Isep

Um sistema em Python voltado para o gerenciamento de acervos literários diretamente pelo terminal, com persistência de dados utilizando arquivos CSV e suporte à Programação Orientada a Objetos (POO).

Como Executar o Programa:
1 - Certifique-se de ter o Python instalado em sua máquina.

2 - Salve o código principal do sistema em um arquivo chamado main.py (ou qualquer outro nome de sua preferência).

3 - Abra o terminal ou prompt de comando na pasta onde o arquivo foi salvo.

4 - Execute o comando: python main.py

O arquivo livros.csv será gerado automaticamente na mesma pasta assim que você cadastrar ou modificar o primeiro livro.

--------------------------------------

Principais Funcionalidades:

[1] Cadastrar Livro: Permite adicionar um novo livro ao sistema informando título, autor, ano de publicação e código ISBN (com validação de duplicidade e tipos numéricos).

[2] Listar Todos os Livros: Exibe no console a listagem completa dos livros cadastrados e seus respectivos status atuais.

[3] Buscar Livro: Realiza buscas dinâmicas no acervo utilizando partes do título ou do autor.

[4] Ordenar Livros: Organiza os livros por título, autor ou ano de publicação, atualizando também a ordem de salvamento no arquivo CSV.

[5] Registrar Empréstimo: Altera o status de um livro disponível para "emprestado" com base no código ISBN.

[6] Registrar Devolução: Retorna o status de um livro emprestado para "disponível".

-----------------------

Requisitos Técnicos Aplicados
Programação Orientada a Objetos (POO): O código foi estruturado utilizando duas classes principais (Biblioteca e Livro), encapsulando dados e comportamentos de forma limpa.

Persistência de Dados com CSV: Utilização das bibliotecas nativas de manipulação de arquivos em Python (csv.DictReader e csv.DictWriter) para salvar e carregar os dados de forma estruturada.

Tratamento de Exceções: Blocos try-except aplicados na leitura/escrita de arquivos e em entradas do usuário (ValueError), garantindo que o programa não quebre com entradas inválidas.

Estruturas de Dados Eficientes: Uso de dicionários (dict) mapeados pelo ISBN para buscas rápidas e manipulação de registros em memória.

Funções de Alta Ordem (Lambdas): Emprego da função sorted() combinada com expressões lambda para gerenciar as ordenações customizadas do acervo.