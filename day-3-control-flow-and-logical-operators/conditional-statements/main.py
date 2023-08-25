print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You can ride the rollercoster!")
    age = int(input("What is your age? "))
    if age > 18:
        print("Adult tickets are $12.")
        ticket_price = 12
    elif age < 12:
        print("Child tickets are $5.")
        ticket_price = 5
    elif 45 <= age <= 55:
        print("Mid-life crisis tickets are $0.")
        ticket_price = 0
    else:
        print("Youth tickets are $7")
        ticket_price = 7
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        print(f"Please pay ${ticket_price + 3}. ")
    elif wants_photo == "N":
        print(f"Please pay ${ticket_price}. ")
    else:
        print("I don't understand, Sir/Ma'am. ")
else:
    print("You can't ride the rollercoster!")
