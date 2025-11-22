"""
Data Transformer Module
Handles all data transformation operations.
"""

import pandas as pd
import numpy as np
from typing import Dict, Any, List
import logging
import re

logger = logging.getLogger(__name__)


class DataTransformer:
    """
    Applies various data transformation operations on DataFrames.
    
    Supports operations like cleaning, filtering, mathematical operations, etc.
    """
    
    def __init__(self):
        """Initialize DataTransformer."""
        pass
    
    def apply_operation(self, df: pd.DataFrame, operation: Dict[str, Any]) -> pd.DataFrame:
        """
        Apply a single operation to the DataFrame.
        
        Args:
            df: Input DataFrame
            operation: Dictionary containing operation details
            
        Returns:
            pd.DataFrame: Transformed DataFrame
        """
        try:
            op_type = operation.get('type')
            op_name = operation.get('operation')
            
            logger.info(f"Applying operation: {op_type} - {op_name}")
            
            if op_type == "Data Cleaning":
                return self._apply_cleaning(df, operation)
            elif op_type == "Filtering":
                return self._apply_filtering(df, operation)
            elif op_type == "Column Operations":
                return self._apply_column_operations(df, operation)
            elif op_type == "Mathematical Operations":
                return self._apply_mathematical(df, operation)
            elif op_type == "Text Operations":
                return self._apply_text_operations(df, operation)
            elif op_type == "Date Operations":
                return self._apply_date_operations(df, operation)
            else:
                logger.warning(f"Unknown operation type: {op_type}")
                return df
                
        except Exception as e:
            logger.error(f"Error applying operation: {str(e)}")
            raise
    
    def _apply_cleaning(self, df: pd.DataFrame, operation: Dict[str, Any]) -> pd.DataFrame:
        """Apply data cleaning operations."""
        op_name = operation.get('operation')
        result_df = df.copy()
        
        if op_name == "Remove Duplicates":
            columns = operation.get('columns')
            keep = operation.get('keep', 'first')
            if columns:
                result_df = result_df.drop_duplicates(subset=columns, keep=keep)
            else:
                result_df = result_df.drop_duplicates(keep=keep)
        
        elif op_name == "Remove Empty Rows":
            result_df = result_df.dropna(how='all')
        
        elif op_name == "Remove Empty Columns":
            result_df = result_df.dropna(axis=1, how='all')
        
        elif op_name == "Fill Missing Values":
            column = operation.get('column')
            method = operation.get('method')
            
            if method == "Forward Fill":
                result_df[column] = result_df[column].fillna(method='ffill')
            elif method == "Backward Fill":
                result_df[column] = result_df[column].fillna(method='bfill')
            elif method == "Mean":
                result_df[column] = result_df[column].fillna(result_df[column].mean())
            elif method == "Median":
                result_df[column] = result_df[column].fillna(result_df[column].median())
            elif method == "Mode":
                result_df[column] = result_df[column].fillna(result_df[column].mode()[0])
            elif method == "Custom Value":
                value = operation.get('value')
                result_df[column] = result_df[column].fillna(value)
        
        return result_df
    
    def _apply_filtering(self, df: pd.DataFrame, operation: Dict[str, Any]) -> pd.DataFrame:
        """Apply filtering operations."""
        column = operation.get('column')
        operator = operation.get('operator')
        value = operation.get('value')
        
        result_df = df.copy()
        
        # Try to convert value to numeric if possible
        try:
            value = float(value)
        except (ValueError, TypeError):
            pass
        
        if operator == "==":
            result_df = result_df[result_df[column] == value]
        elif operator == "!=":
            result_df = result_df[result_df[column] != value]
        elif operator == ">":
            result_df = result_df[result_df[column] > value]
        elif operator == "<":
            result_df = result_df[result_df[column] < value]
        elif operator == ">=":
            result_df = result_df[result_df[column] >= value]
        elif operator == "<=":
            result_df = result_df[result_df[column] <= value]
        elif operator == "contains":
            result_df = result_df[result_df[column].astype(str).str.contains(str(value), na=False)]
        elif operator == "not contains":
            result_df = result_df[~result_df[column].astype(str).str.contains(str(value), na=False)]
        
        return result_df
    
    def _apply_column_operations(self, df: pd.DataFrame, operation: Dict[str, Any]) -> pd.DataFrame:
        """Apply column operations."""
        op_name = operation.get('operation')
        result_df = df.copy()
        
        if op_name == "Merge Columns":
            columns = operation.get('columns', [])
            separator = operation.get('separator', ' ')
            new_column = operation.get('new_column')
            
            if columns and new_column:
                result_df[new_column] = result_df[columns].astype(str).agg(separator.join, axis=1)
        
        elif op_name == "Split Column":
            column = operation.get('column')
            separator = operation.get('separator', ',')
            new_columns = operation.get('new_columns', [])
            
            if column and new_columns:
                split_data = result_df[column].astype(str).str.split(separator, expand=True)
                for idx, new_col in enumerate(new_columns):
                    if idx < len(split_data.columns):
                        result_df[new_col.strip()] = split_data[idx]
        
        elif op_name == "Rename Column":
            old_name = operation.get('old_name')
            new_name = operation.get('new_name')
            
            if old_name and new_name:
                result_df = result_df.rename(columns={old_name: new_name})
        
        elif op_name == "Delete Column":
            columns = operation.get('columns', [])
            result_df = result_df.drop(columns=columns, errors='ignore')
        
        return result_df
    
    def _apply_mathematical(self, df: pd.DataFrame, operation: Dict[str, Any]) -> pd.DataFrame:
        """Apply mathematical operations."""
        op_name = operation.get('operation')
        result_df = df.copy()
        
        if op_name == "Add Columns":
            col1 = operation.get('col1')
            col2 = operation.get('col2')
            result_col = operation.get('result_column')
            result_df[result_col] = result_df[col1] + result_df[col2]
        
        elif op_name == "Subtract Columns":
            col1 = operation.get('col1')
            col2 = operation.get('col2')
            result_col = operation.get('result_column')
            result_df[result_col] = result_df[col1] - result_df[col2]
        
        elif op_name == "Multiply Columns":
            col1 = operation.get('col1')
            col2 = operation.get('col2')
            result_col = operation.get('result_column')
            result_df[result_col] = result_df[col1] * result_df[col2]
        
        elif op_name == "Divide Columns":
            col1 = operation.get('col1')
            col2 = operation.get('col2')
            result_col = operation.get('result_column')
            result_df[result_col] = result_df[col1] / result_df[col2]
        
        elif op_name == "Sum":
            columns = operation.get('columns', [])
            result_col = operation.get('result_column')
            result_df[result_col] = result_df[columns].sum(axis=1)
        
        elif op_name == "Mean":
            columns = operation.get('columns', [])
            result_col = operation.get('result_column')
            result_df[result_col] = result_df[columns].mean(axis=1)
        
        elif op_name == "Median":
            columns = operation.get('columns', [])
            result_col = operation.get('result_column')
            result_df[result_col] = result_df[columns].median(axis=1)
        
        elif op_name == "Min":
            columns = operation.get('columns', [])
            result_col = operation.get('result_column')
            result_df[result_col] = result_df[columns].min(axis=1)
        
        elif op_name == "Max":
            columns = operation.get('columns', [])
            result_col = operation.get('result_column')
            result_df[result_col] = result_df[columns].max(axis=1)
        
        elif op_name == "Percentage Change":
            col1 = operation.get('col1')
            col2 = operation.get('col2')
            result_col = operation.get('result_column')
            result_df[result_col] = ((result_df[col2] - result_df[col1]) / result_df[col1]) * 100
        
        elif op_name == "Conditional Calculation":
            condition_col = operation.get('condition_col')
            operator = operation.get('operator')
            threshold = operation.get('threshold')
            true_value = operation.get('true_value')
            false_value = operation.get('false_value')
            result_col = operation.get('result_column')
            
            # Create condition
            if operator == ">":
                condition = result_df[condition_col] > threshold
            elif operator == "<":
                condition = result_df[condition_col] < threshold
            elif operator == ">=":
                condition = result_df[condition_col] >= threshold
            elif operator == "<=":
                condition = result_df[condition_col] <= threshold
            elif operator == "==":
                condition = result_df[condition_col] == threshold
            elif operator == "!=":
                condition = result_df[condition_col] != threshold
            else:
                condition = pd.Series([False] * len(result_df))
            
            result_df[result_col] = np.where(condition, true_value, false_value)
        
        return result_df
    
    def _apply_text_operations(self, df: pd.DataFrame, operation: Dict[str, Any]) -> pd.DataFrame:
        """Apply text operations."""
        op_name = operation.get('operation')
        column = operation.get('column')
        result_df = df.copy()
        
        if op_name == "Lowercase":
            result_df[column] = result_df[column].astype(str).str.lower()
        
        elif op_name == "Uppercase":
            result_df[column] = result_df[column].astype(str).str.upper()
        
        elif op_name == "Title Case":
            result_df[column] = result_df[column].astype(str).str.title()
        
        elif op_name == "Trim Spaces":
            result_df[column] = result_df[column].astype(str).str.strip()
        
        elif op_name == "Replace Text":
            old_text = operation.get('old_text')
            new_text = operation.get('new_text')
            result_df[column] = result_df[column].astype(str).str.replace(old_text, new_text, regex=False)
        
        return result_df
    
    def _apply_date_operations(self, df: pd.DataFrame, operation: Dict[str, Any]) -> pd.DataFrame:
        """Apply date operations."""
        op_name = operation.get('operation')
        column = operation.get('column')
        result_df = df.copy()
        
        if op_name == "Convert to Date":
            date_format = operation.get('format', '%Y-%m-%d')
            result_df[column] = pd.to_datetime(result_df[column], format=date_format, errors='coerce')
        
        elif op_name == "Extract Year":
            result_df[column] = pd.to_datetime(result_df[column], errors='coerce').dt.year
        
        elif op_name == "Extract Month":
            result_df[column] = pd.to_datetime(result_df[column], errors='coerce').dt.month
        
        elif op_name == "Extract Day":
            result_df[column] = pd.to_datetime(result_df[column], errors='coerce').dt.day
        
        elif op_name == "Format Date":
            output_format = operation.get('output_format', '%Y-%m-%d')
            result_df[column] = pd.to_datetime(result_df[column], errors='coerce').dt.strftime(output_format)
        
        return result_df
