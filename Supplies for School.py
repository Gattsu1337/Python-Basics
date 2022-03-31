number_of_pencils = int(input())
number_of_markers = int(input())
liters_of_cleaning_detergent = int(input())
sale = int(input()) / 100

pencils = number_of_pencils * 5.80
markers = number_of_markers * 7.20
cleaning_detergent = liters_of_cleaning_detergent * 1.20

sum = pencils + markers + cleaning_detergent
final_sum =  sum - (sum * sale)
print(final_sum)