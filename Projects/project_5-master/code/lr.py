import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV,train_test_split

np.random.seed(42)

final_csv = pd.read_csv('../data/ready_for_modeling.csv')


print(final_csv.shape)
print(final_csv.columns)

X=final_csv['tweet']
y=final_csv['label']

X_train,X_test,y_train,y_test = train_test_split(X, y, random_state=42, stratify = y)


pipe_cvec_lr = Pipeline([
    ('cvec' , CountVectorizer()),
    ('lr' , LogisticRegression(max_iter=10_000))
])

pipe_cvec_params = {
    'cvec__max_features': [2_000, 4_000],
    'cvec__stop_words': [None, 'english'],
    'cvec__ngram_range': [(1,1), (2,2)]
}

gs_cvec_lr = GridSearchCV(pipe_cvec_lr,
                         param_grid=pipe_cvec_params,
                         cv=5)

gs_cvec_lr.fit(X_train,y_train)

print(f'log_reg train score {gs_cvec_lr.score(X_train,y_train)}')
print(f'log_reg test score {gs_cvec_lr.score(X_test,y_test)}')
