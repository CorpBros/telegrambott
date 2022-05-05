import telebot
from telebot import types
import time

bot = telebot.TeleBot('5313061496:AAFgZ9xg4ZWhE37-ZmDxbn1JQtnSFDVuXSU')

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
markupstart = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
markuphide = types.ReplyKeyboardRemove()

filmid = 0
tts = 1
choosefilmtype = 0
maxfilm = 42

@bot.message_handler(commands=['start'])
def start(message):
    global choosefilmtype
    choosefilmtype = 0
    markup.keyboard.clear()
    markupstart.keyboard.clear()
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nЯ телеграмм бот, который поможет тебе выбрать фильм на ночь😃', reply_markup = markuphide)
    global tts
    time.sleep(tts)
    button1 = types.KeyboardButton('Начнём😉')
    button2 = types.KeyboardButton('Отзывы на фильмы')
    markupstart.add(button1, button2)
    bot.send_message(message.chat.id, 'Но для этого, ты, мой дорогой юзер, должен пройти небольшой тест, который поможет мне определиться с подходящим для тебя фильмом🙃🙃🙃', reply_markup = markupstart)

@bot.message_handler(content_types=['text'])
def choosegenre(message):
    if message.text == 'Начнём😉':
        markup.keyboard.clear()
        markupstart.keyboard.clear()
        button1 = types.KeyboardButton('Фантастика')
        button2 = types.KeyboardButton('Драма')
        button3 = types.KeyboardButton('Детектив')
        button4 = types.KeyboardButton('Триллер')
        button5 = types.KeyboardButton('Боевик')
        button6 = types.KeyboardButton('Исторические фильмы')
        button7 = types.KeyboardButton('Классические фильмы')
        markup.add(button1, button2, button3, button4, button5, button6, button7)
        bot.send_message(message.chat.id, 'Первый вопрос - Какой жанр Вы предпочитаете? 😍', reply_markup = markup)
        bot.register_next_step_handler(message,choosecon)
    if(message.text == 'Отзывы на фильмы'):
        reviewmenu(message)


def choosecon(message):
    global choosefilmtype
    markup.keyboard.clear()
    button1 = types.KeyboardButton('Зарубежные')
    button2 = types.KeyboardButton('Русские')
    markup.add(button1, button2)
    if message.text == 'Фантастика':
        choosefilmtype = 1
        bot.send_message(message.chat.id, 'Какую фантастические фильмы Вы предпочитаете?', reply_markup = markup)
        bot.register_next_step_handler(message,result)
    elif message.text == 'Драма':
        choosefilmtype = 2
        bot.send_message(message.chat.id, 'Какую драматические фильмы Вы предпочитаете?', reply_markup = markup)
        bot.register_next_step_handler(message,result)
    elif message.text == 'Детектив':
        choosefilmtype = 3
        bot.send_message(message.chat.id, 'Какую детективные фильмы Вы предпочитаете?', reply_markup = markup)
        bot.register_next_step_handler(message,result)
    elif message.text == 'Триллер':
        choosefilmtype = 4
        bot.send_message(message.chat.id, 'Какую триллеры Вы предпочитаете?', reply_markup = markup)
        bot.register_next_step_handler(message,result)
    elif message.text == 'Боевик':
        choosefilmtype = 5
        bot.send_message(message.chat.id, 'Какую боевики Вы предпочитаете?', reply_markup = markup)
        bot.register_next_step_handler(message,result)
    elif message.text == 'Исторические фильмы':
        choosefilmtype = 6
        bot.send_message(message.chat.id, 'Какую исторические фильмы Вы предпочитаете?', reply_markup = markup)
        bot.register_next_step_handler(message,result)
    elif message.text == 'Классические фильмы':
        choosefilmtype = 7
        bot.send_message(message.chat.id, 'Какую классические фильмы Вы предпочитаете?', reply_markup = markup)
        bot.register_next_step_handler(message,result)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста выберите фильм')
        bot.register_next_step_handler(message,choosecon)

