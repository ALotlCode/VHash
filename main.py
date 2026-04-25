import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE vtubers (name TEXT, general TEXT, fan_art TEXT, suggestions TEXT, fuwamoco_morning TEXT, clips TEXT, music TEXT, memes TEXT)')
cursor.execute("INSERT INTO vtubers VALUES ('FUWAMOCO', '#FUWAMOCO', '#FWMCpix', '#helpFWMC', '#FWMCMORNING', '#lilFWMC', '#FWMCbeats', '#FWMCwww')")
conn.commit()

cursor.execute("SELECT * FROM vtubers WHERE name = 'FUWAMOCO'")
result = cursor.fetchone()
print(f'Vtuber: {result[0]}\nGeneral Hashtag: {result[1]}\nFan Art Hashtag: {result[2]}\nSuggestions Hashtag: {result[3]}\nFUWAMOCO Morning Hashtag: {result[4]}\nClips Hashtag: {result[5]}\nMusic Hashtag: {result[6]}\nMemes Hashtag: {result[7]}')