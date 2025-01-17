from flask import Flask, render_template, request
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Set the target date
target_date = datetime(2024, 9, 8)

@app.route("/")
def index():
    # Calculate the countdown
    countdown = target_date - datetime.now()
    days, hours, minutes, seconds = countdown.days, countdown.seconds // 3600, (countdown.seconds // 60) % 60, countdown.seconds % 60
    
    # Generate random numbers
    left_num = random.randint(1, 100)
    right_num = random.randint(1, left_num - 1)
    
    return render_template("index.html", days=days, hours=hours, minutes=minutes, seconds=seconds, left_num=left_num, right_num=right_num)

@app.route("/simulate", methods=["POST"])
def simulate():
    # Generate new random numbers
    left_num = random.randint(1, 100)
    right_num = random.randint(1, left_num - 1)
    
    return {"left_num": left_num, "right_num": right_num}

if __name__ == "__main__":
    app.run(debug=True)