def result(message):
    global choosefilmtype
    global tts
    if choosefilmtype == 1:
        bot.send_message(message.chat.id, 'хо-хо-хо, вот тебе целый список фантастических фильмов😎', reply_markup = markuphide)
        time.sleep(tts)
        if message.text == 'Зарубежные':
            film1 = 'Терминатор (1984) - США, Великобритания\nhttps://www.kinopoisk.ru/film/507/'
            film2 = 'Назад в будущее (1985) - США\nhttps://www.kinopoisk.ru/film/476/'
            film3 = 'Матрица (1999) - США, Австралия\nhttps://www.kinopoisk.ru/film/301/'
            bot.send_message(message.chat.id, str(film1))
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
        elif message.text == 'Русские':
            film1 = 'Вторжение (2019)\nhttps://www.kinopoisk.ru/film/1045582/'
            film2 = 'Хардкор (2016)\nhttps://www.kinopoisk.ru/film/778218/'
            film3 = 'Призрак (2015)\nhttps://www.kinopoisk.ru/film/839960/'
            bot.send_message(message.chat.id, film1)
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
    elif choosefilmtype == 2:
        bot.send_message(message.chat.id, 'хо-хо-хо, вот тебе целый список драматических фильмов😎', reply_markup = markuphide)
        time.sleep(tts)
        if message.text == 'Зарубежные':
            film1 = 'Титаник (1997) - США, Мексика, Австралия\nhttps://www.kinopoisk.ru/film/2213/'
            film2 = '1+1 (2011) - Франция\nhttps://www.kinopoisk.ru/film/535341/'
            film3 = 'Артист (2011) - Франция, Бельгия\nhttps://www.kinopoisk.ru/film/539550/'
            bot.send_message(message.chat.id, film1)
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
        elif message.text == 'Русские':
            film1 = 'Аритмия (2017)\nhttps://www.kinopoisk.ru/film/992605/'
            film2 = 'Лёд (2017)\nhttps://www.kinopoisk.ru/film/900052/'
            film3 = 'Сёстры (2001)\nhttps://www.kinopoisk.ru/film/41109/'
            bot.send_message(message.chat.id, film1)
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
    elif choosefilmtype == 3:
        bot.send_message(message.chat.id, 'хо-хо-хо, вот тебе целый список детективных фильмов😎', reply_markup = markuphide)
        time.sleep(tts)
        if message.text == 'Зарубежные':
            film1 = 'Шерлок Холмс: Игра теней (2011) - США, Великобритания\nhttps://www.kinopoisk.ru/film/474953/'
            film2 = 'Достать ножи (2019) - США\nhttps://www.kinopoisk.ru/film/1188529/'
            film3 = 'Убийство в Восточном экспрессе (2017) - США, Мальта, Великобритания\nhttps://www.kinopoisk.ru/film/817969/'
            bot.send_message(message.chat.id, film1)
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
        elif message.text == 'Русские':
            film1 = 'Правосудие волков (2009)\nhttps://www.kinopoisk.ru/film/400472/'
            film2 = 'Пуля Дурова (2018)\nhttps://www.kinopoisk.ru/film/1185935/'
            film3 = 'Шкварки (2013)\nhttps://www.kinopoisk.ru/film/723984/'
            bot.send_message(message.chat.id, film1)
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
    elif choosefilmtype == 4:
        bot.send_message(message.chat.id, 'хо-хо-хо, вот тебе целый список триллеров😎', reply_markup = markuphide)
        time.sleep(tts)
        if message.text == 'Зарубежные':
            film1 = 'Остров фантазий (2020) - США\nhttps://www.kinopoisk.ru/film/462193/'
            film2 = 'Время (2021) - США, Япония\nhttps://www.kinopoisk.ru/film/1379090/'
            film3 = 'Молчание ягнят (1990) - США\nhttps://www.kinopoisk.ru/film/345/'
            bot.send_message(message.chat.id, film1)
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
        elif message.text == 'Русские':
            film1 = 'Тварь (2019)\nhttps://www.kinopoisk.ru/film/1138880/'
            film2 = 'Кольская сверхглубокая (2020)\nhttps://www.kinopoisk.ru/film/1334853/'
            film3 = 'Саранча (2013)\nhttps://www.kinopoisk.ru/film/838049/'
            bot.send_message(message.chat.id, film1)
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
    elif choosefilmtype == 5:
        bot.send_message(message.chat.id, 'хо-хо-хо, вот тебе целый список боевиков😎', reply_markup = markuphide)
        time.sleep(tts)
        if message.text == 'Зарубежные':
            film1 = 'Форсаж (2001) - США, Германия\nhttps://www.kinopoisk.ru/film/666/'
            film2 = 'Неудержимые (2010) - США, Болгария, Испания, Германия\nkinopoisk.ru/film/432550/'
            film3 = 'Плохие парни (1995) - США\nhttps://www.kinopoisk.ru/film/3908/'
            bot.send_message(message.chat.id, film1)
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
        elif message.text == 'Русские':
            film1 = 'Брат (1997)\nhttps://www.kinopoisk.ru/film/41519/'
            film2 = 'Ворошиловский стрелок (1999)\nhttps://www.kinopoisk.ru/film/41442/'
            film3 = 'Герой (2019)\nhttps://www.kinopoisk.ru/film/1115467/'
            bot.send_message(message.chat.id, film1)
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
    elif choosefilmtype == 6:
        bot.send_message(message.chat.id, 'хо-хо-хо, вот тебе целый список исторических фильмов😎', reply_markup = markuphide)
        time.sleep(tts)
        if message.text == 'Зарубежные':
            film1 = 'Троя (2004) - США, Мальта, Великобритания\nhttps://www.kinopoisk.ru/film/3442/'
            film2 = 'Дюнкерк (2017) - Великобритания, Нидерланды, Франция, США\nhttps://www.kinopoisk.ru/film/931677/'
            film3 = 'В тылу врага (2001) - США\nhttps://www.kinopoisk.ru/film/606/'
            bot.send_message(message.chat.id, film1)
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
        elif message.text == 'Русские':
            film1 = 'Т-34 (2018)\nhttps://www.kinopoisk.ru/film/930878/'
            film2 = 'Сталинград (2013)\nhttps://www.kinopoisk.ru/film/468196/'
            film3 = '...А зори здесь тихие (1972)\nhttps://www.kinopoisk.ru/film/43395/'
            bot.send_message(message.chat.id, film1)
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
    elif choosefilmtype == 7:
        bot.send_message(message.chat.id, 'хо-хо-хо, вот тебе целый список классических фильмов, прошитых временем 😎', reply_markup = markuphide)
        time.sleep(tts)
        if message.text == 'Зарубежные':
            film1 = 'Крестный отец (1972) - США\nhttps://www.kinopoisk.ru/film/325/'
            film2 = 'Побег из Шоушенка (1994) - США\nhttps://www.kinopoisk.ru/film/326/'
            film3 = 'Сияние (1980) - США\nhttps://www.kinopoisk.ru/film/409/'
            bot.send_message(message.chat.id, film1)
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
        elif message.text == 'Русские':
            film1 = 'Бриллиантовая рука (1968)\nhttps://www.kinopoisk.ru/film/46225/'
            film2 = 'Война и Мир (1965, 4 части)\nhttps://www.kinopoisk.ru/series/38898/'
            film3 = 'Операция «Ы» и другие приключения Шурика (1965)\nhttps://www.kinopoisk.ru/film/42782/'
            bot.send_message(message.chat.id, film1)
            time.sleep(tts)
            bot.send_message(message.chat.id, film2)
            time.sleep(tts)
            bot.send_message(message.chat.id, film3)
    time.sleep(tts)
    markup.keyboard.clear()
    button1 = types.KeyboardButton('Завершить выбор фильма')
    button2 = types.KeyboardButton('Начать заново')
    button3 = types.KeyboardButton('Оставить отзыв на фильм')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Надеюсь что тебе понравится моя подборка!\nТакже на предложенные мной фильмы ты можешь оставить отзыв!', reply_markup = markup)
    bot.register_next_step_handler(message,end)

