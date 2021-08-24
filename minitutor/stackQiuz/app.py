from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)


@app.route('/')
def register():
    return render_template('index.html')


@app.route('/quiz', methods=['GET'])
def getQuiz():
    idx = request.args.get('idx')

    print(idx)

    quiz = ""

    if idx == '1':
        quiz = "퀴즈 1번"
    elif idx == '2':
        quiz = "퀴즈 2번"
    elif idx == '3':
        quiz = "퀴즈 3번"
    elif idx == '4':
        quiz = "퀴즈 4번"
    else:
        return render_template('index.html')

    return jsonify({'result': 'success', 'quiz': quiz})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
