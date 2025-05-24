def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    print(f"Total number of items: {item_total}")

def add_to_inventory(inventory, items):
    for item in items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(stuff)
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    stuff = add_to_inventory(stuff, dragon_loot)
    display_inventory(stuff)

if _name_ == "_main_":
    main()
