def divide(num) -> str:
    return "{:.2f}".format(num * 0.12)


def total(num) -> str:
    return "{:.2f}".format(num + float(divide(num)))


def calculate():
    amount = float(input("Enter Num: "))
    print(f"VAT: {divide(amount)}")
    print(f"Total Amount: {total(amount)}")
