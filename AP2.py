#GUILHERME REIS E MATHEUS REIS
import random

# ANSI escape codes for colors
class color:
    RED = '\033[91m'
    END = '\033[0m'

def aventureiro_andar(aventureiro, direcao):
    x, y = aventureiro["posicao"]

    if direcao == "W" and y > 0:
        aventureiro["posicao"] = [x, y - 1]
        return True

    elif direcao == "A" and x > 0:
        aventureiro["posicao"] = [x - 1, y]
        return True

    elif direcao == "S" and y < 9:
        aventureiro["posicao"] = [x, y + 1]
        return True

    elif direcao == "D" and x < 9:
        aventureiro["posicao"] = [x + 1, y]
        return True

    else:
        return False

def aventureiro_atacar(aventureiro):
    dano = aventureiro["forca"] + random.randint(1, 6)
    return dano

def aventureiro_defender(aventureiro, dano):
    dano_reduzido = max(0, dano - aventureiro["defesa"])
    aventureiro["vida"] -= dano_reduzido

def ver_atributos_aventureiro(aventureiro, experiencia_atual, experiencia_necessaria):
    nivel = experiencia_atual // 5 + 1
    exp_restante = experiencia_necessaria - experiencia_atual
    vida_atual = aventureiro["vida"]
    vida_maxima = aventureiro["vida_maxima"]
    forca = aventureiro["forca"]
    defesa = aventureiro["defesa"]

    print(f"Aventureiro nv {nivel} ({experiencia_atual} / {experiencia_necessaria}) - "
          f"Vida {vida_atual}/{vida_maxima} - Força {forca} - Defesa {defesa}")

def aventureiro_esta_vivo(aventureiro):
    return aventureiro['vida'] > 0

def novo_monstro():
    print("Um novo monstro apareceu!")
    return {"forca": random.randint(5, 25), "vida": random.randint(10, 100)}

def monstro_atacar(monstro):
    dano = monstro["forca"]
    return dano

def monstro_defender(monstro, dano):
    monstro["vida"] -= dano
    if monstro["vida"] < 0:
        monstro["vida"] = 0

def monstro_esta_vivo(monstro):
    return monstro["vida"] > 0

def desenhar(aventureiro, tesouro, pocao, rodadas):
    for y in range(10):
        for x in range(10):
            if [x, y] == aventureiro["posicao"]:
                print("@", end=" ")
            elif [x, y] == tesouro:
                print(color.RED + "X" + color.END, end=" ")
            elif [x, y] == pocao["posicao"] and not pocao["encontrado"]:
                print("%", end=" ")
            else:
                print(".", end=" ")
        print()

    print(f"Rodadas: {rodadas}")

def iniciar_combate(aventureiro, monstro):
    while True:
        dano_aventureiro = aventureiro_atacar(aventureiro)
        monstro_defender(monstro, dano_aventureiro)

        print(f"Aventureiro causou {dano_aventureiro} de dano!\n"
              f"Vida atual do monstro: {monstro['vida']}")

        if monstro["vida"] <= 0:
            return True

        dano_monstro = monstro_atacar(monstro)
        aventureiro_defender(aventureiro, dano_monstro)

        print(f"Monstro causou {dano_monstro} de dano!\n"
              f"Vida atual do aventureiro: {aventureiro['vida']}")

        if aventureiro["vida"] <= 0:
            return False

def movimentar(aventureiro, direcao, pocao):
    if not aventureiro_andar(aventureiro, direcao):
        return True

    efeito = random.choices(["nada", "monstro", "pocao"], [0.6, 0.3, 0.1])[0]
    if efeito == "monstro":
        monstro = novo_monstro()
        return iniciar_combate(aventureiro, monstro)
    elif efeito == "pocao" and not pocao["encontrado"]:
        aplicar_efeito_pocao(aventureiro, pocao)
        pocao["encontrado"] = True
        print("Você encontrou uma poção!")

    return True

def aplicar_efeito_pocao(aventureiro, pocao):
    efeito = random.randint(1, 3)
    if efeito == 1:
        aventureiro["vida"] = aventureiro["vida_maxima"] * 2
    elif efeito == 2:
        aventureiro["forca"] += 15
    elif efeito == 3:
        aventureiro["defesa"] += 10

def gerar_tesouro():
    while True:
        posicao_x = random.randint(0, 9)
        posicao_y = random.randint(0, 9)
        if (posicao_x, posicao_y) != (0, 0):
            return [posicao_x, posicao_y]

def main():
    aventureiro = {
        "forca": random.randint(10, 18),
        "defesa": random.randint(10, 18),
        "vida": random.randint(100, 120),
        "vida_maxima": random.randint(150, 180),
        "posicao": [0, 0]
    }

    tesouro = gerar_tesouro()

    pocao = {
        "posicao": gerar_tesouro(),
        "encontrado": False
    }

    experiencia_atual = 0
    experiencia_necessaria = 5

    print("Deseja buscar um tesouro? Primeiro, informe seu nome:")
    aventureiro["nome"] = input()
    print(f"Saudações, {aventureiro['nome']}! Boa sorte!")

    desenhar(aventureiro, tesouro, pocao, 0)

    rodadas = 0
    while True:
        op = input("Insira o seu comando: ").upper()
        if op == "Q":
            print("Já correndo?")
            break
        elif op == "T":
            ver_atributos_aventureiro(aventureiro, experiencia_atual, experiencia_necessaria)
        elif op in ["W", "A", "S", "D"]:
            rodadas += 1
            if movimentar(aventureiro, op, pocao):
                desenhar(aventureiro, tesouro, pocao, rodadas)
            else:
                print("Game Over...")
                break
        else:
            print(f"{aventureiro['nome']}, não conheço essa opção! Tente novamente!")

        if aventureiro["posicao"] == tesouro:
            experiencia_atual += 1
            if experiencia_atual >= experiencia_necessaria:
                experiencia_atual = 0
                experiencia_necessaria += 5
                aventureiro["vida_maxima"] += 10
            print(f"Parabéns, {aventureiro['nome']}! Você encontrou o tesouro!")
            desenhar(aventureiro, tesouro, pocao, rodadas)

if __name__ == "__main__":
    main()
