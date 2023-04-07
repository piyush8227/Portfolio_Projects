def return_basic_statistic(data):
  print("The shape of data is: ", data.shape)
  print("*"*50)
  print("\n")
  print("The head of the data is :", data.head())
  print("*"*50)
  print("\n")
  print("The tail of the data is :", data.tail())
  print("*"*50)
  print("\n")
  print("The null counts of the data is :", data.isnull().sum())
  print("*"*50)
  print("\n")
  print("The info of the data is :", data.info())
  print("*"*50)
  print("\n")
  print("The description of the data is :", data.describe())


def separate_categorical_numerical(data):
  categorical_cols, continuous_cols = [], []
  for column in data.columns:
    if data[column].dtypes == 'object':
      categorical_cols.append(column)
    else:
      continuous_cols.append(column)
  return categorical_cols, continuous_cols