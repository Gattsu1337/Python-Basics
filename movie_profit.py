movie = input()
days = int(input())
tickets = int(input())
ticket_cost = float(input())
cinema_percentage = int(input())
sum_from_day = tickets * ticket_cost
sum_for_period = sum_from_day * days
percentage_taken = sum_for_period * (cinema_percentage / 100)
final_sum = sum_for_period - percentage_taken
print(f"The profit from the movie {movie} is {final_sum:.2f} lv.")
