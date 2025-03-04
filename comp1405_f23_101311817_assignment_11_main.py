# Emily Amos 101311817

# Description: Create lists and dictionaries wiht the room and object info.
# Arguments: None
# Return: list, list, dict
def createLists() -> (list, list, dict):
    x = []
    y = []
    z = {}
    tempList = []
    position = 0

    file = open("comp1405_f23_101311817_assignment_10_data.txt", "r")

    while True:
        temp = file.readline().strip('\n')
        
        if temp == '':
            break
        
        if temp[0] == '@':
            tempList = temp[1:].split(':')
            position = int(tempList[0])
            x.insert(position, [tempList[1]])
            
            tempList = x[position][0].split('|')
            x[position] = tempList
            
            for i in range(len(x[position])):
                tempList = x[position][i].split('>')
                x[position][i] = tuple(tempList)
                
        elif temp[0] == '^':
            tempList = temp[1:].split(':')
            position = int(tempList[0])
            y.insert(position, [tempList[1]])
            
            tempList = y[position][0].split('|')
            y[position] = tempList
            
        elif temp[0] == '*':
            tempList = temp[1:].split(':')
            position = int(tempList[0])
            z[position] = tempList[1]
            
            tempList = z[position].split('|')
            z[position] = tempList
    file.close()
    return x, y, z

# Description: Print an introduction paragraph for the text-based adventure game.
# Arguments: None
# Return: None
def gameIntro() -> None:

    intro_paragraph = """
    You slowly open your eyes, the dim light revealing a room that seems eerily familiar. As you
    regain consciousness, you realize that you're lying on a floor that feels both foreign and oddly
    comforting. The air is heavy with an unsettling stillness, and shadows dance across the walls.

    Panic sets in as you try to recall how you ended up here. The last thing you remember is going
    to bed in your own home, yet this place is twisted, a distorted version of your childhood haven.
    The furniture is warped, the colors are muted, and an unsettling hush blankets the atmosphere.

    Struggling to make sense of your surroundings, you sit up and take in the room. Vague memories
    flicker in your mind, like fragments of a forgotten dream. The room holds remnants of your
    past, but everything is distorted, like a haunting reflection of the familiar.

    Questions linger in your mind: How did you get here? What happened to your once-familiar home?
    With a shiver down your spine, you realize that this is no ordinary morning. The journey ahead
    promises to be filled with mysteries, challenges, and the unsettling truth behind this twisted reality.
    """
    
    print(intro_paragraph)
    print("Type 'h' or 'help' to view game commands.\n")

# Description: Print a help command menu for the text-based adventure game.
# Arguments: None
# Return: None
def helpMenu() -> None:
    
    commands = """
  Commands:
    - 'h' or 'help': Display commands
    - 'n' or 'north': Move north
    - 's' or 'south': Move south
    - 'e' or 'east': Move east
    - 'w' or 'west': Move west
    - 'l' or 'look': Look around the room for objects
    - 'x [object]' or 'examine [object]': Examine an object
    - 'q' or 'quit': Quit the game
    
  TIP: If you're having a hard time figuring out an object's name, try looking around the room.
    """

    print(commands)

# Description: Retrieve info about the current room and generate a list of directions and corresponding room numbers.
# Arguments: list, list, int
# Return: list, list
def infoFinder(adjacencyList: list, roomInfoList: list, playerLocation: int) -> (list, list):
   
    # Retrieve information about the current room
    current_room_info = roomInfoList[playerLocation]

    # Generate a list of directions and corresponding room numbers
    tempList = []

    for neighbor in adjacencyList[playerLocation]:
        direction = ''
        if neighbor[1] == 'n':
            direction = 'North'
        elif neighbor[1] == 's':
            direction = 'South'
        elif neighbor[1] == 'e':
            direction = 'East'
        elif neighbor[1] == 'w':
            direction = 'West'

        # Append a tuple of direction and room number to tempList
        tempList.append([direction, neighbor[0]])

    return current_room_info, tempList

