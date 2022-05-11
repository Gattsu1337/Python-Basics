name_of_tournament = input()
number_of_matches = 0
all_matches = 0
opponent_score = 0
home_score = 0
difference = 0
matches_won = 0
matches_lost = 0
while name_of_tournament != 'End of tournaments':
    number_of_matches = int(input())
    for game in range(1, number_of_matches + 1):
        all_matches += 1
        home_score = int(input())
        opponent_score = int(input())
        difference = abs(home_score - opponent_score)
        if home_score < opponent_score:
            matches_lost += 1
            print(f"Game {game} of tournament {name_of_tournament}: lost with {difference} points.")
        else:
            matches_won += 1
            print(f"Game {game} of tournament {name_of_tournament}: win with {difference} points.")
    name_of_tournament = input()
percent_won = matches_won / all_matches * 100
percent_lost = matches_lost / all_matches * 100
print(f"{percent_won:.2f}% matches win")
print(f"{percent_lost:.2f}% matches lost")