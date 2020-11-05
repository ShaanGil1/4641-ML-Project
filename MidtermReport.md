## CS 4641 - Financial Data Machine Learning Midterm Report
#### Manas Chakka, Sidhant Bhatia, Shaan Gill, Atman Patel, Thomas Napolitano

[Link to Project Proposal](https://mchakka.github.io/4641-ML-Project/)

### Introduction/Background

Aggregate data is available on stock prices and company financial reports that are often used by investment firms to make decisions. With thousands of stocks being traded daily, it is impossible to use all the information manually to make informed decisions [1]. Using a machine learning approach, it is possible to better predict the relations between all stocks that are being traded and to predict market trends.

### Problem Definition

There are thousands of records of temporal stock market data that can be used to model the stock market. Due to the volatility of the stock market and real-world effects, it is difficult to create an accurate model to predict financial data. The particular issues that will be tackled in this project are tentatively: using temporal stock market data to identify clusters and identify relationships between clusters (unsupervised learning), and to use financial report data for an indication of stock price (supervised learning).

### Data Collection

For our data collection, we ended up using the SimFin API for data to use for analysis and machine learning. The API contained a bunch of stock and company financial data but we specifically decided to use the dataset on share prices in order to cluster stocks that move in similar patterns. The SimFin API had simple tutorials on how to extract data, and we were just able to remove columns in the dataset that were unrelated to the goal of our project and as a result, we concentrated on the data in the Open, Close, High, Low columns for our analysis. 

At least for very early analysis, we specifically chose about 10 different stocks and for each stock, we took data from the most recent 100 days. For exact implementation of our process to extract and clean data, please refer to the code in our GitHub repository. 


### Results

With the two goals of the project, the first is to cluster stock data that moves similarly. This can be used to predict how changes in a single cluster can affect another. For example, if cluster A and cluster B have a negative correlation, if cluster A’s value increases, then it can serve as an indicator that cluster B’s value will decrease. The other aspect is to predict stock price using financial reports. More research needs to be done on the financial aspect to determine how a company’s stock price can be estimated from its stock report. These results will allow for better financial portfolio management, and give better insight into stock investment [7].

### Discussion

A lot of the initial time investment will go into researching financial indicators and determining a good financial data set, many of which are readily found online. After developing the preliminary financial knowledge, the data can be feature extracted to use with machine learning techniques. The project checkpoint will be to ensure that the extracted features can be input into ML learning algorithms to determine preliminary results. After this point, pre-processing and different techniques can be applied to generate a more accurate model. For evaluation, it will be worthwhile to perform a holistic overview of the market to determine what external factors could have affected the accuracy of the model.

### References
[1] Didur, K. (2018, July 11). Machine learning in finance: Why, what & how. https://towardsdatascience.com/machine-learning-in-finance-why-what-how-d524a2357b56. \
[2] Lv, D., Yuan, S., Li, M., & Xiang, Y. (2019, April 14). An Empirical Study of Machine Learning Algorithms for Stock Daily Trading Strategy. https://www.hindawi.com/journals/mpe/2019/7816154/. \
[3] Chen, J. (2010). SVM application of financial time series forecasting using empirical technical indicators. https://ieeexplore.ieee.org/abstract/document/5636430. \
[4] Tay, F. E. H., & Cao, L. (2001, June 28). Application of support vector machines in financial time series forecasting. Omega. https://www.sciencedirect.com/science/article/pii/S0305048301000263. \
[5] Zhang, J., Cui, S., Xu, Y., Li, Q., & Li, T. (2017, December 13). A novel data-driven stock price trend prediction system. Expert Systems with Applications.https://www.sciencedirect.com/science/article/pii/S0957417417308485. \
[6] Patel, J., Shah, S., Thakkar, P., & Kotecha, K. (2014, August 5). Predicting stock and stock price index movement using Trend Deterministic Data Preparation and machine learning techniques. Expert Systems with Applications.https://www.sciencedirect.com/science/article/pii/S0957417414004473. \
[7] Huang, J., Chai, J. & Cho, S. Deep learning in finance and banking: A literature review and classification. Front. Bus. Res. China 14, 13 (2020). https://doi.org/10.1186/s11782-020-00082-6 \
