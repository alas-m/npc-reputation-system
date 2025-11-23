import random
import time

MAX_REPUTATION = 12
MIN_REPUTATION = -12
NEMESIS_THRESHOLD = -13
REPUTATION_GAIN = 4
REPUTATION_LOSS = -5

NPC_NAMES = ["Eldric the Mage", "Sarah the Smith", "Grom the Orc", "Lady Aria", "Ratbag the Thief"]

MISSION_POOL = [
    {"title": "Retrieve the Ancient artifact", "difficulty": 15},
    {"title": "Clear rats from basement", "difficulty": 5},
    {"title": "Escort the supply wagon", "difficulty": 10},
    {"title": "Decipher the rune scroll", "difficulty": 12},
    {"title": "Gather 10 healing herbs", "difficulty": 6},
    {"title": "Slay the Forest Troll", "difficulty": 18},
    {"title": "Deliver a love letter", "difficulty": 4},
    {"title": "Spy on the local guard", "difficulty": 14},
]

class Mission:
    def __init__(self, title, difficulty):
        self.title = title
        self.difficulty = difficulty
        self.status = "AVAILABLE"

class NPC:

    def __init__(self, name):
        self.name = name
        self.reputation = 0
        self.is_enemy = False
        self.missions = []
        
        assigned_missions = random.sample(MISSION_POOL, 5)
        for data in assigned_missions:
            new_mission = Mission(data['title'], data['difficulty'])
            self.missions.append(new_mission)

    def get_relationship_status(self):
        if self.is_enemy:
            return "NEMESIS"
        if self.reputation >= 10:
            return "Blood Brother"
        if self.reputation >= 5:
            return "Trusted Ally"
        if self.reputation > 0:
            return "Friendly"
        if self.reputation == 0:
            return "Neutral"
        if self.reputation > -5:
            return "Annoyed"
        if self.reputation > -12:
            return "Hostile"
        return "Hated"

    def update_reputation(self, amount):
        if self.is_enemy:
            print(f"   >> {self.name} refuses to deal with you.")
            return

        self.reputation += amount

        if self.reputation <= NEMESIS_THRESHOLD:
            self.reputation = NEMESIS_THRESHOLD
            self.is_enemy = True
            print(f"   >> {self.name} has declared you a mortal enemy. There is no turning back.")
            return

        if self.reputation > MAX_REPUTATION:
            self.reputation = MAX_REPUTATION
        elif self.reputation < MIN_REPUTATION:
            self.reputation = MIN_REPUTATION

        print(f"   >> Reputation is now {self.reputation} ({self.get_relationship_status()})")

    def attempt_mission(self, index):
        mission = self.missions[index]
        
        print(f"\n--- {mission.title} ---")
        print(f"Difficulty Check: {mission.difficulty}")
        input("Press Enter to roll the dice...")
        
        roll = random.randint(1, 20)
        print(f"   >> Rolled: {roll}")
        time.sleep(0.5)

        if roll >= mission.difficulty:
            print("   >> SUCCESS")
            mission.status = "COMPLETED"
            self.update_reputation(REPUTATION_GAIN)
        else:
            print("   >> FAILED")
            mission.status = "FAILED"
            self.update_reputation(REPUTATION_LOSS)

    def open_menu(self):
        while True:
            print(f"\n=== {self.name} ===")
            print(f"Relation: {self.reputation} [{self.get_relationship_status()}]")
            
            if self.is_enemy:
                print("This NPC is hunting you. You must flee.")
                input("Press Enter to run away...")
                return

            print("1. View Missions")
            print("2. Talk")
            print("3. Return to Map")
            
            user_choice = input("Select: ")

            if user_choice == '1':
                self.print_mission_list()
            elif user_choice == '2':
                self.talk()
            elif user_choice == '3':
                return
            else:
                print("Unknown command.")

    def print_mission_list(self):
        print(f"\n--- Mission Board: {self.name} ---")
        valid_options = []
        
        for index, mission in enumerate(self.missions):
            icon = "[ ]"
            if mission.status == "COMPLETED":
                icon = "[/]"
            elif mission.status == "FAILED":
                icon = "[X]"
            
            print(f"{index + 1}. {icon} {mission.title} (Diff: {mission.difficulty})")
            
            if mission.status == "AVAILABLE":
                valid_options.append(str(index + 1))

        if not valid_options:
            print("No active missions left.")
            input("Back...")
            return

        selection = input("\nSelect mission number (or 'q' to cancel): ")
        if selection in valid_options:
            self.attempt_mission(int(selection) - 1)
        elif selection.lower() == 'q':
            return
        else:
            print("Invalid selection.")

    def talk(self):

        list_positive = ["\"Everything I have is yours.\"", "\"Im so glad to see you!\"", "\"You can have whatever you want.\""]
        list_neutral = ["\"I dont know you. State your business.\"", "\"What would you like? But no discounts!\"", "\"Hey.\""]
        list_negative = ["\"You again? Hope to higher powers I dont make you meet the lord now.\"", "\"For you - twice the price on everything!\"", "\"What do you want, peasant?\"", "\"What again?\"", "\"I sure hope you dont ever come back after that.\""]
        list_else = ["\"Hm?\"", "\"Yes?\"", "\"What?\""]

        print(f"\n{self.name}: ", end="")
        if self.reputation >= 10:
            print(random.choice(list_positive))
        elif self.reputation > 0:
            print(random.choice(list_neutral))
        elif self.reputation < 0:
            print(random.choice(list_negative))
        else:
            print(random.choice(list_else))
        input("Press enter to continue >> ")

class GameWorld:
    def __init__(self):
        self.population = [NPC(name) for name in NPC_NAMES]

    def print_dashboard(self):
        print("\n" + "-"*40)
        print(f"{'Name':<20} | {'Rep':<5} | {'Status'}")
        print("-" * 40)
        for npc in self.population:
            print(f"{npc.name:<20} | {npc.reputation:<5} | {npc.get_relationship_status()}")
        print("-" * 40)
        input("Continue...")

    def start(self):
        while True:
            print("\n=== WORLD MAP ===")
            print("1. Visit NPC")
            print("2. Relationship Status")
            print("3. Quit")
            
            choice = input("Action: ")

            if choice == '1':
                self.travel_menu()
            elif choice == '2':
                self.print_dashboard()
            elif choice == '3':
                break

    def travel_menu(self):
        print("\n--- Travel Destinations ---")
        for i, npc in enumerate(self.population):
            print(f"{i + 1}. {npc.name}")
        
        choice = input("Enter number (or 'b' to back): ")
        if choice.lower() == 'b':
            return
        
        try:
            index = int(choice) - 1
            if 0 <= index < len(self.population):
                self.population[index].open_menu()
        except ValueError:
            pass

if __name__ == "__main__":
    app = GameWorld()
    app.start()