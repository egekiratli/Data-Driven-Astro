import numpy as np
from sklearn.tree import DecisionTreeRegressor

#Get features of the .npy data
def get_features_targets(data):
  features = np.zeros((data.shape[0], 4))
  
  features[:,0] = data['u'] - data['g']
  features[:,1] = data['g'] - data['r']
  features[:,2] = data['r'] - data['i']
  features[:,3] = data['i'] - data['z']
  
  targets = np.zeros(data.shape[0])
  targets[:] = data['redshift']
  
  return features, targets

def median_diff(predicted, actual):
  diff = np.median(np.abs(predicted-actual))
  return diff

# This function splits the data into training and testing subsets
# trains the model and returns the prediction accuracy with median_diff
def validate_model(model, features, targets):
  # split the data into training and testing features and predictions
  split = features.shape[0]//2
  train_features = features[:split]
  test_features = features[split:]
  
  train_targets = targets[:split]
  test_targets = targets[split:]

  # train the model
  model.fit(train_features, train_targets)
  # make predictions using the same features
  predictions = model.predict(test_features)
  
  # use median_diff function to calculate the accuracy
  return median_diff(test_targets, predictions)


if __name__ == "__main__":
  data = np.load('sdss_galaxy_colors.npy')
  features, targets = get_features_targets(data)

  # initialize model
  dtr = DecisionTreeRegressor()

  # validate the model and print the med_diff
  diff = validate_model(dtr, features, targets)
  print('Median difference: {:f}'.format(diff))
