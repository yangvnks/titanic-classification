import matplotlib.pyplot as plt
import matplotlib 
import numpy as np
from sklearn.model_selection import learning_curve
from sklearn.model_selection import validation_curve

def plot_cv_accuracy(classifier,X_train,y_train,cv=10,n_jobs=1):
    train_sizes,train_scores,test_scores =\
                        learning_curve(estimator=classifier,
                                       X=X_train,
                                       y=y_train,
                                       train_sizes=np.linspace(0.1,1.0,10),
                                       cv=10,
                                       n_jobs=1)
    
    train_mean = np.mean(train_scores,axis=1)
    train_std = np.std(train_scores,axis=1)
    test_mean = np.mean(test_scores,axis=1)
    test_std = np.std(test_scores,axis=1)
    
    
    fig = plt.figure(figsize=(10,5))
    plt.plot(train_sizes,
             train_mean,
             color='blue',
             marker='o' ,
             markersize=5,
             label='training accuracy')
    plt.fill_between(train_sizes,
                     train_mean+train_std,
                     train_mean-train_std,
                     alpha=0.15,color='blue')
    plt.plot(train_sizes,
             test_mean,
             color='green',
             linestyle="--",
             marker='s',
             markersize=5,
             label='validation accuracy')
    plt.fill_between(train_sizes,
                     test_mean+test_std,
                     test_mean-test_std,
                     alpha=0.15,color='green')
    plt.grid()
    plt.xlabel('Number of training samples')
    plt.ylabel('Accuracy')
    plt.legend(loc='lower right')
    plt.ylim([0.6 ,1.1])
    plt.show()

def plot_cv_parameters(classifier,X_train,y_train,param, param_range,cv=10):
    train_scores,test_scores= validation_curve(estimator=classifier,
                                              X=X_train,
                                              y=y_train,
                                              param_name=param,
                                              param_range=param_range,
                                              cv=10)
    train_mean = np.mean(train_scores,axis=1)
    train_std = np.std(train_scores,axis=1)
    test_mean = np.mean(test_scores,axis=1)
    test_std = np.std(test_scores,axis=1)
    
    fig = plt.figure(figsize=(10,5))
    
    plt.plot(param_range,
             train_mean,
             color='blue',
             marker='o' ,
             markersize=5,
             label='training accuracy')
    plt.fill_between(param_range,
                     train_mean+train_std,
                     train_mean-train_std,
                     alpha=0.15,color='blue')
    plt.plot(param_range,
             test_mean,
             color='green',
             linestyle="--",
             marker='s',
             markersize=5,
             label='validation accuracy')
    plt.fill_between(param_range,
                     test_mean+test_std,
                     test_mean-test_std,
                     alpha=0.15,color='green')
    plt.grid()
    plt.xscale('log')
    plt.xlabel(param)
    plt.ylabel('Accuracy')
    plt.legend(loc='lower right')
    plt.ylim([0.6 ,1.1])
    plt.show()

def plot_feature_importance(X,importances,indices,feat_labels):
    fig = plt.figure(figsize=(10,5))
    plt.title('Feature importance')
    plt.bar(range(X.shape[1]),
             importances[indices],
             align='center')
    plt.xticks(range(X.shape[1]),
                feat_labels,
                rotation=90)
    plt.xlim([-1,X.shape[1]])
    plt.tight_layout()
    plt.show()

def train_test_separator(train_df):
    y = np.asarray(train_df['Survived'])
    X = train_df.drop(['Survived'], axis=1)
    X = np.asarray(X)
    return X,y