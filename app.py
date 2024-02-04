from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll_dice')
def roll_dice():
    dice_result = random.randint(1, 6)

    if dice_result == 1:
        result_text = "Program"
    elif dice_result == 2:
        result_text = "Program"
    elif dice_result == 3:
        result_text = "Program"
    elif dice_result == 4:
        result_text = "Program"
    elif dice_result == 5:
        result_text = "Program"
    elif dice_result == 6:
        result_text = "Program"

    return jsonify({'dice_result': dice_result, 'result_text': result_text})

if __name__ == '__main__':
    app.run(debug=True)
