#! /usr/bin/env python3
# A script that imports movie data and finds the top-5 highest grossing movies
import csv
import argparse

def find_top_n(filename, n=19):

    """Finds the top 5 highest grossing movies in a CSV dataset.
       Input: filename, a string - points to filename of dataset
       Output: None
       Effect: should print five lines of text
    """
    # read in file contents as list of dictionaries
    with open(filename) as f:
        csvr = csv.DictReader(f)
        rows = [r for r in csvr]
    
    # Reformat some data types
    for row in rows:
        row["Gross"] = int(row["Gross"])
        row["Year"] = int(row["Release Date"][:4])

    # Sort data and get top 5
    gross_sort = lambda x : x["Gross"]
    rows.sort(key=gross_sort)
    top_n = rows[:-(n+1):-1]

    # Print out results
    for i, row in enumerate(top_n):

        print("{ind}. {row[Title]} ({row[Year]}) - ${row[Gross]:,d}".format(
            ind=i+1,
            row=row))


# Script to run
# Movie data comes from "Movie Gross and Ratings" dataset on Kaggle by Yashwanth Sharaf
# https://www.kaggle.com/datasets/thedevastator/movie-gross-and-ratings-from-1989-to-2014
if __name__ == "__main__":
    # from https://stackoverflow.com/questions/4033723/how-do-i-access-command-line-arguments
    parser = argparse.ArgumentParser("movie_top_n")
    # from https://stackoverflow.com/questions/15754208/how-to-make-argument-optional-in-python-argparse
    parser.add_argument("n", nargs='?', help="get the top (n) movies", type=int)
    args = parser.parse_args()
    n = args.n if args.n is not None else 10
    find_top_n("Movies_gross_rating.csv", n)

