# Matheus Reis e Guilherme Reis
import os

class Aluno:
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def __eq__(self, other):
        return self.matricula == other.matricula

    def __str__(self):
        return f"Matrícula: {self.matricula}, Nome: {self.nome}, Idade: {self.idade}"

class GerenciadorAlunos:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.alunos = []
        self.carregar_alunos()

    def carregar_alunos(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r') as file:
                for line in file:
                    matricula, nome, idade = line.strip().split(',')
                    self.alunos.append(Aluno(int(matricula), nome, int(idade)))

    def salvar_alunos(self):
        with open(self.arquivo, 'w') as file:
            for aluno in self.alunos:
                file.write(f"{aluno.matricula},{aluno.nome},{aluno.idade}\n")

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, matricula):
        self.alunos = [aluno for aluno in self.alunos if aluno.matricula != matricula]

    def editar_aluno(self, matricula, novo_nome, nova_idade):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                aluno.nome = novo_nome
                aluno.idade = nova_idade
                break

    def listar_alunos(self):
        if not self.alunos:
            print("Não há alunos cadastrados.")
        else:
            for aluno in self.alunos:
                print(aluno)

if __name__ == "__main__":
    arquivo = "alunos.txt"
    gerenciador_alunos = GerenciadorAlunos(arquivo)
    while True:
        print("\n1. Adicionar novo aluno")
        print("2. Remover aluno")
        print("3. Editar informações de aluno")
        print("4. Listar todos os alunos")
        print("5. Sair")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            matricula = int(input("Digite a matrícula do aluno: "))
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            gerenciador_alunos.adicionar_aluno(Aluno(matricula, nome, idade))
        elif opcao == 2:
            matricula = int(input("Digite a matrícula do aluno a ser removido: "))
            gerenciador_alunos.remover_aluno(matricula)
        elif opcao == 3:
            matricula = int(input("Digite a matrícula do aluno a ser editado: "))
            novo_nome = input("Digite o novo nome do aluno: ")
            nova_idade = int(input("Digite a nova idade do aluno: "))
            gerenciador_alunos.editar_aluno(matricula, novo_nome, nova_idade)
        elif opcao == 4:
            gerenciador_alunos.listar_alunos()
        elif opcao == 5:
            gerenciador_alunos.salvar_alunos()
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")
