import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


# for name, info in data.items():
#     email = info["email"]
#     bio = info["bio"]
#     for race, race_info in race_info.items():
#         race_name = race_info["name"]
#         description = race_info["description"]
#
#     print(f"{name}'s email: {email}, bio: {bio}, description: {description}, race: {race_name}")

# file = open(file_path, "r")
# players = json.load(file)
# for player in players:
#     print(player)

def main() -> None:
    file_path = "./players.json"

    with open(file_path, "r") as file:
        data = json.load(file)
        print(data)

    for player, info in data.items():
        race_data = info["race"]
        race_instance = Race.objects.create(
            name=race_data["name"],
            description=race_data["description"]
        )

        guild_info=info["guild"]
        guild_instance = Guild.objects.get_or_create(
            name=guild_info["guild"]["name"],
            description=guild_info["guild"]["description"]
        )

        skills_info = info["skills"]

        player_instance = Player(
            nickname=player,
            email=info["email"],
            bio=info["bio"],
            guild=guild_instance,
            race=race_instance,
        )
        print(player_instance)

if __name__ == "__main__":
    main()
