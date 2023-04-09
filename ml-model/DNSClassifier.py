import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, recall_score, precision_score, confusion_matrix
from sklearn.metrics import plot_precision_recall_curve
import matplotlib.pyplot as plt

# Load the CSV files into dataframes
visited_data = pd.read_csv('../dataset/experiment_results/dns_visited_experiment.csv', sep='\t', header=None, names=['url', 'load_time'])
not_visited_data = pd.read_csv('../dataset/experiment_results/dns_not_visited_experiment.csv', sep='\t', header=None, names=['url', 'load_time'])

# Drop rows with missing data
visited_data.dropna(inplace=True)
not_visited_data.dropna(inplace=True)

# Drop rows where load_time is not a number
visited_data = visited_data[visited_data['load_time'].apply(lambda x: isinstance(x, (int, float)))]
not_visited_data = not_visited_data[not_visited_data['load_time'].apply(lambda x: isinstance(x, (int, float)))]

# Merge the two dataframes and create a label column
visited_data['label'] = 'visited'
not_visited_data['label'] = 'not visited'
data = pd.concat([visited_data, not_visited_data], ignore_index=True)

# Drop rows where label is missing
data.dropna(subset=['label'], inplace=True)

# Encode the labels
le = LabelEncoder()
data['label'] = le.fit_transform(data['label'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data['load_time'], data['label'], test_size=0.2)

# Convert X_train and X_test into 2D arrays
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

# Train a logistic regression classifier
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy and recall
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

# Print the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Plot the precision-recall curve
disp = plot_precision_recall_curve(clf, X_test, y_test)
disp.ax_.set_title('2-class Precision-Recall curve: '
                   'AP={0:0.2f}, Acc={1:0.2f}, Rec={2:0.2f}'.format(
                    disp.average_precision, accuracy, recall))

plt.show()
