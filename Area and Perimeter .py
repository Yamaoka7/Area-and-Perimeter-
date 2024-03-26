import math

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

# Add functions for other shapes (e.g., triangle, square)

def main():
    shape = input("Enter shape (circle/rectangle): ")
    if shape == "circle":
        radius = float(input("Enter radius: "))
        print("Area:", calculate_circle_area(radius))
        print("Perimeter:", calculate_circle_perimeter(radius))
    elif shape == "rectangle":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area:", calculate_rectangle_area(length, width))
        print("Perimeter:", calculate_rectangle_perimeter(length, width))
    else:
        print("Invalid shape.")

if __name__ == "__main__":
    main()
