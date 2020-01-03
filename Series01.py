import pandas
import numpy
myarray= numpy.array([1,2,3])
rowname=['a','b','c']
myseries=pandas.Series(myarray,index=rowname, dtype=float)
print(type(myarray))
print(type(rowname))
print(type(myseries))
print(myseries)

