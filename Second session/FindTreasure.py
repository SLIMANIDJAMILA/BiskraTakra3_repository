def PrintWelcomeToTreasuryGame():
    print(f'Welcome To Treasury Game')
    print('Choose a path')


if __name__ == '__main__':
    PrintWelcomeToTreasuryGame()
    DoorColor = input('Type Which door do you choose : \n 1.Red Door \n 2.Green Door \n 3.Blue Door \n')
    if DoorColor.lower() == 'red':
        print(f'The Snake appear So Game is Over')
    elif DoorColor.lower() == 'blue':
        print(f'The Lion appear So Game is Over')
    elif DoorColor.lower() == 'green':
        ChooseOption = int(input('Type 1 Or 2 : '))
        if ChooseOption == 1:
            print(f'The Elephant appear So Game is Over')
        if ChooseOption == 2:
            print(f'You find the Gold You Won')
        else:
            print(f'You Typed a Wrong Option')
    else:
        print(f'You Typed a Wrong Color')
