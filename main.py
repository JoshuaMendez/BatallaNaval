# Juego se parte en dos partes del código
# -----------------------
# Parte del Jugador 1
# -----------------------
import time
import os

cuadriculaJ1 = {'A1': '-', 'A2': '-', 'A3': '-', 'A4': '-', 'A5': '-', 'A6': '-', 'A7': '-', 'A8': '-', 'A9': '-', 'A10': '-',
            'B1': '-', 'B2': '-', 'B3': '-', 'B4': '-', 'B5': '-', 'B6': '-', 'B7': '-', 'B8': '-', 'B9': '-', 'B10': '-',
            'C1': '-', 'C2': '-', 'C3': '-', 'C4': '-', 'C5': '-', 'C6': '-', 'C7': '-', 'C8': '-', 'C9': '-', 'C10': '-',
            'D1': '-', 'D2': '-', 'D3': '-', 'D4': '-', 'D5': '-', 'D6': '-', 'D7': '-', 'D8': '-', 'D9': '-', 'D10': '-',
            'E1': '-', 'E2': '-', 'E3': '-', 'E4': '-', 'E5': '-', 'E6': '-', 'E7': '-', 'E8': '-', 'E9': '-', 'E10': '-',
            'F1': '-', 'F2': '-', 'F3': '-', 'F4': '-', 'F5': '-', 'F6': '-', 'F7': '-', 'F8': '-', 'F9': '-', 'F10': '-',
            'G1': '-', 'G2': '-', 'G3': '-', 'G4': '-', 'G5': '-', 'G6': '-', 'G7': '-', 'G8': '-', 'G9': '-', 'G10': '-',
            'H1': '-', 'H2': '-', 'H3': '-', 'H4': '-', 'H5': '-', 'H6': '-', 'H7': '-', 'H8': '-', 'H9': '-', 'H10': '-',
            'I1': '-', 'I2': '-', 'I3': '-', 'I4': '-', 'I5': '-', 'I6': '-', 'I7': '-', 'I8': '-', 'I9': '-', 'I10': '-',
            'J1': '-', 'J2': '-', 'J3': '-', 'J4': '-', 'J5': '-', 'J6': '-', 'J7': '-', 'J8': '-', 'J9': '-', 'J10': '-'
            }

# print(cuadriculaJ1['A1'])

# def cuadriculation():
#     print("    1   2   3   4   5   6   7   8   9  10")
#     print("  +---+---+---+---+---+---+---+---+---+---+")
#     print("A | " + cuadriculaJ1['A1'] + " | " + cuadriculaJ1['A2'] + " | " + cuadriculaJ1['A3'] + " | " + cuadriculaJ1['A4'] + " | " + cuadriculaJ1['A5'])



def printearNombreBatallaNaval():
    print(' __                                          ')
    print(' )_)  _  _)_ _   ) ) _     )\ ) _      _   ) ')
    print('/__) (_( (_ (_( ( ( (_(   (  ( (_( \) (_( (  ')
    print('                                             ')

def inicio():
    global jugador1
    limpiarTerminal()
    print('Bienvenido a ...')
    printearNombreBatallaNaval()
    time.sleep(1.5)
    print('Para empezar, dinos...')
    time.sleep(1)
    print('')
    jugador1=input('¿Cuál es tu nombre?: ')
    print('')
    time.sleep(0.5)
    print('...')
    print('')
    time.sleep(0.5)
    print(f'Perfecto {jugador1} ¡Bienvenido a la Batalla!')
    time.sleep(2)
    limpiarTerminal()
    mostrarCuadricula()

