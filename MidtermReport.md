## CS 4641 - Financial Data Machine Learning Midterm Report
#### Manas Chakka, Sidhant Bhatia, Shaan Gill, Atman Patel, Thomas Napolitano

[Link to Project Proposal](https://mchakka.github.io/4641-ML-Project/)

### Introduction/Background

Aggregate data is available on stock prices and company financial reports that are often used by investment firms to make decisions. With thousands of stocks being traded daily, it is impossible to use all the information manually to make informed decisions [1]. Using a machine learning approach, it is possible to better predict the relations between all stocks that are being traded and to predict market trends.

### Problem Definition

There are thousands of records of temporal stock market data that can be used to model the stock market. Due to the volatility of the stock market and real-world effects, it is difficult to create an accurate model to predict financial data. The particular issues that will be tackled in this project are tentatively: using the stock’s 100 day averages for opening and closing prices and high and low prices to create clusters and identify relationships (unsupervised learning), and to use financial report data for a future indication of stock price (supervised learning). The independent variable for this project would be the opening and closing stock prices for each company we decide to analyze and the dependent variable would be the clusters that would be created from this data. This clustering analysis can help someone diversify their portfolio and/or be more confident in their decisions when investing in stocks. 

### Data Collection

For our data collection, we ended up using the SimFin API for data to use for analysis and machine learning. The API contained a bunch of stock and company financial data but we specifically decided to use the dataset on share prices in order to cluster stocks that move in similar patterns. The SimFin API had simple tutorials on how to extract data, and we were just able to remove columns in the dataset that were unrelated to the goal of our project and as a result, we concentrated on the data in the Open, Close, High, Low columns for our analysis. 

At least for very early analysis, we specifically chose about 10 different stocks and for each stock, we took data from the most recent 100 days. We plan to scale this up as we work on this project and possibly building out testing and training datasets. For exact implementation of our process to extract and clean data, please refer to the code in our GitHub repository.


### Methods


#### KMeans - Stock Movement Clustering

For K-Means the goal was to plot each stock based off their features and any stock in the same cluster would then move in the same way.  For example, if Stock A and B are in the same cluster then if A goes up so should B.  The way this was done by taking all the stocks and compiling the data for each stock into a separate array.  We decided to average the columns and then take the difference between High/Low and Open/Close to be our new features.  We then complied that data into one array and then ran that through the K-Means algorithm (with 2 clusters).  We got the centroids locations based off that.  For exact implementations refer to the GitHub repository

#### KNN - General Stock Classification

To use the KNN method we first needed to separate our data out into labels and data.  We used the labels to be the stock itself and the data to be the values of High, Low, Open and Close. After separating out the data we split the data so that some of the data would become training data and the rest would become testing data.  We decided to split it in half, however this can easily be changed if needed.  We then ran the KNN algorithm through the data to get our predictions, using five as the number of neighbors.  We then also took out data and graphed the error based on the K value (we ran this for K values 1-40).  For exact implementations refer to the GitHub repository.


#### OneClassSVM - Volatility Classification

The goal of the OneClassSVM was to take aggregate stock data and determine whether a measurement from a particular day could be considered to be within normal variation or a significant value. Moreover, this data could possibly be used to be an extra indicator of stock volatility. The OneClassSVM from the sklearn was used to implement this unsupervised learning approach. 

Data from 7 stocks were used to create the model to determine if change within a day was normal or statistically significant. These stocks were chosen somewhat randomly based on the size of the companies, and further testing can be done to find more optimal training data. In order to create a uniform basis of comparison, two features were created from the original data set: normalized change and normalized price range. These features essentially removed the impact of actual stock cost and allowed for a greater emphasis on the change itself. 

A few different kernels, gamma, and nu values were evaluated in order to build the most accurate model. The preliminary analysis was validated visually at a high level in order to determine the efficacy of the approach. After building the model, a few different stocks were evaluated to see if the model managed to classify their data well.

#### SVR  - Stock Price Prediction

The SVR was intended to attempt to predict stock prices based on current open, close, high, and low prices. The prediction values for the stock price were achieved by offsetting the stock price data by a number of days in order to pair a current price with a future price. 

No manipulation other than the offset was done to the features as during this approach, a single stock was selected for analysis. This removed the need to normalize for values between stocks. However, averaging/filtering/selecting values from specific timestamps could prove beneficial to this method.



### Results

#### KMeans - Stock Movement Clustering

After finding the centroids, we graphed the data on a scatter plot:

![img](https://i.ibb.co/jZbnMck/Picture1.png)
 
The orange points represent the centroids, and the blue points represent the averages for the stocks.  The X-axis represents the avg (Open) – avg (Close) for each of the stocks and the Y-axis represents the avg (High) – avg (Low).  The results show only two clusters as we only currently have seven stocks currently being used.  More stocks and clusters will need to be added to make this graph show any sort of results.


#### KNN - General Stock Classification
Given our result from running the KNN algorithm we generated the confusion matrix:
![img](https://i.ibb.co/sgg35Sj/Picture2.png)
 
We then generated our classification report: 
![img](https://i.ibb.co/B4yL4ns/Picture3.png)
 
Given this, we had fairly good results, and the model was pretty accurate in finding out which stock the data belonged to.  

![img](https://i.ibb.co/4Wnt6bR/Picture4.png)
We then graphed the error and found the minimum error would be when the K-value is around 6.  Changing K to 6 instead of 5 would optimize this algorithm and minimize errors.  

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

Moving forward there are many changes we will need to account for.  One of the biggest issues we realized is the fact that KNN algorithm does not accomplish something that is in the scope of our project.  The KNN algorithm given some data would then tell us what stock that data belong to rather than telling us the movement of that stock relative to other stock.  Essentially because the labels are the name of stock that is what the algorithm will seek to find.  This is not the scope that of our project and it does not produce useful information to us, so using this algorithm will not be very useful for us.  As for K-Means, this method we think is promising and given more data will produce the results that we would want.  The idea is that if a stock is in the same cluster as another stock they will move together.  It seems that K-Means would cluster them so that this is possible.  Going forward with K-Means we need to put in more stocks so we can see more accurate clusters.  Given that we should also preform the elbow method this more data to find the optimal number of clusters. Finally, we should also change our cluster to have percentage changes in data rather than just point differences.  This is because if a big stock like Amazon loses 100 points in a day it is not as drastic of a change if a small stock loses that much.  Due to that reason we need to do percentage change to normalize the values. 
