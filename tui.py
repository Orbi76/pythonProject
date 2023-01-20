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
    {"[5]":<10} Visualise one artist's song
    {"[6]":<10} Top 10 on a given day
    {"[7]":<10} List of number 1 songs
    {"[8]":<10} test
    
    {"[9]":<10} Exit the program
    """)
    selection = input("Your selection: ")
    return selection.strip().lower()

