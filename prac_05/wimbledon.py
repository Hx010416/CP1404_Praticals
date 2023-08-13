import csv

def read_csv_file(wimbledon):
    data = []
    with open(wimbledon, "r", encoding="utf-8-sig") as in_file:
        csv_reader = csv.reader(in_file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            data.append(row)
    return data

def count_champions(data):
    champion_count = {}
    for row in data:
        champion = row[4]
        if champion in champion_count:
            champion_count[champion] += 1
        else:
            champion_count[champion] = 1
    return champion_count

def get_countries(data):
    countries = set()
    for row in data:
        country = row[3]
        countries.add(country)
    return sorted(countries)

def main():
    filename = "wimbledon.csv"
    data = read_csv_file(filename)

    champion_count = count_champions(data)
    print("Wimbledon Champions:")
    for champion, count in sorted(champion_count.items()):
        print(f"{champion}: {count}")

    countries = get_countries(data)
    countries_str = ", ".join(countries)
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(countries_str)

if __name__ == "__main__":
    main()