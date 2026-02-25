def show_instructions():
    print("===== ZOMBIE BUNKER ESCAPE =====")
    print("Rotting hands scrape at the steel above as the city dies overhead.")
    print("You are sealed in an underground bunker, stalked by the Alpha Zombie.")
    print("Collect 6 survival items before entering the Control Room,")
    print("or the Alpha Zombie will tear through your defenses and end you.")
    print()
    print("Move commands: go North, go South, go East, go West")
    print("Get items: get <item name>")
    print("You may enter two commands separated by 'and'")
    print("  (e.g., 'go North and get Shotgun').")
    print("-" * 40)


def build_world():
    """Return a dict of rooms with exits and items."""
    rooms = {
        "Central Hub": {
            "name": "Central Hub",
            "exits": {
                "North": "Armory",
                "South": "Observation Post",
                "East": "Lab",
                "West": "Storage Bay",
            },
            "item": None
        },
        "Armory": {
            "name": "Armory",
            "exits": {
                "South": "Central Hub",
                "East": "Med Bay",
            },
            "item": "Shotgun"
        },
        "Med Bay": {
            "name": "Med Bay",
            "exits": {
                "West": "Armory",
                "South": "Lab",
            },
            "item": "Med Kit"
        },
        "Storage Bay": {
            "name": "Storage Bay",
            "exits": {
                "East": "Central Hub",
                "South": "Generator Room",
            },
            "item": "Key Card"
        },
        "Generator Room": {
            "name": "Generator Room",
            "exits": {
                "North": "Storage Bay",
                "East": "Observation Post",
            },
            "item": "Generator Fuse"
        },
        "Lab": {
            "name": "Lab",
            "exits": {
                "North": "Med Bay",
                "West": "Central Hub",
            },
            "item": "Hazmat Suit"
        },
        "Observation Post": {
            "name": "Observation Post",
            "exits": {
                "North": "Central Hub",
                "West": "Generator Room",
                "East": "Control Room",
            },
            "item": "Ammo"
        },
        "Control Room": {
            "name": "Control Room",
            "exits": {
                "West": "Observation Post",
            },
            "item": None
        },
    }
    return rooms


def show_status(current_room_name, inventory, rooms):
    current_room = rooms[current_room_name]
    print(f"\nYou are in the {current_room['name']}")
    print(f"Inventory: {inventory}")

    room_item = current_room.get("item")
    if room_item is not None:
        if room_item in inventory:
            print(f"Empty racks and scattered debris remind you that the {room_item} is already yours.")
        else:
            print(f"The dim emergency lights flicker over a {room_item} within reach.")
    else:
        print("Dust hangs in the stale air. There are no items in this room.")

    exits = []
    for direction, dest in current_room["exits"].items():
        exits.append(f"{direction} to {dest}")
    if exits:
        print("From here you can go: " + ", ".join(exits))

    print("-" * 40)


def handle_go(argument, current_room_name, rooms, inventory):
    direction = argument.strip().title()
    if not direction:
        print("Your nerves fray as you hesitate. That isn't a valid direction (use North, South, East, or West).")
        return current_room_name

    current_room = rooms[current_room_name]
    exits = current_room["exits"]

    if direction in exits:
        next_room_name = exits[direction]
        next_room = rooms[next_room_name]

        # Require Key Card to enter Control Room from Observation Post
        if current_room_name == "Observation Post" and next_room_name == "Control Room":
            if "Key Card" not in inventory:
                print("The blast door to the Control Room stays locked. You swipe your empty hand over the panel.")
                print("Without the Key Card, the override rejects you with a harsh buzz.")
                return current_room_name

        print(f"You push {direction} to the {next_room['name']}.")
        return next_room_name
    else:
        print("Your path is blocked in that direction. Try another way before the dead find you.")
        return current_room_name


def handle_get(argument, current_room_name, rooms, inventory):
    requested_item = argument.strip()
    if not requested_item:
        print("Your hands grasp at empty air. Specify which item to get.")
        return

    current_room = rooms[current_room_name]
    room_item = current_room.get("item")

    if room_item is None:
        print("You search the shadows, but there is nothing here you can use.")
        return

    if requested_item.lower() == room_item.lower() and room_item not in inventory:
        inventory.append(room_item)
        print(f"You snatch up the {room_item}, feeling a little less helpless.")
        print(f"Inventory now: {inventory}")
        current_room["item"] = None
    else:
        print("You fumble around, but that item isn't here. The bunker seems to mock you.")


