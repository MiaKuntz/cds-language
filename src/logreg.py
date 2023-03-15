# system tools
import os
# data munging tools
import pandas as pd
# machine learning stuff
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
# visualisation
import matplotlib.pyplot as plt

# defining load data and train test split function
def load_data():
    # load data
    filename = os.path.join("..",
                            "data",
                            "fake_or_real_news.csv")
    # load into dataframe
    data = pd.read_csv(filename, index_col=0)
    # get text and labels
    X = data["text"]
    y = data["label"]
    # train test split
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=42)
    return X_train, X_test, y_train, y_test

# defining vectorizing function
def doc_vectorizer(training_data, test_data):
    # vectorizer
    vectorizer = CountVectorizer(ngram_range = (1,2),
                                lowercase =  True,  
                                max_df = 0.95,    
                                min_df = 0.05,    
                                max_features = 100)  
    # first we fit to the training data... 
    X_train_feats = vectorizer.fit_transform(training_data)
    #... then do it for our test data
    X_test_feats = vectorizer.transform(test_data)
    return X_train_feats, X_test_feats

# definig the logistic regression model
def lr_model(training_features, test_features, training_labels):
    # initialize the classifier
    classifier = LogisticRegression(random_state=42).fit(training_features, training_labels)
    # making predictions using the classifier
    y_pred = classifier.predict(test_features)
    return y_pred

# creating the main function
def main():
    # load the data
    X_train, X_test, y_train, y_test = load_data()
    # vectorize the docs
    X_train_feats, X_test_feats = doc_vectorizer(X_train, X_test)
    # run classifier
    y_pred = lr_model(X_train_feats, X_test_feats, y_train)
    # print metrics
    classifier_metrics = metrics.classification_report(y_test, y_pred)
    print(classifier_metrics)

if __name__=="__main__":
    main()
