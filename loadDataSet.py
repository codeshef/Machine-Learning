#load iris data set

from sklearn.datasets import load_iris
iris = load_iris()

# store the feautre matrix (X) and response vector y

x= iris.data
y = iris.target

# store the feautre and target names
feature_names = iris.feature_names
target_names = iris.target_names

print("Feature names : ",feature_names)
print("target names : ",target_names)

print("\n Type of X is : ",type(x))

print("\n First 5 rows of x:\n",x[:5])
