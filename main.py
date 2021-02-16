import telebot
import config
import random

bot = telebot.TeleBot(config.token)
keyboard_start = telebot.types.ReplyKeyboardMarkup()
keyboard_start.row('ты пидор', 'ты зая', ':3','/pidor')

keyboard_aww = telebot.types.ReplyKeyboardMarkup()
keyboard_aww.row('похвали меня', 'ты няша', '/start')

compliment_answers = ['я бы посвятил тебе все сонеты Шекспира',
                      'даже если собрать всех котов мира, они не будут и вполовину так милы, как ты',
                      'звезды падают, потому что хотят быть ближе к тебе',
                      'когда тебя рожали - все менты не дрожали а радовались, обнимались, кое-кто даже жене цветы купил по такому случаю',
                      'бог сотворил тебя и ушел на пенсию, потому что ты вершина его карьеры',
                      'когда ты попадешь в ад, сатана будет приходить к тебе по субботам с печеньками, чтобы попить какао и поиграть в шашки',]
aww_answers = ['ой ну скажешь тоже))))))',
               'найди что нибудь вкусное и съешь - это тебе от меня',
               'я хотел посмотреть гороскоп про тебя, но не нашел знака "милая булочка"',
               'а твоя мама знает что ты подкатываешь к ботам?',
               'но это не точно',
               'ты кого няшей называешь, алло. я бот блять, я не знаю страха и жалости. еблет свой береги']


@bot.message_handler(commands=['start'])
def start_message_answer(message):
    bot.send_message(message.chat.id, 'Привет, я вежливый и безумный бот. \
    \n- Хочешь мило поболтать - отправь мне :3 \
    \n- Напиши мне /pidor  и я скажу, кто пидор (btw это ты) \
    \n- но если назовешь меня пидором то ты сам пидор. Понял, пидор? ', reply_markup=keyboard_start)

@bot.message_handler(commands=['pidor'])
def pidor_message_answer(message):
    bot.send_message(message.chat.id, 'пидр это ты)))))')

"""

@bot.message_handler(content_types=['text'])
def text0_message_answer(message):
    print(message)
    bot.send_message(message.chat.id, 'Тебя зовут ' + message.from_user.first_name + ', а ник - @' + message.from_user.username)
"""


@bot.message_handler(content_types=['text'])
def text_message_answer(message):
        if message.text.lower() == 'привет':
            bot.send_message(message.chat.id, 'Привет, мой создатель)')
        if message.text.lower() == 'ты пидор':
            bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAKgkF_zSEbVWZ0KSUBJdFHTa1dtkV7xAAJPAAMv3_gJYXy_28ArGuoeBA')
        if message.text.lower() == 'ты зая':
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAKgsV_zWyuPyzS_raBplpi67kP4jR88AAI_AAPUuLUXO5S_vaiirP0eBA')
        if message.text.lower() == 'ы':
            bot.send_message(message.chat.id, 'Ыыыыыы!))))))')
        if message.text == ':3':
            bot.send_message(message.chat.id, ':33333 че хочешь?)))', reply_markup=keyboard_aww )

        if message.text.lower() == 'похвали меня':
            n = random.randint(0,5)
            bot.send_message(message.chat.id, compliment_answers[n])
        if message.text.lower() == 'ты няша':
            n = random.randint(0,5)
            bot.send_message(message.chat.id, aww_answers[n])

        if 'жопа' in message.text.lower():
            bot.send_message(message.chat.id, 'Ну жопа и что?')
        elif message.text.lower() == 'пока':
            bot.send_message(message.chat.id, 'Прощай, создатель(')


bot.polling()



