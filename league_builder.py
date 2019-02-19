import csv
import random


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


def create_teams(teams, experienced_players, beginner_players):
    number_of_teams = len(teams)
    team_dict = {}

    for team in teams:
        list_of_random_players = random.sample(
            experienced_players, number_of_teams) + random.sample(beginner_players, number_of_teams)
        team_dict.update({team: list_of_random_players})
        for player in list_of_random_players:
            if player in experienced_players:
                experienced_players.remove(player)
            elif player in beginner_players:
                beginner_players.remove(player)
    return team_dict


def write_team_info(team_dict):
    # This function writes the teams.txt file with the three teams and a list of all the players
    for key in team_dict.keys():
        with open("teams.txt", "a") as file:
            file.write("Team {}".format(key) + "\n")
            for player_name, player_experience, player_guardian in team_dict[key]:
                file.write(player_name + ", " + player_experience + ", " + player_guardian + "\n")
            file.write("\n")


def write_welcome_letter(team_dict):
    # Below is the code for writing a welcome text file for each player
    for key in team_dict.keys():
        for player_name, player_experience, player_guardian in team_dict[key]:
            players = player_name.lower().replace(" ", "_")
            with open(players + ".txt", "w") as file:
                file.write("Dear " + player_guardian + ",\n\n" + "We would like to welcome " +
                           player_name + " to the {} team.\n".format(key) +
                           "The first practice is May 25th, 2019 at 2:00pm.")


def create_soccer_league():
    player_info = player_info_list()
    beginner_players = sort_players_by_experience(player_info, "beginner")
    experienced_players = sort_players_by_experience(player_info, "experienced")
    teams = ["Sharks", "Dragons", "Raptors"]
    team_dict = create_teams(teams, experienced_players, beginner_players)
    with open("teams.txt", "w") as file:
        write_team_info(team_dict)
    write_welcome_letter(team_dict)


if __name__ == "__main__":
    create_soccer_league()
