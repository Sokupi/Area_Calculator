Hello, this is my 4th project made in Python. I just finished a course in Python detailing how to create a short program and such. For this project, I am going to create an Area Calculator.
What this does is it asks the user what geometric shape it wants to quantify as well as the values it has so that the code calculates the missing values using the already established ones.

If you want to do one on your own, here is a step-by-step things you can do to create one on your own:

    1. MENU CREATION:

        > Start by printing a menu that lists different shapes like Square, Rectangle, Triangle, and Circle.
        > Ask the user to choose a shape by entering a number (e.g., 1 for Square, 2 for Rectangle, etc.).

    2. USER INPUT:

        > Based on the user’s choice, you’ll need to ask for the dimensions. For example:
            Square: You only need the length of one side.
            Rectangle: You need the width and the height.
            Triangle: You need the base and the height.
            Circle: You need the radius.

    2. FORMULAS:

        > Use the correct formula to calculate the area for each shape:
            Square: Side × Side
            Rectangle: Width × Height
            Triangle: ½ × Base × Height
            Circle: π × Radius² (you can use Python's math.pi for π).

    3. DISPLAY THE RESULTS:

        > After calculating the area, print the result for the user to see.

    3. HANDLE INVALID INPUTS:

        > If the user enters something unexpected (like choosing an option outside of 1–4), print an error message and ask again.