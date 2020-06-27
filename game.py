import random

# GRA: PAPIER, KAMIEŃ, NOŻYCE

my_points = 0
PC_points = 0

# Główna pętla gry
while my_points < 3 or PC_points < 3:

    # Pobieranie mojego wyboru i sprawdzanie poprawności
    player = input("papier, kamień, nożyce?\n")
    if player != "papier" and player != "kamień" and player != "nożyce":
        print("Brak takiej figury!")
        continue
    # Wyświetlenie mojego wyboru
    if player == "kamień":
        print("O", "vs.", end=" ")
    elif player == "papier":
        print("__", "vs.",end=" ")
    elif player == "nożyce":
        print("8<", "vs.", end=" ")

    # Losowy wybór komputera
    computer = random.randint(1, 3)

    # Wyświetlenie wyboru komputera
    if computer == 1:
        choice = "kamień"
        print("O")
    elif computer == 2:
        choice = "papier"
        print("__")
    elif computer == 3:
        choice = "nożyce"
        print("8<")

    # Porównie obu wyborów i wyświetlenie informacji komu przyznany został punkt
    if player == choice:
        print("Remis!")
    elif player == "kamień" and choice == "nożyce":
        my_points += 1
        print("Punkt dla mnie!")
    elif player == "kamień" and choice == "papier":
        PC_points += 1
        print("Punkt dla komputerka!")
    elif player == "nożyce" and choice == "papier":
        my_points += 1
        print("Punkt dla mnie!")
    elif player == "nożyce" and choice == "kamień":
        PC_points += 1
        print("Punkt dla komputerka!")
    elif player == "papier" and choice == "kamień":
        my_points += 1
        print("Punkt dla mnie!")
    elif player == "papier" and choice == "nożyce":
        PC_points += 1
        print("Punkt dla komputerka!")

    # Sprawdzenie przyznanych punktów i informacja kto wygrał
    if my_points == 3:
        print("Wygrałam!")
        break
    elif PC_points == 3:
        print("Przegrałam :/")
        break

print("Koniec gry!")
