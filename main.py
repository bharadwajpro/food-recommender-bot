import aiml
import logging
import time
import sqlite3

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
kernel = aiml.Kernel()
kernel.learn("./aiml-xmls/std-startup.xml")
conn = sqlite3.connect('knowledge-base.db', check_same_thread=False)
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS responses (userResponse text, botResponse text)
''')

kernel.respond('load all')
while True:
    input_message = input("User: ")
    if input_message == 'q':
        kernel.saveBrain('./brain-files/eatery-bot-{}.brn'.format(time.time()))
        break
    outMessage = kernel.respond(input_message)
    print('Bot:', outMessage)
    c.execute('''
        INSERT INTO responses VALUES (?,?)
    ''', (input_message, outMessage))
    conn.commit()

conn.close()
