import streamlit as st
from charts import chartCreator
import plotly.graph_objects as go
import plotly.io as pio
from models import Processor
import PIL.Image
import pyttsx3
from time import sleep
import base64

Process = Processor()

def page2_content():
    chart = chartCreator()

    chart_category = st.sidebar.selectbox("Select chart type",["2D Charts","3D Charts"])

    uploaded_file = st.file_uploader("**Upload your CSV data:**", type=["csv"])

    if chart_category == "2D Charts":
        
        chart_type_2d = st.sidebar.selectbox("Select 2D Chart Type", ["Line Chart", "Bar Chart", "Pie Chart", "Scatter Plot", "Histogram", "Heatmap", "Box Plot"])

        if chart_type_2d == "Line Chart":
            chart.create_line_chart_page(uploaded_file)
        elif chart_type_2d == "Bar Chart":
            chart.create_bar_chart_page(uploaded_file)
        elif chart_type_2d == "Pie Chart":
            chart.create_pie_chart_page(uploaded_file)
        elif chart_type_2d == "Scatter Plot":
            chart.create_scatter_plot_page(uploaded_file)
        elif chart_type_2d == "Histogram":
            chart.create_histogram_page(uploaded_file)
        elif chart_type_2d == "Heatmap":
            chart.create_heatmap_page(uploaded_file)
        elif chart_type_2d == "Box Plot":
            chart.create_box_plot_page(uploaded_file)

    elif chart_category == "3D Charts":
    # 3D Chart options
        chart_type_3d = st.sidebar.selectbox("Select 3D Chart Type", ["Contour3D Plot","3DSurface Plot","3DScatter Plot"])
        if chart_type_3d == "Contour3D Plot":
            chart.create_3d_contour_plot_page(uploaded_file, chart_type_3d)
        elif chart_type_3d == "3DSurface Plot":
            chart.create_3d_surface_plot_page(uploaded_file, chart_type_3d)
        elif chart_type_3d == "3DScatter Plot":
            chart.create_3d_scatter_plot_page(uploaded_file, chart_type_3d)

   
   

def Insights_Generation():
    Prompt = """
    Role: Data Visualization Insight Extractor

    Context: You are an AI system designed to quickly extract and summarize key insights from data visualizations in images.

    Input: An image containing a data visualization (e.g., bar chart, line graph, scatter plot, pie chart).

    Instructions:
    1. Identify the type of chart or graph in the image.
    2. Quickly analyze the main elements and data representation.
    3. Extract 3-5 key insights or trends from the visualization.
    4. Summarize these insights in brief, clear statements.

    Output Expected:
    1. Chart type (in 1-2 words)
    2. 3-5 bullet points of key insights, each 1-2 sentences long
    3. A brief (1-2 sentence) overall summary of the main takeaway

    Important: Focus only on the most significant insights. Keep your response concise and data-driven, based solely on what's clearly shown in the image. If critical information is missing (e.g., axis labels), mention this as a limitation.
    """
    try:
        img = PIL.Image.open('demo.png')
    except:
        pass
    if st.button("GenerateInsights"):
        try:
            redrafted_text = Process.InsightGenerator(Prompt,img) 
            st.markdown( 
                        """
                        <style>
                                .container {
                                    border: 1px solid #ffffff;
                                    padding: 15px;
                                    border-radius: 10px;
                                    margin-top: 20px;
                                    margin-bottom: 20px;
                                    white-space: normal;
                                }
                                
                                .container-header {
                                    color: #ffffff;
                                    font-size: 18px;
                                    font-weight: bold;
                                    margin-bottom: 10px;
                                    background-color: grey;
                                    padding: 5px;
                                    border-radius: 5px;
                                    text-align: center;
                                }
                        </style>
                        """,
                        unsafe_allow_html=True,
                    )
            st.markdown(f"<div class='container-header center-text'>{'Insights Generated'}</div>", unsafe_allow_html=True)
            st.image("demo.png", caption='Example Image', use_column_width=True)
            st.markdown(redrafted_text)         
        
            # Save redrafted_text to a file
            file_path = "response.txt"
            with open(file_path, "w") as file:
                file.write(redrafted_text)

            # Encode data to base64
            encoded_data = base64.b64encode(redrafted_text.encode()).decode()
            href = f'<a href="data:file/txt;base64,{encoded_data}" download="{file_path}">Download Response</a>'
            st.markdown(href, unsafe_allow_html=True)

        except Exception as e:
            st.error("An error occurred: " + str(e))