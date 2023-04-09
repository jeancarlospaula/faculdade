nomeAluno1 = input("Digite o nome do aluno 1: ")
notaAluno1 = float(input("Digite a nota do aluno 1: "))

nomeAluno2 = input("Digite o nome do aluno 2: ")
notaAluno2 = float(input("Digite a nota do aluno 2: "))

nomeAluno3 = input("Digite o nome do aluno 3: ")
notaAluno3 = float(input("Digite a nota do aluno 3: "))

alunos = {
    "aluno1": {
        "nome": nomeAluno1,
        "nota": notaAluno1
    },
    "aluno2": {
        "nome": nomeAluno2,
        "nota": notaAluno2
    },
    "aluno3": {
        "nome": nomeAluno3,
        "nota": notaAluno3
    },
}

mediaNotas = 0
i = 1

while i <= 3:
    mediaNotas += alunos[f"aluno{i}"]["nota"]
    i += 1

print("Média das notas: ", mediaNotas/3)
