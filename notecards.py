import genanki

# List of MLB teams and their stadium
mlb_teams = [
    ('Arizona Diamondbacks', 'Chase Field'),
    ('Atlanta Braves', 'Truist Park'),
    ('Baltimore Orioles', 'Oriole Park at Camden Yards'),
    ('Boston Red Sox', 'Fenway Park'),
    ('Chicago Cubs', 'Wrigley Field'),
    ('Chicago White Sox', 'Guaranteed Rate Field'),
    ('Cincinnati Reds', 'Great American Ball Park'),
    ('Cleveland Indians', 'Progressive Field'),
    ('Colorado Rockies', 'Coors Field'),
    ('Detroit Tigers', 'Comerica Park'),
    ('Houston Astros', 'Minute Maid Park'),
    ('Kansas City Royals', 'Kauffman Stadium'),
    ('Los Angeles Angels', 'Angel Stadium'),
    ('Los Angeles Dodgers', 'Dodger Stadium'),
    ('Miami Marlins', 'LoanDepot Park'),
    ('Milwaukee Brewers', 'American Family Field'),
    ('Minnesota Twins', 'Target Field'),
    ('New York Mets', 'Citi Field'),
    ('New York Yankees', 'Yankee Stadium'),
    ('Oakland Athletics', 'RingCentral Coliseum'),
    ('Philadelphia Phillies', 'Citizens Bank Park'),
    ('Pittsburgh Pirates', 'PNC Park'),
    ('San Diego Padres', 'Petco Park'),
    ('San Francisco Giants', 'Oracle Park'),
    ('Seattle Mariners', 'T-Mobile Park'),
    ('St. Louis Cardinals', 'Busch Stadium'),
    ('Tampa Bay Rays', 'Tropicana Field'),
    ('Texas Rangers', 'Globe Life Field'),
    ('Toronto Blue Jays', 'Rogers Centre'),
    ('Washington Nationals', 'Nationals Park')
]

# Define Anki note model
model_id = 1607392319 #random number here
model = genanki.Model(
    model_id,
    'Simple Model',
    fields=[
        {'name': 'Directory'},
        {'name': 'Description'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Directory}}',
            'afmt': '{{Description}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Description}}',
            'afmt': '{{Directory}}',
        },
    ])

# Generate Anki cards and add them to a deck
deck_id = 2059400110
deck = genanki.Deck(deck_id, 'MLB Stadiums')

for team_name, stadium in mlb_teams:
    note = genanki.Note(model=model, fields=[team_name, stadium])
    deck.add_note(note)

# Save the deck to an Anki package (*.apkg) file
genanki.Package(deck).write_to_file('mlb_stadiums.apkg')