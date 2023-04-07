# Getting or importing the basic statistics information and separating the categorical and continuous columns functions from preprocessing.py file

from preprocessing import return_basic_statistic, separate_categorical_numerical

# Importing the necessary libraries required for the project

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector
from decouple import config

# Reading the data from the csv file

data = pd.read_csv("D:\Lu_Git_Demo\mysql-python-tableau\Data source\Bank Customer Churn Prediction.csv", encoding_errors="ignore")

# Printing the statistical information of the data

print(return_basic_statistic(data))

# Separating the categorical and continuous columns

categorical_cols, continuous_cols = separate_categorical_numerical(data)

# Printing the categorical and continuous columns

print("The categorical columns are: ",categorical_cols)
print("The countinous columns are: ",continuous_cols)

# Establishing the connection with the database

mydb = mysql.connector.connect(host=config("HOST"),
                               user = config("user"),
                               port = 3306,
                               database = "banking",
                               password = config("password"))

print("The database has been successfully connected")
print("The instance is: ",mydb)
mycursor = mydb.cursor()

# Inserting the data into our database and counting total records inserted in db.

data_counter = 0
columns_list = data.columns
for customer_id,credit_score,country,gender,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,churn in zip(data['customer_id'],data['credit_score'],data['country'],data['gender'],data['age'],data['tenure'],data['balance'],data['products_number'],data['credit_card'],data['active_member'],data['estimated_salary'],data['churn']):
    sql = "INSERT INTO banking_customer_churn (customer_id,credit_score,country,gender,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,churn) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
    val = (customer_id,credit_score,country,gender,age,tenure,balance,products_number,credit_card,active_member,estimated_salary,churn)
    mycursor.execute(sql, val)
    mydb.commit()
    data_counter += 1
    print(mycursor.rowcount, "record inserted.")
print("Total data inserted: ",data_counter)