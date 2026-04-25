import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://elif.cz/LA_2526"

def fetch_previous_grades(url=URL):
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    # find the table under “Stav získaných bodů …” (based on your inspection)
    table = soup.find("table")
    if table is None:
        raise RuntimeError("Could not find the grades table")
    # Use pandas to read html table
    dfs = pd.read_html(str(table))
    df = dfs[0]
    return df

def main():
    print("Fetching previous grades …")
    grades_df = fetch_previous_grades()
    print("Here are previous grades:")
    print(grades_df.head())
    
    # Simplified: assume the “Σ” column is the total points (or adapt to grade)
    # Ask user to make a bet:
    user_name = input("Enter your nickname: ")
    bet_points = float(input("Enter how many points you expect to get: "))
    
    actual_points = float(input("Once you have your actual result, input it here: "))
    
    print(f"{user_name}, you bet {bet_points} points.")
    print(f"Your actual result: {actual_points} points.")
    
    if actual_points >= bet_points:
        print("Congratulations — you met or beat your bet!")
    else:
        print("Too bad — you did not reach your bet.")
    
    # Optionally, you could compare how you did vs class averages:
    avg = grades_df["Σ"].mean()
    print(f"Class average so far (based on table): {avg:.2f} points.")
    if actual_points > avg:
        print("You scored above the class average!")
    else:
        print("You scored below the class average.")

if __name__ == "__main__":
    main()
