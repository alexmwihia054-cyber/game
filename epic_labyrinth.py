"""
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
        print(f"\n[ {self.name} | HP: {self.hp}/{self.max_hp} | Gold: {self.gold} | ATK: {self.attack_power} | DEF: {self.defense} ]")
        print(f"[ Inventory: {', '.join(self.inventory)} ]")

class Chamber_Zone_1:
    """Procedural Chamber Vector Matrix Interface 1"""
    def __init__(self):
        self.room_id = 1
        self.description = "You stand inside a grand echoing obsidian gallery with floating blue crystals."
        self.monster_name = "Corrupted Knight"
        self.monster_hp = 78
        self.monster_atk = 22
        self.has_monster = False
        self.loot_item = "Golden Elixir"
        self.has_loot = False
        self.gold_pool = 27

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 1: CHAMBER VECTOR 1")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 2)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 100)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 2
        elif choice == "2":
            player.current_room = 100
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_2:
    """Procedural Chamber Vector Matrix Interface 2"""
    def __init__(self):
        self.room_id = 2
        self.description = "You stand inside a grand echoing obsidian gallery with floating blue crystals."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 78
        self.monster_atk = 11
        self.has_monster = False
        self.loot_item = "Ruby Amulet"
        self.has_loot = True
        self.gold_pool = 39

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 2: CHAMBER VECTOR 2")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 3)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 1)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 3
        elif choice == "2":
            player.current_room = 1
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_3:
    """Procedural Chamber Vector Matrix Interface 3"""
    def __init__(self):
        self.room_id = 3
        self.description = "You stand inside an ancient laboratory scattered with smashed glass vials and brass gears."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 72
        self.monster_atk = 12
        self.has_monster = False
        self.loot_item = "Titanium Shield"
        self.has_loot = False
        self.gold_pool = 12

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 3: CHAMBER VECTOR 3")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 4)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 2)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 4
        elif choice == "2":
            player.current_room = 2
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_4:
    """Procedural Chamber Vector Matrix Interface 4"""
    def __init__(self):
        self.room_id = 4
        self.description = "You stand inside a flooded stone drain where water drops drip heavily from iron grates."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 76
        self.monster_atk = 9
        self.has_monster = False
        self.loot_item = "Steel Longsword"
        self.has_loot = True
        self.gold_pool = 37

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 4: CHAMBER VECTOR 4")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 5)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 3)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 5
        elif choice == "2":
            player.current_room = 3
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_5:
    """Procedural Chamber Vector Matrix Interface 5"""
    def __init__(self):
        self.room_id = 5
        self.description = "You stand inside an ancient laboratory scattered with smashed glass vials and brass gears."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 33
        self.monster_atk = 15
        self.has_monster = True
        self.loot_item = "Steel Longsword"
        self.has_loot = False
        self.gold_pool = 25

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 5: CHAMBER VECTOR 5")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 6)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 4)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 6
        elif choice == "2":
            player.current_room = 4
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_6:
    """Procedural Chamber Vector Matrix Interface 6"""
    def __init__(self):
        self.room_id = 6
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Void Horror"
        self.monster_hp = 65
        self.monster_atk = 18
        self.has_monster = False
        self.loot_item = "Titanium Shield"
        self.has_loot = True
        self.gold_pool = 18

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 6: CHAMBER VECTOR 6")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 7)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 5)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 7
        elif choice == "2":
            player.current_room = 5
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_7:
    """Procedural Chamber Vector Matrix Interface 7"""
    def __init__(self):
        self.room_id = 7
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 90
        self.monster_atk = 22
        self.has_monster = True
        self.loot_item = "Golden Elixir"
        self.has_loot = True
        self.gold_pool = 35

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 7: CHAMBER VECTOR 7")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 8)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 6)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 8
        elif choice == "2":
            player.current_room = 6
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_8:
    """Procedural Chamber Vector Matrix Interface 8"""
    def __init__(self):
        self.room_id = 8
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 46
        self.monster_atk = 14
        self.has_monster = False
        self.loot_item = "Ruby Amulet"
        self.has_loot = False
        self.gold_pool = 53

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 8: CHAMBER VECTOR 8")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 9)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 7)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 9
        elif choice == "2":
            player.current_room = 7
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_9:
    """Procedural Chamber Vector Matrix Interface 9"""
    def __init__(self):
        self.room_id = 9
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Corrupted Knight"
        self.monster_hp = 82
        self.monster_atk = 14
        self.has_monster = True
        self.loot_item = "Steel Longsword"
        self.has_loot = True
        self.gold_pool = 20

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 9: CHAMBER VECTOR 9")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 10)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 8)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 10
        elif choice == "2":
            player.current_room = 8
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_10:
    """Procedural Chamber Vector Matrix Interface 10"""
    def __init__(self):
        self.room_id = 10
        self.description = "You stand inside a flooded stone drain where water drops drip heavily from iron grates."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 41
        self.monster_atk = 24
        self.has_monster = False
        self.loot_item = "Titanium Shield"
        self.has_loot = False
        self.gold_pool = 37

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 10: CHAMBER VECTOR 10")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 11)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 9)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 11
        elif choice == "2":
            player.current_room = 9
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_11:
    """Procedural Chamber Vector Matrix Interface 11"""
    def __init__(self):
        self.room_id = 11
        self.description = "You stand inside a forgotten torture chamber lined with heavy rusted chains."
        self.monster_name = "Void Horror"
        self.monster_hp = 41
        self.monster_atk = 19
        self.has_monster = True
        self.loot_item = "Ruby Amulet"
        self.has_loot = False
        self.gold_pool = 60

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 11: CHAMBER VECTOR 11")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 12)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 10)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 12
        elif choice == "2":
            player.current_room = 10
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_12:
    """Procedural Chamber Vector Matrix Interface 12"""
    def __init__(self):
        self.room_id = 12
        self.description = "You stand inside a forgotten torture chamber lined with heavy rusted chains."
        self.monster_name = "Void Horror"
        self.monster_hp = 47
        self.monster_atk = 12
        self.has_monster = True
        self.loot_item = "Golden Elixir"
        self.has_loot = False
        self.gold_pool = 12

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 12: CHAMBER VECTOR 12")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 13)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 11)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 13
        elif choice == "2":
            player.current_room = 11
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_13:
    """Procedural Chamber Vector Matrix Interface 13"""
    def __init__(self):
        self.room_id = 13
        self.description = "You stand inside an ancient laboratory scattered with smashed glass vials and brass gears."
        self.monster_name = "Void Horror"
        self.monster_hp = 37
        self.monster_atk = 17
        self.has_monster = False
        self.loot_item = "Greater Health Potion"
        self.has_loot = False
        self.gold_pool = 18

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 13: CHAMBER VECTOR 13")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 14)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 12)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 14
        elif choice == "2":
            player.current_room = 12
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_14:
    """Procedural Chamber Vector Matrix Interface 14"""
    def __init__(self):
        self.room_id = 14
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 87
        self.monster_atk = 15
        self.has_monster = True
        self.loot_item = "Diamond Ring"
        self.has_loot = False
        self.gold_pool = 52

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 14: CHAMBER VECTOR 14")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 15)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 13)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 15
        elif choice == "2":
            player.current_room = 13
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_15:
    """Procedural Chamber Vector Matrix Interface 15"""
    def __init__(self):
        self.room_id = 15
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 62
        self.monster_atk = 24
        self.has_monster = True
        self.loot_item = "Ruby Amulet"
        self.has_loot = False
        self.gold_pool = 48

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 15: CHAMBER VECTOR 15")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 16)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 14)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 16
        elif choice == "2":
            player.current_room = 14
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_16:
    """Procedural Chamber Vector Matrix Interface 16"""
    def __init__(self):
        self.room_id = 16
        self.description = "You stand inside a forgotten torture chamber lined with heavy rusted chains."
        self.monster_name = "Void Horror"
        self.monster_hp = 41
        self.monster_atk = 22
        self.has_monster = True
        self.loot_item = "Titanium Shield"
        self.has_loot = False
        self.gold_pool = 31

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 16: CHAMBER VECTOR 16")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 17)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 15)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 17
        elif choice == "2":
            player.current_room = 15
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_17:
    """Procedural Chamber Vector Matrix Interface 17"""
    def __init__(self):
        self.room_id = 17
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 53
        self.monster_atk = 23
        self.has_monster = True
        self.loot_item = "Steel Longsword"
        self.has_loot = True
        self.gold_pool = 16

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 17: CHAMBER VECTOR 17")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 18)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 16)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 18
        elif choice == "2":
            player.current_room = 16
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_18:
    """Procedural Chamber Vector Matrix Interface 18"""
    def __init__(self):
        self.room_id = 18
        self.description = "You stand inside a forgotten torture chamber lined with heavy rusted chains."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 81
        self.monster_atk = 23
        self.has_monster = True
        self.loot_item = "Ruby Amulet"
        self.has_loot = False
        self.gold_pool = 44

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 18: CHAMBER VECTOR 18")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 19)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 17)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 19
        elif choice == "2":
            player.current_room = 17
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_19:
    """Procedural Chamber Vector Matrix Interface 19"""
    def __init__(self):
        self.room_id = 19
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 96
        self.monster_atk = 17
        self.has_monster = False
        self.loot_item = "Titanium Shield"
        self.has_loot = False
        self.gold_pool = 25

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 19: CHAMBER VECTOR 19")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 20)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 18)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 20
        elif choice == "2":
            player.current_room = 18
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_20:
    """Procedural Chamber Vector Matrix Interface 20"""
    def __init__(self):
        self.room_id = 20
        self.description = "You stand inside a forgotten torture chamber lined with heavy rusted chains."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 61
        self.monster_atk = 16
        self.has_monster = True
        self.loot_item = "Titanium Shield"
        self.has_loot = True
        self.gold_pool = 11

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 20: CHAMBER VECTOR 20")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 21)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 19)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 21
        elif choice == "2":
            player.current_room = 19
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_21:
    """Procedural Chamber Vector Matrix Interface 21"""
    def __init__(self):
        self.room_id = 21
        self.description = "You stand inside a forgotten torture chamber lined with heavy rusted chains."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 98
        self.monster_atk = 24
        self.has_monster = False
        self.loot_item = "Golden Elixir"
        self.has_loot = True
        self.gold_pool = 11

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 21: CHAMBER VECTOR 21")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 22)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 20)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 22
        elif choice == "2":
            player.current_room = 20
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_22:
    """Procedural Chamber Vector Matrix Interface 22"""
    def __init__(self):
        self.room_id = 22
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 56
        self.monster_atk = 24
        self.has_monster = True
        self.loot_item = "Ruby Amulet"
        self.has_loot = True
        self.gold_pool = 12

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 22: CHAMBER VECTOR 22")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 23)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 21)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 23
        elif choice == "2":
            player.current_room = 21
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_23:
    """Procedural Chamber Vector Matrix Interface 23"""
    def __init__(self):
        self.room_id = 23
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 55
        self.monster_atk = 20
        self.has_monster = False
        self.loot_item = "Ruby Amulet"
        self.has_loot = False
        self.gold_pool = 14

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 23: CHAMBER VECTOR 23")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 24)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 22)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 24
        elif choice == "2":
            player.current_room = 22
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_24:
    """Procedural Chamber Vector Matrix Interface 24"""
    def __init__(self):
        self.room_id = 24
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 53
        self.monster_atk = 18
        self.has_monster = True
        self.loot_item = "Golden Elixir"
        self.has_loot = True
        self.gold_pool = 54

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 24: CHAMBER VECTOR 24")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 25)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 23)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 25
        elif choice == "2":
            player.current_room = 23
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_25:
    """Procedural Chamber Vector Matrix Interface 25"""
    def __init__(self):
        self.room_id = 25
        self.description = "You stand inside a flooded stone drain where water drops drip heavily from iron grates."
        self.monster_name = "Void Horror"
        self.monster_hp = 91
        self.monster_atk = 24
        self.has_monster = False
        self.loot_item = "Diamond Ring"
        self.has_loot = False
        self.gold_pool = 15

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 25: CHAMBER VECTOR 25")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 26)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 24)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 26
        elif choice == "2":
            player.current_room = 24
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_26:
    """Procedural Chamber Vector Matrix Interface 26"""
    def __init__(self):
        self.room_id = 26
        self.description = "You stand inside a flooded stone drain where water drops drip heavily from iron grates."
        self.monster_name = "Corrupted Knight"
        self.monster_hp = 74
        self.monster_atk = 17
        self.has_monster = False
        self.loot_item = "Titanium Shield"
        self.has_loot = False
        self.gold_pool = 17

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 26: CHAMBER VECTOR 26")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 27)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 25)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 27
        elif choice == "2":
            player.current_room = 25
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_27:
    """Procedural Chamber Vector Matrix Interface 27"""
    def __init__(self):
        self.room_id = 27
        self.description = "You stand inside a grand echoing obsidian gallery with floating blue crystals."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 55
        self.monster_atk = 23
        self.has_monster = False
        self.loot_item = "Titanium Shield"
        self.has_loot = True
        self.gold_pool = 51

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 27: CHAMBER VECTOR 27")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 28)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 26)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 28
        elif choice == "2":
            player.current_room = 26
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_28:
    """Procedural Chamber Vector Matrix Interface 28"""
    def __init__(self):
        self.room_id = 28
        self.description = "You stand inside a grand echoing obsidian gallery with floating blue crystals."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 80
        self.monster_atk = 22
        self.has_monster = True
        self.loot_item = "Ruby Amulet"
        self.has_loot = False
        self.gold_pool = 14

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 28: CHAMBER VECTOR 28")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 29)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 27)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 29
        elif choice == "2":
            player.current_room = 27
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_29:
    """Procedural Chamber Vector Matrix Interface 29"""
    def __init__(self):
        self.room_id = 29
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Corrupted Knight"
        self.monster_hp = 50
        self.monster_atk = 19
        self.has_monster = True
        self.loot_item = "Diamond Ring"
        self.has_loot = False
        self.gold_pool = 18

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 29: CHAMBER VECTOR 29")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 30)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 28)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 30
        elif choice == "2":
            player.current_room = 28
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_30:
    """Procedural Chamber Vector Matrix Interface 30"""
    def __init__(self):
        self.room_id = 30
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 72
        self.monster_atk = 27
        self.has_monster = True
        self.loot_item = "Titanium Shield"
        self.has_loot = True
        self.gold_pool = 22

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 30: CHAMBER VECTOR 30")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 31)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 29)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 31
        elif choice == "2":
            player.current_room = 29
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_31:
    """Procedural Chamber Vector Matrix Interface 31"""
    def __init__(self):
        self.room_id = 31
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Void Horror"
        self.monster_hp = 103
        self.monster_atk = 17
        self.has_monster = True
        self.loot_item = "Greater Health Potion"
        self.has_loot = False
        self.gold_pool = 56

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 31: CHAMBER VECTOR 31")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 32)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 30)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 32
        elif choice == "2":
            player.current_room = 30
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_32:
    """Procedural Chamber Vector Matrix Interface 32"""
    def __init__(self):
        self.room_id = 32
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 84
        self.monster_atk = 14
        self.has_monster = False
        self.loot_item = "Golden Elixir"
        self.has_loot = True
        self.gold_pool = 13

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 32: CHAMBER VECTOR 32")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 33)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 31)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 33
        elif choice == "2":
            player.current_room = 31
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_33:
    """Procedural Chamber Vector Matrix Interface 33"""
    def __init__(self):
        self.room_id = 33
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 66
        self.monster_atk = 20
        self.has_monster = True
        self.loot_item = "Greater Health Potion"
        self.has_loot = True
        self.gold_pool = 34

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 33: CHAMBER VECTOR 33")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 34)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 32)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 34
        elif choice == "2":
            player.current_room = 32
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_34:
    """Procedural Chamber Vector Matrix Interface 34"""
    def __init__(self):
        self.room_id = 34
        self.description = "You stand inside an ancient laboratory scattered with smashed glass vials and brass gears."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 70
        self.monster_atk = 20
        self.has_monster = False
        self.loot_item = "Golden Elixir"
        self.has_loot = False
        self.gold_pool = 41

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 34: CHAMBER VECTOR 34")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 35)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 33)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 35
        elif choice == "2":
            player.current_room = 33
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_35:
    """Procedural Chamber Vector Matrix Interface 35"""
    def __init__(self):
        self.room_id = 35
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 58
        self.monster_atk = 26
        self.has_monster = False
        self.loot_item = "Greater Health Potion"
        self.has_loot = False
        self.gold_pool = 40

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 35: CHAMBER VECTOR 35")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 36)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 34)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 36
        elif choice == "2":
            player.current_room = 34
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_36:
    """Procedural Chamber Vector Matrix Interface 36"""
    def __init__(self):
        self.room_id = 36
        self.description = "You stand inside a grand echoing obsidian gallery with floating blue crystals."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 65
        self.monster_atk = 18
        self.has_monster = True
        self.loot_item = "Diamond Ring"
        self.has_loot = True
        self.gold_pool = 23

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 36: CHAMBER VECTOR 36")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 37)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 35)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 37
        elif choice == "2":
            player.current_room = 35
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_37:
    """Procedural Chamber Vector Matrix Interface 37"""
    def __init__(self):
        self.room_id = 37
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 92
        self.monster_atk = 24
        self.has_monster = True
        self.loot_item = "Greater Health Potion"
        self.has_loot = True
        self.gold_pool = 27

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 37: CHAMBER VECTOR 37")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 38)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 36)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 38
        elif choice == "2":
            player.current_room = 36
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_38:
    """Procedural Chamber Vector Matrix Interface 38"""
    def __init__(self):
        self.room_id = 38
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 90
        self.monster_atk = 22
        self.has_monster = False
        self.loot_item = "Titanium Shield"
        self.has_loot = True
        self.gold_pool = 60

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 38: CHAMBER VECTOR 38")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 39)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 37)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 39
        elif choice == "2":
            player.current_room = 37
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_39:
    """Procedural Chamber Vector Matrix Interface 39"""
    def __init__(self):
        self.room_id = 39
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Void Horror"
        self.monster_hp = 99
        self.monster_atk = 24
        self.has_monster = False
        self.loot_item = "Greater Health Potion"
        self.has_loot = True
        self.gold_pool = 38

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 39: CHAMBER VECTOR 39")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 40)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 38)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 40
        elif choice == "2":
            player.current_room = 38
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_40:
    """Procedural Chamber Vector Matrix Interface 40"""
    def __init__(self):
        self.room_id = 40
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Corrupted Knight"
        self.monster_hp = 52
        self.monster_atk = 29
        self.has_monster = True
        self.loot_item = "Ruby Amulet"
        self.has_loot = False
        self.gold_pool = 19

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 40: CHAMBER VECTOR 40")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 41)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 39)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 41
        elif choice == "2":
            player.current_room = 39
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_41:
    """Procedural Chamber Vector Matrix Interface 41"""
    def __init__(self):
        self.room_id = 41
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 98
        self.monster_atk = 18
        self.has_monster = False
        self.loot_item = "Golden Elixir"
        self.has_loot = True
        self.gold_pool = 22

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 41: CHAMBER VECTOR 41")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 42)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 40)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 42
        elif choice == "2":
            player.current_room = 40
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_42:
    """Procedural Chamber Vector Matrix Interface 42"""
    def __init__(self):
        self.room_id = 42
        self.description = "You stand inside a forgotten torture chamber lined with heavy rusted chains."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 93
        self.monster_atk = 27
        self.has_monster = False
        self.loot_item = "Steel Longsword"
        self.has_loot = False
        self.gold_pool = 46

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 42: CHAMBER VECTOR 42")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 43)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 41)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 43
        elif choice == "2":
            player.current_room = 41
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_43:
    """Procedural Chamber Vector Matrix Interface 43"""
    def __init__(self):
        self.room_id = 43
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 93
        self.monster_atk = 24
        self.has_monster = False
        self.loot_item = "Steel Longsword"
        self.has_loot = False
        self.gold_pool = 13

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 43: CHAMBER VECTOR 43")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 44)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 42)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 44
        elif choice == "2":
            player.current_room = 42
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_44:
    """Procedural Chamber Vector Matrix Interface 44"""
    def __init__(self):
        self.room_id = 44
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 56
        self.monster_atk = 28
        self.has_monster = True
        self.loot_item = "Ruby Amulet"
        self.has_loot = False
        self.gold_pool = 40

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 44: CHAMBER VECTOR 44")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 45)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 43)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 45
        elif choice == "2":
            player.current_room = 43
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_45:
    """Procedural Chamber Vector Matrix Interface 45"""
    def __init__(self):
        self.room_id = 45
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 67
        self.monster_atk = 17
        self.has_monster = False
        self.loot_item = "Ruby Amulet"
        self.has_loot = True
        self.gold_pool = 45

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 45: CHAMBER VECTOR 45")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 46)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 44)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 46
        elif choice == "2":
            player.current_room = 44
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_46:
    """Procedural Chamber Vector Matrix Interface 46"""
    def __init__(self):
        self.room_id = 46
        self.description = "You stand inside a grand echoing obsidian gallery with floating blue crystals."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 112
        self.monster_atk = 18
        self.has_monster = False
        self.loot_item = "Titanium Shield"
        self.has_loot = False
        self.gold_pool = 36

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 46: CHAMBER VECTOR 46")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 47)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 45)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 47
        elif choice == "2":
            player.current_room = 45
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_47:
    """Procedural Chamber Vector Matrix Interface 47"""
    def __init__(self):
        self.room_id = 47
        self.description = "You stand inside a flooded stone drain where water drops drip heavily from iron grates."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 66
        self.monster_atk = 30
        self.has_monster = True
        self.loot_item = "Diamond Ring"
        self.has_loot = True
        self.gold_pool = 17

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 47: CHAMBER VECTOR 47")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 48)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 46)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 48
        elif choice == "2":
            player.current_room = 46
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_48:
    """Procedural Chamber Vector Matrix Interface 48"""
    def __init__(self):
        self.room_id = 48
        self.description = "You stand inside a grand echoing obsidian gallery with floating blue crystals."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 61
        self.monster_atk = 26
        self.has_monster = False
        self.loot_item = "Steel Longsword"
        self.has_loot = False
        self.gold_pool = 43

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 48: CHAMBER VECTOR 48")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 49)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 47)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 49
        elif choice == "2":
            player.current_room = 47
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_49:
    """Procedural Chamber Vector Matrix Interface 49"""
    def __init__(self):
        self.room_id = 49
        self.description = "You stand inside a flooded stone drain where water drops drip heavily from iron grates."
        self.monster_name = "Void Horror"
        self.monster_hp = 108
        self.monster_atk = 27
        self.has_monster = False
        self.loot_item = "Greater Health Potion"
        self.has_loot = True
        self.gold_pool = 14

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 49: CHAMBER VECTOR 49")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 50)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 48)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 50
        elif choice == "2":
            player.current_room = 48
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_50:
    """Procedural Chamber Vector Matrix Interface 50"""
    def __init__(self):
        self.room_id = 50
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 88
        self.monster_atk = 22
        self.has_monster = False
        self.loot_item = "Diamond Ring"
        self.has_loot = False
        self.gold_pool = 36

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 50: CHAMBER VECTOR 50")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 51)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 49)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 51
        elif choice == "2":
            player.current_room = 49
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_51:
    """Procedural Chamber Vector Matrix Interface 51"""
    def __init__(self):
        self.room_id = 51
        self.description = "You stand inside an ancient laboratory scattered with smashed glass vials and brass gears."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 72
        self.monster_atk = 25
        self.has_monster = True
        self.loot_item = "Titanium Shield"
        self.has_loot = True
        self.gold_pool = 26

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 51: CHAMBER VECTOR 51")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 52)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 50)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 52
        elif choice == "2":
            player.current_room = 50
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_52:
    """Procedural Chamber Vector Matrix Interface 52"""
    def __init__(self):
        self.room_id = 52
        self.description = "You stand inside a flooded stone drain where water drops drip heavily from iron grates."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 70
        self.monster_atk = 21
        self.has_monster = True
        self.loot_item = "Golden Elixir"
        self.has_loot = True
        self.gold_pool = 28

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 52: CHAMBER VECTOR 52")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 53)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 51)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 53
        elif choice == "2":
            player.current_room = 51
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_53:
    """Procedural Chamber Vector Matrix Interface 53"""
    def __init__(self):
        self.room_id = 53
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 67
        self.monster_atk = 28
        self.has_monster = False
        self.loot_item = "Diamond Ring"
        self.has_loot = False
        self.gold_pool = 46

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 53: CHAMBER VECTOR 53")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 54)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 52)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 54
        elif choice == "2":
            player.current_room = 52
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_54:
    """Procedural Chamber Vector Matrix Interface 54"""
    def __init__(self):
        self.room_id = 54
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 98
        self.monster_atk = 19
        self.has_monster = False
        self.loot_item = "Diamond Ring"
        self.has_loot = False
        self.gold_pool = 38

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 54: CHAMBER VECTOR 54")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 55)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 53)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 55
        elif choice == "2":
            player.current_room = 53
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_55:
    """Procedural Chamber Vector Matrix Interface 55"""
    def __init__(self):
        self.room_id = 55
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 115
        self.monster_atk = 30
        self.has_monster = True
        self.loot_item = "Diamond Ring"
        self.has_loot = True
        self.gold_pool = 11

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 55: CHAMBER VECTOR 55")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 56)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 54)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 56
        elif choice == "2":
            player.current_room = 54
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_56:
    """Procedural Chamber Vector Matrix Interface 56"""
    def __init__(self):
        self.room_id = 56
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 74
        self.monster_atk = 26
        self.has_monster = False
        self.loot_item = "Ruby Amulet"
        self.has_loot = False
        self.gold_pool = 26

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 56: CHAMBER VECTOR 56")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 57)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 55)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 57
        elif choice == "2":
            player.current_room = 55
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_57:
    """Procedural Chamber Vector Matrix Interface 57"""
    def __init__(self):
        self.room_id = 57
        self.description = "You stand inside a forgotten torture chamber lined with heavy rusted chains."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 110
        self.monster_atk = 20
        self.has_monster = True
        self.loot_item = "Steel Longsword"
        self.has_loot = True
        self.gold_pool = 22

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 57: CHAMBER VECTOR 57")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 58)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 56)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 58
        elif choice == "2":
            player.current_room = 56
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_58:
    """Procedural Chamber Vector Matrix Interface 58"""
    def __init__(self):
        self.room_id = 58
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Corrupted Knight"
        self.monster_hp = 68
        self.monster_atk = 22
        self.has_monster = False
        self.loot_item = "Titanium Shield"
        self.has_loot = True
        self.gold_pool = 29

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 58: CHAMBER VECTOR 58")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 59)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 57)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 59
        elif choice == "2":
            player.current_room = 57
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_59:
    """Procedural Chamber Vector Matrix Interface 59"""
    def __init__(self):
        self.room_id = 59
        self.description = "You stand inside an ancient laboratory scattered with smashed glass vials and brass gears."
        self.monster_name = "Void Horror"
        self.monster_hp = 86
        self.monster_atk = 21
        self.has_monster = True
        self.loot_item = "Ruby Amulet"
        self.has_loot = True
        self.gold_pool = 13

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 59: CHAMBER VECTOR 59")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 60)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 58)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 60
        elif choice == "2":
            player.current_room = 58
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_60:
    """Procedural Chamber Vector Matrix Interface 60"""
    def __init__(self):
        self.room_id = 60
        self.description = "You stand inside a grand echoing obsidian gallery with floating blue crystals."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 85
        self.monster_atk = 24
        self.has_monster = True
        self.loot_item = "Titanium Shield"
        self.has_loot = True
        self.gold_pool = 15

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 60: CHAMBER VECTOR 60")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 61)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 59)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 61
        elif choice == "2":
            player.current_room = 59
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_61:
    """Procedural Chamber Vector Matrix Interface 61"""
    def __init__(self):
        self.room_id = 61
        self.description = "You stand inside an ancient laboratory scattered with smashed glass vials and brass gears."
        self.monster_name = "Corrupted Knight"
        self.monster_hp = 94
        self.monster_atk = 23
        self.has_monster = True
        self.loot_item = "Greater Health Potion"
        self.has_loot = False
        self.gold_pool = 23

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 61: CHAMBER VECTOR 61")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 62)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 60)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 62
        elif choice == "2":
            player.current_room = 60
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_62:
    """Procedural Chamber Vector Matrix Interface 62"""
    def __init__(self):
        self.room_id = 62
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 114
        self.monster_atk = 31
        self.has_monster = True
        self.loot_item = "Titanium Shield"
        self.has_loot = False
        self.gold_pool = 51

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 62: CHAMBER VECTOR 62")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 63)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 61)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 63
        elif choice == "2":
            player.current_room = 61
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_63:
    """Procedural Chamber Vector Matrix Interface 63"""
    def __init__(self):
        self.room_id = 63
        self.description = "You stand inside an ancient laboratory scattered with smashed glass vials and brass gears."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 101
        self.monster_atk = 21
        self.has_monster = False
        self.loot_item = "Golden Elixir"
        self.has_loot = False
        self.gold_pool = 37

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 63: CHAMBER VECTOR 63")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 64)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 62)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 64
        elif choice == "2":
            player.current_room = 62
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_64:
    """Procedural Chamber Vector Matrix Interface 64"""
    def __init__(self):
        self.room_id = 64
        self.description = "You stand inside an ancient laboratory scattered with smashed glass vials and brass gears."
        self.monster_name = "Corrupted Knight"
        self.monster_hp = 104
        self.monster_atk = 33
        self.has_monster = False
        self.loot_item = "Golden Elixir"
        self.has_loot = False
        self.gold_pool = 51

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 64: CHAMBER VECTOR 64")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 65)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 63)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 65
        elif choice == "2":
            player.current_room = 63
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_65:
    """Procedural Chamber Vector Matrix Interface 65"""
    def __init__(self):
        self.room_id = 65
        self.description = "You stand inside an ancient laboratory scattered with smashed glass vials and brass gears."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 86
        self.monster_atk = 24
        self.has_monster = True
        self.loot_item = "Greater Health Potion"
        self.has_loot = True
        self.gold_pool = 20

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 65: CHAMBER VECTOR 65")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 66)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 64)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 66
        elif choice == "2":
            player.current_room = 64
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_66:
    """Procedural Chamber Vector Matrix Interface 66"""
    def __init__(self):
        self.room_id = 66
        self.description = "You stand inside a grand echoing obsidian gallery with floating blue crystals."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 117
        self.monster_atk = 30
        self.has_monster = False
        self.loot_item = "Greater Health Potion"
        self.has_loot = True
        self.gold_pool = 51

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 66: CHAMBER VECTOR 66")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 67)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 65)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 67
        elif choice == "2":
            player.current_room = 65
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_67:
    """Procedural Chamber Vector Matrix Interface 67"""
    def __init__(self):
        self.room_id = 67
        self.description = "You stand inside an ancient laboratory scattered with smashed glass vials and brass gears."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 73
        self.monster_atk = 32
        self.has_monster = False
        self.loot_item = "Titanium Shield"
        self.has_loot = False
        self.gold_pool = 58

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 67: CHAMBER VECTOR 67")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 68)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 66)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 68
        elif choice == "2":
            player.current_room = 66
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_68:
    """Procedural Chamber Vector Matrix Interface 68"""
    def __init__(self):
        self.room_id = 68
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 93
        self.monster_atk = 23
        self.has_monster = False
        self.loot_item = "Titanium Shield"
        self.has_loot = True
        self.gold_pool = 27

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 68: CHAMBER VECTOR 68")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 69)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 67)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 69
        elif choice == "2":
            player.current_room = 67
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_69:
    """Procedural Chamber Vector Matrix Interface 69"""
    def __init__(self):
        self.room_id = 69
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 98
        self.monster_atk = 33
        self.has_monster = False
        self.loot_item = "Diamond Ring"
        self.has_loot = True
        self.gold_pool = 38

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 69: CHAMBER VECTOR 69")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 70)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 68)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 70
        elif choice == "2":
            player.current_room = 68
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_70:
    """Procedural Chamber Vector Matrix Interface 70"""
    def __init__(self):
        self.room_id = 70
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Corrupted Knight"
        self.monster_hp = 98
        self.monster_atk = 33
        self.has_monster = False
        self.loot_item = "Golden Elixir"
        self.has_loot = True
        self.gold_pool = 49

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 70: CHAMBER VECTOR 70")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 71)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 69)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 71
        elif choice == "2":
            player.current_room = 69
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_71:
    """Procedural Chamber Vector Matrix Interface 71"""
    def __init__(self):
        self.room_id = 71
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Corrupted Knight"
        self.monster_hp = 103
        self.monster_atk = 29
        self.has_monster = False
        self.loot_item = "Ruby Amulet"
        self.has_loot = True
        self.gold_pool = 14

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 71: CHAMBER VECTOR 71")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 72)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 70)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 72
        elif choice == "2":
            player.current_room = 70
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_72:
    """Procedural Chamber Vector Matrix Interface 72"""
    def __init__(self):
        self.room_id = 72
        self.description = "You stand inside a flooded stone drain where water drops drip heavily from iron grates."
        self.monster_name = "Corrupted Knight"
        self.monster_hp = 80
        self.monster_atk = 36
        self.has_monster = False
        self.loot_item = "Golden Elixir"
        self.has_loot = True
        self.gold_pool = 34

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 72: CHAMBER VECTOR 72")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 73)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 71)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 73
        elif choice == "2":
            player.current_room = 71
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_73:
    """Procedural Chamber Vector Matrix Interface 73"""
    def __init__(self):
        self.room_id = 73
        self.description = "You stand inside a forgotten torture chamber lined with heavy rusted chains."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 96
        self.monster_atk = 22
        self.has_monster = False
        self.loot_item = "Greater Health Potion"
        self.has_loot = True
        self.gold_pool = 49

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 73: CHAMBER VECTOR 73")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 74)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 72)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 74
        elif choice == "2":
            player.current_room = 72
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_74:
    """Procedural Chamber Vector Matrix Interface 74"""
    def __init__(self):
        self.room_id = 74
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 87
        self.monster_atk = 26
        self.has_monster = False
        self.loot_item = "Golden Elixir"
        self.has_loot = True
        self.gold_pool = 15

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 74: CHAMBER VECTOR 74")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 75)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 73)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 75
        elif choice == "2":
            player.current_room = 73
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_75:
    """Procedural Chamber Vector Matrix Interface 75"""
    def __init__(self):
        self.room_id = 75
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Void Horror"
        self.monster_hp = 101
        self.monster_atk = 36
        self.has_monster = True
        self.loot_item = "Ruby Amulet"
        self.has_loot = True
        self.gold_pool = 39

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 75: CHAMBER VECTOR 75")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 76)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 74)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 76
        elif choice == "2":
            player.current_room = 74
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_76:
    """Procedural Chamber Vector Matrix Interface 76"""
    def __init__(self):
        self.room_id = 76
        self.description = "You stand inside an ancient laboratory scattered with smashed glass vials and brass gears."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 86
        self.monster_atk = 26
        self.has_monster = True
        self.loot_item = "Diamond Ring"
        self.has_loot = False
        self.gold_pool = 27

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 76: CHAMBER VECTOR 76")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 77)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 75)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 77
        elif choice == "2":
            player.current_room = 75
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_77:
    """Procedural Chamber Vector Matrix Interface 77"""
    def __init__(self):
        self.room_id = 77
        self.description = "You stand inside a grand echoing obsidian gallery with floating blue crystals."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 68
        self.monster_atk = 34
        self.has_monster = True
        self.loot_item = "Ruby Amulet"
        self.has_loot = False
        self.gold_pool = 39

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 77: CHAMBER VECTOR 77")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 78)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 76)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 78
        elif choice == "2":
            player.current_room = 76
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_78:
    """Procedural Chamber Vector Matrix Interface 78"""
    def __init__(self):
        self.room_id = 78
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 129
        self.monster_atk = 30
        self.has_monster = False
        self.loot_item = "Steel Longsword"
        self.has_loot = False
        self.gold_pool = 47

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 78: CHAMBER VECTOR 78")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 79)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 77)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 79
        elif choice == "2":
            player.current_room = 77
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_79:
    """Procedural Chamber Vector Matrix Interface 79"""
    def __init__(self):
        self.room_id = 79
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 124
        self.monster_atk = 27
        self.has_monster = False
        self.loot_item = "Golden Elixir"
        self.has_loot = True
        self.gold_pool = 43

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 79: CHAMBER VECTOR 79")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 80)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 78)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 80
        elif choice == "2":
            player.current_room = 78
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_80:
    """Procedural Chamber Vector Matrix Interface 80"""
    def __init__(self):
        self.room_id = 80
        self.description = "You stand inside a flooded stone drain where water drops drip heavily from iron grates."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 115
        self.monster_atk = 37
        self.has_monster = True
        self.loot_item = "Golden Elixir"
        self.has_loot = False
        self.gold_pool = 39

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 80: CHAMBER VECTOR 80")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 81)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 79)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 81
        elif choice == "2":
            player.current_room = 79
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_81:
    """Procedural Chamber Vector Matrix Interface 81"""
    def __init__(self):
        self.room_id = 81
        self.description = "You stand inside a forgotten torture chamber lined with heavy rusted chains."
        self.monster_name = "Void Horror"
        self.monster_hp = 107
        self.monster_atk = 37
        self.has_monster = False
        self.loot_item = "Greater Health Potion"
        self.has_loot = True
        self.gold_pool = 31

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 81: CHAMBER VECTOR 81")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 82)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 80)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 82
        elif choice == "2":
            player.current_room = 80
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_82:
    """Procedural Chamber Vector Matrix Interface 82"""
    def __init__(self):
        self.room_id = 82
        self.description = "You stand inside a flooded stone drain where water drops drip heavily from iron grates."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 130
        self.monster_atk = 27
        self.has_monster = True
        self.loot_item = "Diamond Ring"
        self.has_loot = False
        self.gold_pool = 21

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 82: CHAMBER VECTOR 82")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 83)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 81)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 83
        elif choice == "2":
            player.current_room = 81
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_83:
    """Procedural Chamber Vector Matrix Interface 83"""
    def __init__(self):
        self.room_id = 83
        self.description = "You stand inside a flooded stone drain where water drops drip heavily from iron grates."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 123
        self.monster_atk = 31
        self.has_monster = False
        self.loot_item = "Steel Longsword"
        self.has_loot = True
        self.gold_pool = 20

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 83: CHAMBER VECTOR 83")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 84)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 82)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 84
        elif choice == "2":
            player.current_room = 82
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_84:
    """Procedural Chamber Vector Matrix Interface 84"""
    def __init__(self):
        self.room_id = 84
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 119
        self.monster_atk = 30
        self.has_monster = True
        self.loot_item = "Greater Health Potion"
        self.has_loot = False
        self.gold_pool = 22

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 84: CHAMBER VECTOR 84")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 85)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 83)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 85
        elif choice == "2":
            player.current_room = 83
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_85:
    """Procedural Chamber Vector Matrix Interface 85"""
    def __init__(self):
        self.room_id = 85
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 73
        self.monster_atk = 32
        self.has_monster = True
        self.loot_item = "Diamond Ring"
        self.has_loot = True
        self.gold_pool = 60

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 85: CHAMBER VECTOR 85")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 86)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 84)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 86
        elif choice == "2":
            player.current_room = 84
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_86:
    """Procedural Chamber Vector Matrix Interface 86"""
    def __init__(self):
        self.room_id = 86
        self.description = "You stand inside a grand echoing obsidian gallery with floating blue crystals."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 131
        self.monster_atk = 34
        self.has_monster = False
        self.loot_item = "Greater Health Potion"
        self.has_loot = False
        self.gold_pool = 27

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 86: CHAMBER VECTOR 86")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 87)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 85)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 87
        elif choice == "2":
            player.current_room = 85
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_87:
    """Procedural Chamber Vector Matrix Interface 87"""
    def __init__(self):
        self.room_id = 87
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 112
        self.monster_atk = 28
        self.has_monster = True
        self.loot_item = "Ruby Amulet"
        self.has_loot = False
        self.gold_pool = 25

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 87: CHAMBER VECTOR 87")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 88)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 86)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 88
        elif choice == "2":
            player.current_room = 86
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_88:
    """Procedural Chamber Vector Matrix Interface 88"""
    def __init__(self):
        self.room_id = 88
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Corrupted Knight"
        self.monster_hp = 82
        self.monster_atk = 37
        self.has_monster = False
        self.loot_item = "Steel Longsword"
        self.has_loot = False
        self.gold_pool = 50

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 88: CHAMBER VECTOR 88")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 89)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 87)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 89
        elif choice == "2":
            player.current_room = 87
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_89:
    """Procedural Chamber Vector Matrix Interface 89"""
    def __init__(self):
        self.room_id = 89
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 123
        self.monster_atk = 38
        self.has_monster = False
        self.loot_item = "Titanium Shield"
        self.has_loot = False
        self.gold_pool = 30

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 89: CHAMBER VECTOR 89")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 90)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 88)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 90
        elif choice == "2":
            player.current_room = 88
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_90:
    """Procedural Chamber Vector Matrix Interface 90"""
    def __init__(self):
        self.room_id = 90
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 124
        self.monster_atk = 34
        self.has_monster = True
        self.loot_item = "Diamond Ring"
        self.has_loot = False
        self.gold_pool = 42

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 90: CHAMBER VECTOR 90")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 91)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 89)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 91
        elif choice == "2":
            player.current_room = 89
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_91:
    """Procedural Chamber Vector Matrix Interface 91"""
    def __init__(self):
        self.room_id = 91
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 103
        self.monster_atk = 28
        self.has_monster = True
        self.loot_item = "Steel Longsword"
        self.has_loot = False
        self.gold_pool = 36

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 91: CHAMBER VECTOR 91")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 92)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 90)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 92
        elif choice == "2":
            player.current_room = 90
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_92:
    """Procedural Chamber Vector Matrix Interface 92"""
    def __init__(self):
        self.room_id = 92
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Shadow Lurker"
        self.monster_hp = 92
        self.monster_atk = 35
        self.has_monster = True
        self.loot_item = "Golden Elixir"
        self.has_loot = False
        self.gold_pool = 18

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 92: CHAMBER VECTOR 92")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 93)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 91)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 93
        elif choice == "2":
            player.current_room = 91
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_93:
    """Procedural Chamber Vector Matrix Interface 93"""
    def __init__(self):
        self.room_id = 93
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 128
        self.monster_atk = 35
        self.has_monster = True
        self.loot_item = "Ruby Amulet"
        self.has_loot = True
        self.gold_pool = 43

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 93: CHAMBER VECTOR 93")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 94)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 92)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 94
        elif choice == "2":
            player.current_room = 92
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_94:
    """Procedural Chamber Vector Matrix Interface 94"""
    def __init__(self):
        self.room_id = 94
        self.description = "You stand inside a grand echoing obsidian gallery with floating blue crystals."
        self.monster_name = "Void Horror"
        self.monster_hp = 124
        self.monster_atk = 40
        self.has_monster = True
        self.loot_item = "Diamond Ring"
        self.has_loot = False
        self.gold_pool = 39

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 94: CHAMBER VECTOR 94")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 95)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 93)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 95
        elif choice == "2":
            player.current_room = 93
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_95:
    """Procedural Chamber Vector Matrix Interface 95"""
    def __init__(self):
        self.room_id = 95
        self.description = "You stand inside a forgotten torture chamber lined with heavy rusted chains."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 122
        self.monster_atk = 41
        self.has_monster = False
        self.loot_item = "Greater Health Potion"
        self.has_loot = True
        self.gold_pool = 28

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 95: CHAMBER VECTOR 95")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 96)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 94)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 96
        elif choice == "2":
            player.current_room = 94
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_96:
    """Procedural Chamber Vector Matrix Interface 96"""
    def __init__(self):
        self.room_id = 96
        self.description = "You stand inside a pristine white marble sanctuary holding a single glowing altar."
        self.monster_name = "Obsidian Golem"
        self.monster_hp = 102
        self.monster_atk = 40
        self.has_monster = True
        self.loot_item = "Golden Elixir"
        self.has_loot = False
        self.gold_pool = 13

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 96: CHAMBER VECTOR 96")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 97)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 95)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 97
        elif choice == "2":
            player.current_room = 95
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_97:
    """Procedural Chamber Vector Matrix Interface 97"""
    def __init__(self):
        self.room_id = 97
        self.description = "You stand inside a forgotten torture chamber lined with heavy rusted chains."
        self.monster_name = "Clockwork Sentry"
        self.monster_hp = 109
        self.monster_atk = 39
        self.has_monster = False
        self.loot_item = "Ruby Amulet"
        self.has_loot = False
        self.gold_pool = 46

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 97: CHAMBER VECTOR 97")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 98)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 96)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 98
        elif choice == "2":
            player.current_room = 96
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_98:
    """Procedural Chamber Vector Matrix Interface 98"""
    def __init__(self):
        self.room_id = 98
        self.description = "You stand inside a damp, moss-covered crypt smelling of decayed wood."
        self.monster_name = "Corrupted Knight"
        self.monster_hp = 112
        self.monster_atk = 33
        self.has_monster = True
        self.loot_item = "Diamond Ring"
        self.has_loot = True
        self.gold_pool = 53

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 98: CHAMBER VECTOR 98")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 99)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 97)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 99
        elif choice == "2":
            player.current_room = 97
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_99:
    """Procedural Chamber Vector Matrix Interface 99"""
    def __init__(self):
        self.room_id = 99
        self.description = "You stand inside a forgotten torture chamber lined with heavy rusted chains."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 125
        self.monster_atk = 35
        self.has_monster = False
        self.loot_item = "Greater Health Potion"
        self.has_loot = True
        self.gold_pool = 59

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 99: CHAMBER VECTOR 99")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 100)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 98)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 100
        elif choice == "2":
            player.current_room = 98
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class Chamber_Zone_100:
    """Procedural Chamber Vector Matrix Interface 100"""
    def __init__(self):
        self.room_id = 100
        self.description = "You stand inside a narrow volcanic fissure filled with sulfuric smoke and heat."
        self.monster_name = "Grave Ghoul"
        self.monster_hp = 122
        self.monster_atk = 42
        self.has_monster = True
        self.loot_item = "Ruby Amulet"
        self.has_loot = True
        self.gold_pool = 60

    def entry_trigger(self, player):
        print("\n=======================================================")
        print(f" ENTERING AREA 100: CHAMBER VECTOR 100")
        print("=======================================================")
        print(self.description)
        time.sleep(0.2)
        
        if self.has_monster:
            print(f"⚠️ DANGER! A hostile [{self.monster_name}] leaps out from the darkness!")
            self.resolve_combat(player)
            if not player.is_alive():
                return

        if self.has_loot:
            print(f"🎁 LOOT FOUND: You discover a shimmering [{self.loot_item}] on the ground.")
            player.inventory.append(self.loot_item)
            self.has_loot = False

        if self.gold_pool > 0:
            print(f"💰 POUCH COLLECTED: You picked up {self.gold_pool} pieces of gold.")
            player.gold += self.gold_pool
            self.gold_pool = 0

        self.present_navigation_fork(player)

    def resolve_combat(self, player):
        while self.monster_hp > 0 and player.is_alive():
            print(f"\n--- Fight Node | {player.name} HP: {player.hp} | {self.monster_name} HP: {self.monster_hp} ---")
            print(" 1. Swing weapon with heavy physical force")
            print(" 2. Open quick bag to swallow a Heal Potion")
            action = input("Select strategic move: ").strip()
            
            if action == "1":
                dmg_to_m = max(5, player.attack_power - random.randint(0, 4))
                self.monster_hp -= dmg_to_m
                print(f"⚔️ You slashed the {self.monster_name} for {dmg_to_m} damage.")
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
                print(f"💥 The {self.monster_name} hits you back for {dmg_to_p} damage.")

        if player.is_alive():
            print(f"🎉 TRIUMPH! The {self.monster_name} falls dead into dust fractions.")
            self.has_monster = False
        else:
            print("\n💀 DEATH CRITICAL ERROR: Your consciousness faded out in this dark zone.")

    def present_navigation_fork(self, player):
        player.show_status()
        print("\nChoose your escape pathway route vector:")
        print(f" 1. Push forward through the heavy iron door ahead (Goes to Chamber 1)")
        print(f" 2. Retreat carefully back down the broken hallway (Goes to Chamber 99)")
        print(" 0. Teleport safely out of the simulation matrix (Exit Game)")
        
        choice = input("\nEnter navigation choice: ").strip()
        if choice == "1":
            player.current_room = 1
        elif choice == "2":
            player.current_room = 99
        elif choice == "0":
            print("Terminating simulation nodes...")
            sys.exit(0)
        else:
            print("Invalid coordinates route vector. Staying in this chamber.")

class LabyrinthSimulationEngine:
    def __init__(self):
        self.chambers = {}
        self.build_dungeon_matrix()

    def build_dungeon_matrix(self):
        print("Weaving 100 procedural chamber scripts together...")
        self.chambers[1] = Chamber_Zone_1()
        self.chambers[2] = Chamber_Zone_2()
        self.chambers[3] = Chamber_Zone_3()
        self.chambers[4] = Chamber_Zone_4()
        self.chambers[5] = Chamber_Zone_5()
        self.chambers[6] = Chamber_Zone_6()
        self.chambers[7] = Chamber_Zone_7()
        self.chambers[8] = Chamber_Zone_8()
        self.chambers[9] = Chamber_Zone_9()
        self.chambers[10] = Chamber_Zone_10()
        self.chambers[11] = Chamber_Zone_11()
        self.chambers[12] = Chamber_Zone_12()
        self.chambers[13] = Chamber_Zone_13()
        self.chambers[14] = Chamber_Zone_14()
        self.chambers[15] = Chamber_Zone_15()
        self.chambers[16] = Chamber_Zone_16()
        self.chambers[17] = Chamber_Zone_17()
        self.chambers[18] = Chamber_Zone_18()
        self.chambers[19] = Chamber_Zone_19()
        self.chambers[20] = Chamber_Zone_20()
        self.chambers[21] = Chamber_Zone_21()
        self.chambers[22] = Chamber_Zone_22()
        self.chambers[23] = Chamber_Zone_23()
        self.chambers[24] = Chamber_Zone_24()
        self.chambers[25] = Chamber_Zone_25()
        self.chambers[26] = Chamber_Zone_26()
        self.chambers[27] = Chamber_Zone_27()
        self.chambers[28] = Chamber_Zone_28()
        self.chambers[29] = Chamber_Zone_29()
        self.chambers[30] = Chamber_Zone_30()
        self.chambers[31] = Chamber_Zone_31()
        self.chambers[32] = Chamber_Zone_32()
        self.chambers[33] = Chamber_Zone_33()
        self.chambers[34] = Chamber_Zone_34()
        self.chambers[35] = Chamber_Zone_35()
        self.chambers[36] = Chamber_Zone_36()
        self.chambers[37] = Chamber_Zone_37()
        self.chambers[38] = Chamber_Zone_38()
        self.chambers[39] = Chamber_Zone_39()
        self.chambers[40] = Chamber_Zone_40()
        self.chambers[41] = Chamber_Zone_41()
        self.chambers[42] = Chamber_Zone_42()
        self.chambers[43] = Chamber_Zone_43()
        self.chambers[44] = Chamber_Zone_44()
        self.chambers[45] = Chamber_Zone_45()
        self.chambers[46] = Chamber_Zone_46()
        self.chambers[47] = Chamber_Zone_47()
        self.chambers[48] = Chamber_Zone_48()
        self.chambers[49] = Chamber_Zone_49()
        self.chambers[50] = Chamber_Zone_50()
        self.chambers[51] = Chamber_Zone_51()
        self.chambers[52] = Chamber_Zone_52()
        self.chambers[53] = Chamber_Zone_53()
        self.chambers[54] = Chamber_Zone_54()
        self.chambers[55] = Chamber_Zone_55()
        self.chambers[56] = Chamber_Zone_56()
        self.chambers[57] = Chamber_Zone_57()
        self.chambers[58] = Chamber_Zone_58()
        self.chambers[59] = Chamber_Zone_59()
        self.chambers[60] = Chamber_Zone_60()
        self.chambers[61] = Chamber_Zone_61()
        self.chambers[62] = Chamber_Zone_62()
        self.chambers[63] = Chamber_Zone_63()
        self.chambers[64] = Chamber_Zone_64()
        self.chambers[65] = Chamber_Zone_65()
        self.chambers[66] = Chamber_Zone_66()
        self.chambers[67] = Chamber_Zone_67()
        self.chambers[68] = Chamber_Zone_68()
        self.chambers[69] = Chamber_Zone_69()
        self.chambers[70] = Chamber_Zone_70()
        self.chambers[71] = Chamber_Zone_71()
        self.chambers[72] = Chamber_Zone_72()
        self.chambers[73] = Chamber_Zone_73()
        self.chambers[74] = Chamber_Zone_74()
        self.chambers[75] = Chamber_Zone_75()
        self.chambers[76] = Chamber_Zone_76()
        self.chambers[77] = Chamber_Zone_77()
        self.chambers[78] = Chamber_Zone_78()
        self.chambers[79] = Chamber_Zone_79()
        self.chambers[80] = Chamber_Zone_80()
        self.chambers[81] = Chamber_Zone_81()
        self.chambers[82] = Chamber_Zone_82()
        self.chambers[83] = Chamber_Zone_83()
        self.chambers[84] = Chamber_Zone_84()
        self.chambers[85] = Chamber_Zone_85()
        self.chambers[86] = Chamber_Zone_86()
        self.chambers[87] = Chamber_Zone_87()
        self.chambers[88] = Chamber_Zone_88()
        self.chambers[89] = Chamber_Zone_89()
        self.chambers[90] = Chamber_Zone_90()
        self.chambers[91] = Chamber_Zone_91()
        self.chambers[92] = Chamber_Zone_92()
        self.chambers[93] = Chamber_Zone_93()
        self.chambers[94] = Chamber_Zone_94()
        self.chambers[95] = Chamber_Zone_95()
        self.chambers[96] = Chamber_Zone_96()
        self.chambers[97] = Chamber_Zone_97()
        self.chambers[98] = Chamber_Zone_98()
        self.chambers[99] = Chamber_Zone_99()
        self.chambers[100] = Chamber_Zone_100()

    def run_engine_loop(self, player):
        print("\n=======================================================")
        print("   THE SIMULATION IS ONLINE: WELCOME TO THE INFINITE  ")
        print("=======================================================")
        
        while player.is_alive():
            current_node = self.chambers[player.current_room]
            current_node.entry_trigger(player)
            
        print("\n=======================================================")
        print(" GAME OVER: Press terminal up-arrow + enter to retry.  ")
        print("=======================================================")

if __name__ == "__main__":
    p_name = input("Identify your avatar name: ").strip()
    if not p_name:
        p_name = "Challenger_Zero"
        
    user_player = Player(p_name)
    engine = LabyrinthSimulationEngine()
    engine.run_engine_loop(user_player)
