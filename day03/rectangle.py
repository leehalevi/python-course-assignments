import sys

height = float(sys.argv[1])
width = float(sys.argv[2])
area = height*width
perimeter = (2*width) + (2*height)
print(f"The area of the rectangle is {area}")
print(f"The perimeter of the rectangle is {perimeter}")