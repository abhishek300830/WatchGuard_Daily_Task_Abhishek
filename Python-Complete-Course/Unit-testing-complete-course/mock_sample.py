from mock_dice import roll_dice


def guess_number(num):
    result = roll_dice()

    if result == num:
        return "YOU WON"
    else:
        return "YOU LOST"
