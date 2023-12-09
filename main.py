import csv

def pull_values(driver):
    with open('AbuDhabi.csv', 'r') as race_stats:
        csv_reader = csv.DictReader(race_stats)

        for line in csv_reader:
            if line['Driver Code'] == driver:
                stats = [line['Driver Name'], line['Driver Code'], line['FP2 Time'], line['Quali Time'],
                         line['Final Position'], line['# Pit Stops'], line['Fast Lap']]
                print(line)    # line for verifying process
                return stats

def calculate_score(stats):
    name = stats[0]
    FP2_pos = int(stats[2])
    quali_pos = int(stats[3])
    race_pos = int(stats[4])
    PS_points = int(stats[5])
    FL_points = int(stats[6])
    pole_points = 0
    print(f'{FL_points} for Fastest Lap')    # line for verifying process

# this section in for calculating points earned in Free Practice 2
    if FP2_pos <= 8:
        FP2_points = (8 - FP2_pos + 1) * 0.5
        print(f'{FP2_points} for FP2')    # line for verifying process
    else:
        FP2_points = 0
        print(f'{FP2_points} for FP2')    # line for verifying process

# this section is for calculating points earned in Qualifying
    if quali_pos == 1:
        quali_points = 6
        pole_points = 2
    elif quali_pos <= 10:
        quali_points = 6
    elif quali_pos <= 15:
        quali_points = 3
    else:
        quali_points = 1
    print(f'{quali_points + pole_points} for Qualifying')    # line for verifying process

# this section is for calculating points earned in the Race
    race_points = (20 - race_pos + 1)
    print(f'{race_points + FL_points} for the Race')

# this section is for calculating points earned or lost for change in position during the Race
    if race_pos < quali_pos:
        diff_points = (quali_pos - race_pos)
    elif quali_pos > race_pos:
        diff_points = (race_pos - quali_pos)
    else:
        diff_points = 0
    print(f'{diff_points} for overtakes')    # line for verifying process

    total_points = (FP2_points + quali_points + pole_points + race_points + FL_points + diff_points)

    print(f'This weekend {name} scored:')
    print(f'{FP2_points} point(s) for placing {FP2_pos} in Free Practice 2,')
    print(f'{quali_points} point(s) for placing {quali_pos} in Qualifying,'
          f'{" and an additional 2 points for being on pole" if quali_pos == 1 else ""}')
    print(f'{quali_points} point(s) for placing {quali_pos} in Qualifying,')
    print(f'{race_points} point(s) for finishing {race_pos} in the Race,')
    print(f'{diff_points} point(s) for overtakes during the Race,')
    print(f'and {PS_points} bonus point(s) for pit stops during the race,')
    print(f'for a total of {total_points} point(s).')


if __name__ == "__main__":
    stats = pull_values(str(input('Which driver have you selected?')))
    print(stats)    # line for verifying process

    points = calculate_score(stats)

