import pandas as pd
import matplotlib.pyplot as plt

class SalesAnalyzer:
    def __init__(self, data_file):
        self.sales_data = pd.read_csv(data_file)
        
    def analyze_total_sales(self):
        total_sales = self.sales_data['Revenue'].sum()
        return total_sales
    
    def analyze_sales_by_category(self):
        sales_by_category = self.sales_data.groupby('Category')['Revenue'].sum()
        return sales_by_category
    
    def analyze_sales_by_region(self):
        sales_by_region = self.sales_data.groupby('Region')['Revenue'].sum()
        return sales_by_region
    
    def plot_sales_by_region(self):
        sales_by_region = self.analyze_sales_by_region()
        sales_by_region.plot(kind='bar')
        plt.title('Sales by Region')
        plt.xlabel('Region')
        plt.ylabel('Revenue')
        plt.show()
