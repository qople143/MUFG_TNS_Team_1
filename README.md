# Excel Data Massaging Tool

A user-friendly Python application that transforms and cleans Excel data through an interactive Jupyter notebook interface. Upload your Excel files, apply powerful data transformation operations, and download processed results.

## 🎯 Features

### Data Cleaning Operations

- **Remove Duplicates** - Eliminate duplicate rows based on specified columns
- **Filter Rows** - Filter data using conditions (equals, greater than, contains, etc.)
- **Replace Values** - Find and replace values in columns
- **Merge Columns** - Combine multiple columns with custom separators
- **Normalize Text** - Convert text to lowercase, uppercase, title case, or trim spaces
- **Convert Date Formats** - Parse and format dates in multiple formats

### Mathematical Operations

- **Add/Subtract Columns** - Perform arithmetic operations between columns
- **Multiply/Divide Columns** - Multiply or divide column values
- **Percentage Change** - Calculate percentage change between two columns
- **Aggregate Functions** - Sum, mean, median, min, and max calculations
- **Conditional Calculations** - Apply if-then-else logic to create new columns

### Core Features

- 📤 **File Upload** - Upload single or multiple `.xlsx` files
- 👁️ **Preview** - Preview transformations before applying them
- 📥 **Download** - Download results as Excel files
- ✅ **Validation** - Automatic file format and structure validation
- 🛡️ **Error Handling** - Graceful error messages for debugging
- 📊 **Sample Data** - Included example files to get started quickly

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Jupyter Notebook or JupyterLab
- pip (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/qople143/MUFG_TNS_Team_1
   cd MUFG_TNS_Team_1
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**

   ```bash
   jupyter notebook
   ```

5. **Open the application**
   - Navigate to `notebooks/01_main.ipynb`
   - Click "Run All" or run cells individually

## 📖 Usage Guide

### Basic Workflow

1. **Upload File**

   - Click the file upload button
   - Select your `.xlsx` file
   - View preview of your data

2. **Select Operation**

   - Choose an operation from the dropdown menu
   - Enter operation parameters (column names, values, conditions, etc.)
   - Click "Preview" to see the result

3. **Review Results**

   - Check the transformed data in the preview window
   - Verify the changes are correct
   - Modify operation parameters if needed

4. **Download**
   - Click "Download" to save the transformed file
   - File will be saved as `transformed.xlsx`

### Example: Remove Duplicates

```python
from src.operations import RemoveDuplicates
import pandas as pd

# Load your Excel file
df = pd.read_excel('data.xlsx')

# Create operation
op = RemoveDuplicates(columns=['id', 'email'])

# Apply operation
result = op.apply(df)

# Save result
result.to_excel('data_cleaned.xlsx', index=False)
```

### Example: Filter Rows

```python
from src.operations import FilterRows

# Filter for age > 30
op = FilterRows('age', '>', 30)
result = op.apply(df)
```

### Example: Replace Values

```python
from src.operations import ReplaceValues

# Replace 'NYC' with 'New York'
op = ReplaceValues('city', 'NYC', 'New York')
result = op.apply(df)
```

## 📁 Project Structure

```
MUFG_TNS_Team_1/
├── notebooks/
│   ├── 00_DEMO.ipynb              # Demo walkthrough (coming soon)
│   ├── 01_main.ipynb              # Main application
│   └── 02_exploration.ipynb       # Development notebook
│
├── src/
│   ├── __init__.py                # Package initialization
│   ├── operations.py              # Data transformation operations
│   ├── transformer.py             # Main orchestrator (coming soon)
│   ├── file_handler.py            # File I/O utilities
│   └── ui_helper.py               # UI helper functions
│
├── tests/
│   ├── __init__.py
│   ├── test_operations.py         # Operation unit tests
│   ├── test_file_handler.py       # File handler tests (coming soon)
│   └── test_transformer.py        # Transformer tests (coming soon)
│
├── sample_data/
│   ├── sample_input.xlsx          # Example input file
│   └── sample_output.xlsx         # Example output file
│
├── docs/
│   ├── OPERATIONS.md              # Detailed operation reference
│   ├── INSTALLATION.md            # Detailed setup guide
│   ├── TROUBLESHOOTING.md         # FAQ and common issues
│   └── ARCHITECTURE.md            # Code structure overview
│
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── QUICK_START.md                 # Quick reference guide
├── CHANGELOG.md                   # Version history
└── .gitignore                     # Git ignore rules
```

## 🔧 Supported Operations

### Data Cleaning

| Operation                | Description           | Parameters                                  |
| ------------------------ | --------------------- | ------------------------------------------- |
| **Remove Duplicates**    | Remove duplicate rows | `columns` (optional), `keep` (first/last)   |
| **Filter Rows**          | Filter by condition   | `column`, `operator`, `value`               |
| **Replace Values**       | Find and replace      | `column`, `old_value`, `new_value`          |
| **Merge Columns**        | Combine columns       | `columns`, `separator`                      |
| **Normalize Text**       | Format text           | `column`, `method` (lower/upper/trim/title) |
| **Convert Date Formats** | Parse/format dates    | `column`, `from_format`, `to_format`        |

### Mathematical Operations

| Operation                    | Description          | Parameters                                   |
| ---------------------------- | -------------------- | -------------------------------------------- |
| **Add Columns**              | Add two columns      | `column1`, `column2`, `result_name`          |
| **Subtract Columns**         | Subtract two columns | `column1`, `column2`, `result_name`          |
| **Multiply Columns**         | Multiply two columns | `column1`, `column2`, `result_name`          |
| **Divide Columns**           | Divide two columns   | `column1`, `column2`, `result_name`          |
| **Percentage Change**        | Calculate % change   | `old_value_col`, `new_value_col`             |
| **Aggregate Functions**      | Sum/Mean/Min/Max     | `column`, `function`, `group_by`             |
| **Conditional Calculations** | If-then logic        | `condition_col`, `true_value`, `false_value` |

## 🧪 Testing

Run all tests to ensure everything is working correctly:

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_operations.py -v

# Run with coverage report
pytest tests/ -v --cov=src
```

**Current Test Coverage:** 16+ tests across all modules

## 📋 Requirements

- `pandas>=1.3.0` - Data manipulation and Excel I/O
- `openpyxl>=3.6.0` - Excel file handling
- `jupyter>=1.0.0` - Notebook environment
- `ipywidgets>=7.6.0` - Interactive widgets for Jupyter
- `pytest>=6.0.0` - Testing framework
- `python-dateutil>=2.8.0` - Date utilities
- `numpy>=1.20.0` - Numerical computing

See `requirements.txt` for complete list.

## 📚 Documentation

- **[QUICK_START.md](./QUICK_START.md)** - Quick reference for common tasks
- **[OPERATIONS.md](./docs/OPERATIONS.md)** - Detailed operation documentation (coming soon)
- **[INSTALLATION.md](./docs/INSTALLATION.md)** - Detailed setup instructions (coming soon)
- **[TROUBLESHOOTING.md](./docs/TROUBLESHOOTING.md)** - FAQ and troubleshooting (coming soon)
- **[ARCHITECTURE.md](./docs/ARCHITECTURE.md)** - Code structure and design (coming soon)

## 🐛 Troubleshooting

### Issue: File upload widget not showing

**Solution:** Make sure you're running the notebook in JupyterLab or Jupyter Notebook (not VS Code). Install `jupyter` and run `jupyter notebook`.

### Issue: Module import errors

**Solution:** Ensure you're in the project root directory and have installed all dependencies with `pip install -r requirements.txt`.

### Issue: "No module named 'src'"

**Solution:** Make sure you're running the notebook from the project root directory, not from within the notebooks folder.

### Issue: Operation fails with unexpected error

**Solution:** Check that your column names are correct and that your data types match the operation requirements. Review error message for details.

For more troubleshooting, see [TROUBLESHOOTING.md](./docs/TROUBLESHOOTING.md).

## 🗺️ Roadmap

### v1.0.0 (By November 30, 2025)

- 13 core operations (data cleaning + mathematics)
- Interactive Jupyter UI
- File upload and download
- Unit tests and documentation
- Weighted average operation
- Transformation templates (save/reuse)
- Batch file processing
- Advanced logging and audit trails
- Web UI (Streamlit)
- Database integration
- Scheduled batch jobs
- API interface

## 🤝 Contributing

This is a personal project, but contributions and feedback are welcome!

If you find a bug or have a feature request:

1. Check if it's already reported in Issues
2. Open a new Issue with a clear description
3. Include sample data and steps to reproduce if reporting a bug

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 👤 Author

Created as a data transformation tool for Excel processing workflows.

## 📞 Support

For issues, questions, or feedback:

- Open an issue on GitHub
- Check [TROUBLESHOOTING.md](./docs/TROUBLESHOOTING.md) for common problems
- Review [OPERATIONS.md](./docs/OPERATIONS.md) for detailed operation documentation

---

## 🎯 Current Status

**Version:** v0.1.0 (In Development)  
**Last Updated:** November 09, 2025  
**Status:** Active Development

**Completed:**

- ✅ Project setup and repository initialization
- ✅ 3 core operations implemented (RemoveDuplicates, FilterRows, ReplaceValues)
- ✅ Unit tests (16+ tests passing)
- ✅ Basic documentation

**In Progress:**

- 🔄 Additional data cleaning operations
- 🔄 Mathematical operations module
- 🔄 Main Jupyter UI application
- 🔄 File handler and transformer modules

**Coming Soon:**

- ⏳ Demo notebook with examples
- ⏳ Comprehensive documentation
- ⏳ v1.0.0 Release

---
