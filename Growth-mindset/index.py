import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up Streamlit page config
st.set_page_config(page_title="Data Sweeper", layout='wide')

# Custom CSS Styling
st.markdown("""
    <style>
        /* Global Styling */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #F8F9FA;
            color: #000000;
        }

        h1 {
            color: #2C3E50;
            font-size: 36px;
            text-align: center;
            font-weight: bold;
            margin-bottom: 10px;
        }

        h2, .stSubheader {
            color: #2980B9;
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
        }

        /* File Uploader */
        .stFileUploader {
            background-color: #ECF0F1;
            border: 2px dashed #2980B9;
            padding: 20px;
            border-radius: 8px;
        }

        /* Buttons */
        .stButton>button {
            background-color: #2980B9 !important;
            color: white !important;
            border-radius: 8px;
            padding: 10px 15px;
            font-weight: bold;
            border: none;
            transition: all 0.3s ease;
        }

        .stButton>button:hover {
            background-color: #3498DB !important;
            transform: translateY(-3px);
        }

        /* Checkbox, Selectbox & Other Input Labels */
        .stCheckbox label, .stRadio label, .stSelectbox label, .stMultiselect label {
            color: #333 !important;
            font-size: 16px;
        }

        /* DataFrame Styling */
        .stDataFrame {
            background-color: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Footer */
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #2C3E50;
            color: white;
            text-align: center;
            padding: 12px;
            font-size: 14px;
            font-weight: bold;
            box-shadow: 0px -2px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

st.title("Data Sweeper 🌟")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization. 📊")

# File uploader for CSV and Excel files
st.markdown('<p style="color:white; font-size:16px;">Upload your files (CSV or Excel): 📂</p>', unsafe_allow_html=True)
uploaded_files = st.file_uploader("", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        # Read file based on extension
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"❌ Unsupported file type: {file_ext}")
            continue

        # Display file name and size
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024:.2f} KB")

        # Preview data
        st.write("Preview the head of the DataFrame: 👇")
        st.dataframe(df.head())

        # Data cleaning options
        if st.checkbox(f"Clean Data for {file.name} 🧹"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicates from {file.name} 🚫"):
                    df.drop_duplicates(inplace=True)
                    st.write("✅ Duplicates removed!")

            with col2:
                if st.button(f"Fill missing values for {file.name} ✨"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("✅ Missing values have been filled!")

        # Download cleaned data button
        st.download_button(
            label="Download Cleaned Data 💾",
            data=df.to_csv(index=False).encode('utf-8'),
            file_name=f"cleaned_{file.name}",
            mime="text/csv"
        )

        # Choose specific columns to keep or convert
        st.subheader("Select Columns to Convert 📑")
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]

        # Visualization Section
        st.subheader("Data Visualization 📊")

        if st.checkbox(f"Show Visualization for {file.name}"):
            # Ensure there are numeric columns to visualize
            numeric_data = df.select_dtypes(include='number')

            if not numeric_data.empty:
                # Only show the first 10 rows of numeric data to avoid rendering too much data
                st.bar_chart(numeric_data.head(10))
            else:
                st.write("❌ No numeric data available for visualization. Please ensure your dataset contains numeric columns.")

        # Conversion options for CSV to Excel or vice versa
        st.subheader("Conversion Options 🔄")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "EXCEL"], key=file.name)

        # Initialize the file_name variable outside the conversion section
        file_name = ""
        mime_type = ""

        if conversion_type == "CSV":
            buffer = BytesIO()
            df.to_csv(buffer, index=False)
            file_name = file.name.replace(file_ext, ".csv")
            mime_type = "text/csv"
        elif conversion_type == "EXCEL":
            buffer = BytesIO()
            try:
                df.to_excel(buffer, index=False, engine='openpyxl')
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            except Exception as e:
                st.error(f"❌ An error occurred while converting to Excel: {e}")

        if file_name:  # Only create the download button if file_name is set
            buffer.seek(0)
            st.download_button(
                label=f"Download {file.name} as {conversion_type} 📥",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

# Success message at the end
st.success("✅ All files processed successfully!")

# Footer
st.markdown("""
    <div class="footer">
        Made with ❤️ by Rubi Abid, 2025
    </div>
""", unsafe_allow_html=True)
