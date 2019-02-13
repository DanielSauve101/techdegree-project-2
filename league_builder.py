import csv


def add_players():
    player_name = []
    player_height = []
    player_info = zip(player_name, player_height)

    with open('soccer_players.csv', newline='') as csvfile:
        team_reader = csv.DictReader(csvfile)
        rows = list(team_reader)
        for player in rows:
            player_name.append(player['Name'])
            player_height.append(player['Height (inches)'])

    with open("teams.txt", "w") as file:
        for player_name, player_height in player_info:
            # write info to file
            file.write(player_name + ", " + player_height + "\n")


if __name__ == "__main__":
    add_players()
