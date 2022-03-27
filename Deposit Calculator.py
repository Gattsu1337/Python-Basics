deposited_sum = float(input())
term_of_deposit = int(input())
annual_interest_rate = float(input()) / 100

sum = deposited_sum + term_of_deposit * ((deposited_sum * annual_interest_rate) / 12)

print(sum)