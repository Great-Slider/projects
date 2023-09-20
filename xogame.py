POLE = {1: ".", 2: ".", 3: ".", 4: ".", 5: ".", 6: ".", 7: ".", 8: ".", 9: "."}
IGROKS = {"X": [], "O": []}
COMBOS = ((1, 2, 3), (1, 4, 7), (1, 5, 9), (2, 5, 8), (3, 5, 7), (3, 6, 9), (4, 5, 6), (7, 8, 9))
def set_yacheika(yacheika, znak):
    POLE[yacheika] = znak
    IGROKS[znak].append(yacheika)

def pokazhi_pole():
    print(f"\n{POLE[7]} {POLE[8]} {POLE[9]}")
    print(f"{POLE[4]} {POLE[5]} {POLE[6]}")
    print(f"{POLE[1]} {POLE[2]} {POLE[3]}")

def proverka(znak):
    maska_doski = set(IGROKS[znak])
    return bool([True for pravilo in COMBOS if len(maska_doski.intersection(pravilo)) == 3])

def begin():
    znak = "X"
    shag = 1
    while True:
        pokazhi_pole()
        yacheika = int(input(f"\nХод игрока «{znak}», введи номер ячейки [1-9] или «0» для выхода из игры:"))
        if not yacheika:
            print(f"\nПечалька, вы покинули игру :-(")
            break
        elif yacheika in list(range(1, 10)):
            if POLE[yacheika] == ".":
                set_yacheika(yacheika, znak)
            else:
                print(f"\nЯчейка занята... повтори ход")
                continue
            if proverka(znak):
                print(f"\nЗнак {znak} выиграл!!!")
                pokazhi_pole()
                break
            else:
                if shag == 9:
                    print(f"\nБольше ходов не осталось!!! GAME OVER как говорится...")
                    pokazhi_pole()
                    break
                else:
                    shag += 1

            znak = "X" if znak == "O" else "O"

        else:
            print("\nНеправильный ход: Введи цифру [1-9] для выбора ячейки, или «0» для выхода из игры:")
            continue

print(f"Пошаговая игра в крестики-нолики.")
print(f"Игровое поле соответствует цифрам на правой цифровой клавиатуре:")
begin()