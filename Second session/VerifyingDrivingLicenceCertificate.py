def verifying_driving_licence_certificate():
    print(f'Welcome To Verifying Driving Licence Certificate')


if __name__ == '__main__':
    verifying_driving_licence_certificate()
    print('Enter your Situation Conditions : ')
    algerian = input('Are you an algerian man or women?\n')
    age = int(input('How old are you ?\n'))
    if algerian.lower() == '':
        print('you did not enter one of the parameters')
    if (algerian.lower() == 'yes') and (age >= 18):
        print(f'you can got your Driving certificate ')
    elif (algerian.lower() == 'yes') or (age <= 18):
        print(f'you can got your Driving certificate ')
    else:
        print(f'you can not got your Driving certificate ')
