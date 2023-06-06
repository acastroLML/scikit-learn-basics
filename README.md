# scikit-learn-basics

1. kmeans (ex1 y ex2)  
2. GMM   
3. Logistic regression
4. Dimensionality Reduction  
5. Linear Regression  


## Supervised Learning

Is when the model is getting trained on a labelled dataset. A labelled dataset is one that has both input (input features, predictors) and output parameters (output labels)

data: training(80%), validation(20%)

Supervised learning is typically divided into two main categories: regression and classification. In regression, the algorithm learns to predict a continuous output value, such as the price of a house or the temperature of a city. In classification, the algorithm learns to predict a categorical output variable or class label, such as whether a customer is likely to purchase a product or not.

### Regression 

In regression, the target variable is a continuous value. The goal of regression is to predict the value of the target variable based on the input variables. **Linear regression, polynomial regression, and decision trees** are some of the examples of regression algorithms.

- Linear Regression
- Polynomial Regression
- Stepwise regression
- Decision tree Regression
- Random Forest Regression
- Support vector Regression
- Ridge Regression
- ElasticNet Regression
- Bayesian Linear Regression 

- Lasso Regression
- Ridge Regression
- XGBoots Regressor
- LGBM Regressor

Evaluation Metrics:
- Mean Square Error
- R2-score 
- MAPE 



### Classification

In classification, the target variable is a categorical value. The goal of classification is to predict the class or category of the target variable based on the input variables. Some examples of classification algorithms include **logistic regression, decision trees, support vector machines, and neural networks**.

- Desicion Tree  
- Random Forest Classifier
- K-Nearest Neighbors
- Support vector Machine
- Logistic Regression  
- Single Layer Perceptron 
- Stochastic Gradient Descent SGD classifier
- Naive Bayes 
- AdaBoots  
- Bagging Classifier  
- Multi-layer Artificial Neural Networks

Evaluation Metrics / Model evaluations:
- **Clasification Accuracy**: The proportion of correctly classified instances.
- **Precision**:  (true positives)/(predicted positives)
- **Recall**: (true positives)/(total number of actual positives)
- **F1-score**: metrica cuando precision y recall are important -- 2 x (precision x recall) / (precision + recall).
- **ROC**: Receiver Operating Characteristic. ROC is a plot of the true positive rate (recall) against the false positive rate (1-specificity) for different threshold values of the classifier’s decision function.
- **AUC**: measures the overall performance of the classifier, with values ranging from 0.5 (random guessing) to 1 (perfect classification).
- **Confusion matrix**: A table that shows the number of true positives, true negatives, false positives, and false negatives for each class, which can be used to calculate various evaluation metrics.
- **Cross Validation**: A technique that divides the data into multiple folds and trains the model on each fold while testing on the others, to obtain a more robust estimate of the model’s performance



## Unsupervised Learning

## Semi-supervised Learning


## Reinforcement Learning
