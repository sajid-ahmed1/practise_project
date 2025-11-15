from src.base import BaseModel


class MaxModel(BaseModel):
    def transform(self, X):
        return X
    
    def fit(self, X, y):
        self.max_ =   max(y)   # fill this
    
    def predict(self, X):
        return [self.max_] * len(X)
    

'''
2) MaxModel

transform = identity
fit = stores max of y
predict = always returns that max
'''
