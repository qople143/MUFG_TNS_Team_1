import pytest
import pandas as pd
import numpy as np
from src.operations import RemoveDuplicates, FilterRows, ReplaceValues

class TestRemoveDuplicates:
    """Tests for RemoveDuplicates operation."""
    
    @pytest.fixture
    def sample_df(self):
        """Create sample DataFrame with duplicates."""
        return pd.DataFrame({
            'id': [1, 2, 2, 3, 4, 5, 5],
            'name': ['Alice', 'Bob', 'Bob', 'Charlie', 'David', 'Eve', 'Eve'],
            'age': [25, 30, 30, 35, 28, 32, 32],
        })
    
    def test_remove_all_duplicates(self, sample_df):
        """Test removing all duplicate rows."""
        op = RemoveDuplicates()
        result = op.apply(sample_df)
        
        assert result.shape[0] == 5  # 7 rows - 2 duplicates = 5 rows
        assert len(result) < len(sample_df)
    
    def test_remove_duplicates_by_column(self, sample_df):
        """Test removing duplicates by specific column."""
        op = RemoveDuplicates(columns=['id'])
        result = op.apply(sample_df)
        
        assert result.shape[0] == 5
        assert result['id'].duplicated().sum() == 0
    
    def test_keep_last(self, sample_df):
        """Test keeping last occurrence of duplicate."""
        op = RemoveDuplicates(keep='last')
        result = op.apply(sample_df)
        
        assert result.shape[0] == 5
        # Check that last index is kept
        assert 6 in result.index  # Last Eve row
    
    def test_empty_dataframe(self):
        """Test with empty DataFrame."""
        df = pd.DataFrame()
        op = RemoveDuplicates()
        result = op.apply(df)
        
        assert result.shape[0] == 0
    
    def test_no_duplicates(self):
        """Test DataFrame with no duplicates."""
        df = pd.DataFrame({
            'id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie']
        })
        op = RemoveDuplicates()
        result = op.apply(df)
        
        assert result.shape[0] == 3  # No change


class TestFilterRows:
    """Tests for FilterRows operation."""
    
    @pytest.fixture
    def sample_df(self):
        """Create sample DataFrame."""
        return pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'age': [25, 30, 35, 28, 32],
            'city': ['NYC', 'LA', 'NYC', 'Chicago', 'Boston'],
        })
    
    def test_filter_equals(self, sample_df):
        """Test filtering with == operator."""
        op = FilterRows('age', '==', 30)
        result = op.apply(sample_df)
        
        assert result.shape[0] == 1
        assert result['name'].values == 'Bob'
    
    def test_filter_greater_than(self, sample_df):
        """Test filtering with > operator."""
        op = FilterRows('age', '>', 30)
        result = op.apply(sample_df)
        
        assert result.shape[0] == 2  # Charlie (35), Eve (32)
    
    def test_filter_contains(self, sample_df):
        """Test filtering with contains operator."""
        op = FilterRows('city', 'contains', 'York')
        result = op.apply(sample_df)
        
        assert result.shape[0] == 0  # NYC rows
       
    def test_filter_in(self, sample_df):
        """Test filtering with in operator."""
        op = FilterRows('name', 'in', ['Alice', 'Bob', 'Charlie'])
        result = op.apply(sample_df)
        
        assert result.shape[0] == 3
    
    def test_invalid_operator(self):
        """Test that invalid operator raises error."""
        with pytest.raises(ValueError):
            FilterRows('age', 'invalid_op', 30)
    
    def test_empty_result(self, sample_df):
        """Test filter that returns no rows."""
        op = FilterRows('age', '>', 100)
        result = op.apply(sample_df)
        
        assert result.shape[0] == 0


class TestReplaceValues:
    """Tests for ReplaceValues operation."""
    
    @pytest.fixture
    def sample_df(self):
        """Create sample DataFrame."""
        return pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'city': ['NYC', 'LA', 'NYC', 'Chicago', 'NYC'],
            'status': ['active', 'inactive', 'active', 'active', 'inactive'],
        })
    
    def test_replace_string(self, sample_df):
        """Test replacing string values."""
        op = ReplaceValues('city', 'NYC', 'New York')
        result = op.apply(sample_df)
        
        assert 'New York' in result['city'].values
        assert 'NYC' not in result['city'].values
    
    def test_replace_numeric(self, sample_df):
        """Test replacing numeric values."""
        df = pd.DataFrame({'value': [1, 2, 3, 2, 1]})
        op = ReplaceValues('value', 2, 99)
        result = op.apply(df)
        
        assert (result['value'] == 99).sum() == 2
        assert (result['value'] == 2).sum() == 0
    
    def test_replace_multiple_occurrences(self, sample_df):
        """Test that all occurrences are replaced."""
        op = ReplaceValues('city', 'NYC', 'New York')
        result = op.apply(sample_df)
        
        assert (result['city'] == 'New York').sum() == 3
    
    def test_replace_nonexistent_value(self, sample_df):
        """Test replacing value that doesn't exist."""
        op = ReplaceValues('city', 'Toronto', 'Canada')
        result = op.apply(sample_df)
        
        # Should return unchanged
        assert result.equals(sample_df)
    
    def test_original_unchanged(self, sample_df):
        """Test that original DataFrame is not modified."""
        original_copy = sample_df.copy()
        op = ReplaceValues('city', 'NYC', 'New York')
        result = op.apply(sample_df)
        
        # Original should be unchanged
        assert sample_df.equals(original_copy)