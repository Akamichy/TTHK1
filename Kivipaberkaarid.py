from random import randint

var = ["камень", "ножницы", "бумага"]
decision = input("Здравствуйте, вы играете в камень-ножницы-бумага. Если хотите играть с роботом - напишите 1, если с человеком - 2. ")
score1 = 0
score2 = 0
fscore = 0

if decision == "1":
    print("Хорошо! Играем до трех побед.")
    while score1 < 3 and score2 < 3:
        var2 = input(f'Пожалуйста, выберите {var[0]}, {var[1]} или {var[2]}. ').lower()
        if var2 not in var:
            while var2 not in var:
                var2 = input(f'Пожалуйста, выберите {var[0]}, {var[1]} или {var[2]}. ').lower()
        num = randint(0, 2)
        robot_var = var[num]
        print(robot_var)
        if var2 == robot_var:
            print(f'{var2} и {robot_var}, ничья.')
        elif var2 == "камень" and num == 2:
            score2 += 1
            fscore += 1
            print("Камень против бумаги. Плюс одно очко роботу.")
        elif var2 == "бумага" and num == 0:
            score1 += 1
            fscore += 1
            print("Бумага против камня. Плюс одно очко человеку.")
        elif var2 == "камень" and num == 1:
            score1 += 1
            fscore += 1
            print("Камень против ножниц. Плюс одно очко человеку.")
        elif var2 == "ножницы" and num == 0:
            score2 += 1
            fscore += 1
            print("Ножницы против камня. Плюс одно очко роботу.")
        elif var2 == "ножницы" and num == 2:
            score1 += 1
            fscore += 1
            print("Ножницы против бумаги. Плюс одно очко человеку.")
        elif var2 == "бумага" and num == 1:
            score2 += 1
            fscore += 1
            print("Бумага против ножниц. Плюс одно очко роботу.")
        print(f"Счет: Человек - {score1}, Робот - {score2}")
    print(f"Игра завершена! Вы закончили за {fscore} попыток")

if decision == 2:
    while score1 < 3 and score2 < 3:
        player1 = input(f'Игрок 1, выберите {var[0]}, {var[1]} или {var[2]}. ').lower()
        while player1 not in var:
            player1 = input(f'Игрок 1, выберите {var[0]}, {var[1]} или {var[2]}. ').lower()

        player2 = input(f'Игрок 2, выберите {var[0]}, {var[1]} или {var[2]}. ').lower()
        while player2 not in var:
            player2 = input(f'Игрок 2, выберите {var[0]}, {var[1]} или {var[2]}. ').lower()

        fscore += 2

        if player1 == player2:
            print(f'{player1} и {player2}, ничья.')
        elif player1 == "камень" and player2 == "ножницы":
            score1 += 1
            fscore += 1
            print("Камень против ножниц. Победа игрока 1.")
        elif player1 == "ножницы" and player2 == "бумага":
            score1 += 1
            fscore += 1
            print("Ножницы против бумаги. Победа игрока 1.")
        elif player1 == "бумага" and player2 == "камень":
            score1 += 1
            fscore += 1
            print("Бумага против камня. Победа игрока 1.")

        if player2 == "камень" and player1 == "ножницы":
            score2 += 1
            fscore += 1
            print("Камень против ножниц. Победа игрока 2.")
        elif player2 == "ножницы" and player1 == "бумага":
            score2 += 1
            fscore += 1
            print("Ножницы против бумаги. Победа игрока 2.")
        elif player2 == "бумага" and player1 == "камень":
            score2 += 1
            fscore += 1
            print("Бумага против камня. Победа игрока 2.")

        print(f"Счет: Игрок 1 - {score1}, Игрок 2 - {score2}")

    print(f"Игра завершена! Вы зкончили за {fscore} попыток")