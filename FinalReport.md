## CS 4641 - Financial Data Machine Learning Final Report
#### Manas Chakka, Sidhant Bhatia, Shaan Gill, Atman Patel, Thomas Napolitano

[Link to Project Proposal](https://mchakka.github.io/4641-ML-Project/)

[Link to Midterm Report](https://mchakka.github.io/4641-ML-Project/MidtermReport)

[Link to Final Report Presentation Video](https://mchakka.github.io/4641-ML-Project/)

### Introduction/Background

Aggregate data is available on stock prices and company financial reports that are often used by investment firms to make decisions. With thousands of stocks being traded daily, it is impossible to use all the information manually to make informed decisions [1]. Using a machine learning approach, it is possible to better predict the relations between all stocks that are being traded and to predict market trends.

### Problem Definition

There are thousands of records of temporal stock market data that can be used to model the stock market. Due to the volatility of the stock market and real-world effects, it is difficult to create an accurate model to predict financial data. The particular issues that will be tackled in this project are tentatively: using the stock’s 100 day averages for opening and closing prices and high and low prices to create clusters and identify relationships (unsupervised learning), and to use financial report data for a future indication of stock price (supervised learning). The independent variable for this project would be the opening and closing stock prices for each company we decide to analyze and the dependent variable would be the clusters that would be created from this data. This clustering analysis can help someone diversify their portfolio and/or be more confident in their decisions when investing in stocks. 

### Data Collection

For our data collection, we ended up using the SimFin API for data to use for analysis and machine learning. The API contained a bunch of stock and company financial data but we specifically decided to use the dataset on share prices in order to cluster stocks that move in similar patterns. The SimFin API had simple tutorials on how to extract data, and we were just able to remove columns in the dataset that were unrelated to the goal of our project. Most of our project is focused on data in the **Share Prices Dataset** but our SVR part uses **Income and Balance Sheet Datasets** and that's discussed in the SVR Methods section. 

Here's an metadata overview of the Share Prices Dataset
![original-data](https://i.ibb.co/BCBxCjr/metadata.png)

Here's an sample section of the dataset as well in CSV format
![sample-data](https://i.ibb.co/VpnFVN5/sample.png)

At least for very early analysis, we specifically chose about 10 different stocks and for each stock, we took data from the most recent 100 days. As we progressed in the project, we ended up using about 100 stock tickers for analysis, specifically for KMeans, KNN, and OneClassSVM. However as we scaled up our data that we used for this project, we had to clean the dataset. This included removing rows that had any NaNs, removing unnecessary columns, and etc. 

Our project specifically focused on the High, Low, Open, and Close columns of the dataset. The next section will go in-depth on how each of these columns were used and in our analysis. For exact implementation of our process to extract and clean data, please refer to the code in our GitHub repository.


### Methods


#### KMeans - Stock Movement Clustering

For K-Means the goal was to plot each stock based on their features and any stock in the same cluster would then move in the same way.  For example, if Stock A and B are in the same cluster then if A goes up so should B.  The way this was done by taking all the stocks and compiling the data for each stock into a separate array.  We decided to average the columns and then take the percentage change between High/Low and Open/Close to be our new features.  We then compiled that data into one array and then ran the elbow method to find the ideal number of clusters.  We then ran the K-Means algorithm will the ideal number of clusters.  We got the centroids locations based on that.  For exact implementations refer to the GitHub repository.

#### KNN - General Stock Classification

To use the KNN method we first needed to separate our data out into labels and data.  We used the labels to be the stock itself and the data to be the values of High, Low, Open and Close. After separating out the data we split the data so that some of the data would become training data and the rest would become testing data.  We decided to split it in half, however this can easily be changed if needed.  We then also took out data and graphed the error based on the K value (we ran this for K values 1-40).  We then ran the KNN algorithm through the data to get our predictions, using number found to have the least error as the number of neighbors.  For exact implementations refer to the GitHub repository.

#### OneClassSVM - Volatility Classification

The goal of the OneClassSVM was to take aggregate stock data and determine whether a measurement from a particular day could be considered to be within normal variation or a significant value. Moreover, this data could possibly be used to be an extra indicator of stock volatility. The OneClassSVM from the sklearn was used to implement this unsupervised learning approach.

Data from 7 stocks were used to create the model to determine if change within a day was normal or statistically significant. These stocks were chosen somewhat randomly based on the size of the companies, and further testing can be done to find more optimal training data. In order to create a uniform basis of comparison, two features were created from the original data set: normalized change and normalized price range. These features essentially removed the impact of actual stock cost and allowed for a greater emphasis on the change itself.

A few different kernels, gamma, and nu values were evaluated in order to build the most accurate model. The preliminary analysis was validated visually at a high level in order to determine the efficacy of the approach. After building the model, a few different stocks were evaluated to see if the model managed to classify their data well.

#### SVR  - Stock Price Prediction

The SVR was intended to attempt to predict stock prices based on current open, close, high, and low prices. The prediction values for the stock price were achieved by offsetting the stock price data by a number of days in order to pair a current price with a future price. 

No manipulation other than the offset was done to the features as during this approach, a single stock was selected for analysis. This removed the need to normalize for values between stocks. Even after manipulation such as filtering/averaging/rolling average, there simply was not enough data and features present to make a meaningful prediction.

_Using Financial Data_

Using the SimFin API, it was also possible to calculate financial indications, growth signals, and valuation signals from the income and balance sheets of the company. (More information can be found about these financial factors, but they are not too relevant to understand other than the fact that they exist for the purposes of this project.) The API provided functions to calculate these and interpolate them on a daily bases based on share prices. Using this method allowed for more features to be used in predicting the stocks. However, rather than predicting the stock prices themselves, it would predict the mean-log revenue of 1-3 years. This essentially means that within 1-3 years of purchasing the stock the mean-log revenue was the percent of money you could make (or lose) from you current investment depending on the time. Since the number of features went from a few to over 40, more data cleaning needed to be done for the larger dataset.

![original-data](https://i.ibb.co/MgfV3jW/original-data.png)

The original data looked like the above image. Many calculated values were NaN and the DataFrame had 46 columns. Many of those columns were riddled with Nan values. To clean the data, columns with less than 90% completeness were removed. This resulted in a total of 26 remaining columns. All rows that had NaN values were removed because that would later cause issues in the machine learning. Finally, the stock data was filtered so only companies that had been present for 3 years were used in the final analysis. This was to ensure that there weren't too many young/volatile companies being used to train and test the model. A lot of the process was referenced from the SimFin API tutorials.

After the cleaning process, around 1.2 million data values remained. There was an attempt to insert them into the SVR and perform the machine learning, but the time it took was astronomical and the results did not finish even after running the model training overnight. Thus a random subset of 100 companies were used to create the model. Afterwards, the training data was plotted against the predicted data, and test data was also plotted against the actual data. These were done on a company by company basis. Parameters were also changed along the process to determine which features and what type of parameters to use in the modeling process.


### Results

#### KMeans - Stock Movement Clustering

Running the Elbow method:
![img](https://i.ibb.co/z4x73g9/elbow-Method.png)

After finding the centroids, we graphed the data on a scatter plot:
![img](https://i.ibb.co/rQjS7cG/scatter-Plot.png)
 
The orange points represent the centroids, and the blue points represent the averages for the stocks.  The X-axis represents the avg (Close) – avg (Open)/ avg (Open) for each of the stocks and the Y-axis represents the avg (High) – avg (Low)/ avg (Low).  The results show that there are 3 clusters indicated by the orange points.  A lot of the data is centralized showing that majority of stocks would move in the same way.  

#### KNN - General Stock Classification

![img](https://i.ibb.co/bQN44qP/KNNError.png)
We then graphed the error and found the minimum error would be when the K-value is around 12, so we should use 12 to minimize error.

Given our result from running the KNN algorithm we generated the confusion matrix:
![img](https://i.ibb.co/ZK8cd5K/Confusion-Matrix.png)
 
We then generated our classification report: 
![img](https://i.ibb.co/hVF5rZm/Classification-Report.png)
 
Given this, we had bad results and the accuracy was fairly poor.

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

#### SVR - Log Return Prediction

###### Training vs Predicted

Three stocks from the training data were plotted against their predicted mean log return values: PG, KMI, and HP.

![train-PG](https://i.ibb.co/rFfFvL6/train-PG.png)
![train-KMI](https://i.ibb.co/ctyVYCP/train-KMI.png)
![train-HP](https://i.ibb.co/hfBCXhX/train-HP.png)

These three results show how varied the results are in the training data itself.



###### Testing vs Predicted

Four stocks (AAPL, MSFT, TJX, GE) that were not part of the training set were also plotted against the model's predicted values.

![TEST-AAPL](https://i.ibb.co/z8NcDKh/TEST-AAPL.png)
![test-MSFT](https://i.ibb.co/M2zMYjM/test-MSFT.png)
![test-TJX](https://i.ibb.co/428q5Sj/test-TJX.png)
![test-GE](https://i.ibb.co/h8DfkZ9/test-GE.png)

None of the predictions are particularly close the the actual calculated returns.



### Discussion

Although KNN was not in the scope of our project we just decided to run it so see the results on a large amount of data and found that it did very poorly in comparison to large data set, it could not accurately predict the stocks at all likely due to the high number of stocks in the first place.  However, running KNN did provide some insights to what issues were produced from our K-Means.  When running K-Means we got the ideal number of clusters to be 3.  This is due to the high volume of data that was clumped near the center which made for one very large cluster in the center and 2 other clusters that were further out.  Clearly some of our data is too similar which is also why KNN has difficulties predicting with it. However, something to consider is a lot of stocks do follow the same trends which does give some hope on what our model produced to be somewhat accurate.  A lot of stocks tend to do the same thing depending on the overall market which makes sense why there also so many that are together.  I think overall it produced a model that seemed to be at least somewhat accurate to what we wanted to do.  Points that are in the same cluster should move together which is the aim of using this algorithm. We have considered something we could do to potentially make this better, one would be to check the results with some test data and actually check if some stock in a cluster goes up how much of the other things the clusters follow that trend.  Another thing would be to use a different metric to plot.  Since we used the average % change in the open/close and the high/low it made so that our data was centralized around the one big cluster.  This is because taking the mean over a long time in a stock market would more about the overall market rather than that stock.  So as a fix we could maybe consider individual days more rather than averaging days so that the data is more spread out and could give more accurate results.

The stock market volatility using the OneClassSVM had promising results, especially if the parameters and training data was tuned to better determine whether fluctuations were due to random variation or possibly due to some external events. In this case the normalization of the two features used proved to be useful to create a general model that applies to stocks in the database that were not used to train. The SVR to predict stock prices was not effective and resulted in strongly overfit and useless models. Using only the open, close, high, and low values from the stock prices was not enough to obtain any discernable information to create a model. However, papers (reference the project proposal) suggested that SVMs are indeed useful in predicting stock price. The selected dataset has information from financial statements which provide more parameters which can be used to predict revenue from stocks. Between these two approaches, the approach to predict revenue or stock prices with SVM will be continued as it provides an opportunity for supervised learning. This complements the stock classification portion which takes an unsupervised approach.

### Conclusion
In conclusion, using the aggregate data available on stock prices and company financial reports, specifically the opening/closing stock prices and high/low prices, we were able to use machine learning techniques to better predict relations between different stocks and predict some market trends. The different techniques we used in our process were KMeans, KNN, OneClassSVM, and SVR. Using KMeans, we were able to get centroid locations by plotting each stock based off their features. Using KNN, 
Using OneClassSVM, we were able to take the stock data and determine whether a measurement from a particular day could be considered to be within normal variation or a significant value. Finally using SVR, we were able to show our predictions for stock prices based on the selected data we decided to use. 
