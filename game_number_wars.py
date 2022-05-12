player1 = input()
player2 = input()
number_wars = False
points_of_player1 = 0
points_of_player2 = 0
command = input()
while command != 'End of game':
    card_of_player1 = int(command)
    card_of_player2 = int(input())
    if card_of_player1 == card_of_player2:
        number_wars = True
        break
    elif card_of_player1 > card_of_player2:
        points_of_player1 += card_of_player1 - card_of_player2
    else:
        points_of_player2 += card_of_player2 - card_of_player1
    command = input()
if number_wars:
    print(f"Number wars!")
    second_card_of_player1 = int(input())
    second_card_of_player2 = int(input())
    if second_card_of_player1 > second_card_of_player2:
        print(f"{player1} is winner with {points_of_player1} points")
    else:
        print(f"{player2} is winner with {points_of_player2} points")
elif command == "End of game":
    print(f"{player1} has {points_of_player1} points")
    print(f"{player2} has {points_of_player2} points")