def cuadriculaJugador1():
    time.sleep(1)
    print('')
    print(f'    1   2   3   4   5   6   7   8   9   10')
    print(f'  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐')
    print(f'A | {cuadriculaJ1["A1"]} | {cuadriculaJ1["A2"]} | {cuadriculaJ1["A3"]} | {cuadriculaJ1["A4"]} | {cuadriculaJ1["A5"]} | {cuadriculaJ1["A6"]} | {cuadriculaJ1["A7"]} | {cuadriculaJ1["A8"]} | {cuadriculaJ1["A9"]} | {cuadriculaJ1["A10"]} |')
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    print(f'B | {cuadriculaJ1["B1"]} | {cuadriculaJ1["B2"]} | {cuadriculaJ1["B3"]} | {cuadriculaJ1["B4"]} | {cuadriculaJ1["B5"]} | {cuadriculaJ1["B6"]} | {cuadriculaJ1["B7"]} | {cuadriculaJ1["B8"]} | {cuadriculaJ1["B9"]} | {cuadriculaJ1["B10"]} |')
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    print(f'C | {cuadriculaJ1["C1"]} | {cuadriculaJ1["C2"]} | {cuadriculaJ1["C3"]} | {cuadriculaJ1["C4"]} | {cuadriculaJ1["C5"]} | {cuadriculaJ1["C6"]} | {cuadriculaJ1["C7"]} | {cuadriculaJ1["C8"]} | {cuadriculaJ1["C9"]} | {cuadriculaJ1["C10"]} |')
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    print(f'D | {cuadriculaJ1["D1"]} | {cuadriculaJ1["D2"]} | {cuadriculaJ1["D3"]} | {cuadriculaJ1["D4"]} | {cuadriculaJ1["D5"]} | {cuadriculaJ1["D6"]} | {cuadriculaJ1["D7"]} | {cuadriculaJ1["D8"]} | {cuadriculaJ1["D9"]} | {cuadriculaJ1["D10"]} |')
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    print(f'E | {cuadriculaJ1["E1"]} | {cuadriculaJ1["E2"]} | {cuadriculaJ1["E3"]} | {cuadriculaJ1["E4"]} | {cuadriculaJ1["E5"]} | {cuadriculaJ1["E6"]} | {cuadriculaJ1["E7"]} | {cuadriculaJ1["E8"]} | {cuadriculaJ1["E9"]} | {cuadriculaJ1["E10"]} |')
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    print(f'F | {cuadriculaJ1["F1"]} | {cuadriculaJ1["F2"]} | {cuadriculaJ1["F3"]} | {cuadriculaJ1["F4"]} | {cuadriculaJ1["F5"]} | {cuadriculaJ1["F6"]} | {cuadriculaJ1["F7"]} | {cuadriculaJ1["F8"]} | {cuadriculaJ1["F9"]} | {cuadriculaJ1["F10"]} |')
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    print(f'G | {cuadriculaJ1["G1"]} | {cuadriculaJ1["G2"]} | {cuadriculaJ1["G3"]} | {cuadriculaJ1["G4"]} | {cuadriculaJ1["G5"]} | {cuadriculaJ1["G6"]} | {cuadriculaJ1["G7"]} | {cuadriculaJ1["G8"]} | {cuadriculaJ1["G9"]} | {cuadriculaJ1["G10"]} |')
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    print(f'H | {cuadriculaJ1["H1"]} | {cuadriculaJ1["H2"]} | {cuadriculaJ1["H3"]} | {cuadriculaJ1["H4"]} | {cuadriculaJ1["H5"]} | {cuadriculaJ1["H6"]} | {cuadriculaJ1["H7"]} | {cuadriculaJ1["H8"]} | {cuadriculaJ1["H9"]} | {cuadriculaJ1["H10"]} |')
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    print(f'I | {cuadriculaJ1["I1"]} | {cuadriculaJ1["I2"]} | {cuadriculaJ1["I3"]} | {cuadriculaJ1["I4"]} | {cuadriculaJ1["I5"]} | {cuadriculaJ1["I6"]} | {cuadriculaJ1["I7"]} | {cuadriculaJ1["I8"]} | {cuadriculaJ1["I9"]} | {cuadriculaJ1["I10"]} |')
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    print(f'J | {cuadriculaJ1["J1"]} | {cuadriculaJ1["J2"]} | {cuadriculaJ1["J3"]} | {cuadriculaJ1["J4"]} | {cuadriculaJ1["J5"]} | {cuadriculaJ1["J6"]} | {cuadriculaJ1["J7"]} | {cuadriculaJ1["J8"]} | {cuadriculaJ1["J9"]} | {cuadriculaJ1["J10"]} |')
    print(f'  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘')
    print('')

