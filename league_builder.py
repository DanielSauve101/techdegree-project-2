import csv
import random


def player_info_list():
    # This function opens the soccer_players.csv file and seperates the player
    # information into three lists. Then orders the list by using zip and returns
    # the list of player_info.
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
    # This function is to sort the players into to lists. experienced_players
    # and beginner_players and return the list accordingly.
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
    # This function is used to generate random players from both beginner_players
    # and experienced_players lists. Which then seperates then into equal teams
    # as a dictionary using the team as the key and list of equal players as the value.
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
    with open("teams.txt", "w") as f:
        for key in team_dict.keys():
            f.write("Team {}".format(key) + "\n")
            for player_name, player_experience, player_guardian in team_dict[key]:
                f.write(player_name + ", " + player_experience +
                        ", " + player_guardian + "\n")
            f.write("\n")


def write_welcome_letter(team_dict):
    # This function is for writing a welcome text file for each player
    for key in team_dict.keys():
        for player_name, player_experience, player_guardian in team_dict[key]:
            players = player_name.lower().replace(" ", "_")
            with open(players + ".txt", "w") as f:
                f.write("Dear " + player_guardian + ",\n\n" + "We would like to welcome " +
                        player_name + " to the {} team\n".format(key) +
                        "The first practice is May 25th, 2019 at 2:00pm.")


def create_soccer_league():
    # This function creates the soccer league and creates all the files.
    player_info = player_info_list()
    beginner_players = sort_players_by_experience(player_info, "beginner")
    experienced_players = sort_players_by_experience(player_info, "experienced")
    teams = ["Sharks", "Dragons", "Raptors"]
    team_dict = create_teams(teams, experienced_players, beginner_players)
    write_team_info(team_dict)
    write_welcome_letter(team_dict)


if __name__ == "__main__":
    create_soccer_league()
