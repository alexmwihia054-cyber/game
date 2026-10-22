import os
import random

def generate_giant_rpg():
    filename = "epic_labyrinth.py"
    
    # 1. Header and Engine Foundation Setup
    header = '''"""
================================================================================
          THE CHRONICLES OF THE INFINITE ARCHITECTURE: LABYRINTH
================================================================================
A massive, programmatically expanded text-adventure and spatial RPG.
File Tracking Dimension: 3,000+ Lines of Valid, Playable Python.
================================================================================
"""
import sys
import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 150
        self.max_hp = 150
        self.gold = 50
        self.attack_power = 15
        self.defense = 5
        self.inventory = ["Heal Potion", "Rusty Key"]
        self.current_room = 1

    def is_alive(self):
        return self.hp > 0

    def show_status(self):
        print(f"\\n[ {self.name} | HP: {self.hp}/{self.max_hp} | Gold: {self.gold} | ATK: {self.attack_power} | DEF: {self.defense} ]")
        print(f"[ Inventory: {', '.join(self.inventory)} ]")
'''

    # Dictionary setups for procedural generation variations
    room_atmospheres = [
        "a damp, moss-covered crypt smelling of decayed wood",
        "a grand echoing obsidian gallery with floating blue crystals",
        "a narrow volcanic fissure filled with sulfuric smoke and heat",
        "an ancient laboratory scattered with smashed glass vials and brass gears",
        "a flooded stone drain where water drops drip heavily from iron grates",
        "a forgotten torture chamber lined with heavy rusted chains",
        "a pristine white marble sanctuary holding a single glowing altar"
    ]
    
    monster_types = ["Grave Ghoul", "Shadow Lurker", "Clockwork Sentry", "Obsidian Golem", "Void Horror", "Corrupted Knight"]
    loot_items = ["Golden Elixir", "Steel Longsword", "Titanium Shield", "Diamond Ring", "Greater Health Potion", "Ruby Amulet"]

    # 2. Programmatically building 100 sprawling chamber classes
    middle_blocks = []
    for i in range(1, 101):
        # Choose random environmental layouts
        desc = random.choice(room_atmospheres)
        monster = random.choice(monster_types)
        monster_hp = random.randint(30, 90) + (i // 2)
        monster_atk = random.randint(8, 22) + (i // 5)
        loot = random.choice(loot_items)
        gold_reward = random.randint(10, 60)
        
        # Determine exit directions logically linked to adjacent indexes
        next_room = i + 1 if i < 100 else 1
        prev_room = i - 1 if i > 1 else 100

        class_template = f'''
class Chamber_Zone_{i}:
    """Procedural Chamber Vector Matrix Interface {i}"""
    def __init__(self):
        self.room_id = {i}
        self.description = "You stand inside {desc}."
        self.monster_name = "{monster}"
        self.monster_hp = {monster_hp}
        self.monster_atk = {monster_atk}
        self.has_monster = {random.choice([True, False])}
        self.loot_item = "{loot}"
        self.has_loot = {random.choice([True, False])}
        self.gold_pool = {gold_reward}

    def entry_trigger(self, player):
        print("\\n=======================================================")
        print(f" ENTERING AREA {i}: CHAMBER VECTOR {i}")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{{self.monster_name}}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{{self.loot_item}}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {{self.gold_pool}} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\\n--- Fight Node | {{player.name}} HP: {{player.hp}} | {{self.monster_name}} HP: {{self.monster_hp}} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {{self.monster_name}} for {{dmg_to_m}} damage.")
            elif action == "2":
                if "Heal Potion" in player.inventory:
                    player.inventory.remove("Heal Potion")
                    player.hp = min(player.max_hp, player.hp + 50)
                    print("❤️ Swallowed potion! Restored 50 HP.")
                else:
                    print("❌ Matrix Error: No Heal Potions left in your inventory bags.")
                    continue
            else:
                print("Invalid input vector. You miss your turn.")

            if self.monster_hp > 0:
                dmg_to_p = max(1, self.monster_atk - player.defense + random.randint(-2, 2))
                player.hp -= dmg_to_p
                print(f"💥 The {{self.monster_name}} hits you back for {{dmg_to_p}} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {{self.monster_name}} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber {next_room})")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber {prev_room})")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = {next_room}
        elif choice == "2":
            player.current_room = {prev_room}
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")
'''
        middle_blocks.append(class_template)

    # 3. Game Loop Orchestration Layer
    footer = '''
class LabyrinthSimulationEngine:
    def __init__(self):
        self.chambers = {}
        self.build_dungeon_matrix()

    def build_dungeon_matrix(self):
        print("Weaving 100 procedural chamber scripts together...")
'''
    # Dynamically map the instantiation statements inside the layout constructor
    for i in range(1, 101):
        footer += f"        self.chambers[{i}] = Chamber_Zone_{i}()\n"

    footer += '''
    def run_engine_loop(self, player):
        print("\\n=======================================================")
        print("   THE SIMULATION IS ONLINE: WELCOME TO THE INFINITE  ")
        print("=======================================================")
        
        while player.is_alive():
            current_node = self.chambers[player.current_room]
            current_node.entry_trigger(player)
            
        print("\\n=======================================================")
        print(" GAME OVER: Press terminal up-arrow + enter to retry.  ")
        print("=======================================================")

if __name__ == "__main__":
    p_name = input("Identify your avatar name: ").strip()
    if not p_name:
        p_name = "Challenger_Zero"
        
    user_player = Player(p_name)
    engine = LabyrinthSimulationEngine()
    engine.run_engine_loop(user_player)
'''

    # Combine string pieces and dump to disk file configuration matrix
    full_code = header + "".join(middle_blocks) + footer
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_code)
    
    # Calculate file lengths lines count
    with open(filename, "r", encoding="utf-8") as f:
        line_count = len(f.readlines())
        
    print(f"Success! Built '{filename}' containing exactly {line_count} lines of deep textual layout gameplay.")

if __name__ == "__main__":
    generate_giant_rpg()
