class GuildAI:
    def __init__(self, guild_members):
        self.guild_members = guild_members

    def interact(self, person):
        if person in self.guild_members:
            return self.guild_interaction(person)
        else:
            return self.non_guild_interaction(person)

    def guild_interaction(self, person):
        return f'Hello {person}, welcome back to the guild!'

    def non_guild_interaction(self, person):
        return f'Hello {person}, you are not a guild member. How can I assist you?'

if __name__ == "__main__":
    guild_members = ["Alice", "Bob", "Charlie"]
    ai = GuildAI(guild_members)

    people = ["Alice", "Dave"]
    for person in people:
        print(ai.interact(person))
