import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text

# Dataset
data = {
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast',
                'Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    
    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Cool',
                    'Mild','Cool','Mild','Mild','Mild','Hot','Mild'],
    
    'Humidity': ['High','High','High','High','Normal','Normal','Normal',
                 'High','Normal','Normal','Normal','High','Normal','High'],
    
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong',
             'Weak','Weak','Weak','Strong','Strong','Weak','Strong'],
    
    'Play Tennis': ['No','No','Yes','Yes','Yes','No','Yes',
                    'No','Yes','Yes','Yes','Yes','Yes','No']
}

# Create DataFrame
df = pd.DataFrame(data)

# Separate input and target
X = df.drop('Play Tennis', axis=1)
y = df['Play Tennis']

# Convert categorical values into numerical values
X = pd.get_dummies(X)

# Create ID3 Decision Tree using Entropy
model = DecisionTreeClassifier(
    criterion='entropy',
    random_state=0
)

# Train the model
model.fit(X, y)

# Print Decision Tree
print("ID3 Decision Tree:")
print(export_text(model, feature_names=list(X.columns)))

# Plot Decision Tree
plt.figure(figsize=(14, 8))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=['No', 'Yes'],
    filled=True,
    rounded=True
)

plt.title("ID3 Decision Tree - Play Tennis")
plt.show()