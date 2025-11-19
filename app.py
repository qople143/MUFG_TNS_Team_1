"""
Excel Data Massaging Tool - Main Application
A user-friendly Streamlit application for Excel data transformation and processing.
"""

import streamlit as st
import pandas as pd
import io
from datetime import datetime
import json
from typing import Dict, List, Any
import traceback

# Import custom modules
from utils.file_handler import FileHandler
from utils.data_transformer import DataTransformer
from utils.template_manager import TemplateManager

# Page configuration
st.set_page_config(
    page_title="Excel Data Massaging Tool",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .step-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .success-box {
        padding: 1rem;
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
    }
    .error-box {
        padding: 1rem;
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []
if 'dataframes' not in st.session_state:
    st.session_state.dataframes = {}
if 'operations' not in st.session_state:
    st.session_state.operations = []
if 'processed_data' not in st.session_state:
    st.session_state.processed_data = None


def main():
    """Main application function."""
    
    # Header
    st.markdown('<div class="main-header">📊 Excel Data Massaging Tool</div>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("📋 Navigation")
        step = st.radio(
            "Select Step:",
            ["1️⃣ Upload Files", "2️⃣ Configure Operations", "3️⃣ Preview & Execute", "4️⃣ Download Results"],
            index=0
        )
        
        st.markdown("---")
        st.header("💾 Templates")
        template_manager = TemplateManager()
        
        # Load template
        saved_templates = template_manager.list_templates()
        if saved_templates:
            selected_template = st.selectbox("Load Template:", ["None"] + saved_templates)
            if selected_template != "None" and st.button("Load"):
                template_data = template_manager.load_template(selected_template)
                if template_data:
                    st.session_state.operations = template_data.get('operations', [])
                    st.success(f"Template '{selected_template}' loaded!")
        
        # Save template
        st.markdown("---")
        template_name = st.text_input("Template Name:")
        if st.button("Save Current Operations") and template_name:
            template_manager.save_template(template_name, st.session_state.operations)
            st.success(f"Template '{template_name}' saved!")
    
    # Main content based on selected step
    if step == "1️⃣ Upload Files":
        step_1_upload_files()
    elif step == "2️⃣ Configure Operations":
        step_2_configure_operations()
    elif step == "3️⃣ Preview & Execute":
        step_3_preview_execute()
    elif step == "4️⃣ Download Results":
        step_4_download_results()


def step_1_upload_files():
    """Step 1: File Upload Interface."""
    st.markdown('<div class="step-header">Step 1: Upload Excel Files</div>', unsafe_allow_html=True)
    
    uploaded_files = st.file_uploader(
        "Upload Excel files (.xlsx, .xls)",
        type=['xlsx', 'xls'],
        accept_multiple_files=True,
        help="You can upload multiple Excel files"
    )
    
    if uploaded_files:
        file_handler = FileHandler()
        
        for uploaded_file in uploaded_files:
            try:
                # Validate and load file
                df_dict = file_handler.load_excel(uploaded_file)
                
                if df_dict:
                    st.session_state.dataframes[uploaded_file.name] = df_dict
                    
                    st.success(f"✅ Successfully loaded: {uploaded_file.name}")
                    
                    # Display file info
                    with st.expander(f"📄 Preview: {uploaded_file.name}"):
                        for sheet_name, df in df_dict.items():
                            st.write(f"**Sheet: {sheet_name}**")
                            st.write(f"Rows: {len(df)}, Columns: {len(df.columns)}")
                            st.dataframe(df.head(10), use_container_width=True)
                            
            except Exception as e:
                st.error(f"❌ Error loading {uploaded_file.name}: {str(e)}")
    
    if st.session_state.dataframes:
        st.info(f"📊 Total files loaded: {len(st.session_state.dataframes)}")


def step_2_configure_operations():
    """Step 2: Configure Data Operations."""
    st.markdown('<div class="step-header">Step 2: Configure Operations</div>', unsafe_allow_html=True)
    
    if not st.session_state.dataframes:
        st.warning("⚠️ Please upload files first!")
        return
    
    # Select file and sheet
    col1, col2 = st.columns(2)
    with col1:
        selected_file = st.selectbox("Select File:", list(st.session_state.dataframes.keys()))
    with col2:
        selected_sheet = st.selectbox("Select Sheet:", list(st.session_state.dataframes[selected_file].keys()))
    
    df = st.session_state.dataframes[selected_file][selected_sheet]
    
    # Operation categories
    st.markdown("### Select Operation Type")
    operation_type = st.selectbox(
        "Operation Category:",
        ["Data Cleaning", "Filtering", "Column Operations", "Mathematical Operations", "Text Operations", "Date Operations"]
    )
    
    # Configure operation based on type
    operation_config = {}
    
    if operation_type == "Data Cleaning":
        operation_config = configure_data_cleaning(df)
    elif operation_type == "Filtering":
        operation_config = configure_filtering(df)
    elif operation_type == "Column Operations":
        operation_config = configure_column_operations(df)
    elif operation_type == "Mathematical Operations":
        operation_config = configure_mathematical_operations(df)
    elif operation_type == "Text Operations":
        operation_config = configure_text_operations(df)
    elif operation_type == "Date Operations":
        operation_config = configure_date_operations(df)
    
    # Add operation
    if st.button("➕ Add Operation", type="primary"):
        if operation_config:
            operation_config['file'] = selected_file
            operation_config['sheet'] = selected_sheet
            operation_config['type'] = operation_type
            st.session_state.operations.append(operation_config)
            st.success("✅ Operation added!")
    
    # Display current operations
    if st.session_state.operations:
        st.markdown("---")
        st.markdown("### 📋 Current Operations Queue")
        for idx, op in enumerate(st.session_state.operations):
            with st.expander(f"Operation {idx + 1}: {op['type']} - {op.get('operation', '')}"):
                st.json(op)
                if st.button(f"🗑️ Remove", key=f"remove_{idx}"):
                    st.session_state.operations.pop(idx)
                    st.rerun()


def configure_data_cleaning(df: pd.DataFrame) -> Dict[str, Any]:
    """Configure data cleaning operations."""
    operation = st.selectbox(
        "Cleaning Operation:",
        ["Remove Duplicates", "Remove Empty Rows", "Remove Empty Columns", "Fill Missing Values"]
    )
    
    config = {'operation': operation}
    
    if operation == "Remove Duplicates":
        columns = st.multiselect("Select columns to check for duplicates:", df.columns.tolist())
        config['columns'] = columns
        config['keep'] = st.selectbox("Keep:", ["first", "last", False])
    
    elif operation == "Fill Missing Values":
        column = st.selectbox("Select column:", df.columns.tolist())
        method = st.selectbox("Fill method:", ["Forward Fill", "Backward Fill", "Mean", "Median", "Mode", "Custom Value"])
        config['column'] = column
        config['method'] = method
        if method == "Custom Value":
            config['value'] = st.text_input("Fill value:")
    
    return config


def configure_filtering(df: pd.DataFrame) -> Dict[str, Any]:
    """Configure filtering operations."""
    column = st.selectbox("Select column to filter:", df.columns.tolist())
    operator = st.selectbox("Operator:", ["==", "!=", ">", "<", ">=", "<=", "contains", "not contains"])
    value = st.text_input("Value:")
    
    return {
        'operation': 'Filter Rows',
        'column': column,
        'operator': operator,
        'value': value
    }


def configure_column_operations(df: pd.DataFrame) -> Dict[str, Any]:
    """Configure column operations."""
    operation = st.selectbox(
        "Column Operation:",
        ["Merge Columns", "Split Column", "Rename Column", "Delete Column", "Reorder Columns"]
    )
    
    config = {'operation': operation}
    
    if operation == "Merge Columns":
        columns = st.multiselect("Select columns to merge:", df.columns.tolist())
        separator = st.text_input("Separator:", value=" ")
        new_column = st.text_input("New column name:")
        config.update({'columns': columns, 'separator': separator, 'new_column': new_column})
    
    elif operation == "Split Column":
        column = st.selectbox("Select column:", df.columns.tolist())
        separator = st.text_input("Separator:", value=",")
        new_columns = st.text_input("New column names (comma-separated):")
        config.update({'column': column, 'separator': separator, 'new_columns': new_columns.split(',')})
    
    elif operation == "Rename Column":
        old_name = st.selectbox("Select column:", df.columns.tolist())
        new_name = st.text_input("New name:")
        config.update({'old_name': old_name, 'new_name': new_name})
    
    elif operation == "Delete Column":
        columns = st.multiselect("Select columns to delete:", df.columns.tolist())
        config['columns'] = columns
    
    return config


def configure_mathematical_operations(df: pd.DataFrame) -> Dict[str, Any]:
    """Configure mathematical operations."""
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    
    operation = st.selectbox(
        "Mathematical Operation:",
        ["Add Columns", "Subtract Columns", "Multiply Columns", "Divide Columns", 
         "Percentage Change", "Weighted Average", "Sum", "Mean", "Median", "Min", "Max",
         "Conditional Calculation"]
    )
    
    config = {'operation': operation}
    
    if operation in ["Add Columns", "Subtract Columns", "Multiply Columns", "Divide Columns"]:
        col1 = st.selectbox("First column:", numeric_cols, key="math_col1")
        col2 = st.selectbox("Second column:", numeric_cols, key="math_col2")
        result_col = st.text_input("Result column name:")
        config.update({'col1': col1, 'col2': col2, 'result_column': result_col})
    
    elif operation in ["Sum", "Mean", "Median", "Min", "Max"]:
        columns = st.multiselect("Select columns:", numeric_cols)
        result_col = st.text_input("Result column name:")
        config.update({'columns': columns, 'result_column': result_col})
    
    elif operation == "Conditional Calculation":
        condition_col = st.selectbox("Condition column:", df.columns.tolist())
        operator = st.selectbox("Operator:", [">", "<", ">=", "<=", "==", "!="])
        threshold = st.number_input("Threshold value:")
        true_value = st.text_input("Value if true:")
        false_value = st.text_input("Value if false:")
        result_col = st.text_input("Result column name:")
        config.update({
            'condition_col': condition_col,
            'operator': operator,
            'threshold': threshold,
            'true_value': true_value,
            'false_value': false_value,
            'result_column': result_col
        })
    
    return config


def configure_text_operations(df: pd.DataFrame) -> Dict[str, Any]:
    """Configure text operations."""
    text_cols = df.select_dtypes(include=['object']).columns.tolist()
    
    operation = st.selectbox(
        "Text Operation:",
        ["Lowercase", "Uppercase", "Title Case", "Trim Spaces", "Replace Text", "Extract Pattern"]
    )
    
    config = {'operation': operation}
    
    column = st.selectbox("Select column:", text_cols)
    config['column'] = column
    
    if operation == "Replace Text":
        old_text = st.text_input("Text to replace:")
        new_text = st.text_input("Replace with:")
        config.update({'old_text': old_text, 'new_text': new_text})
    
    return config


def configure_date_operations(df: pd.DataFrame) -> Dict[str, Any]:
    """Configure date operations."""
    operation = st.selectbox(
        "Date Operation:",
        ["Convert to Date", "Extract Year", "Extract Month", "Extract Day", "Format Date"]
    )
    
    column = st.selectbox("Select column:", df.columns.tolist())
    
    config = {'operation': operation, 'column': column}
    
    if operation == "Convert to Date":
        format_str = st.text_input("Date format (e.g., %Y-%m-%d):", value="%Y-%m-%d")
        config['format'] = format_str
    
    elif operation == "Format Date":
        output_format = st.text_input("Output format:", value="%Y-%m-%d")
        config['output_format'] = output_format
    
    return config


def step_3_preview_execute():
    """Step 3: Preview and Execute Operations."""
    st.markdown('<div class="step-header">Step 3: Preview & Execute</div>', unsafe_allow_html=True)
    
    if not st.session_state.operations:
        st.warning("⚠️ No operations configured!")
        return
    
    # Display operations summary
    st.markdown("### 📋 Operations Summary")
    for idx, op in enumerate(st.session_state.operations):
        st.write(f"{idx + 1}. **{op['type']}** - {op.get('operation', '')} on {op['file']}/{op['sheet']}")
    
    st.markdown("---")
    
    # Execute button
    if st.button("▶️ Execute All Operations", type="primary"):
        with st.spinner("Processing..."):
            try:
                transformer = DataTransformer()
                processed_data = {}
                
                # Process each file
                for file_name, sheets in st.session_state.dataframes.items():
                    processed_data[file_name] = {}
                    
                    for sheet_name, df in sheets.items():
                        # Get operations for this file/sheet
                        relevant_ops = [op for op in st.session_state.operations 
                                      if op['file'] == file_name and op['sheet'] == sheet_name]
                        
                        # Apply operations
                        result_df = df.copy()
                        for op in relevant_ops:
                            result_df = transformer.apply_operation(result_df, op)
                        
                        processed_data[file_name][sheet_name] = result_df
                
                st.session_state.processed_data = processed_data
                st.success("✅ All operations executed successfully!")
                
            except Exception as e:
                st.error(f"❌ Error during execution: {str(e)}")
                st.code(traceback.format_exc())
    
    # Preview results
    if st.session_state.processed_data:
        st.markdown("---")
        st.markdown("### 👁️ Preview Results")
        
        for file_name, sheets in st.session_state.processed_data.items():
            with st.expander(f"📄 {file_name}"):
                for sheet_name, df in sheets.items():
                    st.write(f"**Sheet: {sheet_name}**")
                    st.write(f"Rows: {len(df)}, Columns: {len(df.columns)}")
                    st.dataframe(df.head(20), use_container_width=True)


def step_4_download_results():
    """Step 4: Download Processed Files."""
    st.markdown('<div class="step-header">Step 4: Download Results</div>', unsafe_allow_html=True)
    
    if not st.session_state.processed_data:
        st.warning("⚠️ No processed data available. Please execute operations first!")
        return
    
    st.markdown("### 📥 Download Processed Files")
    
    for file_name, sheets in st.session_state.processed_data.items():
        # Create Excel file in memory
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            for sheet_name, df in sheets.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        output.seek(0)
        
        # Generate download button
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        download_name = f"processed_{file_name.replace('.xlsx', '')}_{timestamp}.xlsx"
        
        st.download_button(
            label=f"📥 Download {file_name}",
            data=output,
            file_name=download_name,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    
    st.success("✅ Files ready for download!")


if __name__ == "__main__":
    main()
