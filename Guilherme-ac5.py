from random import randint

def main():
    # Atributos iniciais
    vida_aventureiro = 100
    ataque_aventureiro = randint(10, 20)
    defesa_aventureiro = randint(1, 5)
    vida_monstro = randint(60, 80)
    ataque_monstro = randint(20, 30)
    
    # Introdução
    print("Você está explorando uma caverna escura quando se depara com um monstro assustador!")
    print("Sem pensar duas vezes, você decide lutar pela sua vida.\n")

    # Início do combate
    rodada = 1
    while vida_aventureiro > 0 and vida_monstro > 0:
        print(f"*** Rodada {rodada} ***\n")
        
        # Ataque do aventureiro
        dano_aventureiro = randint(ataque_aventureiro // 2, ataque_aventureiro)
        vida_monstro -= dano_aventureiro
        print(f"Você avança corajosamente e ataca o monstro com sua espada, causando {dano_aventureiro} de dano!")
        print(f"Agora o monstro tem {max(0, vida_monstro)} de vida restante.\n")

        if vida_monstro <= 0:
            print("Com um golpe final, você derrota o monstro e vence a batalha!\n")
            break
        
        # Ataque do monstro
        dano_monstro = randint(ataque_monstro // 2, ataque_monstro)
        dano_monstro -= defesa_aventureiro
        vida_aventureiro -= max(0, dano_monstro)
        print(f"O monstro contra-ataca! Você sofre {max(0, dano_monstro)} de dano!")
        print(f"Sua vida agora é {max(0, vida_aventureiro)}.\n")

        rodada += 1
    
    # Resultado final
    if vida_aventureiro <= 0:
        print("Infelizmente, o monstro foi forte demais e você foi derrotado... Melhor sorte na próxima vez!")
    else:
        print("Com um suspiro de alívio, você emerge vitorioso desta perigosa batalha!")

# Início da aventura
main()
