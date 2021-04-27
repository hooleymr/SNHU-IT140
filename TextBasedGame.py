# MASON HOOLEY #

# GLOBAL VARIABLES #
inventoryList = []

rooms = {
    'Foyer': {'South': 'Blood Stores', 'North': 'Scrying Chamber', 'West': 'Western Hall', 'East': 'Eastern Hall',
              'item': 'Wooden Stake'},
    'Blood Stores': {'North': 'Foyer', 'East': 'Balcony', 'item': 'Bible'},
    'Balcony': {'West': 'Blood Stores', 'item': 'Holy Water'},
    'Western Hall': {'South': 'Trophy Room', 'East': 'Foyer'},
    'Trophy Room': {'North': 'Western Hall', 'item': 'Helsing Hat'},
    'Eastern Hall': {'North': 'Coffin Chambers', 'West': 'Foyer'},
    'Coffin Chambers': {'South': 'Eastern Hall', 'item': 'Crucifix'},
    'Scrying Chamber': {'South': 'Foyer', 'West': 'Study', 'East': 'Armory'},
    'Armory': {'West': 'Scrying Chamber', 'item': 'Rosemary Beads'},
    'Study': {'East': 'Scrying Chamber', 'item': 'Lord Dracula'}
}

def winner():
    print('--------------------------------------------------------------------')
    print('You entered the study and found Lord Dracula.')
    print('You do not have the items needed to defeat him and became his supper')
    print('You need all six items to defeat him!')
    print('Crucifix, Helsing Hat, Bible')
    print('Rosemary Beads, Holy Water, Wooden Stake')
    print('Your Items:', inventoryList)
    print('You Lose!')
    print('--------------------------------------------------------------------')
    exit()

def loser():
    print('--------------------------------------------------------------------')
    print('You entered the study and found Lord Dracula.')
    print('You have collected all the items and can defeat him!')
    print('The crucifix repels him, and the Helsing Hat strikes fear.')
    print('The Bible angers him, and the Rosemary Beads immobilize him.')
    print('The Holy Water burns him and the Wooden Stake finishes him.')
    print('You Win!')
    print('--------------------------------------------------------------------')
    exit()

def startUp():
    print('--------------------------------------------------------------------')
    print('Welcome to the Lord Dracula Text Adventure Game!')
    print('Move between rooms to collect the 6 items before facing Lord Dracula')
    print('Move commands: go South, go North, go East, go West')
    print("Add to inventory: get 'item name' ")
    print('--------------------------------------------------------------------')

def main():
    startUp()

# STARTING ROOM #
    current_room = 'Eastern Hall'
# GAME PLAY LOOP #
    while True:
        if current_room == 'Study' and len(inventoryList) < 6:  #VICTORY CHECKS
            winner()
        elif current_room == 'Study' and len(inventoryList) >= 6:  #VICTORY CHECKS
            loser()

        print('--------------------------------------------------------------------')
        print('You are currently in the:', current_room)
        print('Inventory:', inventoryList)
        for room, connected in rooms.items():
            if (current_room == room) and ('item' in connected):
                print('You see a', rooms[current_room]['item'])
        print('--------------------------------------------------------------------')

        player_command = input('Enter a command: ').split()  # SPLIT COMMAND INTO ACTION AND DIRECTION IF PRESENT

        if len(player_command) > 2:  # MAKES 2 WORD ITEMS INTO SINGLE STRING
            player_command[1] = ' '.join(player_command[1:])

        if player_command[0].lower() == 'go':  #LOGIC IF PLAYER MOVES ROOMS
            for room,connected in rooms.items():
                if (current_room == room) and (player_command[1].capitalize() in connected):
                    current_room = rooms[room][player_command[1].capitalize()]
                    break
                if(current_room == room) and (player_command[1].capitalize() not in connected):
                    print("You can't go that way!")

        elif player_command[0].lower() == 'get':  #GET ITEM FROM ROOM AND DELETE ITEM FROM ROOMS
            for room,connected in rooms.items():
                if (current_room == room) and ('item' in connected) and (rooms[current_room]['item'] == player_command[1]):
                    inventoryList.append(rooms[current_room]['item'])
                    print('You got the',rooms[current_room]['item'])
                    del rooms[current_room]['item']
                elif (current_room == room) and ('item' not in connected):  #LOGIC IF ROOM HAS ITEM BUT INPUT ISNT CORRECT ITEM
                    print('There are no items in this room')
                elif (current_room == room) and ('item' in connected) and (rooms[current_room]['item'] != player_command[1]):  #LOGIC IF NO ITEM IN ROOM
                    print('That item is not in this room: Check your spelling!')
        else:
            print('Invalid command, please input a go or get command and ensure your spelling is correct')
main()