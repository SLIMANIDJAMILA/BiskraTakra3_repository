def calculate_weight_of_body_bmi():
    print(f'Welcome To calculate weight of body bmi')


if __name__ == '__main__':
    calculate_weight_of_body_bmi()
    weight = float(input('What is your weight in Kg?\n'))
    height = float(input('What is your height in m?\n'))
    if weight or height != 0:
        bmi = weight/(height*2)
        if bmi < 18.5:
            print(f'Your BMi => {bmi} Weight is Low')
        elif 18.5 < bmi < 25:
            print(f'Your BMi => {bmi} Weight is in Normal state')
        elif bmi > 30:
            print(f'Your BMi => {bmi} Overweight state')
    else:
        print(f'Wrong info')
