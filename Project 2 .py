# Name: Christopher Grullon
# Course: CSC 152 Programming Fundamentals
# Project: Project 2 – Parking Fines Calculator
# Description: Calculates a parking fine based on the number of minutes
# a vehicle is over the time limit and whether it is parked
# in a handicapped parking space.

minutes = int(input("Enter the number of minutes over the time limit: "))
handicapped = input("Is the vehicle parked in a handicapped parking space? (yes/no): ")

if minutes < 0:
    print("Invalid input: minutes cannot be negative.")
else:
    if minutes == 0:
        fine = 0
    elif minutes <= 15:
        fine = 10
    elif minutes <= 30:
        fine = 20
    elif minutes <= 60:
        fine = 40
    else:
        fine = 75

    if handicapped == "yes":
        fine += 150

    print("\nParking Fine")
    print(f"Minutes over time limit:", minutes)
    print(f"Handicapped parking:",handicapped)
    print("Fine due: $" + format(fine, ".2f"))
