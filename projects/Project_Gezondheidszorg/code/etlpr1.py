

"""
Imports data from database
ETL on Data
Creates 4 databases: 1 bigger with outliers, 1 smaller with outliers, 
1 bigger without outliers, 1 smaller without outliers
"""

# Installing libraries
import logging
import sqlite3
import pandas as pd

#logging info
logging.basicConfig(level = logging.DEBUG)


# LOG LEVELS
# DEBUG		Detailed information, useful during bugfixing
# INFO		Just enough information to be able to understand the flow
# WARNING	Information about unexpected conditions that might be solved later
# ERROR		Reporting that the program can perform some task
# CRITICAL	Reporting that the program can not continue

# Global variables
DBPATH = "../database"

# Collecting the data
# Specify the con
con = sqlite3.connect(f'{DBPATH}/db.sqlite3')

# Convert to DataFrame (first df)
lsd = pd.read_sql('SELECT * FROM rest_api_netlify', con=con)

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
lsd.dropna()

# create bmi column
lsd['bmi'] = round(lsd['mass']/((lsd['length']**2)*0.0001))

# create second df (includes outliers) and without mass and length
lsd_light = lsd.drop(["length","mass"], axis='columns')

# create third df without outliers (including length and mass)
Q1 = lsd.quantile(0.25)
Q3 = lsd.quantile(0.75)
IQR = Q3 - Q1

lsd_no_outl = lsd[~((lsd < (Q1 - 1.5 * IQR)) |(lsd > (Q3 + 1.5 * IQR))).any(axis=1)]

# create fourth df (outliers excluded, length and mass excluded)

lsd_light_no_outl = lsd_no_outl.drop(["length","mass"], axis='columns')

# Save dfs as new table
lsd.to_sql('dblsd', con=con, index=False)
lsd_light.to_sql('dblsd_light', con=con, index=False)
lsd_no_outl.to_sql('dblsd_no_outl', con=con, index=False)
lsd_light_no_outl.to_sql('dblsd_light_no_outl', con=con, index=False)

logging.info("Logging to file..")

# close Connection
con.close()