def end(message):
    if message.text == 'Начать заново':
        start(message)
    elif message.text == 'Завершить выбор фильма':
        bot.send_message(message.chat.id, 'Если ты снова захочешь найти фильм по твоему вкусу, то пропиши /start', reply_markup = markuphide)
        bot.register_next_step_handler(message,waiting)
    elif message.text == 'Оставить отзыв на фильм':
        reviewfilm(message)
def reviewfilm(message):
    listf = ''
    bot.send_message(message.chat.id, 'Напиши номер фильма, на который ты хочешь оставить отзыв', reply_markup = markuphide)
    global tts
    time.sleep(tts)
    with open('efiles/films.txt','r+', encoding = 'utf-8') as filef:
        listf = filef.read()
        msg = f'Cписок:\n{listf}'
        bot.send_message(message.chat.id, msg, reply_markup = markuphide)
    bot.register_next_step_handler(message,reviewfilm1)

def reviewfilm1(message):
    global filmid
    global maxfilm
    filmid = message.text
    try:
        if int(filmid) <= maxfilm:
            with open('efiles/films.txt','r', encoding = 'utf-8') as filef:
                for i in filef:
                    if(message.text == i):
                        filmid = i
            bot.send_message(message.chat.id, 'Теперь напишите отзыв')
            bot.register_next_step_handler(message,reviewfilmtext)
        else:
            bot.send_message(message.chat.id, 'У меня нет такого фильма. Попробуй ввести другое значение')
            bot.register_next_step_handler(message,reviewfilm1)
    except:
        bot.send_message(message.chat.id, 'Ты ввёл не число. Попробуй ввести значение снова')
        bot.register_next_step_handler(message,reviewfilm1)

