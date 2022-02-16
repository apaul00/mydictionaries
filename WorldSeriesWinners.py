#This file - WorldSeriesWinners.txt contains a chronological list of the World Series
#winning teams from 1903 through 2009. The first line in the file is the name of the team that won in 1903, and the 
#last line is the name of the team that won in 2009. (Note the World Series was not played in 1904 or 1994. There are
#entries in the file indicating this.) Write a program that reads this file and creates a dictionary in which the keys
#are the names of the teams, and each key’s associated value is the number of times the team has won the World Series.
#Create another dictionary in which the keys are the years, and each key’s associated value is the name of the team that
#won that year.The program should prompt the user for a year in the range of 1903 through 2009. It should then display 
#the name of the team that won the World Series that year, and the number of times that team has won the World Series.

infile = open("WorldSeriesWinners.txt", "r")

win_frequency = {}
teams_list = []
year_winner = {}

for line in infile:
    line = line.strip()
    line = line.split("  ")

    for team in line:
        team = team.strip(' ')
        if team in win_frequency:
            win_frequency[team] = win_frequency[team] + 1
            teams_list.append(team)
        else:
            win_frequency[team] = 1
            teams_list.append(team)

count = 1903
for team in teams_list:
    if count == 1904:
        count += 1
    if count == 1994:
        count += 1
    else:
        year_winner[count] = team
    count += 1


year = int(input(" Enter a year between 1903-2008: "))
if year == 1904 or year == 1994:
    print('No World Series was played in', year)


else:
    team_name = year_winner[year]
    print(year_winner[year], ':', win_frequency[team_name])

