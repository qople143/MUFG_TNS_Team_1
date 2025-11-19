"""
Test script to verify all components work correctly.
Run this before starting the application.
"""

import sys
import pandas as pd
from utils.file_handler import FileHandler
from utils.data_transformer import DataTransformer
from utils.template_manager import TemplateManager

def test_file_handler():
    """Test FileHandler functionality."""
    print("Testing FileHandler...")
    handler = FileHandler()
    
    # Test with sample file
    try:
        # Test file validation
        class MockFile:
            def __init__(self, name):
                self.name = name
        
        valid_file = MockFile('test.xlsx')
        invalid_file = MockFile('test.txt')
        
        assert handler.validate_file(valid_file), "Failed to validate .xlsx file"
        assert not handler.validate_file(invalid_file), "Incorrectly validated .txt file"
        print("  ✅ File validation works")
        
        # Test loading actual file
        dataframes = pd.read_excel('sample_data/sample_input.xlsx', sheet_name=None)
        assert dataframes is not None, "Failed to load file"
        assert len(dataframes) > 0, "No sheets loaded"
        print(f"  ✅ Can load Excel files ({len(dataframes)} sheet(s))")
        
        for sheet_name, df in dataframes.items():
            print(f"  ✅ Sheet '{sheet_name}': {len(df)} rows, {len(df.columns)} columns")
    
    except Exception as e:
        print(f"  ❌ Error: {str(e)}")
        return False
    
    return True

def test_data_transformer():
    """Test DataTransformer functionality."""
    print("\nTesting DataTransformer...")
    transformer = DataTransformer()
    
    # Create test DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': ['a', 'b', 'c', 'd', 'e']
    })
    
    try:
        # Test mathematical operation
        operation = {
            'type': 'Mathematical Operations',
            'operation': 'Add Columns',
            'col1': 'A',
            'col2': 'B',
            'result_column': 'Sum'
        }
        result = transformer.apply_operation(df, operation)
        assert 'Sum' in result.columns, "Sum column not created"
        assert result['Sum'].iloc[0] == 11, "Incorrect calculation"
        print("  ✅ Mathematical operations work")
        
        # Test text operation
        operation = {
            'type': 'Text Operations',
            'operation': 'Uppercase',
            'column': 'C'
        }
        result = transformer.apply_operation(df, operation)
        assert result['C'].iloc[0] == 'A', "Text operation failed"
        print("  ✅ Text operations work")
        
        # Test filtering
        operation = {
            'type': 'Filtering',
            'operation': 'Filter Rows',
            'column': 'A',
            'operator': '>',
            'value': '2'
        }
        result = transformer.apply_operation(df, operation)
        assert len(result) == 3, "Filtering failed"
        print("  ✅ Filtering works")
        
    except Exception as e:
        print(f"  ❌ Error: {str(e)}")
        return False
    
    return True

def test_template_manager():
    """Test TemplateManager functionality."""
    print("\nTesting TemplateManager...")
    manager = TemplateManager()
    
    try:
        # Test save template
        test_operations = [
            {'type': 'Data Cleaning', 'operation': 'Remove Duplicates'},
            {'type': 'Mathematical Operations', 'operation': 'Add Columns'}
        ]
        
        success = manager.save_template('test_template', test_operations)
        assert success, "Failed to save template"
        print("  ✅ Template saving works")
        
        # Test list templates
        templates = manager.list_templates()
        assert 'test_template' in templates, "Template not in list"
        print("  ✅ Template listing works")
        
        # Test load template
        loaded = manager.load_template('test_template')
        assert loaded is not None, "Failed to load template"
        assert len(loaded['operations']) == 2, "Incorrect operations count"
        print("  ✅ Template loading works")
        
        # Test delete template
        success = manager.delete_template('test_template')
        assert success, "Failed to delete template"
        print("  ✅ Template deletion works")
        
    except Exception as e:
        print(f"  ❌ Error: {str(e)}")
        return False
    
    return True

def test_dependencies():
    """Test if all required packages are installed."""
    print("\nTesting Dependencies...")
    
    required_packages = {
        'streamlit': 'streamlit',
        'pandas': 'pandas',
        'openpyxl': 'openpyxl',
        'numpy': 'numpy'
    }
    
    all_installed = True
    for package_name, import_name in required_packages.items():
        try:
            __import__(import_name)
            print(f"  ✅ {package_name} installed")
        except ImportError:
            print(f"  ❌ {package_name} NOT installed")
            all_installed = False
    
    return all_installed

def main():
    """Run all tests."""
    print("=" * 60)
    print("Excel Data Massaging Tool - Component Tests")
    print("=" * 60)
    
    results = {
        'Dependencies': test_dependencies(),
        'FileHandler': test_file_handler(),
        'DataTransformer': test_data_transformer(),
        'TemplateManager': test_template_manager()
    }
    
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    
    all_passed = True
    for component, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{component}: {status}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n🎉 All tests passed! You can run the application with:")
        print("   streamlit run app.py")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues before running the application.")
        sys.exit(1)

if __name__ == "__main__":
    main()
