import requests
import os
import json

# Asks user to specify a day, and then uses the session and year in the privateconfig.json file to fetch the input for the specified day

# uses a config file named privateconfig.json which has a year and session, i.e.
# the session ID can be found in developer mode on the adventofcode.com website once you have logged in
"""
{
    "year": 2025,
    "session": "YOUR_SESSION_COOKIE"
}
"""
CONFIG_FILE = "privateconfig.json"

def load_config(path=CONFIG_FILE):
    try:
        with open(path, "r") as f:
            data = json.load(f)

        year = data.get("year")
        session_cookie = data.get("session")

        if not year or not session_cookie:
            raise ValueError("Config file must contain 'year' and 'session'.")

        return year, session_cookie

    except FileNotFoundError:
        raise Exception(f"Config file '{path}' not found.")
    except json.JSONDecodeError:
        raise Exception("Config file contains invalid JSON.")

def get_day():
    day_str = input("Enter day: ").strip().lower()
    day = int(day_str)
    if 1 <= day <= 25:
        return day
    print("Invalid format. Input a number between 1 and 25")

def fetch_aoc_input(year, day, session_cookie):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session_cookie}

    response = requests.get(url, cookies=cookies)

    if response.status_code == 200:
        return response.text.strip()
    elif response.status_code == 400:
        raise Exception("Bad Request — your session cookie is probably invalid.")
    elif response.status_code == 404:
        raise Exception(f"Puzzle input for day {day} not found.")
    else:
        raise Exception(f"Unexpected status {response.status_code}")

def main():
    print("=== Advent of Code Input Fetcher ===")
    day = get_day()
    year, session_cookie = load_config()

    try:
        puzzle_input = fetch_aoc_input(year, day, session_cookie)
        dirname = f"day{day:02d}"
        with open(os.path.join(dirname, "input.txt"), "w") as inputfile:
            inputfile.write(puzzle_input)
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()