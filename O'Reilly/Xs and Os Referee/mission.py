from typing import List


def checkio(game_result: List[str]) -> str:
    game_str = ''.join(game_result)
    print(game_str)
    all_results = game_result + [game_str[i:9:3] for i in range(3)] \
                  + [game_str[0:9:4], game_str[2:8:2]]
    print(all_results)

    if 'XXX' in all_results:
        return "X"
    elif 'OOO' in all_results:
        return "O"
    else:
        return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print(
        "Coding complete? Click 'Check' to review your tests and earn cool rewards!")
