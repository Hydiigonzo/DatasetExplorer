# DatasetExplorer
# 🌸 Iris Dataset Explorer

A Streamlit web application for exploring the famous Iris flower dataset with interactive filters and visualizations.

## Features

- **Interactive Filtering**: Filter data by species and feature ranges using sliders
- **Real-time Statistics**: View summary statistics that update as you filter
- **Multiple Visualizations**: 
  - Interactive scatter plots
  - Correlation heatmaps
  - Feature distribution histograms
- **Species Analysis**: Analyze distribution across different iris species
- **Educational Content**: Information about the dataset and its features

## Setup and Installation

### 1. Clone or Download Files
Make sure you have the following files:
- `iris_explorer_app.py` (main app)
- `requirements.txt` (dependencies)

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run iris_explorer_app.py
```

The app will open in your browser at `http://localhost:8501`

## How to Use

1. **Sidebar Controls**: Use the filters in the sidebar to:
   - Select specific iris species
   - Adjust feature ranges with sliders

2. **Main Dashboard**: View:
   - Filtered dataset table
   - Summary statistics
   - Species distribution chart

3. **Visualizations**: Explore three different chart types:
   - **Scatter Plot**: Compare any two features
   - **Correlation Heatmap**: See feature relationships
   - **Distribution**: Analyze feature distributions by species

## Deployment Options

### Streamlit Community Cloud
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy with one click!

### Local Network
To share on your local network:
```bash
streamlit run iris_explorer_app.py --server.address 0.0.0.0
```

## About the Dataset

The Iris dataset contains 150 samples of iris flowers with 4 features each:
- Sepal Length and Width
- Petal Length and Width
- Species (Setosa, Versicolor, Virginica)

Perfect for learning data science, machine learning, and statistical analysis!

## Requirements

- Python 3.7+
- See `requirements.txt` for package dependencies

## Lab Exercise Ideas

- Modify filters to add more complex conditions
- Add new visualization types
- Implement machine learning classification
- Create data export functionality
- Add data upload feature for custom datasets
