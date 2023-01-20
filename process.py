import tui
from operator import itemgetter
import pandas as pd
from itertools import zip_longest

def top_song_details_for_a_day(data):
    dayreq = input("giv a date in YYYY-MM-DD format (like 2021-10-30)")
    song_details = []
    for row in data:
        if row[0] == dayreq and row[1] == '1':
            song_details = row  #.append(row[2], row[3], row[4], row[5] ,row[6])
    print("On the "+dayreq+" the top song was:")
    print("{:<15} {:<15} {:<20} {:<15} {:<8}".format('Song title', 'Artist', 'Last week result', 'peak rank', 'weeks on board'))
  #  for row in song_details:
    print("{:<15} {:<15} {:<20} {:<15} {:<8}".format(song_details[2], song_details[3], song_details[4], song_details[5], song_details[6] ))


def top10_songs_of_a_day(data):
    rate_song = {}
    dayreq = input("giv a date in YYYY-MM-DD format")
    #dayreq = '2021-10-30'
    for row in data:
        if row[0] == dayreq and int(row[1]) < 11:
            rate_song.update({row[1]: row[2]})
    print("{:<8} {:<15}".format('Rank', 'Song title'))
    for row in rate_song:
        print("{:<8} {:<15}".format(row, rate_song.get(row[0])))
    tui.completed()


def details_of_artists_mtrs(data):
    numer_one_songs = {}
    sum_top_songs= {}
    total = 1
    hit = 1
    for row in data:
        if row[1] == "1":

            if row[2] in numer_one_songs:
                total = total+1
                sum_top_songs.update({"Artist": row[3], "Song": row[2], "Total number 1 position": total})
         #   for row[2] in numer_one_songs.values():

          #      total = total+1
        numer_one_songs = {"Artist": row[3], "Song": row[2], "Total number 1 position": total}

    print(numer_one_songs)
    print(sum_top_songs)

def list_of_number1_songs(data):
    numer_one_songs = []
    for row in data:
        if row[1] == "1":
#        numer_one_songs = {"Artist": row[3], "Song": row[2], "Total number 1 position": total}
            numer_one_songs.append(row)
    for row in numer_one_songs:
        print(row)

def top10_weeksonboard(data):
    top10 = []
    topwob = 0
    result = []
    for row in data:

        if int(row[6]) > 1:
            top10.append(row)
            topwob = int(row[6])
  #  result = (sorted(top10, key=lambda x:x[6]))
    top10.sort(reverse = True)
    print(top10)
  #  print(top10)
  #  for row in top10:
   #     print("{:<15} {:<15} {:<20} {:<15} {:<8}".format('Song title', 'Artist', 'Last week result', 'peak rank', 'weeks on board'))
    #    print("{:<15} {:<15} {:<20} {:<15} {:<8}".format(row[2], row[3], row[4], row[5], row[6]))

def sortdata(data):
    sorted_list = {}
    ezt = []
    ezt.append(data.sort(key= lambda l:l[6]))
    print(data)
#    sorted_list.(ezt)
    print(sorted_list)




def top10_weeksonboard2(data):
    elsolista = []
    masdic = {"date": "06/11/2021",	"rank": "1", "song": "Easy on Me", "artist": "Adele", "last-week": "1", "peak-rank":"1", "weeks-on-board":"3"}



    elsodictionary = {}
    for i in range(330088):
        elsolista.append(i)
  #  print(elsolista)

    elsodictionary = dict(zip_longest(elsolista, data))
   # print(elsodictionary)

    print(masdic)
    masdic.update(elsodictionary)
    for row in masdic:
        print(row)
