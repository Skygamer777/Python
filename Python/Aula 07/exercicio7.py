Aluno1 = ("Gabriel",16,"Desenvolvimento De Sistemas 2")
Aluno2 = ("Gustavo",17,"Administração 2")
Aluno3 = ("Vinicius",15,"Enfermagem 2")

notas_aluno1 = (8.3,7.9,10,10)
notas_aluno2 = (9.5,6.2,7.3,8.5)
notas_aluno3 = (3.5,6.1,8.7,9)

nome1,idade1,turma1 = Aluno1
print(f"Nome: {nome1}, Idade: {idade1}, Turma: {turma1}")
nome2,idade2,turma2 = Aluno2
print(f"Nome: {nome2}, Idade: {idade2}, Turma: {turma2}")
nome3,idade3,turma3 = Aluno3
print(f"Nome: {nome3}, Idade: {idade3}, Turma: {turma3}")

nota1_1,nota1_2,nota1_3,nota1_4 = notas_aluno1
print(f"Notas de {nome1}: {nota1_1}, {nota1_2}, {nota1_3}, {nota1_4}")
nota2_1,nota2_2,nota2_3,nota2_4 = notas_aluno2
print(f"Notas de {nome2}: {nota2_1}, {nota2_2}, {nota2_3}, {nota2_4}")
nota3_1,nota3_2,nota3_3,nota3_4 = notas_aluno3
print(f"Notas de {nome3}: {nota3_1}, {nota3_2}, {nota3_3}, {nota3_4}")
print(f"Menor nota do {nome1}: ",min(notas_aluno1))
print(f"Maior nota do {nome2}: ",max(notas_aluno2))
print(f"Menor nota do {nome3}: ",sum(notas_aluno3))

