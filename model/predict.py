import pickle
import pandas as pd

def predict_productivity(hours_studied, tasks_completed):
    with open("model/progress_model.pkl", "rb") as f:
        model = pickle.load(f)

    # ✅ Add DataFrame column names to match training format
    X_new = pd.DataFrame([[hours_studied, tasks_completed]],
                         columns=["hours_studied", "tasks_completed"])

    pred = model.predict(X_new)
    return pred[0]
