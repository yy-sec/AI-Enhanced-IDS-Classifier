import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, 
    confusion_matrix,  
    f1_score, 
    precision_score, 
    recall_score
)
from category_encoders import TargetEncoder


DATA_PATH = r"Path_to\cic_ids2017_clean_version.csv"

TARGET_COLUMN = 'binary_label' 
ENCODE_COLUMN = ' Destination Port'
TEST_SIZE = 0.2
RANDOM_STATE = 42


df = pd.read_csv(DATA_PATH)


df.columns = df.columns.str.strip()
TARGET_COLUMN = TARGET_COLUMN.strip()
ENCODE_COLUMN = ENCODE_COLUMN.strip()

X = df.drop(columns=[TARGET_COLUMN])
y = df[TARGET_COLUMN]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
)

X_train = X_train.reset_index(drop=True)
X_test = X_test.reset_index(drop=True)
y_train = y_train.reset_index(drop=True)
y_test = y_test.reset_index(drop=True)



port_train = X_train[ENCODE_COLUMN]
port_test = X_test[ENCODE_COLUMN]

cols_to_scale = X_train.columns.drop(ENCODE_COLUMN)
scaler = RobustScaler()

X_train_scaled = pd.DataFrame(
    scaler.fit_transform(X_train[cols_to_scale]), 
    columns=cols_to_scale
)
X_test_scaled = pd.DataFrame(
    scaler.transform(X_test[cols_to_scale]), 
    columns=cols_to_scale
)

encoder = TargetEncoder(cols=[ENCODE_COLUMN])
encoder.fit(port_train, y_train)

X_train_final = X_train_scaled.copy()
X_test_final = X_test_scaled.copy()

X_train_final[ENCODE_COLUMN] = encoder.transform(port_train)
X_test_final[ENCODE_COLUMN] = encoder.transform(port_test)

joblib.dump(scaler, "robust_scaler_binary.joblib")
joblib.dump(encoder, "target_encoder_binary.joblib")




model = RandomForestClassifier(
    n_estimators=100, 
    max_depth=20, 
    random_state=RANDOM_STATE,
    class_weight='balanced', 
    n_jobs=-1 
)

model.fit(X_train_final, y_train)

# Save the model
joblib.dump(model, "ids_model_binary.joblib")


y_pred = model.predict(X_test_final)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='binary') 
recall = recall_score(y_test, y_pred, average='binary')
f1 = f1_score(y_test, y_pred, average='binary')

print(f"\n--- Binary Classification Performance ---")
print(f"Accuracy:  {accuracy}")
print(f"Precision: {precision}")
print(f"Recall:    {recall}")
print(f"F1-Score:  {f1}")


cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', 
            xticklabels=['Benign', 'Attack'], yticklabels=['Benign', 'Attack'])
plt.title('Confusion Matrix Heatmap (Binary)')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.show()

print("\nBinary model and preprocessing objects have been saved.")
