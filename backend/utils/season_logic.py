from datetime import datetime

def get_season():
    today = datetime.now()
    year = 2025

    # Define season start and end dates for 2025
    seasons = {
        "Vasantha Ruthu": (datetime(year, 2, 18), datetime(year, 4, 20)),
        "Greeshma Ruthu": (datetime(year, 4, 20), datetime(year, 6, 21)),
        "Varsha Ruthu": (datetime(year, 6, 21), datetime(year, 8, 23)),
        "Sarath Ruthu": (datetime(year, 8, 23), datetime(year, 10, 23)),
        "Haemantha Ruthu": (datetime(year, 10, 23), datetime(year, 12, 21)),
        "Sisira Ruthu": (datetime(year, 12, 21), datetime(year + 1, 2, 18))
    }

    # Determine the current season
    for season, (start, end) in seasons.items():
        if start <= today <= end:
            return season

    return "Unknown"

# Example usage
if __name__ == "__main__":
    current_season = get_season()
    print(f"Current Season: {current_season}")