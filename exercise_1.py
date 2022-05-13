price_for_one_page = float(input())
price_for_one_cover = float(input())
discount_percentage = int(input())
designer_cost = float(input())
team_percentage = int(input())
pages = 899
covers = 2
price_for_all_pages = price_for_one_page * pages
price_for_all_covers = price_for_one_cover * covers
price_for_both = price_for_all_pages + price_for_all_covers
price_after_discount = price_for_both - (price_for_both * discount_percentage / 100)
price_after_discount += designer_cost
price_after_team = price_after_discount - (price_after_discount * team_percentage / 100)
print(f"Avtonom should pay {price_after_team:.2f} BGN.")
