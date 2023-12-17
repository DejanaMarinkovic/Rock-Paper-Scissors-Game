import random

while True:
    user = int(input("Choose 1 for paper, 2 for scissors, and 3 for rock: "))
    computer = random.randint(1, 3)

    if user == 1:
        print('''
        ***** You chose: *****\n 
        -------------------------------------------------------------
        |  8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba, |
        |  88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8 | 
        |  88       d8 ,adPPPPP88 88       d8 8PP""""""" 88         | 
        |  88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88         | 
        |  88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88         | 
        |  88                     88                                | 
        |  88                     88                                |
        -------------------------------------------------------------
        ''')
    elif user == 2:
        print('''
        ***** You chose: *****\n 
        -----------------------------------------------------------------------------------                     
        |                         88                                                      | 
        |                         ""                                                      | 
        |                                                                                 |
        |    ,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba, | 
        |    I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    "" | 
        |     `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,  |
        |    aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I | 
        |    `"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"' |
        -----------------------------------------------------------------------------------
        ''')
    elif user == 3:
        print('''
        ***** You chose: *****\n
        --------------------------------------------------                                             
        |                                      88        | 
        |                                      88        | 
        |                                      88        | 
        |    8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8  | 
        |    88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"   | 
        |    88         8b       d8 8b         8888[     | 
        |    88         "8a,   ,a8" "8a,   ,aa 88`"Yba,  | 
        |    88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a |
        --------------------------------------------------
        
                 
                    
        ''')

    if computer == 1:
        computer_choice = '''
        -------------------------------------------------------------
        |  8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba, |
        |  88P'    "8a ""     `Y8 88P'    "8a a8P_____88 88P'   "Y8 | 
        |  88       d8 ,adPPPPP88 88       d8 8PP""""""" 88         | 
        |  88b,   ,a8" 88,    ,88 88b,   ,a8" "8b,   ,aa 88         | 
        |  88`YbbdP"'  `"8bbdP"Y8 88`YbbdP"'   `"Ybbd8"' 88         | 
        |  88                     88                                | 
        |  88                     88                                |
        -------------------------------------------------------------
        '''
    elif computer == 2:
        computer_choice = '''
        -----------------------------------------------------------------------------------                     
        |                         88                                                      | 
        |                         ""                                                      | 
        |                                                                                 |
        |    ,adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba, | 
        |    I8[    "" a8"     "" 88 I8[    "" I8[    "" a8"     "8a 88P'   "Y8 I8[    "" | 
        |     `"Y8ba,  8b         88  `"Y8ba,   `"Y8ba,  8b       d8 88          `"Y8ba,  |
        |    aa    ]8I "8a,   ,aa 88 aa    ]8I aa    ]8I "8a,   ,a8" 88         aa    ]8I | 
        |    `"YbbdP"'  `"Ybbd8"' 88 `"YbbdP"' `"YbbdP"'  `"YbbdP"'  88         `"YbbdP"' |
        -----------------------------------------------------------------------------------
        '''
    elif computer == 3:
        computer_choice = '''
        --------------------------------------------------                                             
        |                                      88        | 
        |                                      88        | 
        |                                      88        | 
        |    8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8  | 
        |    88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"   | 
        |    88         8b       d8 8b         8888[     | 
        |    88         "8a,   ,a8" "8a,   ,aa 88`"Yba,  | 
        |    88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a |
        --------------------------------------------------
        '''

    print("        ***** Computer chose: *****")
    print(computer_choice)

    if user == computer:
        print("It's a tie! Play again.")
    elif user == 1 and computer == 2:
        print("You lost!")
        break
    elif user == 1 and computer == 3:
        print("You won!")
        break
    elif user == 2 and computer == 1:
        print("You won!")
        break
    elif user == 2 and computer == 2:
        print("It's a tie! Play again.")
    elif user == 2 and computer == 3:
        print("You lost!")
        break
    elif user == 3 and computer == 1:
        print("You lost!")
        break
    elif user == 3 and computer == 2:
        print("You won!")
        break
    elif user == 3 and computer == 3:
        print("It's a tie! Play again.")



