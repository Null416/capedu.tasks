import telebot
import requests
from telebot import types

token = '8878277091:AAFwfvcbS22MIKEOlmvCAH38tlJD695ZV_A'
Weather_API_key = 'ecfab250aff940f38b7152251261706'
bot = telebot.TeleBot(token)

user_city = {}

city_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
city_markup.add(types.KeyboardButton('Astana'))
city_markup.add(types.KeyboardButton('Moskva'))
city_markup.add(types.KeyboardButton('New York'))

def days_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('📅 1 день'))
    markup.add(types.KeyboardButton('📅 3 дня'))
    markup.add(types.KeyboardButton('📅 7 дней'))
    markup.add(types.KeyboardButton('🏙 Сменить город'))
    return markup

def get_weather(city, days=1):
    try:
        url = f'http://api.weatherapi.com/v1/forecast.json?key={Weather_API_key}&q={city}&days={days}&aqi=no'
        response = requests.get(url, timeout=10)
        data = response.json()

        print(f'Статус: {response.status_code}, Данные: {data}')  # ✅ для отладки

        if 'error' in data:
            return None, f'❌ Город "{city}" не найден. Проверьте название.'

        location = data['location']['name']
        country = data['location']['country']
        report = f'📍 Погода в {location}, {country}:\n\n'

        for day in data['forecast']['forecastday']:
            date = day['date']
            avg_temp = day['day']['avgtemp_c']
            max_temp = day['day']['maxtemp_c']
            min_temp = day['day']['mintemp_c']
            humidity = day['day']['avghumidity']
            wind_speed = day['day']['maxwind_kph']
            desc = day['day']['condition']['text']

            report += (
                f'📆 Дата: {date}\n'
                f'🌤 Описание: {desc}\n'
                f'🌡 Температура: {avg_temp}°C (макс: {max_temp}°C, мин: {min_temp}°C)\n'
                f'💧 Влажность: {humidity}%\n'
                f'💨 Скорость ветра: {wind_speed} км/ч\n'
                f'{"─" * 25}\n'
            )
        return report, None  # ✅ возвращаем (результат, ошибка)

    except requests.exceptions.ConnectionError:
        return None, '❌ Нет подключения к интернету.'
    except requests.exceptions.Timeout:
        return None, '❌ Сервер не отвечает, попробуйте позже.'
    except Exception as e:
        return None, f'❌ Неизвестная ошибка: {e}'


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 'Привет! Я бот погоды 🌤\nВыберите город или напишите свой:',
                 reply_markup=city_markup)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.strip()

    if text in ['📅 1 день', '📅 3 дня', '📅 7 дней']:
        city = user_city.get(message.chat.id)
        if not city:
            bot.reply_to(message, '❌ Сначала выберите город!', reply_markup=city_markup)
            return

        days = 1 if '1' in text else 3 if '3' in text else 7
        result, error = get_weather(city, days)

        if error:
            bot.reply_to(message, error, reply_markup=city_markup)
        else:
            bot.reply_to(message, result, reply_markup=days_markup())

    elif text == '🏙 Сменить город':
        user_city.pop(message.chat.id, None)  # ✅ сбрасываем город
        bot.reply_to(message, 'Выберите или напишите город:', reply_markup=city_markup)

    else:
        # Проверяем город
        result, error = get_weather(text, 1)
        if error:
            # ✅ Город неверный — не сохраняем
            bot.reply_to(message, error + '\nПопробуйте ещё раз:', reply_markup=city_markup)
        else:
            # ✅ Город верный — сохраняем
            user_city[message.chat.id] = text
            bot.reply_to(message,
                         f'✅ Город выбран: {text}\nНа сколько дней показать погоду?',
                         reply_markup=days_markup())


bot.polling()