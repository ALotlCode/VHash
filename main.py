import sqlite3

# establish connection to SQLite DB

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()


# defining the structure of a VTuber hashtag record

cursor.execute('''
    CREATE TABLE vtubers 
               (name TEXT, 
               general TEXT, 
               fan_art TEXT, 
               suggestions TEXT, 
               morning_show TEXT, 
               clips TEXT, 
               music TEXT, 
               memes TEXT,
               live TEXT,
               NSFW TEXT,
               community_posts TEXT)
''')


# insert various VTubers into the table

cursor.execute('''
               INSERT INTO vtubers VALUES 
               ('FUWAMOCO', 
               '#FUWAMOCO', 
               '#FWMCpix', 
               '#helpFWMC', 
               '#FWMCMORNING', 
               '#lilFWMC', 
               '#FWMCbeats', 
               '#FWMCwww',
               'None',
               'None',
               'None')
''')

cursor.execute('''
               INSERT INTO vtubers VALUES 
               ('Lazuli', 
               '#lazufish', 
               '#paintfins', 
               'None',
               'None',
               '#lazufishnclips',
               'None',
               '#lazulaff',
               '#lazulazulook',
               '#lazukashii',
               'None')
''')

cursor.execute('''
               INSERT INTO vtubers VALUES 
               ('PillowDear', 
               '#PillowDear', 
               '#PillowDraw', 
               'None',
               'None',
               'None',
               'None',
               'None',
               'None',
               'None',
               '#ThePiwwos')
''')

cursor.execute('''
               INSERT INTO vtubers VALUES 
               ('Mitzy', 
               '#mitzypluv', 
               '#drawtzy', 
               'None',
               'None',
               'None',
               'None',
               'None',
               'None',
               'None',
               'None')
''')

conn.commit()

# ask for a VTuber name

vtuberName = input("Enter a VTuber name: ")


try:
    cursor.execute(f"SELECT * FROM vtubers WHERE name = '{vtuberName}'")

    # print the entire hashtag record
    
    result = cursor.fetchone()
    
    print(f'''
          Vtuber: {result[0]}\n 
          General Hashtag: {result[1]}\n 
          Fan Art Hashtag: {result[2]}\n 
          Suggestions Hashtag: {result[3]}\n 
          Morning show Hashtag: {result[4]}\n 
          Clips Hashtag: {result[5]}\n 
          Music Hashtag: {result[6]}\n 
          Memes Hashtag: {result[7]}\n 
          Livestream Hashtag: {result[8]}\n 
          NSFW Hashtag: {result[8]}\n 
          Community Posts: {result[9]}\n''') 

except:
    print("That VTuber is not in our records")
