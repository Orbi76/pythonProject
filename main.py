# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv
from pathlib import Path
import tui
def read_data(file_path):
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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def run():
    song_data = read_data("charts.csv")

    while True:
        selection = tui.menu()
        if selection == "1":
            print(1)
          # process.list_years(athlete_data)
        elif selection == "2":
            print(2)
           # process.tally_medals(athlete_data)
        elif selection == "3":
            print(3)
            #process.tally_team_medals(athlete_data)
        elif selection == "4":
            break
        else:
            tui.error("Invalid Selection!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
