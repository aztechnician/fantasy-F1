import csv


# The following function reads a .csv file containing the results for each driver in each driving session over a
# race weekend. It then returns the row from that document pertaining to the driver selected by the user. If the user's
# input does not match the driver code for one of the twenty drivers in the file, it provides a list of options as a
# string and ends the program.
def pull_values(driver):
    found_driver = 0

    with open('AbuDhabi.csv', 'r') as race_stats:
        csv_reader = csv.DictReader(race_stats)
        for line in csv_reader:
            if line['Driver Code'] == driver:
                stats = [line['Driver Name'], line['Driver Code'], line['FP2 Time'], line['Quali Time'],
                         line['Final Position'], line['# Pit Stops'], line['Fast Lap']]
                found_driver = 1
                return stats

    if found_driver == 0:
        print('That is not a recognized code for a driver in this Grand Prix.\n')
        print('The driver codes are as follows: \n'
              'Max Verstappen:      VER         Sergio Perez:        PER\n'
              'Lewis Hamilton:      HAM         George Russell:      RUS\n'
              'Charles Leclerc:     LEC         Carlos Sainz:        SAI\n'
              'Lando Norris:        NOR         Oscar Piastri:       PIA\n'
              'Fernando Alonso:     ALO         Lance Stroll:        STR\n'
              'Pierre Gasly:        GAS         Esteban Ocon:        OCO\n'
              'Alex Albon:          ALB         Logan Sargeant:      SAR\n'
              'Yuki Tsunoda:        TSU         Daniel Ricciardo:    RIC\n'
              'Valtteri Bottas:     BOT         Guanyu Zhou:         ZHO\n'
              'Kevin Magnussen:     MAG         Nico Hulkenberg:     HUL\n')
        exit()


# This second function calculates a number of different points-scoring categories for the user-selected driver based on
# the weekend results pulled from the .csv file in the function above.
def display_score(stats):
    # The following section assigns the elements of the chosen driver's line from the .csv file to their own variable.
    # The variable names are simplified versions of the column headers, full names above starting in line 15.
    name = stats[0]
    FP2_pos = int(stats[2])
    quali_pos = int(stats[3])
    race_pos = int(stats[4])
    PS_points = int(stats[5])
    FL_points = int(stats[6])

    # This section assigns variable names to round number values used later that may otherwise appear arbitrary.
    total_drivers = 20
    top_fifteen = 15
    top_ten = 10
    top_eight = 8
    pole_points = 0

    # This section is for calculating points earned in Free Practice 2, 0.5 points for 8th all the way up to 4 points
    # for 1st in 0.5 point increments.
    if FP2_pos <= top_eight:
        FP2_points = (top_eight - FP2_pos + 1) * 0.5
    else:
        FP2_points = 0

    # This section is for calculating points earned in Qualifying, and includes extra points for the driver in 1st.
    if quali_pos == 1:
        quali_points = 6
        pole_points = 2
    elif quali_pos <= top_ten:
        quali_points = 6
    elif quali_pos <= top_fifteen:
        quali_points = 3
    else:
        quali_points = 1

    # This section is for calculating points earned in the race, 20 points for 1st, decreasing by 1 each position.
    race_points = (total_drivers - race_pos + 1)

    # This section is for calculating points earned or lost for change in position during the race.
    if race_pos < quali_pos:
        diff_points = (quali_pos - race_pos)
        print(diff_points)
    elif race_pos > quali_pos:
        diff_points = (quali_pos - race_pos)
        print(diff_points)
    else:
        diff_points = 0
        print(diff_points)

    total_points = (FP2_points + quali_points + pole_points + race_points + FL_points + PS_points + diff_points)

    # The following is the primary desired output of the program and provides a point breakdown and point total for
    # the user-selected driver. There are two conditional strings that print if a driver has qualified first or claimed
    # the fastest lap of the race.

    print(f'This weekend {name} scored:')
    print(f'{FP2_points} point(s) for placing {FP2_pos} in Free Practice 2,')
    print(f'{float(quali_points)} point(s) for placing {quali_pos} in Qualifying,'
          f'{" plus an additional 2.0 points for being on pole," if quali_pos == 1 else ""}')
    print(f'{float(race_points)} point(s) for finishing {race_pos} in the Race,'
          f'{" plus an additional 2.0 points for having the fastest lap," if FL_points == 1 else ""}')
    print(f'{float(diff_points)} point(s) for overtakes during the Race,')
    print(f'and {float(PS_points)} bonus point(s) for pit stops during the race,')
    print(f'for a total of {total_points} point(s).')


# The main program first receives a user input to determine which driver it will be tallying points for. Then it runs
# the pull_values function to extract only that driver's results from the desired .csv file. Finally, it runs the
# display_score function to tally the points and print them for the user to view.
if __name__ == "__main__":
    chosen_driver = (str(input('Please enter the three letter code to select your driver. \n'))).upper()
    stats = pull_values(chosen_driver)
    points = display_score(stats)