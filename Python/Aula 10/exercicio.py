class Aluno:
    lista_alunos = ["João","Maria","Pedro"]
    @classmethod
    def ler_alunos(cls):
        print("Lista de Alunos: ")
        for aluno in cls.lista_alunos:
            print(aluno)
Aluno.ler_alunos()
        