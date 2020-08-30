import random #random function for randomisation
import sys #module for quiting program

def deal(): #function name
    boxes = {"box1": 200, 'box2':250, 'box3':500, 'box4':1000, 'box5':10000}#dic with boxs values 

    entry_list = list(boxes.items())#turns dic into a list
    random_entry = random.choice(entry_list) #random box alloctor 
    print('')
    print('')
    print('Your Box =   :' + str(random_entry))#prints the choosen box
    print('')
    print('')
    random_entry1 = random.choice(entry_list)#random box alloctor for new box
    restart = 'yes'
    restart = input('Pick another box? Yes or No '.lower())#user input, not case senstive
    if restart == 'yes':

        

        if random_entry == random_entry1:
            
            deal()
            random_entry1 = random.choice(entry_list)#randomises box again if same box picked
        elif random_entry < random_entry1:# if value is higher print this statement
            print('')
            print('')
            print('Increased amount, Box number = '+str(random_entry1))
            print('')
            print('')
        else: #otherwise print this statement
            print('')
            print('')
            print('lower value  ' + str (random_entry1))
            print('')
            print('')
            
    if restart == 'no': #if no is picked print the value they won
        print('You won = ' +str(random_entry))
        



    again = input('Another game? yes or no ').lower()#user input for another game
    while again == 'yes':#if yes run function
        deal()
    while again == 'no':#if no run sys.exit to kill program
        sys.exit()
deal()
