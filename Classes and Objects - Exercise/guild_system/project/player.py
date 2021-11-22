class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills:
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        output = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"

        output += "\n".join(f"==={s_name} - {s_mana}" for s_name, s_mana in self.skills.items()).rstrip()

        return output + "\n"


if __name__ == "__main__":
    player = Player("George", 50, 100)
    print(player.add_skill("Shield Break", 20))
    print(player.player_info())
