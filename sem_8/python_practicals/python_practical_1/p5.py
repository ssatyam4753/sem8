#Write a Python program which accepts the radius of a circle from the user and compute the area
PI = 3.14159265

def main() :
    radius = float(input("enter radius: "))
    print("radius: ",radius)
    # area of circle = pi*r*r
    print("area: ",PI *radius*radius)

if __name__ == "__main__" :
    main()
