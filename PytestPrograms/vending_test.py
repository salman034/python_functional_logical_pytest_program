
def vending_test(amount_to_return):
    possible_changes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    notes_list = []
    number_of_notes = 0
    while amount_to_return != 0:
        for i in possible_changes:
            if amount_to_return >= i:
                number_of_notes += 1
                amount_to_return -= i
                notes_list.append(i)
                vending_test(amount_to_return)
                break

    return number_of_notes, notes_list, amount_to_return


def test_vinding():
    no_of_notes, notes, balance = vending_test(200)
    assert balance == 0
    print("no.of notes: ", no_of_notes)
    print("notes retained: ", notes)