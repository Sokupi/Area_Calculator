import math

def get_valid_float(prompt):  # Checks for the input to be positive
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print('Value must be positive')
            else:
                return value
        except ValueError:
            print('Value must be an integer')


def area_calculator():
    while True:
        print("\nArea Calculator")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Circle")
        print("5. Exit")

        choice = input("Enter your choice(1 - 5): ")

        if choice == "1":
            print("You have chosen Square")
            print("")

            try:
                side = get_valid_float("Enter the side length of the square: ")  # Takes in the side length value
                area = side ** 2  # Calculates the area of the Square (Area = side^2)
                print(f"The area of your Square is {area}m²")

            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "2":
            print("You have chosen Rectangle")
            print("")

            try:
                width = get_valid_float("Enter the width of the rectangle: ")  # Takes in the width value
                height = get_valid_float("Enter the height of the rectangle: ")  # Takes in the height value
                area = width * height  # Calculates the area of the Rectangle (Area = width x height)
                print(f"The area of your Rectangle is {area:.2f}m²")

            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "3":
            print("You have chosen Triangle")
            print("")

            try:
                base = get_valid_float("Enter the Base length of the triangle: ")  # Takes in the Width value
                height = get_valid_float("Enter the Height of the triangle: ")  # Takes in the Height Value
                area = 0.5 * base * height  # Calculates the area of the Triangle (1/2 x base x height)
                print(f"The area of your Triangle is {area:.2f}m²")

            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "4":
            print("You have chosen Circle")
            print("")

            try:
                radius = get_valid_float("Enter the radius of the circle: ")  # Takes in the radius value
                area = math.pi * (radius ** 2)  # Calculates the area of the Circle (π x radius²)
                print(f"The area of your Circle is {area:.2f}m²")

            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "5":
            print("Exiting the Program")
            break  # This closes the program

        else:
            print("Invalid Choice")


area_calculator()