def check_game_over(current_room_name, inventory):
    if current_room_name != "Control Room":
        return False

    print("\nYou push into the Control Room. The stench of decay hits first.")
    print("The Alpha Zombie towers over the consoles, a knot of muscle, bone, and ruined armor.")

    has_hazmat = "Hazmat Suit" in inventory
    has_ammo = "Ammo" in inventory
    has_shotgun = "Shotgun" in inventory
    has_medkit = "Med Kit" in inventory
    has_fuse = "Generator Fuse" in inventory

    if not has_hazmat:
        print("\nThe air is thick with glowing spores and rancid vapor. Without your Hazmat Suit,")
        print("every breath is poison. Your skin blisters as the Alpha lurches toward you.")
        print("You choke, cough, and collapse in the contaminated Control Room. GAME OVER.")
        return True
    else:
        print("\nYour Hazmat Suit hisses as filters strain, sealing you off from the worst of the fallout.")

    if not has_shotgun and not has_ammo:
        print("\nYou rush in with nothing but your bare hands.")
        print("The Alpha doesn't hesitate. Claws and teeth tear through you before you can react.")
        print("The bunker falls silent. GAME OVER.")
        return True

    if not has_shotgun and has_ammo:
        print("\nLoose rounds rattle in your pocket, useless without a weapon to load.")
        print("The Alpha watches you fumble, then crosses the distance in one brutal charge.")
        print("The bunker claims you. GAME OVER.")
        return True

    if has_shotgun and not has_ammo:
        print("\nYou raise the shotgun, but the chamber clicks empty. No ammo. No second chances.")
        print("The Alpha surges forward, filling your world with claws and teeth.")
        print("You bleed out on the Control Room floor. GAME OVER.")
        return True

    print("\nYou slam shells into the shotgun, chamber a round, and unleash a deafening blast.")
    print("Chunks of rotting flesh and armor explode across the room as the Alpha roars and staggers.")
    print("The recoil slams through your shoulder as the Alpha crashes into you, claws raking across your armor.")

    if not has_medkit:
        print("\nPain blooms white-hot through your body where the Alpha tore into you.")
        print("Without a Med Kit, your injuries and trauma win.")
        print("You collapse beside the Alpha's corpse. You stopped the monster, but you die with it.")
        print("The bunker remains sealed, a tomb for you and the dead. GAME OVER.")
        return True
    else:
        print("\nBlood soaks through your gear where the Alpha's claws ripped into you.")
        print("You tear open the Med Kit, flooding your system with painkillers and antitoxins.")
        print("Your vision clears just enough to stay conscious as alarms blare around you.")

    if not has_fuse:
        print("\nThe console is a shattered mess, power flickering in and out.")
        print("Without the Generator Fuse, you cannot fully restore control to the bunker.")
        print("You have killed the Alpha and patched yourself up, but the doors stay locked.")
        print("You survive a little longer, but the bunker becomes your grave.")
        print("Bittersweet victory: the monster dies, but so do you. GAME OVER.")
        return True

    print("\nSparks dance across the ruined console. You rip open a panel and jam the Generator Fuse into place.")
    print("Systems reboot with a deep, shuddering hum. Locks cycle open throughout the bunker.")
    print("The Key Card in your hand unlocks the final security overrides.")
    print("You override the last door and climb toward the ruined city above. You escaped. You win!")
    print("Thanks for playing. The bunker will carry the scars of your escape.")
    return True


def main():
    rooms = build_world()
    current_room_name = "Central Hub"
    inventory = []

    show_instructions()

    while True:
        show_status(current_room_name, inventory, rooms)

        if check_game_over(current_room_name, inventory):
            break

        user_input = input(
            "Enter your move (e.g., 'go North', 'get Med Kit', or 'go North and get Shotgun'): "
        ).strip()

        if not user_input:
            print("Your voice echoes in the bunker. Use 'go <direction>' or 'get <item>'.")
            continue

        # Allow up to two commands separated by "and"
        raw_commands = [c.strip() for c in user_input.split("and") if c.strip()]

        for cmd_str in raw_commands:
            parts = cmd_str.split(" ", 1)
            command = parts[0].lower()
            argument = parts[1].strip() if len(parts) > 1 else ""

            if command == "go":
                current_room_name = handle_go(argument, current_room_name, rooms, inventory)
            elif command == "get":
                handle_get(argument, current_room_name, rooms, inventory)
            else:
                print("That command makes no sense in the dark. Use 'go <direction>' or 'get <item>'.")

            if check_game_over(current_room_name, inventory):
                return


if __name__ == "__main__":

    main()
