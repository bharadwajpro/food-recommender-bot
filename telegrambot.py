import aiml
import logging
import telepot
import time
import sqlite3
import atexit

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
bot = telepot.Bot(<token-here>)
try:
    currentUpdateId = bot.getUpdates()[-1]['update_id']
except IndexError:
    currentUpdateId = 0
kernel = aiml.Kernel()
kernel.learn("./aiml-xmls/std-startup.xml")
conn = sqlite3.connect('knowledge-base.db', check_same_thread=False)
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS responses (userResponse text, botResponse text)
''')


kernel.respond('load all')


def save_brain(k):
    k.saveBrain('./brain-files/eatery-bot-{}.brn'.format(time.time()))


atexit.register(save_brain, kernel)
while True:
    updates = bot.getUpdates(offset=currentUpdateId+1)
    for update in updates:
        currentUpdateId = update['update_id']
        message = update['message']
        content_type, chat_type, chat_id = telepot.glance(message)
        out_message = kernel.respond(message['text'])
        if content_type == 'text':
            out_message = out_message.replace('||', '\n')
            if 'IMG_URL' in out_message:
                bot.sendPhoto(chat_id, out_message[8:])
            else:
                bot.sendMessage(chat_id, out_message, parse_mode='html')
            c.execute('''
                    INSERT INTO responses VALUES (?,?)
                ''', (message['text'], out_message))
            conn.commit()
    time.sleep(1)
