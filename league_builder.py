import csv


def player_info_list():
    player_name = []
    player_experience = []
    guardian = []

    with open('soccer_players.csv', newline='') as csvfile:
        team_reader = csv.DictReader(csvfile)
        rows = list(team_reader)
        for player in rows:
            player_name.append(player['Name'])
            player_experience.append(player['Soccer Experience'])
            guardian.append(player['Guardian Name(s)'])

    player_info_order = zip(player_name, player_experience, guardian)
    player_info = list(player_info_order)
    return player_info


def sort_players_by_experience(player_info, type_of_player):
    experienced_players = []
    beginner_players = []

    for player in player_info:
        for experience in player:
            if experience == "YES":
                experienced_players.append(player)
            elif experience == "NO":
                beginner_players.append(player)

    if type_of_player == "experienced":
        return experienced_players
    elif type_of_player == "beginner":
        return beginner_players


def create_team(team, experienced_players, beginner_players):
    exp_num_per_team = int(len(experienced_players) / 3)
    beg_num_per_team = int(len(beginner_players) / 3)

    if team == "team_one":
        team = experienced_players[:exp_num_per_team] + beginner_players[:beg_num_per_team]
        return team
    elif team == "team_two":
        team = experienced_players[exp_num_per_team:(
            exp_num_per_team*2)] + beginner_players[beg_num_per_team:(beg_num_per_team*2)]
        return team
    elif team == "team_three":
        team = experienced_players[-1:(exp_num_per_team*2-1):-1] + \
            beginner_players[-1:(beg_num_per_team*2-1):-1]
        return team


def write_team_info(team, title):
    with open("teams.txt", "a") as file:
        file.write("Team " + title + "\n")
        for player_name, player_experience, player_guardian in team:
            # write info to file
            file.write(player_name + ", " + player_experience + ", " + player_guardian + "\n")
        file.write("\n")

    for player_name, player_experience, player_guardian in team:
        players = player_name.lower().replace(" ", "_")
        with open(players + ".txt", "w") as file:
            file.write("Dear " + player_guardian + ",\n\n" + "We would like to welcome " +
                       player_name + " to the " + title + " team." +
                       "\nThe first practice is May 25th, 2019 at 2:00pm.")


def create_soccer_league():
    player_info = player_info_list()
    beginner_players = sort_players_by_experience(player_info, "beginner")
    experienced_players = sort_players_by_experience(player_info, "experienced")
    Sharks = create_team("team_one", experienced_players, beginner_players)
    Dragons = create_team("team_two", experienced_players, beginner_players)
    Raptors = create_team("team_three", experienced_players, beginner_players)
    with open("teams.txt", "w") as file:
        write_team_info(Sharks, "Sharks")
        write_team_info(Dragons, "Dragons")
        write_team_info(Raptors, "Raptors")


if __name__ == "__main__":
    create_soccer_league()
