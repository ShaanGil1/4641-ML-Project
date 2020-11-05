## CS 4641 - Financial Data Machine Learning Midterm Report
#### Manas Chakka, Sidhant Bhatia, Shaan Gill, Atman Patel, Thomas Napolitano

[Link to Project Proposal](https://mchakka.github.io/4641-ML-Project/)

### Introduction/Background



### Problem Definition


### Data Collection

For our data collection, we ended up using the SimFin API for data to use for analysis and machine learning. The API contained a bunch of stock and company financial data but we specifically decided to use the dataset on share prices in order to cluster stocks that move in similar patterns. The SimFin API had simple tutorials on how to extract data, and we were just able to remove columns in the dataset that were unrelated to the goal of our project and as a result, we concentrated on the data in the Open, Close, High, Low columns for our analysis. 

At least for very early analysis, we specifically chose about 10 different stocks and for each stock, we took data from the most recent 100 days. We plan to scale this up as we work on this project and possibly building out testing and training datasets. For exact implementation of our process to extract and clean data, please refer to the code in our GitHub repository.


### Methods

#### OneClassSVM - Volatility Classification

The goal of the OneClassSVM was to take aggregate stock data and determine whether a measurement from a particular day could be considered to be within normal variation or a significant value. Moreover, this data could possibly be used to be an extra indicator of stock volatility. The OneClassSVM from the sklearn was used to implement this unsupervised learning approach. 

Data from 7 stocks were used to create the model to determine if change within a day was normal or statistically significant. These stocks were chosen somewhat randomly based on the size of the companies, and further testing can be done to find more optimal training data. In order to create a uniform basis of comparison, two features were created from the original data set: normalized change and normalized price range. These features essentially removed the impact of actual stock cost and allowed for a greater emphasis on the change itself. 

A few different kernels, gamma, and nu values were evaluated in order to build the most accurate model. The preliminary analysis was validated visually at a high level in order to determine the efficacy of the approach. After building the model, a few different stocks were evaluated to see if the model managed to classify their data well.

#### SVR  - Stock Price Prediction

The SVR was intended to attempt to predict stock prices based on current open, close, high, and low prices. The prediction values for the stock price were achieved by offsetting the stock price data by a number of days in order to pair a current price with a future price. 

No manipulation other than the offset was done to the features as during this approach, a single stock was selected for analysis. This removed the need to normalize for values between stocks. However, averaging/filtering/selecting values from specific timestamps could prove beneficial to this method.



### Results

#### OneClassSVM - Volatility Classification

The data used to train the data is displayed below. From a rough visual analysis,  it is easy to tell that there is a particular point where the data becomes less clustered and from this a boundary to separate inlier and outlier points can be created.

![img](https://i.ibb.co/z2nTMDm/rawPlot.png)

![img](https://i.ibb.co/Q685z6s/train-Split.png)

After changing parameters, the above model was chosen as the final model. The inliers are colored in red whereas deviant measurements are colored in blue.



Whirlpool and GE were selected to evaluate the model. 

![img](https://i.ibb.co/GxdXnZL/WHRvolatility.png)

![https://i.ibb.co/KN4MSKc/GEvolatility.png](https://i.ibb.co/KN4MSKc/GEvolatility.png)

The results do look somewhat promising, although the model does seem to be loose in terms of classifying the normal points. There are points in the above graphs that appear as if they should be classified as outliers but they are still classified by the model as inliers. This could be adjusted by once again changing the model parameters to create for a more strict model. However, in terms of normalization and applying to companies, it seems to work well for at least mid to large size corporations. 



#### SVR - Stock Price Prediction

Two stocks (AAPL and GE) were tested using the SVR.

![img](https://i.ibb.co/Dtb1Qf0/APPL-svr.png)

![APPL2-svr](https://i.ibb.co/jRV0Xn5/APPL2-svr.png)

The results for Apple stock look decent in training and testing, but in actuality, it is a bad model that does not do well to predict the future. The predicted model simply shows a rough estimate of the real data with a delay of around 10 days. This is more apparent in the case of the GE stock as shown below.

![GE-svr](https://i.ibb.co/NnhmVSV/GE-svr.png)

![GE2-svr](https://i.ibb.co/dDqQLWJ/GE2-svr.png)

Overall the results are poor and the results really give no useful information about stock prices.



### Discussion

The stock market volatility using the OneClassSVM had promising results, especially if the parameters and training data was tuned to better determine whether fluctuations were due to random variation or possibly due to some external events. In this case the normalization of the two features used proved to be useful to create a general model that applies to stocks in the database that were not used to train. The SVR to predict stock prices was not effective and resulted in strongly overfit and useless models. Using only the open, close, high, and low values from the stock prices was not enough to obtain any discernable information to create a model. However, papers (reference the project proposal) suggested that SVMs are indeed useful in predicting stock price. The selected dataset has information from financial statements which provide more parameters which can be used to predict revenue from stocks. Between these two approaches, the approach to predict revenue or stock prices with SVM will be continued as it provides an opportunity for supervised learning. This complements the stock classification portion which takes an unsupervised approach.