def reviewfilmtext(message):
    reviewtext = message.text
    global filmid
    global tts
    with open('efiles/reviews.txt','a', encoding = 'utf-8') as filer:
        filer.write(f'[{filmid}]{reviewtext}\n')
    bot.send_message(message.chat.id, 'Ваш отзыв сохранён!😁')
    time.sleep(tts)
    bot.send_message(message.chat.id, 'Если ты снова захочешь найти фильм по твоему вкусу, то пропиши /start', reply_markup = markuphide)
    bot.register_next_step_handler(message,waiting)

def waiting(message):
    if(message.text == '/start'):
        start(message)
    else:
        bot.send_message(message.chat.id, 'Если ты снова захочешь найти фильм по твоему вкусу, то пропиши /start', reply_markup = markuphide)
        bot.register_next_step_handler(message,waiting)

def reviewmenu(message):
    markup.keyboard.clear()
    button1 = types.KeyboardButton('Оставить отзыв на фильм')
    button2 = types.KeyboardButton('Посмотреть на отзывы других')
    button3 = types.KeyboardButton('Назад')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Что Вы хотите сделать?', reply_markup = markup)
    bot.register_next_step_handler(message,reviewmenucr)

def reviewmenucr(message):
    if message.text == 'Оставить отзыв на фильм':
        reviewfilm(message)
    elif message.text == 'Посмотреть на отзывы других':
        reviewother(message)
    elif message.text == 'Назад':
        start(message)

def reviewother(message):
    listf = ''
    bot.send_message(message.chat.id, 'Напиши номер фильма, на отзывы которого ты хочешь посмотреть', reply_markup = markuphide)
    global tts
    time.sleep(tts)
    with open('efiles/films.txt','r+', encoding = 'utf-8') as filef:
        listf = filef.read()
        msg = f'Cписок:\n{listf}'
        bot.send_message(message.chat.id, msg, reply_markup = markuphide)
    bot.register_next_step_handler(message,reviewother1)

def reviewother1(message):
    global maxfilm
    global filmid
    global tts
    filmid = message.text
    try:
        float(filmid)
        if int(filmid) <= maxfilm:
            listr = ''
            reviewcount = 0
            bigreview = 0
            with open('efiles/reviews.txt','r+', encoding = 'utf-8') as filer:
                for line in filer:
                    try:
                        if int(line[1:3]) >= 10:
                            if line[1:3] == str(filmid):
                                bigreview = 1
                                reviewcount += 1 
                                if line != '':
                                    listr = listr + f'{reviewcount}.{line[4::]}'
                        if bigreview == 1:
                            try:
                                int(line[1:3])
                            except:
                                listr = listr + line
                    except:
                        if line[1] == str(filmid):
                            bigreview = 1
                            reviewcount += 1 
                            if line != '':
                                listr = listr + f'{reviewcount}.{line[3::]}'
                        if bigreview == 1:
                            try:
                                int(line[1])
                            except:
                                listr = listr + line
            if(listr == ''):
                bot.send_message(message.chat.id, 'Отзывов нету😕')
                time.sleep(tts)
                reviewmenu(message)
            else:
                bot.send_message(message.chat.id, f'Отзывы:\n{listr}')
                time.sleep(tts)
                reviewmenu(message)
        else:
            bot.send_message(message.chat.id, 'У меня нет такого фильма.Попробуй ввести другое значение')
            bot.register_next_step_handler(message,reviewother1)
    except:
    #else:
        bot.send_message(message.chat.id, 'Ты ввёл не число. Попробуй ввести значение снова')
        bot.register_next_step_handler(message,reviewother1)


bot.polling(none_stop=True)