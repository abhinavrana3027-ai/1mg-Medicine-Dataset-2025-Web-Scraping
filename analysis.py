#!/usr/bin/env python3
"""
1mg Medicine Dataset - Comprehensive Analysis Script
Author: Abhinav Rana
Date: November 2025

Usage: python analysis.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings

warnings.filterwarnings('ignore')
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (14, 8)

class MedicineAnalyzer:
    def __init__(self, csv_path='onemg.csv'):
        print("Loading dataset...")
        self.df = pd.read_csv(csv_path)
        print(f"Dataset loaded: {self.df.shape[0]} records, {self.df.shape[1]} columns")
    
    def data_quality_report(self):
        print("\n" + "="*70)
        print("DATA QUALITY REPORT")
        print("="*70)
        print(f"\nDataset Shape: {self.df.shape}")
        print(f"\nColumn Names:\n{list(self.df.columns)}")
        print(f"\nData Types:\n{self.df.dtypes}")
        print(f"\nMissing Values:\n{self.df.isnull().sum()}")
        print(f"\nDuplicates: {self.df.duplicated().sum()}")
    
    def statistical_summary(self):
        print("\n" + "="*70)
        print("STATISTICAL SUMMARY")
        print("="*70)
        print(self.df.describe())
    
    def create_visualizations(self):
        print("\nGenerating visualizations...")
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) > 0:
            fig, axes = plt.subplots(2, 2, figsize=(16, 12))
            for idx, col in enumerate(list(numeric_cols)[:4]):
                ax = axes.flat[idx]
                self.df[col].hist(bins=30, ax=ax, color='skyblue', edgecolor='black')
                ax.set_title(f'{col} Distribution', fontweight='bold')
                ax.set_xlabel(col)
                ax.set_ylabel('Frequency')
            plt.tight_layout()
            plt.savefig('medicine_analysis.png', dpi=300, bbox_inches='tight')
            print("✓ Saved: medicine_analysis.png")
            plt.close()
    
    def generate_report(self):
        print("\n" + "#"*70)
        print("# 1MG MEDICINE DATASET - ANALYSIS REPORT")
        print("#"*70)
        self.data_quality_report()
        self.statistical_summary()
        self.create_visualizations()
        print("\n" + "="*70)
        print("ANALYSIS COMPLETE!")
        print("="*70)
        print("\nNext: Run 'streamlit run dashboard.py' for interactive dashboard")

if __name__ == '__main__':
    analyzer = MedicineAnalyzer('onemg.csv')
    analyzer.generate_report()
