import numpy as np
from bokeh.charts import Line, output_file, show

# (dict, OrderedDict, lists, arrays and DataFrames are valid inputs)
xyvalues = np.array([[2, 3, 7, 5, 26], [12, 33, 47, 15, 126], [22, 43, 10, 25, 26]])

line = Line(xyvalues, title="line", legend="top_left", ylabel='Languages')

output_file('line.html')
show(line)




