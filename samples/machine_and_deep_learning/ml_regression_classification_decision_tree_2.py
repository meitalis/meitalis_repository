# Ex 300 - entropy
import pandas as pd
import numpy as np

def compute_entropy(data):
    yes_count = sum(map(lambda x: x == 'yes', data))
    no_count = sum(map(lambda x: x == 'no', data))

    if (no_count != 0 and yes_count != 0):
        yes_ratio = yes_count / (yes_count + no_count)
        no_ratio = no_count / (yes_count + no_count)

        return ((- (yes_ratio) * np.log2(yes_ratio)) - ((no_ratio) * np.log2(no_ratio)))
    else:
        return 0

#x_feature = (X[feature]
def compute_feature_entropy(x_feature,y):
  uniques, indexes, counts = np.unique(x_feature, return_counts=True, return_index=True)
  # print('feature',feature,'uniques', uniques,'counts',counts)

  feature_entropy = 0
  for value in uniques:
      idx_values = x_feature.index[x_feature == value].tolist()
      y = y[idx_values]
      feature_entropy += compute_entropy(y[idx_values]) * (y.shape[0] / x_feature.size )


def best_feature_entropy(X,y):
    entropies = []
    for feature in X.columns:
        feature_entropy = compute_feature_entropy(X[feature],y)
        entropies.append(feature_entropy)

    entropy_min = np.argmin(entropies)
    print('entropies find min', entropy_min)

    return X.columns[entropy_min]

def build_tree(X,y):
    best_feature = best_feature_entropy(X,y)
    uniques, indexes, counts = np.unique(X[best_feature], return_counts=True, return_index=True)
    # print('feature_max',feature_max,'uniques', uniques,'counts',counts)
    for value in uniques:
        idx_values = X[best_feature].index[X[best_feature] == value].tolist()
        y = y[idx_values]

        yes_count = sum(map(lambda x: x == 'yes', y))
        no_count = sum(map(lambda x: x == 'no', y))
        # print('value',value,'idx_values',idx_values,'yes_count',yes_count,'no_count',no_count)
        if (yes_count == 0):
            print('best_feature', best_feature, 'value', value, '[NO]')
        if (no_count == 0):
            print('best_feature', best_feature, 'value', value, '[YES]')
        else:
            build_tree(X.drop(best_feature, axis=1),y)


d = {'outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny',
                 'Overcast', 'Overcast', 'Rain'],
     'temp': ['hot', 'hot', 'hot', 'm', 'c', 'c', 'c', 'm', 'c', 'm', 'm', 'm', 'hot', 'm'],
     'humidity': ['High', 'High', 'High', 'High', 'Nomral', 'Nomral', 'Nomral', 'High', 'Nomral', 'Nomral', 'Nomral',
                  'High', 'Nomral', 'High'],
     'wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong',
              'Weak', 'Strong'],
     'play': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']}
df = pd.DataFrame(d)

X = df.drop('play', axis=1)
y = df.play

print('************* ROOT *************')
build_tree(X, y)

