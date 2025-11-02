import random
from datetime import datetime, timedelta

def generate_week_data():
    today = datetime.now()
    week_data = []
    for i in range(7):
        day = (today - timedelta(days=6 - i)).strftime("%A")
        hours = random.randint(1, 8)
        tasks = random.randint(1, 10)
        week_data.append({"day": day, "hours_studied": hours, "tasks_completed": tasks})
    return week_data
