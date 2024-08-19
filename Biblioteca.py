class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def exibirDetalhes(self):
        if self.disponivel:
            status = "Disponível"
        else:
            status = "Emprestado"
        print(f"Título: {self.titulo}\n"
              f"Autor: {self.autor}\n"
              f"Status: {status}\n")

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livrosEmprestados = []

    def emprestarLivro(self, livro):
            if livro.disponivel:
                livro.disponivel = False
                self.livrosEmprestados.append(livro)
                print(f'{self.nome} pegou o livro "{livro.titulo}" emprestado.\n')
            else:
                print(f'Desculpe, o livro "{livro.titulo}" já está emprestado.\n')
    
    def devolverLivro(self, livro):
        if livro in self.livrosEmprestados:
            livro.disponivel = True
            self.livrosEmprestados.remove(livro)
            print(f'{self.nome} devolveu o livro "{livro.titulo}".\n')
        else:
            print(f'{self.nome} não possui o livro "{livro.titulo}".\n')

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
    
    def adicionarLivro(self, livro):
        self.livros.append(livro)
        print(f'O livro "{livro.titulo}" foi adicionado à biblioteca.\n')

    def exibirLivrosDisponiveis(self):
        print(f"Livros disponíveis na biblioteca:")
        disponiveis = [livro for livro in self.livros if livro.disponivel]
        if disponiveis:
            for livro in disponiveis:
                livro.exibirDetalhes()
        else:
            print("Nenhum livro disponível no momento.")

livro1 = Livro("O Anticristo", "Friedrich Nietzsche")
livro2 = Livro("Drácula", "Bam Stoker")
livro3 = Livro("Macunaíma", "Mário de Andrade")

usuario1 = Usuario("Caim")
usuario2 = Usuario("Abel")

biblioteca = Biblioteca("Biblioteca Pública")

print()
biblioteca.adicionarLivro(livro1)
biblioteca.adicionarLivro(livro2)
biblioteca.adicionarLivro(livro3)

biblioteca.exibirLivrosDisponiveis()

usuario1.emprestarLivro(livro1)
usuario2.emprestarLivro(livro2)

biblioteca.exibirLivrosDisponiveis()

usuario1.devolverLivro(livro1)

biblioteca.exibirLivrosDisponiveis()
