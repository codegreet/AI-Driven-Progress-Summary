from flask import Flask, render_template, jsonify
from utils.data_generator import generate_week_data
from utils.summarize_llm import summarize_progress
from model.predict import predict_productivity

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_progress', methods=['GET'])
def get_progress():
    week_data = generate_week_data()

    for day in week_data:
        day["prediction"] = predict_productivity(day["hours_studied"], day["tasks_completed"])

    try:
        summary = summarize_progress(week_data)
    except Exception as e:
        summary = f"Error generating summary: {str(e)}"

    return jsonify({"week_data": week_data, "summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
