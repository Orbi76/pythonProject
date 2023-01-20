import csv
import matplotlib
import matplotlib.pyplot as plt
import unittest
from pathlib import Path
import tui
import process
def read_data(file_path):
    try:
        tui.started(f"Reading data from {file_path}")

        data_folder = Path("/Users/gabor/Documents/Solent/5. év Masters/Computer Fundamentals/Python/")

        file_to_open = data_folder / file_path

        f = open(file_to_open)

        data = []

        reader = csv.reader(f)
        header = []
        header = next(reader)
        for row in reader:
            data.append(row)
        tui.completed()
        return data
    except IOError:
        print("Cannot read file.")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def run():
    song_data = read_data("charts.csv")
    #date = '2021-10-30'
  #  date = input("giv a date")
    while True:
        selection = tui.menu()
        if selection == "1":
            print(1)
            process.top_song_details_for_a_day(song_data)

        elif selection == "2":
            print(2)
            process.details_of_artists_mtrs(song_data)

        elif selection == "3":
            print(3)
            process.top10_weeksonboard2(song_data)

        elif selection == "4":
            print(4)
            process.moved_the_most(song_data)
        elif selection == "5":
            process.display_one_artists_results(song_data)
        elif selection == "6":
            process.top10_songs_of_a_day(song_data)
        elif selection == "7":
            print("List of number 1 songs")
            process.list_of_number1_songs(song_data)
        elif selection == "8":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == '__main__':
    run()



