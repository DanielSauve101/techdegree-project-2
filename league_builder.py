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
    experienced_player = []
    beginner_player = []

    for player in player_info:
        for experience in player:
            if experience == "YES":
                experienced_player.append(player)
            elif experience == "NO":
                beginner_player.append(player)

    if type_of_player == "experienced":
        return experienced_player
    elif type_of_player == "beginner":
        return beginner_player


def create_team(team, experienced_player, beginner_player):
    exp_num_per_team = int(len(experienced_player) / 3)
    beg_num_per_team = int(len(beginner_player) / 3)

    if team == "Sharks":
        team = experienced_player[:exp_num_per_team] + beginner_player[:beg_num_per_team]
        return team
    elif team == "Dragons":
        team = experienced_player[exp_num_per_team:(
            exp_num_per_team*2)] + beginner_player[beg_num_per_team:(beg_num_per_team*2)]
        return team
    elif team == "Raptors":
        team = experienced_player[-1:(exp_num_per_team*2-1):-1] + \
            beginner_player[-1:(beg_num_per_team*2-1):-1]
        return team


def write_team_info(team, title):
    with open("teams.txt", "a") as file:
        file.write("Team " + title + "\n")
        for player_name, player_experience, player_guardian in team:
            # write info to file
            file.write(player_name + ", " + player_experience + ", " + player_guardian + "\n")
        file.write("\n")


def create_soccer_league():
    player_info = player_info_list()
    beginner_player = sort_players_by_experience(player_info, "beginner")
    experienced_player = sort_players_by_experience(player_info, "experienced")
    Sharks = create_team("Sharks", experienced_player, beginner_player)
    Dragons = create_team("Dragons", experienced_player, beginner_player)
    Raptors = create_team("Raptors", experienced_player, beginner_player)
    with open("teams.txt", "w") as file:
        write_team_info(Sharks, "Sharks")
        write_team_info(Dragons, "Dragons")
        write_team_info(Raptors, "Raptors")


if __name__ == "__main__":
    create_soccer_league()
