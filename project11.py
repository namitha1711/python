class Kangaroo:
    def __init__(self, name, contents=None):
        self.name = name
        if contents is None:
            contents = []
        self.pouch_contents = list(contents)

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def __str__(self):
        lines = [f"{self.name} has pouch contents:"]
        for obj in self.pouch_contents:
            lines.append(f"  {obj}")
        return "\n".join(lines)

# Testing
kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print()
print(roo)
