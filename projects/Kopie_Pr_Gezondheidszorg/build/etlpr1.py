"""
Imports data from database
ETL on Data
Creates 4 databases: 1 bigger with outliers, 1 smaller with outliers, 
1 bigger without outliers, 1 smaller without outliers

"""

# Installing libraries
import logging
import sqlite3
#import math
import pickle
#import numpy as np
import pandas as pd
from sklearn import linear_model
#from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

#logging info
logging.basicConfig(level = logging.INFO)

# LOG LEVELS
# DEBUG		Detailed information, useful during bugfixing
# INFO		Just enough information to be able to understand the flow
# WARNING	Information about unexpected conditions that might be solved later
# ERROR		Reporting that the program can perform some task
# CRITICAL	Reporting that the program can not continue

# Global variables
DBPATH = ".."

# Collecting the data
# Specify the con
con = sqlite3.connect('db.sqlite3')

# Convert to DataFrame (first df)
# lsd = pd.read_sql('SELECT * FROM rest_api_netlify', con=con)
lsd = pd.read_sql_query(f"SELECT * FROM {'rest_api_netlify'}", con)

# TRANSFORM
# make sure that all values (and therefore columns) are numeric
for n in lsd.keys():
    lsd[n] = pd.to_numeric(lsd[n], errors='coerce')

# remove duplicate rows, if there are any:
lsd = lsd.drop_duplicates().copy()

# remove any negative values from df
negvals = lsd[(lsd < 0).any(axis=1)]
indexnegvals = lsd[(lsd < 0).any(axis=1)].index
lsd = lsd.drop(indexnegvals).copy() # drop the rows

# drop NaN values
lsd = lsd.dropna()

# create bmi column
lsd['bmi'] = round(lsd['mass']/((lsd['length']**2)*0.0001))

# create second df (includes outliers) and without mass and length
lsd_light = lsd.drop(["length","mass"], axis='columns')

# create third df without outliers (including length and mass)
Q1 = lsd.quantile(0.25)
Q3 = lsd.quantile(0.75)
IQR = Q3 - Q1

lsd_no_outl = lsd[~((lsd < (Q1 - 1.5 * IQR)) |\
(lsd > (Q3 + 1.5 * IQR))).any(axis=1)]

# create fourth df (outliers excluded, length and mass excluded)

lsd_light_no_outl = lsd_no_outl.drop(["length","mass"], axis='columns')

# Save dfs as new table
lsd.to_sql('dblsd', con=con, index=False, if_exists='replace')
lsd_light.to_sql('dblsd_light', con=con, index=False, if_exists='replace')
lsd_no_outl.to_sql('dblsd_no_outl', con=con, index=False, if_exists='replace')
lsd_light_no_outl.to_sql('dblsd_light_no_outl', con=con, index=False, if_exists='replace')

logging.info("Logging to file..")

# close Connection
con.close()


# Define X, y in LinearRegr model & create train_test_split
y = lsd_no_outl.lifespan.values
X = lsd_no_outl[['genetic','length','mass','exercise','smoking','alcohol','sugar','bmi']].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create linear regression class object
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)

# Getraind model wegschrijven
with open("reg.pkl", "wb") as f:
    pickle.dump(reg, f)
