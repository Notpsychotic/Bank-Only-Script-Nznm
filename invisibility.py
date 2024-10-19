class InvisibilityCloak:
    def __init__(self):
        self.invisible_items = set()

    def make_invisible(self, item):
        self.invisible_items.add(item)

    def update_invisibility(self, new_items):
        self.invisible_items.update(new_items)

    def is_invisible(self, item):
        return item in self.invisible_items

    def get_visible_items(self, items):
        return [item for item in items if item not in self.invisible_items]

# Example usage
cloak = InvisibilityCloak()
cloak.make_invisible('item1')
cloak.update_invisibility(['item2', 'item3'])

items = ['item1', 'item2', 'item3', 'item4']
visible_items = cloak.get_visible_items(items)
print('Visible items:', visible_items)
