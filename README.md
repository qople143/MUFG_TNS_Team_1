# 📊 Excel Data Messaging Tool

A powerful, user-friendly Streamlit application for Excel data transformation and processing.

> **Case Study Project**: Building a Data Structuring Tool for Excel  
> **Status**: ✅ Complete and Production-Ready  
> **Version**: 1.0.0

## 🎬 Quick Demo

```bash
# One-command setup and run
./run.sh
```

Or manually:
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🎯 Features

### Data Cleaning
- Remove duplicates
- Remove empty rows/columns
- Fill missing values (forward fill, backward fill, mean, median, mode, custom value)

### Filtering
- Filter rows based on conditions
- Support for multiple operators (==, !=, >, <, >=, <=, contains, not contains)

### Column Operations
- Merge columns
- Split columns
- Rename columns
- Delete columns
- Reorder columns

### Mathematical Operations
- Basic arithmetic (add, subtract, multiply, divide)
- Aggregate functions (sum, mean, median, min, max)
- Percentage change calculations
- Weighted averages
- Conditional calculations

### Text Operations
- Convert to lowercase/uppercase/title case
- Trim spaces
- Replace text
- Extract patterns

### Date Operations
- Convert to date format
- Extract year/month/day
- Format dates

### Additional Features
- **Multi-file support**: Upload and process multiple Excel files
- **Multi-sheet support**: Handle Excel files with multiple sheets
- **Template system**: Save and reuse transformation workflows
- **Preview feature**: Preview results before downloading
- **Error handling**: Graceful error handling with detailed messages
- **Logging**: Built-in logging for debugging and audit

## 🚀 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd excel-data-massaging-tool
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Follow the 4-step workflow:
   - **Step 1**: Upload Excel files
   - **Step 2**: Configure operations
   - **Step 3**: Preview and execute
   - **Step 4**: Download results

## 📁 Project Structure

```
excel-data-massaging-tool/
├── app.py                      # Main Streamlit application
├── utils/
│   ├── __init__.py
│   ├── file_handler.py         # File upload and validation
│   ├── data_transformer.py     # Data transformation operations
│   └── template_manager.py     # Template save/load functionality
├── docs/                       # Complete documentation
│   ├── START_HERE.md          # Quick start guide
│   ├── QUICKSTART.md          # 5-minute tutorial
│   ├── DOCUMENTATION.md       # Complete manual
│   ├── DEMO_SCRIPT.md         # Demo walkthrough
│   ├── PROJECT_SUMMARY.md     # Executive summary
│   ├── PROJECT_OVERVIEW.md    # Full overview
│   ├── PRESENTATION.md        # Presentation slides
│   └── CHECKLIST.md           # Requirements checklist
├── templates/                  # Saved operation templates
├── sample_data/               # Sample input/output files
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 📚 Documentation

Comprehensive documentation is available in the `docs/` folder:

- **[START_HERE.md](docs/START_HERE.md)** - Quick start guide
- **[QUICKSTART.md](docs/QUICKSTART.md)** - 5-minute tutorial
- **[DOCUMENTATION.md](docs/DOCUMENTATION.md)** - Complete user manual
- **[DEMO_SCRIPT.md](docs/DEMO_SCRIPT.md)** - Video demonstration script
- **[PROJECT_SUMMARY.md](docs/PROJECT_SUMMARY.md)** - Executive summary
- **[PROJECT_OVERVIEW.md](docs/PROJECT_OVERVIEW.md)** - Full project overview
- **[PRESENTATION.md](docs/PRESENTATION.md)** - Presentation slides
- **[CHECKLIST.md](docs/CHECKLIST.md)** - Requirements verification

## 📝 Code Documentation

All functions and classes include comprehensive docstrings following Google style.

## 📊 Sample Files

Sample input and output files are provided in the `sample_data/` directory:
- `sample_input.xlsx`: Example input file with raw data
- `sample_output.xlsx`: Example output file after transformations

## 🧪 Testing

The application includes error handling for:
- Invalid file formats
- Missing columns
- Invalid operations
- Data type mismatches
- Empty datasets

## 🔧 Technical Details

- **Framework**: Streamlit
- **Data Processing**: Pandas
- **Excel I/O**: OpenPyXL
- **Numerical Operations**: NumPy

## 📋 Requirements Met

✅ File upload with validation  
✅ Flexible operation configuration  
✅ Data cleaning operations  
✅ Mathematical operations (3+ types)  
✅ Text operations  
✅ Date operations  
✅ Preview feature  
✅ Error handling  
✅ Template system  
✅ Multi-file and multi-sheet support  
✅ Comprehensive documentation  
✅ Modular code structure  


## 📄 License

MIT License

