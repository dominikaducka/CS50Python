def main():
    mass = int(input('Mass[kg]: '))
    einstein(mass)

def einstein(mass):
    speed = pow(300000000,2)
    energy = mass*speed
    print(energy)

main()
