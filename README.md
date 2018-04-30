# Titanic survivor classification challenge
Titanic classification [challenge on Kaggle](https://www.kaggle.com/c/titanic).
Given a dataset of a subset of the Titanic's passengers predict wheter they will survive or not.

## Credits
* Claudia Chianella ([@clauchian](https://github.com/clauchian))
* Yannick Giovanakis ([@yangi92](https://github.com/yangi92))
* Flavio Primo ([@flaprimo](https://github.com/flaprimo/))
* Francesco Zinnari ([@FrancescoZinnari](https://github.com/FrancescoZinnari))

## Method
Below are provided the steps that were followed for this project. Each step and classifiers have their own document.

1. **Data visualization**: data analysis to understand missing values, data relations and usefulness of features
2. **Preprocessing**: with the knowledge acquired with the preceding step, apply preprocessing of data including dealing with missing values, drop unuseful features and build new features
3. **Classifier**: build classifiers based on the preprocessed data using a variety of techniques

## Classification techniques
Classification techniques together with the relative scores.

| Classifier | Test set score | CV score | Kaggle score |
| ------ |:------:|:------:|:------:|
| *KNN* | - | - | - |
| *Logistic Regression* | - | - | - |
| *Neural Networks* | - | - | - |
| *Random Forest* | - | - | - |
| *Support Vector Machines* | 0.85 | 0.84 | 0.80861 |
| *Perceptron* | 0.78 | - | 0.62679 |
| *Naive Bayes* | 0.78 | 0.80 | 0.76076 |
| *Ensemble (RF+SVM+LR)* | - | - | - |

## Folder structures
* `\` contains all of the jupyter's notebooks including classifiers, preprocessing and data visualization
* `\Data` contains the project dataset given in the Kaggle challenge
* `\Data\output` contains the outputs given by the classifiers that were submitted to Kaggle

## Installation instructions
1. Install Python and clone this repository
2. Install required Python modules with `pip install -r requirements.txt`

to run the [jupyter](http://jupyter.org/)'s notebooks just go with `jupyter notebook`
