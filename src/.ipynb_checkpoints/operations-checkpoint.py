"""
Excel transformation operations module.

This module contains all data transformation operations that can be
applied to Excel DataFrames.

Operations:
    - RemoveDuplicates: Remove duplicate rows
    - FilterRows: Filter rows by condition
    - ReplaceValues: Replace values in columns
    - MergeColumns: Combine multiple columns
    - NormalizeText: Normalize text values
    - ConvertDateFormat: Convert date formats
"""

import pandas as pd
import numpy as np
from datetime import datetime


class RemoveDuplicates:
    """
    Remove duplicate rows from DataFrame.
    
    This operation identifies and removes rows that are duplicates
    based on specified columns.
    
    Attributes:
        columns (list): List of column names to check for duplicates.
                       If None, checks all columns.
        keep (str): Which duplicates to keep:
                   - 'first': Keep first occurrence (default)
                   - 'last': Keep last occurrence
                   - False: Remove all duplicates
    """
    
    def __init__(self, columns=None, keep='first'):
        """
        Initialize RemoveDuplicates operation.
        
        Args:
            columns (list, optional): Column names to check for duplicates.
                                     Defaults to None (all columns).
            keep (str): Which duplicates to keep ('first', 'last', or False).
                       Defaults to 'first'.
        """
        self.columns = columns
        self.keep = keep
    
    def apply(self, df):
        """
        Apply the remove duplicates operation to a DataFrame.
        
        Args:
            df (pd.DataFrame): Input DataFrame.
        
        Returns:
            pd.DataFrame: DataFrame with duplicates removed.
        
        Raises:
            ValueError: If operation fails due to invalid input.
        
        Example:
            >>> op = RemoveDuplicates(columns=['id', 'name'])
            >>> result = op.apply(df)
        """
        try:
            # Make a copy to avoid modifying original
            result = df.copy()
            
            # Drop duplicates
            result = result.drop_duplicates(
                subset=self.columns, 
                keep=self.keep
            )
            
            return result
        except Exception as e:
            raise ValueError(f"Remove duplicates failed: {str(e)}")


class FilterRows:
    """
    Filter rows from DataFrame based on a condition.
    
    This operation allows filtering rows by comparing a column
    value against a specified condition and value.
    
    Attributes:
        column (str): Column name to filter by.
        operator (str): Comparison operator:
                       '==', '!=', '>', '<', '>=', '<=', 'contains', 'in'
        value: The value to compare against.
    """
    
    def __init__(self, column, operator, value):
        """
        Initialize FilterRows operation.
        
        Args:
            column (str): Column name to filter by.
            operator (str): Comparison operator.
            value: Value to compare against.
        
        Raises:
            ValueError: If operator is not valid.
        """
        valid_operators = ['==', '!=', '>', '<', '>=', '<=', 'contains', 'in']
        if operator not in valid_operators:
            raise ValueError(f"Operator must be one of: {valid_operators}")
        
        self.column = column
        self.operator = operator
        self.value = value
    
    def apply(self, df):
        """
        Apply the filter operation to a DataFrame.
        
        Args:
            df (pd.DataFrame): Input DataFrame.
        
        Returns:
            pd.DataFrame: Filtered DataFrame.
        
        Raises:
            ValueError: If operation fails.
        
        Example:
            >>> op = FilterRows('age', '>', 30)
            >>> result = op.apply(df)  # Get all rows where age > 30
        """
        try:
            df = df.copy()
            
            if self.operator == '==':
                result = df[df[self.column] == self.value]
            elif self.operator == '!=':
                result = df[df[self.column] != self.value]
            elif self.operator == '>':
                result = df[df[self.column] > self.value]
            elif self.operator == '<':
                result = df[df[self.column] < self.value]
            elif self.operator == '>=':
                result = df[df[self.column] >= self.value]
            elif self.operator == '<=':
                result = df[df[self.column] <= self.value]
            elif self.operator == 'contains':
                result = df[df[self.column].astype(str).str.contains(str(self.value))]
            elif self.operator == 'in':
                result = df[df[self.column].isin(self.value)]
            else:
                raise ValueError(f"Unknown operator: {self.operator}")
            
            return result
        except Exception as e:
            raise ValueError(f"Filter failed: {str(e)}")


class ReplaceValues:
    """
    Replace values in a DataFrame column.
    
    This operation finds all occurrences of a specific value
    in a column and replaces them with a new value.
    
    Attributes:
        column (str): Column name where replacements occur.
        old_value: Value to find and replace.
        new_value: Value to replace with.
    """
    
    def __init__(self, column, old_value, new_value):
        """
        Initialize ReplaceValues operation.
        
        Args:
            column (str): Column name.
            old_value: Value to replace.
            new_value: Replacement value.
        """
        self.column = column
        self.old_value = old_value
        self.new_value = new_value
    
    def apply(self, df):
        """
        Apply the replace operation to a DataFrame.
        
        Args:
            df (pd.DataFrame): Input DataFrame.
        
        Returns:
            pd.DataFrame: DataFrame with replacements made.
        
        Raises:
            ValueError: If operation fails.
        
        Example:
            >>> op = ReplaceValues('city', 'NYC', 'New York')
            >>> result = op.apply(df)
        """
        try:
            df = df.copy()
            
            # Replace the values
            df[self.column] = df[self.column].replace(
                self.old_value, 
                self.new_value
            )
            
            return df
        except Exception as e:
            raise ValueError(f"Replace failed: {str(e)}")