# FreeCodeCamp - Python Basics
# In here lets make a fun project where we have a member for a movie

base_ticket_price = 21
seat_type = "Unknown"
is_member = False
charges = 0

if is_member and base_ticket_price == 20:
    print("You are a member for this film")
    discount = 3
    seat_type = "Silver"
    if seat_type == "Silver":
        seat_type = "Gold"
        discount = 6
        print("You just became a Gold seater!")
    else:
        seat_type = "Premium"
        discount = 10
elif base_ticket_price > 20 and seat_type == "Unknown" and is_member != True:
    print("Thanks for the tip.")
    seat_type = "Premium"
    is_member = True
    discount = 10
else:
    discount = 0
    print("You are not a member for this movie")
    charges = 2

actual_price = base_ticket_price + charges - discount
print("Based on your rank, you will pay a total of:", actual_price)
