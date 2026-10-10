class Aluno:
    lista_alunos = ["João", "Maria", "Pedro"]

    @classmethod
    def ler_alunos(cls):
        print("Lista de alunos:")
        for aluno in cls.lista_alunos:
            print(aluno)