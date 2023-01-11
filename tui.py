from pprint import pprint

import matplotlib.pyplot as plt


LINE_WIDTH = 85


def started(msg=""):
    output = f"Operation started: {msg}..."
    dashes = "-" * LINE_WIDTH
    # print("-------------------------------------------------------------------------------------")
    print(f"{dashes}\n {output}\n")


def completed():
    dashes = "-" * LINE_WIDTH
    print(f"\nOperation completed.\n{dashes}\n")


# print("-------------------------------------------------------------------------------------")

def error(msg):
    print(f"Error! {msg}\n")


def menu():
    print(f"""Please select on of the following options:
    {"[1]":<10} Top ranked song for a particular day
    {"[2]":<10} Artist with the most top ranked songs
    {"[3]":<10} 10 songs with the longest number of weeks on the board
    {"[4]":<10} song that has moved the most in ranking on the board
    {"[5]":<10} Exit the program
    """)
    selection = input("Your selection: ")
    return selection.strip().lower()

def top_song_from_a_day(data):
    rate = []
    song_title = []
    rate_song = {}
    dayreq = '2021-11-06'
    howManySongs = 0
    howManySongs2 = 0
    for row in data:
        howManySongs = howManySongs+1
        if row[0] == dayreq and int(row[1]) <= 10:

            howManySongs2 = howManySongs2+1

            song_title.append(row[2])
            rate.append(row[1])
            rate_song.update({row[1]: row[2]})


           # song.append(row[2])
    bar_plot = dict(rate_song)   #(df['Genre'].values).most_common(5))
    plt.bar(*zip(*bar_plot.items()))
    plt.show()
    print(rate_song)
    print(song_title, rate)

    print(howManySongs2)




   # print(date,song)
"""
    plt.plot(date, song, color='g', linestyle='dashed',
             marker='o', label="Weather Data")

    plt.xticks(rotation = 25)
    plt.xlabel('Dates')
    plt.ylabel('Temperature(°C)')
    plt.title('Weather Report', fontsize=20)
    plt.grid()
    plt.legend()
    plt.show()
"""


def display_medal_tally(tally):
    numberOfGoldMedals = tally.get("Gold")
    numberOfSilverMedals = tally.get("Silver")
    numberOfBronzeMedals = tally.get("Bronze")

    print(f"| Gold       |  {numberOfGoldMedals}  |")
    print(f"| Silver     |  {numberOfSilverMedals}  |")
    print(f"| Bronze     |  {numberOfBronzeMedals}  |")


def display_team_medal_tally(team_tally):
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")


"""        
    numberOfGoldMedals = team_tally.get("Gold")
    numberOfSilverMedals = team_tally.get("Silver")
    numberOfBronzeMedals = team_tally.get("Bronze")


    for i in team_tally:
        print(team_tally[i].get("Name"))
        print(f"\t\tGold:"+str(team_tally[i].get("Gold"))+", Silver:"+str(team_tally[i].get("Silver"))+", Bronze:"+str(team_tally[i].get("Bronze")))
"""


# years = {"2022", "2021","2023", "2020"}

def display_years(years):
    sorted_years = sorted(years, reverse=True)
    for row in sorted_years:
        print(row)


"""
started("ezt")
completed()
error("Hiba")
menu()
display_medal_tally(tally)
display_team_medal_tally(team_tally)
display_years(years)

"""
# menu()