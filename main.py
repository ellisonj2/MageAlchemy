from spell import Spell

def main():
    materials = ["fire", "water", "earth", "air", "light", "shadow", "crystal"]

    spell_combinations = {
        ("fire", "air"): Spell("Firestorm", 90, "A tornado made of flames.", "Epic"),
        ("water", "air"): Spell("Ice Blast", 70, "A freezing blast of icy wind.", "Rare"),
        ("earth", "fire"): Spell("Lava Burst", 85, "Hot lava shoots from the ground.", "Epic"),
        ("light", "shadow"): Spell("Eclipse Beam", 100, "A powerful beam of mixed light and darkness.", "Legendary"),
        ("crystal", "light"): Spell("Prism Shield", 60, "A glowing shield made of crystal light.", "Rare"),
        ("water", "earth"): Spell("Healing Moss", 45, "Soft magical moss heals small wounds.", "Common")
    }

    print("Welcome to Magic Alchemy!")
    print("Combine two materials to create a spell.")

    while True:
        print("\nAvailable materials:")
        for material in materials:
            print("-", material.title())

        first = input("\nChoose your first material: ").lower()
        second = input("Choose your second material: ").lower()

        if first not in materials or second not in materials:
            print("Invalid choice. Please choose materials from the list.")
            continue

        combo = (first, second)
        reverse_combo = (second, first)

        if combo in spell_combinations:
            spell = spell_combinations[combo]
        elif reverse_combo in spell_combinations:
            spell = spell_combinations[reverse_combo]
        else:
            spell = Spell("Unknown Spark", 10, "The materials fizzled but still made a tiny spark.", "Common")

        print("\nYou created a spell!")
        print("Name:", spell.name)
        print("Power:", spell.power)
        print("Rarity:", spell.rarity)
        print("Description:", spell.description)

        again = input("\nWould you like to craft another spell? yes/no: ").lower()

        if again != "yes":
            print("Thanks for playing Spell Crafter!")
            break

main()
