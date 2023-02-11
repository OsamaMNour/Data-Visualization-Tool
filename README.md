# DataVisualizationTool

#Introduction

This project provides a python class, DataVisualizationTool, for generating various types of visualizations of a data set. The class accepts a data set in the form of a pandas data frame, as well as various optional arguments for customization of the visualizations. The supported plot types are:

    Histogram
    Violin
    Box
    Scatter
    Line
    Bar
    Scatter with regression line
    Heatmap

#Dependencies

This project requires the following packages:

    pandas
    matplotlib
    seaborn
    numpy
    scikit-learn

#Usage

To use the DataVisualizationTool, you will need to create an instance of the class and pass your data set to the constructor. The constructor has several optional arguments that you can use to customize the visualizations.

Here is an example of how you can use the class to generate a histogram:

Assuming you have the csv file named data.csv, you can run the tool as follows:
--------------
Python 3
import pandas as pd
from DataVisualizationTool import DataVisualizationTool

data = pd.read_csv('data.csv')
dvt = DataVisualizationTool(data)

dvt.plot('histogram', ['column_1', 'column_2'], title='Histogram Plot', xlabel='Column Names', ylabel='Frequency')
----------

Replace 'histogram', ['column_1', 'column_2'], 'Histogram Plot', 'Column Names', and 'Frequency' with the desired plot type, column names, title, xlabel, and ylabel for your visualization.

For more information on the other optional arguments and the different plot types that you can generate, please refer to the class definition in the source code.

#Conclusion

This project provides a convenient and flexible tool for visualizing your data sets. By using the DataVisualizationTool class, you can quickly generate a variety of plots with customizable options, allowing you to gain insights into your data and communicate those insights effectively.
