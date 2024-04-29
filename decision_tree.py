from sklearn import tree

x = [[25, 50000],[35, 75000], [45, 100000], [20, 30000], [30, 60000]]
y = [0, 1, 1, 0, 0]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

new_data = [[40, 120000], [28, 40000]]
prediction = clf.predict(new_data)

for i in range(len(new_data)):
    print(f"Prediction for {new_data[i]}: {'yes' if prediction[i] == 1 else 'No'}")