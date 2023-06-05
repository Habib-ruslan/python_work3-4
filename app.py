from flask import Flask, render_template, request

app = Flask(__name__)


def count_words(file_path):
    word_counts = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word = ''.join(filter(str.isalpha, word))  # Убираем всё, кроме букв
                if word:
                    word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        file_path = f"uploads/{file.filename}"
        file.save(file_path)
        word_counts = count_words(file_path)
        most_common_word = max(word_counts, key=word_counts.get)
        most_count = word_counts.get(most_common_word, 0)
        return render_template('result.html', most_common_word=most_common_word, word_counts=word_counts, most_count=most_count)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
