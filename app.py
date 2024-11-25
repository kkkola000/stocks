from flask import Flask, render_template, send_file, request
import yaml
from datetime import datetime

app = Flask(__name__)

# Загружаем данные из YML
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

# Основной маршрут для отображения остатков
@app.route('/')
def index():
    data = load_data("market.yml")  # Путь к вашему файлу YML
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")  # Дата для предотвращения кеширования
    return render_template('index.html', products=data['products'], date=current_date)

# Маршрут для скачивания файла (если нужно)
@app.route('/download')
def download():
    return send_file("market.yml", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
