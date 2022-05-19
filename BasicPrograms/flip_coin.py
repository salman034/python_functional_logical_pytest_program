import random


def flip_coin(toss):
    """
    This method is to find head or tail and its percentage.
    :return: Percentage
    """

    head = 0
    tail = 0
    while toss > 0:
        flip = random.random()
        if flip > 0.5:
            print('Head...')
            head += 1
        else:
            print('Tail...')
            tail += 1
        toss -= 1
    print('head : ', head, ' tail : ', tail)
    total = head + tail
    head_per = "{:.2f}".format(head * 100 / total)
    tail_per = "{:.2f}".format(tail * 100 / total)
    print('head% : ', head_per, ' $ tail% : ', tail_per)


if __name__ == '__main__':
    print("Enter how many time you want to flip the coin")
    toss = int(input())
    flip_coin(toss)