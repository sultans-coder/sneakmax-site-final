from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

def format_order_items(items):
    items_list = json.loads(items)  
    formatted_items = []
    for item in items_list:
        formatted_title = item['title'].strip()
        formatted_price = item['price'].strip()
        formatted_item = f"Название: {formatted_title}\nЦена: {formatted_price}\n"
        formatted_items.append(formatted_item)
    return "\n".join(formatted_items)

@app.route('/submit_order', methods=['POST'])
def submit_order():
    data = request.form.to_dict()
    telegram_token = '6131934501:AAEGYkLqYf1bz-RvB7KndaTXqlrhyQeM36A'
    chat_id = '1066297089'
    formatted_items = format_order_items(data["Товары"])
    message = f'Жаңа заказ!\n\nЕсімі: {data["Имя"]}\nТелефон номері: {data["Телефон"]}\nEmail: {data["Email"]}\nТауарлар:\n{formatted_items}'
    telegram_url = f'https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}'
    response = requests.get(telegram_url)

    if response.status_code == 200:
        return 'Данные успешно отправлены в телеграм-бота'
    else:
        return 'Ошибка при отправке данных в телеграм-бота'

if __name__ == '__main__':
    app.run(debug=True)
