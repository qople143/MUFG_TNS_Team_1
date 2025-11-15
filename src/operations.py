import pandas as pd
import numpy as np
from datetime import datetime


class RemoveDuplicates:
    def __init__(self, columns=None, keep='first'):
        self.columns = columns
        self.keep = keep
    
    def apply(self, df):
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
    def __init__(self, column, operator, value):
        valid_operators = ['==', '!=', '>', '<', '>=', '<=', 'contains', 'in']
        if operator not in valid_operators:
            raise ValueError(f"Operator must be one of: {valid_operators}")
        
        self.column = column
        self.operator = operator
        self.value = value
    
    def apply(self, df):
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
    def __init__(self, column, old_value, new_value):
        self.column = column
        self.old_value = old_value
        self.new_value = new_value
    
    def apply(self, df):
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

class MergeColumns:    
    def __init__(self, columns, new_column_name='Merged', separator=' '):
        self.columns = columns
        self.new_column_name = new_column_name
        self.separator = separator
    
    def apply(self, df):
        try:
            df = df.copy()
            
            # Convert all columns to string and merge
            df[self.new_column_name] = df[self.columns].astype(str).agg(
                self.separator.join, axis=1
            )
            
            return df
        except Exception as e:
            raise ValueError(f"Merge columns failed: {str(e)}")

class NormalizeText:
    def __init__(self, column, method='lower'):
        valid_methods = ['lower', 'upper', 'title', 'trim', 'capitalize']
        if method not in valid_methods:
            raise ValueError(f"Method must be one of: {valid_methods}")
        
        self.column = column
        self.method = method
    
    def apply(self, df):
        try:
            df = df.copy()
            
            # Convert to string first
            df[self.column] = df[self.column].astype(str)
            
            if self.method == 'lower':
                df[self.column] = df[self.column].str.lower()
            elif self.method == 'upper':
                df[self.column] = df[self.column].str.upper()
            elif self.method == 'title':
                df[self.column] = df[self.column].str.title()
            elif self.method == 'trim':
                df[self.column] = df[self.column].str.strip()
            elif self.method == 'capitalize':
                df[self.column] = df[self.column].str.capitalize()
            
            return df
        except Exception as e:
            raise ValueError(f"Text normalization failed: {str(e)}")

class ConvertDateFormat:
    def __init__(self, column, from_format='auto', to_format='%Y-%m-%d'):
        self.column = column
        self.from_format = from_format
        self.to_format = to_format
    
    def apply(self, df):
        try:
            df = df.copy()
            
            # Parse dates
            if self.from_format == 'auto':
                df[self.column] = pd.to_datetime(df[self.column])
            else:
                df[self.column] = pd.to_datetime(
                    df[self.column], 
                    format=self.from_format
                )
            
            # Format dates
            df[self.column] = df[self.column].dt.strftime(self.to_format)
            
            return df
        except Exception as e:
            raise ValueError(f"Date conversion failed: {str(e)}")
