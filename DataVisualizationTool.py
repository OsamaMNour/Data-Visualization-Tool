import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
import numpy as np

class DataVisualizationTool:
    def __init__(self, data, figsize=(8,6), color=None, markers=None, violin_inner="box", violin_showmeans=True, violin_showextrema=True, violin_showmedians=True, heatmap_cmap=None, alpha=0.5, fliers=False):
        self.data = data
        self.figsize = figsize
        self.color = color
        self.markers = markers
        self.violin_inner = violin_inner
        self.violin_showmeans = violin_showmeans
        self.violin_showextrema = violin_showextrema
        self.violin_showmedians = violin_showmedians
        self.heatmap_cmap = heatmap_cmap
        self.alpha = alpha
        self.fliers = fliers

    def plot(self, plot_type, column_names, title=None, xlabel=None, ylabel=None, save=False, filename=None):
        if not self._check_numeric(column_names):
            print("Error: Columns must be numeric to generate this plot type.")
            return

        if plot_type not in ['histogram', 'violin', 'box', 'scatter', 'line', 'bar', 'scatter_reg', 'heatmap']:
            print("Error: Invalid plot type.")
            return

        if plot_type == 'histogram':
            self._histogram(column_names, title, xlabel, ylabel, save, filename)
        elif plot_type == 'violin':
            self._violin(column_names, title, xlabel, ylabel, save, filename)
        elif plot_type == 'box':
            self._box(column_names, title, xlabel, ylabel, save, filename)
        elif plot_type == 'scatter':
            self._scatter(column_names, title, xlabel, ylabel, save, filename)
        elif plot_type == 'line':
            self._line(column_names, title, xlabel, ylabel, save, filename)
        elif plot_type == 'bar':
            self._bar(column_names, title, xlabel, ylabel, save, filename)
        elif plot_type == 'scatter_reg':
            self._scatter_reg(column_names, title, xlabel, ylabel, save, filename)
        elif plot_type == 'heatmap':
            self._heatmap(column_names, title, xlabel, ylabel, save, filename)

    def _check_numeric(self, column_names):
        columns = [col for col in column_names if col in self.data.columns]
        return all([self.data[col].dtype in [int, float] for col in columns])


    def _histogram(self, column_names, title, xlabel, ylabel, save, filename):
        fig, ax = plt.subplots(figsize=self.figsize)
        for col in column_names:
            sns.histplot(data=self.data, x=col, color=self.color, kde=False)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if save:
            plt.savefig(filename)
        plt.show()
    def _violin(self, column_names, title, xlabel, ylabel, save, filename):
        fig, ax = plt.subplots(figsize=self.figsize)
        for col in column_names:
            sns.violinplot(data=self.data, x=None, y=col, color=self.color, inner=self.violin_inner, showmeans=self.violin_showmeans, showextrema=self.violin_showextrema, showmedians=self.violin_showmedians)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if save:
            plt.savefig(filename)
        plt.show()

    def _box(self, column_names, title, xlabel, ylabel, save, filename):
        fig, ax = plt.subplots(figsize=self.figsize)
        sns.boxplot(data=self.data[column_names], fliersize=self.fliers, color=self.color)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if save:
            plt.savefig(filename)
        plt.show()

    def _scatter(self, column_names, title, xlabel, ylabel, save, filename):
        fig, ax = plt.subplots(figsize=self.figsize)
        sns.scatterplot(data=self.data, x=column_names[0], y=column_names[1], hue=self.color, style=self.markers)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if save:
            plt.savefig(filename)
        plt.show()

    def _line(self, column_names, title, xlabel, ylabel, save, filename):
        fig, ax = plt.subplots(figsize=self.figsize)
        sns.lineplot(data=self.data, x=column_names[0], y=column_names[1], color=self.color)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if save:
            plt.savefig(filename)
        plt.show()
        
    def _scatter(self, column_names, title, xlabel, ylabel, save, filename):
        fig, ax = plt.subplots(figsize=self.figsize)
        sns.scatterplot(data=self.data, x=column_names[0], y=column_names[1], color=self.color, alpha=self.alpha, markers=self.markers)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if save:
            plt.savefig(filename)
        plt.show()
     
    def _bar(self, column_names, title, xlabel, ylabel, save, filename):
        fig, ax = plt.subplots(figsize=self.figsize)
        sns.barplot(data=self.data, x=column_names[0], y=column_names[1], color=self.color)
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
        if save:
            plt.savefig(filename)
        plt.show()
    
    def _scatter_reg(self, column_names, title, xlabel, ylabel, save, filename):
        fig, ax = plt.subplots(figsize=self.figsize)
        sns.regplot(data=self.data, x=column_names[0], y=column_names[1], ax=ax)
        if title:
            ax.set_title(title)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)
        if save:
            fig.savefig(filename)
        plt.show()
    
    def _heatmap(self, column_names, title, xlabel, ylabel, save, filename):
        fig, ax = plt.subplots(figsize=self.figsize)
        sns.heatmap(data=self.data[column_names].corr(), annot=True, cmap='coolwarm', ax=ax)
        if title:
            ax.set_title(title)
        if xlabel:
            ax.set_xlabel(xlabel)
        if ylabel:
            ax.set_ylabel(ylabel)
        if save:
            fig.savefig(filename)
        plt.show()
        

def run_tool():
    while True:
        data = None
        while data is None:
            data_path = input("Enter the path to the data file (or 'q' to quit): ")
            if data_path.lower() == 'q':
                return
            try:
                data = pd.read_csv(data_path)
            except FileNotFoundError:
                print("File not found. Please enter a valid file path or 'q' to quit.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please enter a valid file path or 'q' to quit.")
        
        if data is None:
            continue
        
        plot_type = None
        while plot_type not in ['histogram', 'violin', 'box', 'scatter', 'line', 'bar', 'scatter_reg', 'heatmap']:
            plot_type = input("Enter the type of plot you want to generate (histogram, violin, box, scatter, line, bar, scatter_reg, heatmap) or 'b' to go back: ")
            if plot_type.lower() == 'b':
                data = None
                break
            if plot_type not in ['histogram', 'violin', 'box', 'scatter', 'line', 'bar', 'scatter_reg', 'heatmap']:
                print("Invalid plot type. Please enter either 'histogram', 'violin', 'box', 'scatter', 'line', 'bar', 'scatter_reg', 'heatmap' or 'b' to go back.")
        
        if plot_type is None:
            continue
        
        column_names = None
        while column_names is None:
            column_names_input = input("Enter the names of the columns to be plotted (separated by comma) or 'b' to go back: ")
            if column_names_input.lower() == 'b':
                plot_type = None
                break
            try:
                column_names = [col.strip() for col in column_names_input.split(',')]
                if any([col not in data.columns for col in column_names]):
                    raise Exception("Invalid column names")
            except Exception as e:
                print(f"Error: {e}")
                column_names = None

        
        if column_names is None:
            continue
    
        tool = DataVisualizationTool(data)
        tool.plot(plot_type, column_names)
        
if __name__ == "__main__":
    run_tool()