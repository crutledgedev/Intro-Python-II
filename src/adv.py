from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# create items

item = {
    'rock': Item("rock", "Just an ordinary rock... this isn't a survival game, leave it alone"),
    'newspaper': Item("newspaper", "An old weathered news paper too faded to read"),
    'shoe': Item("shoe", "An old shoe.. I wonder how it got here? Maybe someone got a little too close to that edge. Be careful!"),
    'crate': Item("crate", "Just an emptyh wooden crate"),
    'spider': Item("spider", "An ordinary spider... not much a treasure, but it's yours if you want to keep it"),
    'sign': Item("sign", "This sign reads - NO TRESPASSING"),


}


# add items to rooms

room['outside'].items.append(item['rock'])
room['outside'].items.append(item['sign'])
room['foyer'].items.append(item['newspaper'])
room['overlook'].items.append(item['shoe'])
room['narrow'].items.append(item['crate'])
room['treasure'].items.append(item['spider'])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("Chance", room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while True:
    print(f"Items in room:")
    for each in player1.current_room.items:
        print(each.name)
    answer = input(
        f"\n{player1.name}'s location: {player1.current_room.name}. {player1.current_room.description} \n\nChoose n, s, e, w, i, q, take [item], drop [item]: ")
    if len(answer) == 1:
        player1.move(answer)
    else:
        takeOrDrop = answer.split()[0]
        itemName = answer.split()[1]
        player1.take_drop(takeOrDrop, itemName)
