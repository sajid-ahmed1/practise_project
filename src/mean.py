from src.base import BaseModel


class MeanModel(BaseModel):
    def transform(self, X):
        return X
    
    def fit(self, X, y):
        self.mean_ = sum(y)/ len(y)    # fill this
    
    def predict(self, X):
        return [self.mean_] * len(X)
    
'''
1) MeanModel

transform = identity
fit = stores the mean of y
predict = always returns that mean
'''