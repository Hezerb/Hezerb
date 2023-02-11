import random
import string
from forca_visual import vizualizador_de_vidas
from palavras import palavras


def boas_vindas():
    print("\033[1;33;40m SEJA BEM VINDO, VAMOS JOGAR UM JOGO!!!\n"
          " VOCÊ TEM 7 CHANCES DE SAIR VIVO E A FORCA ESTÁ ANSIOSA POR UM NOVO PESCOSO.  \n"
          "\033[m")


def pegar_palavra(palavra):
    palavra = random.choice(palavra)  # escolhe as palavras aleatorias
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavra)
    return palavra.upper()


def forca():
    palavra = pegar_palavra(palavras)
    letras_palavras = set(palavra)  # letras nas palavras
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()  # usuario vai adivinhar
    vidas = 7
    while len(letras_palavras) > 0 and vidas > 0:  # quantidade de letras]
        lista_palavra = [letter if letter in letras_usadas else '-' for letter in palavra]
        print(vizualizador_de_vidas[vidas])
        print('\033[1;33;40m Palavra OCULTA: \033[m', ' '.join(lista_palavra))
        print('\033[1;33;40m Vocês tem', vidas,
              'Vidas restantes para adivinhar a palavra OCULTA e você usou essas letras: \033[m',
              ' '.join(letras_usadas))
        letra_usuario = input('\033[1;33;40m Adivinhe a Letra: \033[m').upper()
        if letra_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letra_usuario)
            if letra_usuario in letras_palavras:
                letras_palavras.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1
                print('\n \033[1;33;40m Sua letra,', letra_usuario, 'não está na palavra OCULTA.\033[m')
        elif letra_usuario in letras_usadas:
            print('\n \033[1;33;40m  Você já usou essa letra, seu verme insolente, Escolha outra.\033[m')
        else:
            print('\n \033[1;33;40m Essa não é uma letra válida, tenha atenção, verme.\033[m')

    if vidas == 0:
        print(vizualizador_de_vidas[vidas])
        print(
            '\033[1;33;40m VOCÊ MORREU!!! A FORCA LAÇOU UM NOVO PESCOÇO, SUFOQUE NA SUA IGNORÂNCIA. \n A palavra '
            'oculta era \033[m',
            palavra)
    else:
        print("Você Adivinhou a palavra correta, Você conquistou sua liberdade. A palavra è ', palavra, '!! "
              "Suma Daqui!!")


def reiniciar():
    print("")
    start_stop = int(input("\033[1;33;40m[1] - Deseja testar novamente seus conhecimento em troca da sua vida?\033[m\n"
                           "\033[1;33;40m[2] - Sair\033[m "))
    if start_stop == 1:
        boas_vindas()
        forca()
        reiniciar()
    elif start_stop == 2:
        quit()


boas_vindas()
forca()
reiniciar()
