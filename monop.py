import pandas as pd

# Define all Monopoly properties in a single table with color, name, price, build cost, and rent values
data = [
    # Brown
    ("Brown", "Mediterranean Avenue", 60, 50, 2, 10, 30, 90, 160, 250),
    ("Brown", "Baltic Avenue", 60, 50, 4, 20, 60, 180, 320, 450),
    # Light Blue
    ("Light Blue", "Oriental Avenue", 100, 50, 6, 30, 90, 270, 400, 550),
    ("Light Blue", "Vermont Avenue", 100, 50, 6, 30, 90, 270, 400, 550),
    ("Light Blue", "Connecticut Avenue", 120, 50, 8, 40, 100, 300, 450, 600),
    # Pink
    ("Pink", "St. Charles Place", 140, 100, 10, 50, 150, 450, 625, 750),
    ("Pink", "States Avenue", 140, 100, 10, 50, 150, 450, 625, 750),
    ("Pink", "Virginia Avenue", 160, 100, 12, 60, 180, 500, 700, 900),
    # Orange
    ("Orange", "St. James Place", 180, 100, 14, 70, 200, 550, 750, 950),
    ("Orange", "Tennessee Avenue", 180, 100, 14, 70, 200, 550, 750, 950),
    ("Orange", "New York Avenue", 200, 100, 16, 80, 220, 600, 800, 1000),
    # Red
    ("Red", "Kentucky Avenue", 220, 150, 18, 90, 250, 700, 875, 1050),
    ("Red", "Indiana Avenue", 220, 150, 18, 90, 250, 700, 875, 1050),
    ("Red", "Illinois Avenue", 240, 150, 20, 100, 300, 750, 925, 1100),
    # Yellow
    ("Yellow", "Atlantic Avenue", 260, 150, 22, 110, 330, 800, 975, 1150),
    ("Yellow", "Ventnor Avenue", 260, 150, 22, 110, 330, 800, 975, 1150),
    ("Yellow", "Marvin Gardens", 280, 150, 24, 120, 360, 850, 1025, 1200),
    # Green
    ("Green", "Pacific Avenue", 300, 200, 26, 130, 390, 900, 1100, 1275),
    ("Green", "North Carolina Avenue", 300, 200, 26, 130, 390, 900, 1100, 1275),
    ("Green", "Pennsylvania Avenue", 320, 200, 28, 150, 450, 1000, 1200, 1400),
    # Dark Blue
    ("Dark Blue", "Park Place", 350, 200, 35, 175, 500, 1100, 1300, 1500),
    ("Dark Blue", "Boardwalk", 400, 200, 50, 200, 600, 1400, 1700, 2000)
]

columns = ["Color", "Property", "Price", "Build Cost", "Rent", "1 House", "2 Houses", "3 Houses", "4 Houses", "Hotel"]
df = pd.DataFrame(data, columns=columns)
print(df)