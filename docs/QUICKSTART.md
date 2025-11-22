# 🚀 Quick Start Guide

Get up and running with the Excel Data Massaging Tool in 5 minutes!

## Installation (2 minutes)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## Your First Transformation (3 minutes)

### Example: Process Sample Sales Data

We'll clean sales data, remove duplicates, and calculate profit margins.

#### Step 1: Upload File (30 seconds)
1. Click "Browse files" in Step 1
2. Select `sample_data/sample_input.xlsx`
3. See preview of your data

#### Step 2: Add Operations (1 minute)

**Operation 1: Remove Duplicates**
- Select "Data Cleaning"
- Choose "Remove Duplicates"
- Keep: "first"
- Click "Add Operation"

**Operation 2: Fill Missing Values**
- Select "Data Cleaning"
- Choose "Fill Missing Values"
- Column: "Sales"
- Method: "Mean"
- Click "Add Operation"

**Operation 3: Calculate Profit**
- Select "Mathematical Operations"
- Choose "Subtract Columns"
- First column: "Sales"
- Second column: "Cost"
- Result column: "Profit"
- Click "Add Operation"

**Operation 4: Calculate Profit Margin**
- Select "Mathematical Operations"
- Choose "Divide Columns"
- First column: "Profit"
- Second column: "Sales"
- Result column: "Profit_Ratio"
- Click "Add Operation"

#### Step 3: Execute (30 seconds)
1. Go to "Step 3: Preview & Execute"
2. Click "Execute All Operations"
3. Review the preview

#### Step 4: Download (30 seconds)
1. Go to "Step 4: Download Results"
2. Click "Download" button
3. Open the file in Excel

## Common Use Cases

### Use Case 1: Merge Name Columns
```
Operation: Merge Columns
Columns: First Name, Last Name
Separator: " "
New Column: Full Name
```

### Use Case 2: Filter High-Value Transactions
```
Operation: Filter Rows
Column: Amount
Operator: >
Value: 1000
```

### Use Case 3: Standardize Text
```
Operation: Lowercase
Column: Email
```

### Use Case 4: Extract Date Components
```
Operation: Extract Month
Column: Transaction Date
```

## Save Your Workflow

1. After configuring operations, go to sidebar
2. Enter template name: "Sales Processing"
3. Click "Save Current Operations"
4. Next time, just load the template!

## Tips for Success

✅ **Start Small**: Test with a few operations first  
✅ **Use Preview**: Always preview before downloading  
✅ **Save Templates**: Save frequently used workflows  
✅ **Check Data Types**: Ensure columns have correct data types  
✅ **Order Matters**: Operations execute in the order added  

## Next Steps

- Read [DOCUMENTATION.md](DOCUMENTATION.md) for detailed guide
- Explore all operation types
- Create custom templates for your workflows
- Process your own data files

## Need Help?

- Check [DOCUMENTATION.md](DOCUMENTATION.md) for detailed documentation
- Review sample files in `sample_data/` directory
- See operation examples in documentation

Happy data processing! 🎉
