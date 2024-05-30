def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    a = d.removeprefix('$')
    f = float(a)
    return f


def percent_to_float(p):
    a = p.removesuffix('%')
    f = float(a) / 100
    return f

main()
