# Creates new Foam notes and notes for missing dates
# There are better options for doing this, check out the Foam discord 
# at https://discord.gg/qkm8Js4ZyZ to see what other people are doing

import datetime, os, glob, sys
from pathlib import Path
from myosotis import *

# Take in a datetime and return a string of the desired entry
def create_daily_note_string(day, tomorrow_footers):
    entry = "# "
    entry += day.strftime("%A, %B %d, %Y")
    entry += "\n\n"
    if tomorrow_footers:
        yesterday = day - datetime.timedelta(days=1)
        tomorrow = day + datetime.timedelta(days=1)
        entry += f"<<   {yesterday.strftime('[[%Y-%m-%d]]')} || {tomorrow.strftime('[[%Y-%m-%d]]')}  >>"
        entry += "\n\n"
    # Work template
    PRIORITIES = False 
    if PRIORITIES:
        if day.weekday() <= 4:
            entry += "\nPRIORITIES:\n"
    return entry


# list_of_files = glob.glob(PATH_TO_JOURNAL_ENTRIES) # * means all if need specific format then *.csv

# iterate over date range and create missing entries
# datetime d1s: First datetime to make a date for
# datetime d2s: Second datetime to make a date for
def make_date_pages(start_date, end_date, nav_footers):
    diff = end_date - start_date
    for i in range(diff.days + 1):
        newdate = start_date + datetime.timedelta(days=i)
        new_daily_note_filename = newdate.strftime("%Y-%m-%d.md")
        print(new_daily_note_filename)
        fullpath = Path(journal_directory + new_daily_note_filename)
        print(fullpath)
        if fullpath.is_file():
            print(f"Entry for {newdate.strftime('%A, %B %d, %Y')} already exists")
        else:
            if DRY_RUN:
                print(create_daily_note_string(newdate, nav_footers))
            else:
                f = open(fullpath, "w",encoding="utf-8")
                f.write(create_daily_note_string(newdate, nav_footers))
                f.close()


def make_new_note_interactive():
    title = input("Title: ")
    # Check if the note already exists
    note_already_exists = search_for_filename(title)
    if note_already_exists:
        print(f"A note about {title} already exists at {note_already_exists}")
        return       
    description = input("Description: ")
    parent = input("Please enter another note to link to: ")
    directory = input("Please enter the directory to save the note, or press [ENTER]: ")
    print("Would you like to search for previous instances of this note to create backlinks? [Y/N]")
    if input().upper() == "Y":
        print("Yeah, so would I")
    else:
        print("Good, that's not an option")

DRY_RUN = False
if not DRY_RUN:
    # TODO USE MYOSOTIS CONFIG
    journal_directory = get_config().get_root() + r"/journal/"
    ADD_NAVIGATION_FOOTERS = True
    FIRST_DATE = input("First date (YYYY-MM-DD): ")
    LAST_DATE  = input("Last date  (YYYY-MM-DD): ")
    date1 = datetime.datetime.strptime(FIRST_DATE, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(LAST_DATE, "%Y-%m-%d")
    make_date_pages(date1, date2, ADD_NAVIGATION_FOOTERS)
