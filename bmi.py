def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi=weight/(height**2)

    print(f"Your BMI is : {bmi:.2f}")

    if bmi<18.5:
        print("You are underweight.")
    elif 18.5 <= bmi <24.9:
        print("You are normal weight. ")
    elif bmi >24.9:
        print("You are overweight. ")

calculate_bmi(weight=57, height=1.73)