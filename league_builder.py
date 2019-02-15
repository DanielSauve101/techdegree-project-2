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


def sort_experienced_player(player_info):
    experienced_player = []
    for player in player_info:
        for experience in player:
            if experience == "YES":
                experienced_player.append(player)
    return experienced_player


def sort_beginner_player(player_info):
    beginner_player = []
    for player in player_info:
        for experience in player:
            if experience == "NO":
                beginner_player.append(player)
    return beginner_player


def num_of_experienced_player(experienced_player):
    exp_num_per_team = int(len(experienced_player) / 3)
    return exp_num_per_team


def num_of_beginner_player(beginner_player):
    beg_num_per_team = int(len(beginner_player) / 3)
    return beg_num_per_team


def team_Sharks(experienced_player, beginner_player, beg_num_per_team, exp_num_per_team):
    Sharks = experienced_player[:exp_num_per_team] + beginner_player[:beg_num_per_team]
    return Sharks


def team_Dragons(experienced_player, beginner_player, beg_num_per_team, exp_num_per_team):
    Dragons = experienced_player[exp_num_per_team:(
        exp_num_per_team*2)] + beginner_player[beg_num_per_team:(beg_num_per_team*2)]
    return Dragons


def team_Raptors(experienced_player, beginner_player, beg_num_per_team, exp_num_per_team):
    Raptors = experienced_player[-1:(exp_num_per_team*2-1):-1] + \
        beginner_player[-1:(beg_num_per_team*2-1):-1]
    return Raptors


def write_player_info(Sharks, Dragons, Raptors):

    with open("teams.txt", "w") as file:
        file.write("Team Sharks" + "\n")
        for player_name, player_height, player_experience in Sharks:
            # write info to file
            file.write(player_name + ", " + player_height + ", " + player_experience + "\n")

        file.write("\n" + "Team Dragons" + "\n")
        for player_name, player_height, player_experience in Dragons:
            # write info to file
            file.write(player_name + ", " + player_height + ", " + player_experience + "\n")

        file.write("\n" + "Team Raptors" + "\n")
        for player_name, player_height, player_experience in Raptors:
            # write info to file
            file.write(player_name + ", " + player_height + ", " + player_experience + "\n")


def create_soccer_league():
    player_info = player_info_list()
    beginner_player = sort_beginner_player(player_info)
    experienced_player = sort_experienced_player(player_info)
    beg_num_per_team = num_of_beginner_player(beginner_player)
    exp_num_per_team = num_of_experienced_player(experienced_player)
    Sharks = team_Sharks(experienced_player, beginner_player, beg_num_per_team, exp_num_per_team)
    Dragons = team_Dragons(experienced_player, beginner_player, beg_num_per_team, exp_num_per_team)
    Raptors = team_Raptors(experienced_player, beginner_player, beg_num_per_team, exp_num_per_team)
    write_player_info(Sharks, Dragons, Raptors)


if __name__ == "__main__":
    create_soccer_league()
