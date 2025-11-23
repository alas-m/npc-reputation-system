# RPG Reputation & Mission Engine 🎲

A Python-based simulation of an NPC relationship system commonly found in RPGs. This lightweight engine handles reputation tracking, randomized mission assignment, dice-roll mechanics (d20), and dynamic state changes (e.g., turning an NPC into a permanent Nemesis).

## 🚀 Features

* **Dynamic Reputation Scale:** Tracks relationships from **-12 (Hostile)** to **12 (Blood Brother)**.
* **The Nemesis System:** If reputation drops to **-13**, the NPC hits a "Point of No Return," permanently blocking interactions and marking the player as an enemy.
* **Randomized Mission Pools:** NPCs are automatically assigned 5 unique missions from a global pool with varying difficulty levels.
* **d20 Dice Mechanics:** Success isn't guaranteed. Players must roll a virtual d20 against a difficulty check (DC) to complete tasks.
* **Interactive Dashboard:** View the status of all NPCs and your current standing with them in a clean table format.
* **One-Try Constraints:** Missions can only be attempted once. Success boosts reputation; failure damages it.

## 🛠️ How it Works

The system is built on three main classes:

1.  **`Mission`**: Stores the title, difficulty rating, and completion status.
2.  **`NPC`**: Manages the reputation score, calculates the "Relationship Title" (e.g., Trusted Ally, Hated), and handles the interaction menu.
3.  **`GameWorld`**: The main controller that generates the population and handles the travel menu.

## 📦 How to Run

1.  Clone the repository:
    ```bash
    git clone https://github.com/alas-m/npc-reputation-system.git
    ```
2.  Navigate to the folder:
    ```bash
    cd npc-reputation-system
    ```
3.  Run the script:
    ```bash
    python main.py
    ```

## 🎮 Gameplay Example

```text
=== WORLD MAP ===
1. Visit NPC
2. Relationship Status
3. Quit
Action: 1

--- Travel Destinations ---
1. Eldric the Mage
2. Sarah the Smith
...
Select: 1

=== Eldric the Mage ===
Relation: 0 [Neutral]
1. View Missions
2. Talk
3. Return to Map
Select: 1

--- Mission Board: Eldric the Mage ---
1. [ ] Retrieve the Ancient artifact (Diff: 15)
...
Select mission number: 1

--- Retrieve the Ancient artifact ---
Difficulty Check: 15
Press Enter to roll d20...
>> Rolled: 18
>> SUCCESS
>> Reputation is now 4 (Friendly)

```

## 📷 Screenshots
<img width="695" height="411" alt="Screenshot 2025-11-23 212137" src="https://github.com/user-attachments/assets/c33b676d-298c-4142-9413-e5c7e18b6281" />
<img width="700" height="408" alt="Screenshot 2025-11-23 212051" src="https://github.com/user-attachments/assets/ccab5b36-1810-4627-8f1e-6c2059e6effc" />
<img width="667" height="277" alt="Screenshot 2025-11-23 212021" src="https://github.com/user-attachments/assets/ec795cf9-d038-4727-b802-d519bb8f3d76" />

