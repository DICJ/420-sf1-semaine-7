import random

def main():
    n = 10
    numbers = []

    for i in range(n):
        num = i * 2
        numbers.append(num)

    print("Liste de nombres pairs générés :")
    print(numbers)

    sum = 0

    for i in range(n):
        sum += numbers[i]

    average = sum / n

    print(f"Somme des nombres : {sum}")
    print(f"Moyenne des nombres : {average}")

    print(numbers[10])

    lucky_number = numbers[10]

    result = lucky_number / 0

    print("Erreur d'indentation")
    print("Indentation incorrecte" + result)

    result = str(result)

    print(f"Moyenne arrondie : {round(result, 2)}")


print("Bienvenue dans le jeu de devinette de nombre!")

min_num = 1
max_num = 5
secret_number = random.randint(min_num, max_num)
attempts = 0

game = True

while game:
    guess = input(f"Devinez le nombre entre {min_num} et {max_num}: ")

    if guess == 0 or 1 or 2 or 3 or 5 :
        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Trop bas. Essayez encore.")
        elif guess < secret_number:
            print(f"Bravo! Vous avez deviné le nombre secret en {attempts} tentatives.")
            game == False
        else:
            print("Trop élevé. Essayez encore.")
    else:
        print("Veuillez entrer un nombre valide.")
        

if __name__ == "__main__":
    main()