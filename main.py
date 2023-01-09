import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import warnings
#import pickle5 as pickle
import joblib
warnings.filterwarnings("ignore")

df = pd.read_csv("concrete.csv")
shuffle_df = df.sample(frac=1)
train_size = int(0.80*len(df))

train_set = shuffle_df[:train_size]
test_set  = shuffle_df[train_size:]

X_train = np.array(train_set[["cement", "slag", "ash", "water", "superplastic", "coarseagg", "fineagg", "age"]])

Y_train = np.array(train_set[["strength"]])
X_test = np.array(test_set[["cement", "slag", "ash", "water", "superplastic", "coarseagg", "fineagg", "age"]])
Y_test = np.array(test_set[["strength"]])

rfr = RandomForestRegressor()
rfr.fit(X_train, Y_train)

#pickle.dump(rfr,open('model.pkl','wb'))

#> from joblib import dump, load
joblib.dump(rfr,'model.joblib') 