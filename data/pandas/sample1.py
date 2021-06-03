import pandas as pd

dataSet = {
    'cars': ['BMW', 'volvo', 'ford'],
    'passings': [3, 7, 2]
}

xVar = pd.DataFrame(dataSet)

print(xVar)

print(pd.__version__)

d = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])}


xVar = pd.DataFrame(d)
print(xVar.loc['b'])

print(xVar[0:4])


del xVar['three']
print(xVar)

xVar.pop('two')
print(xVar)
