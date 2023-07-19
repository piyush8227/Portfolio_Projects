

<center><h2><b>Hotel Reservation Classification Project</b></h2></center>

<br>

<a id=Section1></a>

# **1. Project Description**

 - Goal: The primary objective is to predict hotel booking cancellations to mitigate revenue loss due to unoccupied rooms.

- Data: Our dataset contains detailed information about hotel bookings, including customer specifics and whether the booking was cancelled or not.

- Model: We aim to develop a binary classification model that can predict future booking cancellations accurately.

- Business Value: This model can enable hotel management to identify potential cancellations early. The benefits include improved room occupancy rates, optimized revenue, and enhanced customer satisfaction.

### **Success Metrics**

- The success of our model will be evaluated based on its predictive performance. In particular, we will use the following metrics:

- Accuracy: This is the most intuitive performance measure. It is simply the ratio of correctly predicted observations to the total observations.

- Precision: Precision looks at the ratio of correct positive observations to the total predicted positives. It is a measure of a classifier's exactness. Low precision indicates a high number of false positives.

- Recall (Sensitivity): Recall is the ratio of correct positive observations to the all observations in actual class. It is a measure of a classifier's completeness. Low recall indicates a high number of false negatives.

- F1 Score: The F1 Score is the weighted average of Precision and Recall. This score tries to balance both precision and recall. It is suitable for uneven class distribution problems.
<br>


<a id=Section2></a>
# **2. Approach towards the problem**

- The approach to this project was to predict hotel booking cancellations to mitigate revenue loss due to unoccupied rooms.

- Initially all the necessary libraries were imported and installed, followed by reading the data and getting summary of data.

- Then while performing **preprocessing** we separated the categorical and numerical features of data. 

- We did uni-variate and bi-variate analysis of data using different graphs and charts.

- We performed features engineering and preprocessed the data.

- Then after preprocessing, we genarated train and test data to fit into the model.

- After that we build a Logistic Regression, Random Forest Model, and XGBoost.

- We recieved a validation accuracy of **95%** on train data and **88** on test data with XGBoost model.

<a id=Section3></a>
# **3. Summary**

- In this project an **Hotel Reservation Classification Project** was made from scratch.
- The Random Forest model has the highest accuracy on the training data, but it seems to be overfitting and performs worse on the test data compared to the other models.
- The XGBoost model performs slightly worse on the training data but better on the test data, indicating that it generalizes better to new data.
- The Logistic Regression model performs similarly on both the training and test data, indicating good generalization, but its overall accuracy is lower than the XGBoost model.