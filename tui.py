from pprint import pprint
import pandas as pd
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
    {"[2]":<10} Details of the Artists with the most top ranked songs
    {"[3]":<10} Details of the 10 songs with the longest number of weeks on the board
    {"[4]":<10} song that has moved the most in ranking on the board
    {"[5]":<10} Visualise the top songs
    {"[6]":<10} Top 10 on a given day
    {"[7]":<10} Test
    
    {"[9]":<10} Exit the program
    """)
    selection = input("Your selection: ")
    return selection.strip().lower()

"""
def top_song_details_for_a_day(data,dayreq):
    song_details = []
    for row in data:
        if row[0] == dayreq and row[1] == '1':
            song_details = row  #.append(row[2], row[3], row[4], row[5] ,row[6])
    print("On the "+dayreq+" the top song was:")
    print("{:<15} {:<15} {:<20} {:<15} {:<8}".format('Song title', 'Artist', 'Last week result', 'peak rank', 'weeks on board'))
  #  for row in song_details:
    print("{:<15} {:<15} {:<20} {:<15} {:<8}".format(song_details[2], song_details[3], song_details[4], song_details[5], song_details[6] ))




def top10_songs_of_a_day(data, dayreq):
    rate_song = {}
 #   dayreq = '2021-10-30'
    for row in data:
        if row[0] == dayreq and int(row[1]) < 11:
            rate_song.update({row[1]: row[2]})
    print("{:<8} {:<15}".format('Rank', 'Song title'))
    for row in rate_song:
        print("{:<8} {:<15}".format(row, rate_song.get(row[0])))
    completed()

def details_of_artist_mtr_song(data):
    top_songs = []


    for row in data:
        if row[1] == "1":
            top_songs.append(row)

           




def artist_most_top_ranked_song(data):
    artist_song_sum_top_rank = 0

#    artist_song_sum_top_rank2 = {"Rank": {"Artist": "Adele", "Song": "EASY", "totalrank": 1},
#                                 "Rank1": {"Artist": "Bdele", "BSong": "BEASY", "Btotalrank": 1}}
#    print(artist_song_sum_top_rank2)
#    print(artist_song_sum_top_rank2.keys())
#    print(artist_song_sum_top_rank2.values())
#    print(artist_song_sum_top_rank2.get(1))
#    print(artist_song_sum_top_rank2.get(2))
#    print(artist_song_sum_top_rank2["Rank"]["Artist"])

    number_of_1_place_artists = 0
    arttot1 = 1
    startrank = 1
    sor = 1
    for row in data:
        sor = sor+1

        if row[1] == "1":
            number_of_1_place_artists = number_of_1_place_artists+1
            artist_song_sum_top_rank={"Rank": {"Artist": row[3], "Song": row[2], "totalrank": startrank}}
        if row[3] == artist_song_sum_top_rank[row[sor][artist_most_top_ranked_song("Artist")]]:
            print(artist_song_sum_top_rank.values())
            song = artist_most_top_ranked_song("Song")
            if row[2] == artist_song_sum_top_rank['Rank'][song]:
                arttot1 == arttot1+1
                artist_song_sum_top_rank.update(
                    {number_of_1_place_artists: number_of_1_place_artists,"Artist": row[3], "Song": row[2],
                    "totalrank": arttot1})
            else:
                artist_song_sum_top_rank.update(
                    {number_of_1_place_artists: number_of_1_place_artists, "Artist": row[3], "Song": row[2],
                     "totalrank": startrank})
        else:
            artist_song_sum_top_rank.update({number_of_1_place_artists: number_of_1_place_artists, "Artist": row[3], "Song": row[2], "totalrank": startrank})
        artist_song_sum_top_rank ={number_of_1_place_artists: {"Artist": row[3], "Song": row[2], "totalrank": arttot1}}
    print("{:<8} {:<15} {:<15} {:<15} ".format('Rank', 'Artist', 'Song title', 'Total top 1'))
    print(artist_song_sum_top_rank)
#        for row in artist_song_sum_top_rank:
 #         print("{:<8} {:<15} {:<15} {:<15}".format(row, artist_song_sum_top_rank.values(row[3]), artist_song_sum_top_rank.values(row[2]), number_of_1_place_artists))

"""




"""
           # song.append(row[2])
    bar_plot = dict(rate_song)   #(df['Genre'].values).most_common(5))
    plt.bar(*zip(*bar_plot.items()))
  #  bar_plot.plot
    plt.show()
    print(rate_song)
    print(song_title, rate)

    print(howManySongs2)

*/
"""

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