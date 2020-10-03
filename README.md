## CS 4641 - Financial Data Machine Learning Project Proposal

You can use the [editor on GitHub](https://github.com/mchakka/4641-ML-Project/edit/main/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Introduction/Background

Aggregate data is available on stock prices and company financial reports that are often used by investment firms to make decisions. With thousands of stocks being traded daily, it is impossible to use all the information manually to make informed decisions [1]. Using a machine learning approach, it is possible to better predict the relations between all stocks that are being traded and to predict market trends.

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[https://youtu.be/WorlYZWGzrU](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Problem Definition

There are thousands of records of temporal stock market data that can be used to model the stock market. Due to the volatility of the stock market and real-world effects, it is difficult to create an accurate model to predict financial data. The particular issues that will be tackled in this project are tentatively: using temporal stock market data to identify clusters and identify relationships between clusters (unsupervised learning), and to use financial report data for an indication of stock price (supervised learning).

### Methods

The overall process is divided into data acquisition, preparation, machine learning, and evaluation [2]. Before beginning any machine learning itself, potential datasets and features must be identified of interest to use in machine learning. SVMs have proven to be successful in previous endeavors [3] [4] for market prediction and will be used in the project. Random forests will also be used for prediction [5] to compare the two machine learning approaches. Pre-processing the data is crucial to achieving more accurate results [6], so data will be averaged, filtered, and manipulated to extract robust features to help predict overall market trends rather than fixate on transient fluctuations.

### Potential Results

With the two goals of the project, the first is to cluster stock data that moves similarly. This can be used to predict how changes in a single cluster can affect another. For example, if cluster A and cluster B have a negative correlation, if cluster A’s value increases, then it can serve as an indicator that cluster B’s value will decrease. The other aspect is to predict stock price using financial reports. More research needs to be done on the financial aspect to determine how a company’s stock price can be estimated from its stock report. These results will allow for better financial portfolio management, and give better insight into stock investment [7].

### Discussion

A lot of the initial time investment will go into researching financial indicators and determining a good financial data set, many of which are readily found online. After developing the preliminary financial knowledge, the data can be feature extracted to use with machine learning techniques. The project checkpoint will be to ensure that the extracted features can be input into ML learning algorithms to determine preliminary results. After this point, pre-processing and different techniques can be applied to generate a more accurate model. For evaluation, it will be worthwhile to perform a holistic overview of the market to determine what external factors could have affected the accuracy of the model.
