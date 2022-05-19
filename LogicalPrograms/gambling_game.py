import random


def gambling(number_of_bets, goal, money):
    win = 0
    lose = 0
    count = 0

    for i in range(number_of_bets):
        random_number = random.random()
        count += 1
        if random_number > 0.5:
            money += 1
            win += 1
        else:
            money -= 1
            lose += 1

        if money == goal:
            print('You have reached your goal on bet number ' + str(count))
            break
        elif money == 0:
            print('You have exhausted your money')
            break
    print('Number of win : ' + str(win))
    print('Number of lose :' + str(lose))
    print('Percentage of win : ' + str((win * 100) / count))
    print('Percentage of lose : ' + str((lose * 100) / count))


if __name__ == "__main__":
    numberofbets = int(input('Enter number of times you want to gamble: '))
    goal = int(input('Enter your goal: '))
    money = int(input('Enter amount of money you have: '))
    gambling(numberofbets, goal, money)