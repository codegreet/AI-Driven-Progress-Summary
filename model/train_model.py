import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Dummy data
data = {
    "hours_studied": [1, 2, 4, 5, 7, 3, 8, 6, 2, 9],
    "tasks_completed": [1, 2, 3, 4, 6, 2, 8, 5, 2, 9],
    "productivity_level": ["low", "average", "average", "productive", "productive",
                           "average", "productive", "productive", "low", "productive"]
}

df = pd.DataFrame(data)

X = df[["hours_studied", "tasks_completed"]]
y = df["productivity_level"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

with open("model/progress_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to model/progress_model.pkl")