# Description: Validate user input for the text-based adventure game.
# Arguments: list, dict, int
# Return: None
def inputValidation(adjacencyList: list, objectInfoDict: dict, playerLocation: int) -> str:
    
    while True:
        user_input = input("Enter a command: ").lower()  # Convert input to lowercase for case-insensitivity

        # Quit, look and help commands
        if user_input in {'q', 'quit', 'l', 'look', 'h', 'help'}:
            break

        # Direction commands
        elif user_input in {'n', 'north', 's', 'south', 'w', 'west', 'e', 'east'}:
            valid_directions = [adjacencyList[playerLocation][i][1].lower() for i in range(len(adjacencyList[playerLocation]))]
            
            if user_input == 'north':
                user_input = 'n'
            elif user_input == 'south':
                user_input = 's'
            elif user_input == 'east':
                user_input = 'e'
            elif user_input == 'west':
                user_input = 'w' 
            
            if user_input in valid_directions:
                break
            else:
                print("There's nothing notable in that direction. (Invalid Command)\n")

        # Examine command
        elif user_input.startswith(('x', 'examine')):
            if playerLocation in objectInfoDict:
                if user_input[2:] == objectInfoDict[playerLocation][0].lower() or user_input[8:] == objectInfoDict[playerLocation][0].lower():
                    break
                else:
                    print("There's no object with that name around. (Invalid Command)\n")
            else:
                print("There's no notable objects around. (Invalid Command)\n")

        else:
            print("You cannot do that. (Invalid Command)\n")
    
    return user_input

def main():

    # Initialize variables
    playerLocation = 0
    objectsEncountered = []
    
    adjacencyList, roomInfoList, objectInfoDict = createLists()
    
    gameIntro()
    
    while True:
        roomInfo, roomExits = infoFinder(adjacencyList, roomInfoList, playerLocation)
        
        # Print the desired room info
        print(f"{roomInfo[0]}:\n{roomInfo[1]}\n")
    
        # Print the object if present
        print(f"Objects Encountered ({len(objectsEncountered)}/{len(objectInfoDict)}):")
        if len(objectsEncountered) == 0:
            print("None")
        else:
            for i in range(len(objectsEncountered)):
                print(f"{objectsEncountered[i]}", end="    ")
            print("")
        #if playerLocation in objectInfoDict:
            #print(f"Object(s):\n{objectInfoDict[playerLocation][0]}\n")
        
        # Print the exit directions in the same line
        direction_names = [direction[0] for direction in roomExits]
        print(f"\nAvailable Exits:\n{'    '.join(direction_names)}\n")
        
        # Recieve valid user input
        validInput = inputValidation(adjacencyList, objectInfoDict, playerLocation)
        
        # Command actions
        if validInput == 'q' or validInput == 'quit':
            break
        elif validInput == 'h' or validInput == 'help':
            helpMenu()
        elif validInput == 'l' or validInput == 'look':
            if playerLocation in objectInfoDict:
                print(f"\nYou look around the area. The {objectInfoDict[playerLocation][0]} catches your eye.\n")
            else:
                print("\nYou look around the area, but nothing catches your eye.\n")
        elif validInput[:1] == 'x' or validInput[:7] == 'examine':
            if objectInfoDict[playerLocation][0] not in objectsEncountered:
                objectsEncountered.append(objectInfoDict[playerLocation][0])
            
            print(f"\nYou take a closer look at the {objectInfoDict[playerLocation][0]}.")
            print(f"\n{objectInfoDict[playerLocation][0]}:\n{objectInfoDict[playerLocation][1]}\n")
        else:
            # Iterate through the adjacency list for the current player location
            for neighbor in adjacencyList[playerLocation]:
                if validInput[0] == neighbor[1].lower():
                    # If the direction in validInput matches a direction in the adjacency list
                    playerLocation = int(neighbor[0])
                    
                    if validInput[0] == 'n':
                        tempVar = 'North'
                    elif validInput[0] == 's':
                        tempVar = 'South'
                    elif validInput[0] == 'e':
                        tempVar = 'East'
                    else:
                        tempVar = 'West'
                    
                    print(f"\nYou go {tempVar}.\n")
                    break
main()