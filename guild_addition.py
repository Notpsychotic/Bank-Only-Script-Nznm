def add_guild_members(guild, new_members):
    guild.extend(new_members)
    return guild

if __name__ == "__main__":
    current_guild = ["Alice", "Bob", "Charlie"]
    new_members = ["Dave", "Eve"]
    updated_guild = add_guild_members(current_guild, new_members)
    print("Updated Guild Members:", updated_guild)