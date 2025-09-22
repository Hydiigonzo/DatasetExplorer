
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import plotly.express as px

# Configure the page
st.set_page_config(
    page_title="Iris Dataset Explorer",
    page_icon="🌸",
    layout="wide"
)

# Load the Iris dataset
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target_names[iris.target]
    return df

# Main app function
def main():
    st.title("🌸 Iris Dataset Explorer")
    st.markdown("### Explore the famous Iris flower dataset with interactive filters and visualizations")

    # Load data
    df = load_data()

    # Sidebar for controls
    st.sidebar.header("Filter Controls")
    st.sidebar.markdown("Use the controls below to filter and explore the dataset")

    # Species filter
    species_options = ['All'] + list(df['species'].unique())
    selected_species = st.sidebar.selectbox("Select Species:", species_options)

    # Feature range filters
    st.sidebar.subheader("Feature Ranges")

    sepal_length_range = st.sidebar.slider(
        "Sepal Length (cm)",
        float(df['sepal length (cm)'].min()),
        float(df['sepal length (cm)'].max()),
        (float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
    )

    sepal_width_range = st.sidebar.slider(
        "Sepal Width (cm)",
        float(df['sepal width (cm)'].min()),
        float(df['sepal width (cm)'].max()),
        (float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
    )

    petal_length_range = st.sidebar.slider(
        "Petal Length (cm)",
        float(df['petal length (cm)'].min()),
        float(df['petal length (cm)'].max()),
        (float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
    )

    petal_width_range = st.sidebar.slider(
        "Petal Width (cm)",
        float(df['petal width (cm)'].min()),
        float(df['petal width (cm)'].max()),
        (float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))
    )

    # Apply filters
    filtered_df = df.copy()

    if selected_species != 'All':
        filtered_df = filtered_df[filtered_df['species'] == selected_species]

    filtered_df = filtered_df[
        (filtered_df['sepal length (cm)'] >= sepal_length_range[0]) &
        (filtered_df['sepal length (cm)'] <= sepal_length_range[1]) &
        (filtered_df['sepal width (cm)'] >= sepal_width_range[0]) &
        (filtered_df['sepal width (cm)'] <= sepal_width_range[1]) &
        (filtered_df['petal length (cm)'] >= petal_length_range[0]) &
        (filtered_df['petal length (cm)'] <= petal_length_range[1]) &
        (filtered_df['petal width (cm)'] >= petal_width_range[0]) &
        (filtered_df['petal width (cm)'] <= petal_width_range[1])
    ]

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📊 Filtered Dataset")
        st.write(f"Showing {len(filtered_df)} out of {len(df)} records")
        st.dataframe(filtered_df, use_container_width=True)

    with col2:
        st.subheader("📈 Summary Statistics")
        if len(filtered_df) > 0:
            numeric_columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
            summary_stats = filtered_df[numeric_columns].describe().round(2)
            st.dataframe(summary_stats, use_container_width=True)

            # Species count
            st.subheader("🌺 Species Distribution")
            species_count = filtered_df['species'].value_counts()
            st.bar_chart(species_count)
        else:
            st.warning("No data matches the current filters!")

    # Visualizations
    if len(filtered_df) > 0:
        st.subheader("📈 Data Visualizations")

        # Create tabs for different visualizations
        tab1, tab2, tab3 = st.tabs(["Scatter Plot", "Correlation Heatmap", "Feature Distribution"])

        with tab1:
            col1, col2 = st.columns(2)
            with col1:
                x_axis = st.selectbox("X-axis feature:", numeric_columns, index=0)
            with col2:
                y_axis = st.selectbox("Y-axis feature:", numeric_columns, index=1)

            fig = px.scatter(filtered_df, x=x_axis, y=y_axis, color='species',
                           title=f'{x_axis.title()} vs {y_axis.title()}',
                           height=500)
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            # Correlation heatmap
            corr_matrix = filtered_df[numeric_columns].corr()
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
            ax.set_title('Feature Correlation Matrix')
            st.pyplot(fig)

        with tab3:
            # Feature distribution
            selected_feature = st.selectbox("Select feature for distribution:", numeric_columns)

            fig = px.histogram(filtered_df, x=selected_feature, color='species',
                             title=f'Distribution of {selected_feature.title()}',
                             height=400, marginal="box")
            st.plotly_chart(fig, use_container_width=True)

    # Dataset info
    with st.expander("ℹ️ About the Iris Dataset"):
        st.markdown("""
        The **Iris flower dataset** is a classic dataset in machine learning and statistics, introduced by Ronald Fisher in 1936.

        **Dataset Features:**
        - **Sepal Length**: Length of the sepal in centimeters
        - **Sepal Width**: Width of the sepal in centimeters  
        - **Petal Length**: Length of the petal in centimeters
        - **Petal Width**: Width of the petal in centimeters
        - **Species**: The species of iris flower (Setosa, Versicolor, Virginica)

        **Total Records:** 150 (50 of each species)

        This dataset is commonly used for:
        - Classification algorithms
        - Data visualization techniques
        - Statistical analysis
        - Machine learning tutorials
        """)

if __name__ == "__main__":
    main()