def mostrarCuadricula():
    print('')
    print('Esta es tu cuadrícula')
    print('')
    time.sleep(0.1)
    print(f'    1   2   3   4   5   6   7   8   9   10')
    time.sleep(0.1)
    print(f'  ┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┐')
    time.sleep(0.1)
    print(f'A | - | - | - | - | - | - | - | - | - | - |')
    time.sleep(0.1)
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    time.sleep(0.1)
    print(f'B | - | - | - | - | - | - | - | - | - | - |')
    time.sleep(0.1)
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    time.sleep(0.1)
    print(f'C | - | - | - | - | - | - | - | - | - | - |')
    time.sleep(0.1)
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    time.sleep(0.1)
    print(f'D | - | - | - | - | - | - | - | - | - | - |')
    time.sleep(0.1)
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    time.sleep(0.1)
    print(f'E | - | - | - | - | - | - | - | - | - | - |')
    time.sleep(0.1)
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    time.sleep(0.1)
    print(f'F | - | - | - | - | - | - | - | - | - | - |')
    time.sleep(0.1)
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    time.sleep(0.1)
    print(f'G | - | - | - | - | - | - | - | - | - | - |')
    time.sleep(0.1)
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    time.sleep(0.1)
    print(f'H | - | - | - | - | - | - | - | - | - | - |')
    time.sleep(0.1)
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    time.sleep(0.1)
    print(f'I | - | - | - | - | - | - | - | - | - | - |')
    time.sleep(0.1)
    print(f'  ├───┼───┼───┼───┼───┼───┼───┼───┼───┼───┤')
    time.sleep(0.1)
    print(f'J | - | - | - | - | - | - | - | - | - | - |')
    time.sleep(0.1)
    print(f'  └───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘')
    print('')
    print('¿Listo?')
    print('')
    time.sleep(3)
    limpiarTerminal()
    posicionarBarcosJugador1()

def posicionarBarcosJugador1():
    time.sleep(2)
    print(f'¡Vamos a posicionar tus barcos {jugador1}!')
    time.sleep(1)
    print('Para esto tienes que saber los barcos que existen:')
    time.sleep(1)
    print('[1] Lancha ▢ ▢')
    time.sleep(1)
    print('[2] Destructor ▢ ▢ ▢')
    time.sleep(1)
    print('[3] Submarino ▢ ▢ ▢')
    time.sleep(1)
    print('[4] Acorazado ▢ ▢ ▢ ▢')
    time.sleep(1)
    print('[5] Portaviones ▢ ▢ ▢ ▢ ▢')
    time.sleep(1)
    print('')
    print('▢ *Cantidad de misiles que le pueden caer a cada barco')
    time.sleep(1)
    print('')
    contadorPosicionesBarcos=0
    while contadorPosicionesBarcos <= 4:
        try:
            barcoAEmpezar=int(input('¿Cuál quieres ubicar primero?: '))
            print('')
            if barcoAEmpezar == 1:
                limpiarTerminal()
                time.sleep(0.5)
                print('¡Genial! Vamos a ubicar tu Lancha ▢ ▢')
                time.sleep(0.5)
                cuadriculaJugador1()
                print(
                    'Recuerda que para digitar el espacio en la casilla escribe la letra y el número juntos')
                time.sleep(0.2)
                print('Ejemplo: A1, J10, G5')
                print('')
                time.sleep(0.5)
                print('Vas a digitar el primer punto en el mapa y después el segundo.')
                time.sleep(0.5)
                print('Recuerda que tu Lancha tiene ▢ ▢ espacios')
                time.sleep(0.5)
                print('Elige sabiamente...')
                print('')
                time.sleep(0.5)
                # Casilla 1 / 2
                sitioLancha1=input(
                    '¿En qué casilla quieres posicionar tu Lancha ▢ ▢ ?: ')
                sitioLancha1=sitioLancha1.upper()

                if sitioLancha1 in cuadriculaJ1:
                    cuadriculaJ1[sitioLancha1]='▢'
                else:
                    print('No creemos que exista esa casilla.')

                print(cuadriculaJ1)
                print('')
                cuadriculaJugador1()


                contadorPosicionesBarcos += 1
            elif barcoAEmpezar == 2:
                print('Destructor')
                contadorPosicionesBarcos += 1
            elif barcoAEmpezar == 3:
                print('Submarino')
                contadorPosicionesBarcos += 1
            elif barcoAEmpezar == 4:
                print('Acorazado')
                contadorPosicionesBarcos += 1
            elif barcoAEmpezar == 5:
                print('Portaviones')
                contadorPosicionesBarcos += 1
            else:
                print(f'Recuerda que hay 5 opciones {jugador1}.')
                print('')
        except ValueError:
                print('')
                print(f'Eso no parece un número {jugador1}...')
                print('')


def cuadricula():
    print('cuadricula')

def limpiarTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

inicio()
