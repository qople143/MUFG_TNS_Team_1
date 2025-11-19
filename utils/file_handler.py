"""
File Handler Module
Handles file upload, validation, and loading operations.
"""

import pandas as pd
from typing import Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FileHandler:
    """
    Handles Excel file operations including validation and loading.
    
    Attributes:
        supported_formats (list): List of supported file extensions
    """
    
    def __init__(self):
        """Initialize FileHandler with supported formats."""
        self.supported_formats = ['.xlsx', '.xls']
    
    def validate_file(self, file) -> bool:
        """
        Validate if the uploaded file is a supported Excel format.
        
        Args:
            file: Uploaded file object
            
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            file_extension = f".{file.name.split('.')[-1]}"
            return file_extension.lower() in self.supported_formats
        except Exception as e:
            logger.error(f"File validation error: {str(e)}")
            return False
    
    def load_excel(self, file) -> Optional[Dict[str, pd.DataFrame]]:
        """
        Load Excel file and return dictionary of DataFrames (one per sheet).
        
        Args:
            file: Uploaded Excel file object
            
        Returns:
            Dict[str, pd.DataFrame]: Dictionary with sheet names as keys and DataFrames as values
            
        Raises:
            ValueError: If file format is not supported
            Exception: For other loading errors
        """
        try:
            if not self.validate_file(file):
                raise ValueError(f"Unsupported file format. Supported formats: {self.supported_formats}")
            
            # Read all sheets
            excel_file = pd.ExcelFile(file)
            dataframes = {}
            
            for sheet_name in excel_file.sheet_names:
                df = pd.read_excel(file, sheet_name=sheet_name)
                dataframes[sheet_name] = df
                logger.info(f"Loaded sheet '{sheet_name}' with {len(df)} rows and {len(df.columns)} columns")
            
            return dataframes
            
        except Exception as e:
            logger.error(f"Error loading Excel file: {str(e)}")
            raise
    
    def get_file_info(self, dataframes: Dict[str, pd.DataFrame]) -> Dict[str, any]:
        """
        Get summary information about loaded Excel file.
        
        Args:
            dataframes: Dictionary of DataFrames
            
        Returns:
            Dict containing file statistics
        """
        info = {
            'total_sheets': len(dataframes),
            'sheets': {}
        }
        
        for sheet_name, df in dataframes.items():
            info['sheets'][sheet_name] = {
                'rows': len(df),
                'columns': len(df.columns),
                'column_names': df.columns.tolist(),
                'dtypes': df.dtypes.to_dict()
            }
        
        return info
