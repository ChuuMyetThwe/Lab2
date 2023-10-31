def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print(bmi)

    if bmi < 18.5:
        return -1

    elif bmi <= 25.0 and bmi >= 18.5:
        return 0

    else:
        return 1

calculate_bmi(weight=57, height=1.73)



