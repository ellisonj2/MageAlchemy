class Spell:
    def __init__(self, name, power, description, rarity):
        self._name = name
        self._power = power
        self._description = description
        self._rarity = rarity

    @property
    def name(self):
        return self._name

    @property
    def power(self):
        return self._power

    @property
    def description(self):
        return self._description

    @property
    def rarity(self):
        return self._rarity
