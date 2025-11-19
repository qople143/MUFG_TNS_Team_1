# 📚 Excel Data Massaging Tool - Complete Documentation

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [User Guide](#user-guide)
4. [Technical Documentation](#technical-documentation)
5. [API Reference](#api-reference)
6. [Examples](#examples)

## Overview

The Excel Data Massaging Tool is a comprehensive solution for transforming and processing Excel data. Built with Streamlit and Pandas, it provides an intuitive interface for complex data operations without requiring programming knowledge.

### Key Features
- **Multi-file Processing**: Handle multiple Excel files simultaneously
- **Multi-sheet Support**: Process all sheets within Excel files
- **Template System**: Save and reuse transformation workflows
- **Real-time Preview**: See results before downloading
- **Comprehensive Operations**: 30+ data transformation operations
- **Error Handling**: Robust error handling with clear messages

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step-by-Step Installation

1. **Clone or download the project**
```bash
git clone <repository-url>
cd excel-data-massaging-tool
```

2. **Create virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Access the application**
Open your browser and go to `http://localhost:8501`

## User Guide

### Step 1: Upload Files

1. Click on "Browse files" or drag and drop Excel files
2. Supported formats: .xlsx, .xls
3. Multiple files can be uploaded simultaneously
4. Preview shows first 10 rows of each sheet

**Tips:**
- Ensure your Excel files are not password-protected
- Large files (>100MB) may take longer to process
- Check the preview to verify data loaded correctly

### Step 2: Configure Operations

#### Data Cleaning Operations

**Remove Duplicates**
- Select columns to check for duplicates
- Choose which duplicate to keep (first, last, or none)
- Use case: Remove duplicate customer records

**Fill Missing Values**
- Choose fill method: Forward Fill, Backward Fill, Mean, Median, Mode, or Custom Value
- Use case: Fill missing sales data with average values

**Remove Empty Rows/Columns**
- Automatically removes completely empty rows or columns
- Use case: Clean up imported data with blank rows

#### Filtering Operations

**Filter Rows**
- Select column to filter
- Choose operator: ==, !=, >, <, >=, <=, contains, not contains
- Enter filter value
- Use case: Filter sales data for specific regions

#### Column Operations

**Merge Columns**
- Select multiple columns to merge
- Specify separator (space, comma, etc.)
- Name the new merged column
- Use case: Combine first name and last name

**Split Column**
- Select column to split
- Specify separator
- Name the new columns
- Use case: Split full address into street, city, state

**Rename Column**
- Select column to rename
- Enter new name
- Use case: Standardize column names

**Delete Column**
- Select columns to remove
- Use case: Remove unnecessary columns before analysis

#### Mathematical Operations

**Basic Arithmetic**
- Add, Subtract, Multiply, Divide columns
- Specify result column name
- Use case: Calculate profit (Sales - Cost)

**Aggregate Functions**
- Sum, Mean, Median, Min, Max across multiple columns
- Use case: Calculate total score from multiple test scores

**Percentage Change**
- Calculate percentage change between two columns
- Use case: Calculate sales growth rate

**Conditional Calculation**
- Set condition (column, operator, threshold)
- Specify values for true/false conditions
- Use case: Apply discount if purchase amount > $100

#### Text Operations

**Case Conversion**
- Lowercase, Uppercase, Title Case
- Use case: Standardize text formatting

**Trim Spaces**
- Remove leading and trailing spaces
- Use case: Clean up imported data

**Replace Text**
- Find and replace text in column
- Use case: Standardize product names

#### Date Operations

**Convert to Date**
- Parse text as date with specified format
- Use case: Convert "2024-01-15" to date type

**Extract Date Components**
- Extract year, month, or day from date
- Use case: Group sales by month

**Format Date**
- Change date display format
- Use case: Convert "2024-01-15" to "15-Jan-2024"

### Step 3: Preview & Execute

1. Review the operations queue
2. Click "Execute All Operations"
3. View preview of transformed data
4. Check for any errors or unexpected results

**Tips:**
- Start with a small subset of operations to test
- Use preview to verify results before downloading
- Operations are applied in the order they were added

### Step 4: Download Results

1. Review final results
2. Click download button for each processed file
3. Files are named with timestamp for version control

**Output Format:**
- Same format as input (Excel .xlsx)
- All sheets preserved
- Original formatting maintained where possible

## Technical Documentation

### Architecture

```
┌─────────────────┐
│   Streamlit UI  │
└────────┬────────┘
         │
    ┌────▼────┐
    │  app.py │
    └────┬────┘
         │
    ┌────▼──────────────────────┐
    │     Utils Package         │
    ├───────────────────────────┤
    │ • file_handler.py         │
    │ • data_transformer.py     │
    │ • template_manager.py     │
    └───────────────────────────┘
```

### Module Descriptions

#### app.py
Main application file containing:
- Streamlit UI configuration
- Session state management
- Step-by-step workflow implementation
- Operation configuration interfaces

#### utils/file_handler.py
Handles file operations:
- File validation
- Excel file loading
- Multi-sheet support
- File information extraction

#### utils/data_transformer.py
Core transformation engine:
- Operation execution
- Data cleaning
- Mathematical operations
- Text and date operations

#### utils/template_manager.py
Template management:
- Save operation workflows
- Load saved templates
- Template listing and deletion

### Data Flow

1. **Upload**: User uploads Excel file(s)
2. **Validation**: FileHandler validates format and structure
3. **Loading**: Data loaded into Pandas DataFrames
4. **Configuration**: User configures operations via UI
5. **Execution**: DataTransformer applies operations sequentially
6. **Preview**: Results displayed for review
7. **Download**: Processed data exported to Excel

### Error Handling

The application includes comprehensive error handling:

```python
try:
    # Operation execution
    result = transformer.apply_operation(df, operation)
except ValueError as e:
    # Handle invalid values
    logger.error(f"Value error: {str(e)}")
except KeyError as e:
    # Handle missing columns
    logger.error(f"Column not found: {str(e)}")
except Exception as e:
    # Handle unexpected errors
    logger.error(f"Unexpected error: {str(e)}")
```

## API Reference

### FileHandler Class

```python
class FileHandler:
    """Handles Excel file operations."""
    
    def validate_file(self, file) -> bool:
        """Validate file format."""
        
    def load_excel(self, file) -> Dict[str, pd.DataFrame]:
        """Load Excel file and return DataFrames."""
        
    def get_file_info(self, dataframes: Dict) -> Dict:
        """Get file statistics."""
```

### DataTransformer Class

```python
class DataTransformer:
    """Applies data transformations."""
    
    def apply_operation(self, df: pd.DataFrame, operation: Dict) -> pd.DataFrame:
        """Apply single operation to DataFrame."""
        
    def _apply_cleaning(self, df: pd.DataFrame, operation: Dict) -> pd.DataFrame:
        """Apply cleaning operations."""
        
    def _apply_mathematical(self, df: pd.DataFrame, operation: Dict) -> pd.DataFrame:
        """Apply mathematical operations."""
```

### TemplateManager Class

```python
class TemplateManager:
    """Manages operation templates."""
    
    def save_template(self, name: str, operations: List[Dict]) -> bool:
        """Save operations as template."""
        
    def load_template(self, name: str) -> Optional[Dict]:
        """Load template by name."""
        
    def list_templates(self) -> List[str]:
        """List all templates."""
```

## Examples

### Example 1: Clean Sales Data

**Objective**: Remove duplicates, fill missing values, calculate profit

**Steps**:
1. Upload sales data file
2. Add operation: Remove Duplicates (all columns, keep first)
3. Add operation: Fill Missing Values (Sales column, method: Mean)
4. Add operation: Subtract Columns (Sales - Cost = Profit)
5. Execute and download

### Example 2: Merge Customer Names

**Objective**: Combine first and last name columns

**Steps**:
1. Upload customer data
2. Add operation: Merge Columns (First Name, Last Name, separator: space, new column: Full Name)
3. Add operation: Delete Column (First Name, Last Name)
4. Execute and download

### Example 3: Filter and Calculate

**Objective**: Filter high-value sales and calculate commission

**Steps**:
1. Upload sales data
2. Add operation: Filter Rows (Sales > 1000)
3. Add operation: Multiply Columns (Sales * 0.1 = Commission)
4. Execute and download

### Example 4: Date Processing

**Objective**: Extract month from date and group data

**Steps**:
1. Upload transaction data
2. Add operation: Convert to Date (Date column, format: %Y-%m-%d)
3. Add operation: Extract Month (Date column)
4. Execute and download

## Troubleshooting

### Common Issues

**Issue**: File upload fails
- **Solution**: Check file format (.xlsx or .xls), ensure file is not corrupted

**Issue**: Operation fails with "Column not found"
- **Solution**: Verify column name spelling, check if previous operations removed the column

**Issue**: Mathematical operation returns NaN
- **Solution**: Check for missing values, ensure columns contain numeric data

**Issue**: Template not loading
- **Solution**: Verify template file exists in templates/ directory

### Performance Tips

1. **Large Files**: Process in batches if file > 100MB
2. **Multiple Operations**: Group similar operations together
3. **Preview**: Use preview before executing all operations
4. **Templates**: Save frequently used workflows as templates

## Support

For issues, questions, or contributions:
- Create an issue on GitHub
- Contact: [your-email@example.com]
- Documentation: [link to docs]

## Version History

- **v1.0.0** (2024-01-15): Initial release
  - Core functionality
  - Template system
  - Multi-file support
