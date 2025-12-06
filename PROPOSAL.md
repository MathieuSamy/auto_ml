Below is the email I sent to our TA, Anna Smirnova, as the proposal for my capstone project: Predicting Short-Term Excess Returns in the Car Industry. 

Hi Anna,

I hope you’re doing well. I wanted to briefly present my capstone project idea for the Data Science and Advanced Programming course.

My project focuses on predicting short-term excess returns in the car industry using publicly available financial data from Yahoo Finance. Specifically, I’m collecting daily price data for a selection of major automotive companies (e.g., Tesla, Ford, GM, Toyota, BMW, Renault, Honda, Stellantis) along with a benchmark (CARZ ETF or an equal-weighted index).

After cleaning and preprocessing the data, I’ll compute several time-series–based features such as:
short-, medium-, and long-term momentum (5, 20, 60-day returns), realized volatility (20-day standard deviation of returns), price-to-moving-average ratio (Price/MA20), and the 14-day RSI (Relative Strength Index).

The goal is to train regression models, starting with Ridge Regression and then Random Forest, to predict whether a stock will outperform or underperform the benchmark over a 5-day horizon. The predicted variable will be the future excess return, defined as the stock’s forward log-return minus the benchmark’s over the same period.

Model performance will be evaluated using MSE, MAE, and R², as well as the Information Coefficient to measure the correlation between predicted and realized excess returns. I also plan to backtest a simple Top-K long strategy based on the model’s forecasts and visualize the resulting equity curve.
This topic allows me to combine the key components of the course such as data processing, feature engineering, regression modeling, and evaluation metrics, while linking them to my finance background and interests.

Here is the link to my GitHub repository where I’ve already implemented the first version of the code and project structure: https://github.com/MathieuSamy/DS-AP-Capstone-Project.git

Please let me know if this approach sounds appropriate, or if you would recommend any adjustments to the data sources, model design, or evaluation metrics.

Thank you very much for your time and feedback!

Best regards,
Mathieu Samy