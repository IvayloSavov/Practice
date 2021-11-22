from project.player import Player


class Guild:
    players: [Player]

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        player = [p for p in self.players if p.name == player_name]

        if player:
            p_index = self.players.index(player[0])
            player = self.players.pop(p_index)
            player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        output = f"Guild: {self.name}\n"
        output += "\n".join(p.player_info() for p in self.players)

        return output


if __name__ == "__main__":
    player = Player("George", 50, 100)
    print(player.add_skill("Shield Break", 20))
    print(player.player_info())
    guild = Guild("UGT")
    print(guild.assign_player(player))
    print(guild.guild_info())
