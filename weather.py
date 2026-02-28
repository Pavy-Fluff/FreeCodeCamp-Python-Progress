# FreeCodeCamp - Python Basics
# In here i'll try to show a fun project that will make you decide if you should go outside or not

is_distance = 4
is_raining = False
has_car = True
has_bike = True
has_Uber_ride_app = True

if not is_distance:
    print("You stay at home.")
elif is_distance and is_raining:
    if has_car:
        print("I'll go with my car")
    elif has_bike:
        print("I won't go with my bike in this rain")
    elif has_Uber_ride_app:
        print("I'll go with a Uber... it's costly")
    else:
        print("I'll tell them that i cannot go.")
else:
    if has_car or has_bike or has_Uber_ride_app:
        print("I can comfortably go outside")
    else:
        print("I can just walk")

# It works, but it is only for boolean values, so that is_distance may be very VERY hard to read or the whole code... but that was what it was required to do.