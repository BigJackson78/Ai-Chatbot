from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    bot_response = ''

    if request.method == 'POST':
        user_input = request.form.get('message', '').strip()

        if user_input:
            if 'hello' in user_input.lower():
                bot_response = 'Hey there!'
            elif 'bye' in user_input.lower():
                bot_response = 'Goodbye!'
            else:
                bot_response = 'I do not understand that yet.'

    # ✅ Always return something
    return render_template('index.html', response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)
