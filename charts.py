import streamlit as st
import plotly.express as px
import pandas as pd
from PIL import Image
import io
from PIL import Image, ImageOps  # Import ImageOps to handle image conversion
import plotly.graph_objects as go

class chartCreator():
    def create_line_chart_page(self,uploaded_file):
    # Streamlit UI for the Line Chart page
   
        st.title("Line Chart Page")
        if uploaded_file is None:
            st.warning("Please upload a valid CSV file.")
            return

        with st.form("line_chart_form"):
            if uploaded_file is not None:
                # Read the uploaded data
                data = pd.read_csv(uploaded_file)
                # After reading the data

                # User customization options
                chart_title = st.text_input("Chart Title", "Line Chart")
                x_axis = st.selectbox("Select X-axis", data.columns)
                y_axis = st.selectbox("Select Y-axis", data.columns)
                x_label = st.text_input("X-axis Label", "X-axis")
                y_label = st.text_input("Y-axis Label", "Y-axis")
                line_style = st.selectbox("Line Style", ["solid", "dot", "dash", "dashdot"], index=0)
                line_color = st.color_picker("Line Color", "#1f77b4")

                # Submit button to trigger chart creation
                submit_button = st.form_submit_button("Generate Line Chart")

        # Move the chart rendering outside the st.form block
            
        if submit_button:
            # Navigate to another Streamlit page
            fig = px.line(data, x=data[x_axis], y=data[y_axis], title=chart_title, labels={x_axis: x_label, y_axis: y_label})
            fig.update_traces(line=dict(dash=line_style, color=line_color))

            # st.plotly_chart(fig)
            st.plotly_chart(fig)
            try:
                fig.write_image("demo.png", format='png', width=800, height=600)
            except:
                pass

    import plotly.express as px

    def create_bar_chart_page(self, uploaded_file):
        # Streamlit UI for the Bar Chart page
        st.title("Bar Chart Page")

        if uploaded_file is None:
            st.warning("Please upload a valid CSV file.")
            return

        with st.form("bar_chart_form"):
            if uploaded_file is not None:
                # Read the uploaded data
                data = pd.read_csv(uploaded_file)

                # User customization options
                chart_title = st.text_input("Chart Title", "Bar Chart")
                x_axis = st.selectbox("Select X-axis", data.columns)
                y_axis = st.selectbox("Select Y-axis", data.columns)
                x_label = st.text_input("X-axis Label", "X-axis")
                y_label = st.text_input("Y-axis Label", "Y-axis")
                color_by = st.selectbox("Color By", data.columns, help="Select a column for color categorization")
                bar_mode = st.selectbox("Bar Mode", ["group", "stack"], help="Select the bar mode")
                bar_orientation = st.selectbox("Bar Orientation", ["vertical", "horizontal"], help="Select the bar orientation")
                show_legend = st.checkbox("Show Legend", value=True, help="Show or hide the legend")
                show_values = st.checkbox("Show Values", value=True, help="Show or hide values on the bars")

                # Submit button to trigger chart creation
                submit_button = st.form_submit_button("Generate Bar Chart")

        # Move the chart rendering outside the st.form block
        if submit_button:
            # Navigate to another Streamlit page
            if bar_orientation == "vertical":
                orientation_param = "v"
            else:
                orientation_param = "h"

            # Determine if it's necessary to use stacked barchart
            if bar_mode == "stack" and len(data[color_by].unique()) > 1:
                barmode_param = "stack"
            else:
                barmode_param = "group"

            # Configure legend visibility
            legend_visibility = show_legend

            # Configure text values visibility
            text_visibility = 'inside' if show_values else None

            fig = px.bar(data, x=data[x_axis], y=data[y_axis], title=chart_title,
                        labels={x_axis: x_label, y_axis: y_label}, color=data[color_by],
                        barmode=barmode_param, orientation=orientation_param,
                        category_orders={color_by: data[color_by].unique()},
                        text=data[y_axis] if show_values else None)

            # Update the layout to show or hide the legend
            fig.update_layout(showlegend=legend_visibility)

            # Update text position
            if show_values:
                fig.update_traces(textposition='inside')

            st.plotly_chart(fig)
            
            # Save the plot as an image
            fig.write_image("demo.png", format='png', width=800, height=600)





    def create_pie_chart_page(self, uploaded_file):
        # Streamlit UI for the Pie Chart page
        st.title("Pie Chart Page")

        if uploaded_file is None:
            st.warning("Please upload a valid CSV file.")
            return

        with st.form("pie_chart_form"):
            if uploaded_file is not None:
                # Read the uploaded data
                data = pd.read_csv(uploaded_file)

                # User customization options
                chart_title = st.text_input("Chart Title", "Pie Chart")
                labels_column = st.selectbox("Select Labels Column", data.columns)
                values_column = st.selectbox("Select Values Column", data.columns)
                show_legend = st.checkbox("Show Legend", value=True, help="Show or hide the legend")
                show_values = st.checkbox("Show Values", value=True, help="Show or hide values on the pie chart")

                # Submit button to trigger chart creation
                submit_button = st.form_submit_button("Generate Pie Chart")

        # Move the chart rendering outside the st.form block
        if submit_button:
            # Configure legend visibility
            legend_visibility = show_legend

            # Configure text values visibility
            text_visibility = 'inside' if show_values else 'none'

            # Explicitly set colors for pie chart slices
            colors = px.colors.qualitative.Plotly

            fig = px.pie(data, names=data[labels_column], values=data[values_column], title=chart_title,
                        labels={labels_column: 'Label', values_column: 'Value'}, 
                        hole=0.3,  # Set the size of the hole in the middle of the pie chart
                        color_discrete_sequence=colors  # Set colors for pie chart slices
                        )

            # Update the layout to show or hide the legend
            fig.update_layout(showlegend=legend_visibility)

            # Update text position
            fig.update_traces(textposition=text_visibility)

            st.plotly_chart(fig)
            
            # Save the plot as an image
            img_bytes = fig.to_image(format='png')
            img = Image.open(io.BytesIO(img_bytes))
            img = ImageOps.exif_transpose(img.convert('RGB'))

            # Save the PIL image to a file
            img.save("demo.png")




    

    def create_scatter_plot_page(self, uploaded_file):
        # Streamlit UI for the Scatter Plot page
        st.title("Scatter Plot Page")

        if uploaded_file is None:
            st.warning("Please upload a valid CSV file.")
            return

        with st.form("scatter_plot_form"):
            if uploaded_file is not None:
                # Read the uploaded data
                data = pd.read_csv(uploaded_file)

                # User customization options
                chart_title = st.text_input("Chart Title", "Scatter Plot")
                x_axis = st.selectbox("Select X-axis", data.columns)
                y_axis = st.selectbox("Select Y-axis", data.columns)

                x_label = st.text_input("X-axis Label", "X-axis")
                y_label = st.text_input("Y-axis Label", "Y-axis")
                show_legend = st.checkbox("Show Legend", value=True, help="Show or hide the legend")
                show_grid = st.checkbox("Show Grid", value=True, help="Show or hide the grid lines")
                marker_opacity = st.slider("Marker Opacity", min_value=0.1, max_value=1.0, value=0.7, step=0.1, help="Set the marker opacity")
                show_trendline = st.checkbox("Show Trendline", value=False, help="Show or hide the trendline")
                trendline_order = st.slider("Trendline Order", min_value=1, max_value=5, value=1, help="Set the order of the trendline")

                # Submit button to trigger chart creation
                submit_button = st.form_submit_button("Generate Scatter Plot")

        # Move the chart rendering outside the st.form block
        if submit_button:
            # Configure legend visibility
            legend_visibility = show_legend

            # Configure grid visibility
            grid_visibility = show_grid

            # Configure trendline visibility
            trendline_visibility = 'ols' if show_trendline else None

            # Create a new column for X values raised to the power of the desired order
            if show_trendline:
                data[f'{x_axis}^{trendline_order}'] = data[x_axis] ** trendline_order
                trendline_x_column = f'{x_axis}^{trendline_order}'
            else:
                trendline_x_column = None

            fig = px.scatter(data, x=data[x_axis], y=data[y_axis], title=chart_title,
                            labels={x_axis: x_label, y_axis: y_label},
                            opacity=marker_opacity,
                            trendline=trendline_visibility)

            # Update the layout to show or hide the legend, grid, and trendline
            fig.update_layout(showlegend=legend_visibility, xaxis=dict(showgrid=grid_visibility), yaxis=dict(showgrid=grid_visibility))

            # Set color scheme
            fig.update_traces(marker=dict(color='blue'))  # Change 'blue' to any color you prefer

            st.plotly_chart(fig)
            fig.write_image("demo.png", format='png', width=800, height=600)




    def create_histogram_page(self, uploaded_file):
        # Streamlit UI for the Histogram Page
        st.title("Histogram Page")

        if uploaded_file is None:
            st.warning("Please upload a valid CSV file.")
            return

        with st.form("histogram_form"):
            if uploaded_file is not None:
                # Read the uploaded data
                data = pd.read_csv(uploaded_file)

                # User customization options
                chart_title = st.text_input("Chart Title", "Histogram")
                x_axis = st.selectbox("Select X-axis", data.columns)
                bins = st.slider("Number of Bins", min_value=1, max_value=100, value=10, help="Set the number of bins for the histogram")
                color_column = st.selectbox("Select Color Column", data.columns, help="Select a column for color grouping")
                show_legend = st.checkbox("Show Legend", value=True, help="Show or hide the legend")
                show_grid = st.checkbox("Show Grid", value=True, help="Show or hide the grid lines")
                opacity = st.slider("Opacity", min_value=0.1, max_value=1.0, value=0.7, step=0.1, help="Set the opacity of the bars")

                # Submit button to trigger chart creation
                submit_button = st.form_submit_button("Generate Histogram")

        # Move the chart rendering outside the st.form block
        if submit_button:
            # Configure legend visibility
            legend_visibility = show_legend

            # Configure grid visibility
            grid_visibility = show_grid

            # Get unique values in the color column
            color_values = data[color_column].unique()

            # Assign colors to the unique values
            color_map = dict(zip(color_values, px.colors.qualitative.Plotly[:len(color_values)]))

            # Assign colors to data based on the color column
            data['color'] = data[color_column].map(color_map)

            fig = px.histogram(data, x=data[x_axis], title=chart_title, nbins=bins, color='color',
                            opacity=opacity)

            # Update the layout to show or hide the legend, grid
            fig.update_layout(showlegend=legend_visibility, xaxis=dict(showgrid=grid_visibility), yaxis=dict(showgrid=grid_visibility))

            st.plotly_chart(fig)
            
            # Save the plot as an image
            fig.write_image("demo.png", format='png', width=800, height=600)


    def create_heatmap_page(self,uploaded_file):
    # Streamlit UI for the Heatmap Page
        st.title("Heatmap Page")

        if uploaded_file is None:
            st.warning("Please upload a valid CSV file.")
            return

        with st.form("heatmap_form"):
            if uploaded_file is not None:
                # Read the uploaded data
                data = pd.read_csv(uploaded_file)

                # User customization options
                chart_title = st.text_input("Chart Title", "Heatmap")

                # Dynamically ask the user for X and Y axes
                x_axis = st.selectbox("Select X-axis", data.columns, key='heatmap_x_axis')
                y_axis = st.selectbox("Select Y-axis", data.columns, key='heatmap_y_axis')

                show_legend = st.checkbox("Show Legend", value=True, help="Show or hide the legend")
                show_grid = st.checkbox("Show Grid", value=True, help="Show or hide the grid lines")
                color_scale = st.select_slider("Color Scale", options=["viridis", "plasma", "inferno", "magma", "cividis"], help="Select a color scale")
                reverse_color_scale = st.checkbox("Reverse Color Scale", value=False, help="Reverse the color scale")

                # Submit button to trigger chart creation
                submit_button = st.form_submit_button("Generate Heatmap")

        # Move the chart rendering outside the st.form block
        if submit_button:
            # Configure legend visibility
            legend_visibility = show_legend

            # Configure grid visibility
            grid_visibility = show_grid

            # Configure color scale
            colorscale = color_scale if not reverse_color_scale else f"{color_scale}_r"

            # fig = px.imshow(data.pivot(x_axis, y_axis), 
            #                 labels={x_axis: x_axis, y_axis: y_axis},
            #                 color_continuous_scale=colorscale)
            fig = px.imshow(data.pivot_table(index=x_axis, columns=y_axis), 
                labels={x_axis: x_axis, y_axis: y_axis},
                color_continuous_scale=colorscale)


            # Update the layout to show or hide the legend, grid
            fig.update_layout(title=chart_title, showlegend=legend_visibility, xaxis=dict(showgrid=grid_visibility), yaxis=dict(showgrid=grid_visibility))

            st.plotly_chart(fig)
            fig.write_image("demo.png", format='png', width=800, height=600)

    def create_box_plot_page(self, uploaded_file):
        # Streamlit UI for the Box Plot page
        st.title("Box Plot Page")

        if uploaded_file is None:
            st.warning("Please upload a valid CSV file.")
            return

        data = pd.read_csv(uploaded_file)
        
        if data.empty:
            st.warning("The uploaded CSV file is empty.")
            return

        with st.form("box_plot_form"):
            # User customization options
            chart_title = st.text_input("Chart Title", "Box Plot")
            y_axis = st.selectbox("Select Column for Box Plot", data.columns, key='boxplot_y_axis')
            show_legend = st.checkbox("Show Legend", value=True, help="Show or hide the legend")

            # Submit button to trigger chart creation
            submit_button = st.form_submit_button("Generate Box Plot")

        # Move the chart rendering outside the st.form block
        if submit_button:
            # Configure legend visibility
            legend_visibility = show_legend

            # Create the box plot using Plotly Express
            fig = px.box(data, y=y_axis, title=chart_title, points="all", color_discrete_sequence=px.colors.qualitative.Plotly)

            # Update the layout to show or hide the legend
            fig.update_layout(showlegend=legend_visibility)

            st.plotly_chart(fig)
            
            # Save the plot as an image
            fig.write_image("demo.png", format='png', width=800, height=600)



    def create_3d_contour_plot_page(self,uploaded_file, chart_type="3D Contour Plot"):
    # Streamlit UI for the 3D Contour Plot Page
        st.title("3D Contour Plot Page")

        if uploaded_file is None:
            st.warning("Please upload a valid CSV file.")
            return

        with st.form("contour3d_plot_form"):
            if uploaded_file is not None:
                # Read the uploaded data
                data = pd.read_csv(uploaded_file)

                # User customization options
                chart_title = st.text_input("Chart Title", chart_type)
                x_axis = st.selectbox("Select X-axis", data.columns, key='contour3dplot_x_axis')
                y_axis = st.selectbox("Select Y-axis", data.columns, key='contour3dplot_y_axis')
                z_axis = st.selectbox("Select Z-axis", data.columns, key='contour3dplot_z_axis')
                x_label = st.text_input("X-axis Label", x_axis)
                y_label = st.text_input("Y-axis Label", y_axis)
                z_label = st.text_input("Z-axis Label", z_axis)
                show_legend = st.checkbox("Show Legend", value=True, help="Show or hide the legend")
                marker_size = st.slider("Marker Size", min_value=1, max_value=20, value=6, help="Set the marker size")

                # Submit button to trigger chart creation
                submit_button = st.form_submit_button("Generate 3D Contour Plot")

        # Move the chart rendering outside the st.form block
        if submit_button:
            # Configure legend visibility
            legend_visibility = show_legend

            # Create the 3D contour plot using Plotly
            fig = go.Figure()

            fig.add_trace(go.Scatter3d(
                x=data[x_axis],
                y=data[y_axis],
                z=data[z_axis],
                mode='markers',
                marker=dict(
                    size=marker_size,
                    color=data[z_axis],
                    colorscale='Viridis',
                    opacity=0.8
                )
            ))

            fig.update_layout(scene=dict(
                xaxis_title=x_label,
                yaxis_title=y_label,
                zaxis_title=z_label
            ))

            # Set chart title
            fig.update_layout(title=chart_title)

            # Show or hide legend
            if not legend_visibility:
                fig.update_layout(scene=dict(showlegend=False))

            # Display the plot with increased size
            st.plotly_chart(fig, use_container_width=True, width=1000000, height=600000)
            fig.write_image("demo.png", format='png', width=800, height=600)

    def create_3d_scatter_plot_page(self,uploaded_file, chart_type="3D Scatter Plot"):
    # Streamlit UI for the 3D Scatter Plot Page
        st.title("3D Scatter Plot Page")

        if uploaded_file is None:
            st.warning("Please upload a valid CSV file.")
            return

        with st.form("scatter3d_plot_form"):
            if uploaded_file is not None:
                # Read the uploaded data
                data = pd.read_csv(uploaded_file)

                # User customization options
                chart_title = st.text_input("Chart Title", chart_type)
                x_axis = st.selectbox("Select X-axis", data.columns, key='scatter3dplot_x_axis')
                y_axis = st.selectbox("Select Y-axis", data.columns, key='scatter3dplot_y_axis')
                z_axis = st.selectbox("Select Z-axis", data.columns, key='scatter3dplot_z_axis')
                x_label = st.text_input("X-axis Label", x_axis)
                y_label = st.text_input("Y-axis Label", y_axis)
                z_label = st.text_input("Z-axis Label", z_axis)
                color_column = st.selectbox("Select Color Column", data.columns, help="Select a column for color grouping")
                size_column = st.selectbox("Select Size Column", data.columns, help="Select a column for marker size")
                show_legend = st.checkbox("Show Legend", value=True, help="Show or hide the legend")
                marker_size = st.slider("Marker Size", min_value=1, max_value=20, value=6, help="Set the marker size")

                # Submit button to trigger chart creation
                submit_button = st.form_submit_button("Generate 3D Scatter Plot")

        # Move the chart rendering outside the st.form block
        if submit_button:
            # Configure legend visibility
            legend_visibility = show_legend

            # Create the 3D scatter plot using Plotly Express with additional styling
            fig = px.scatter_3d(data, x=x_axis, y=y_axis, z=z_axis, color=data[color_column], size=data[size_column],
                                title=chart_title, labels={x_axis: x_label, y_axis: y_label, z_axis: z_label},
                                size_max=marker_size)

            # Styling options
            fig.update_traces(marker=dict(line=dict(width=0.5, color='DarkSlateGray')), selector=dict(mode='markers'))
            fig.update_layout(scene=dict(bgcolor='rgba(0,0,0,0)'))  # Transparent background
            fig.update_layout(margin=dict(l=0, r=0, b=0, t=50))  # Adjust margin

            # Set chart title
            fig.update_layout(title=dict(text=chart_title, x=0.5, xanchor='center', y=0.95, yanchor='top'))

            # Show or hide legend
            if not legend_visibility:
                fig.update_layout(showlegend=False)

            # Display the plot
            st.plotly_chart(fig)
            fig.write_image("demo.png", format='png', width=800, height=600)



    import plotly.graph_objects as go

    def create_3d_surface_plot_page(self, uploaded_file, chart_type="3D Surface Plot"):
        # Streamlit UI for the 3D Surface Plot Page
        st.title("3D Surface Plot Page")

        if uploaded_file is None:
            st.warning("Please upload a valid CSV file.")
            return

        data = pd.read_csv(uploaded_file)
        
        if data.empty:
            st.warning("The uploaded CSV file is empty.")
            return

        with st.form("surface3d_plot_form"):
            # User customization options
            chart_title = st.text_input("Chart Title", chart_type)
            x_axis = st.selectbox("Select X-axis", data.columns, key='surface3dplot_x_axis')
            y_axis = st.selectbox("Select Y-axis", data.columns, key='surface3dplot_y_axis')
            z_axis = st.selectbox("Select Z-axis", data.columns, key='surface3dplot_z_axis')
            x_label = st.text_input("X-axis Label", x_axis)
            y_label = st.text_input("Y-axis Label", y_axis)
            z_label = st.text_input("Z-axis Label", z_axis)
            show_legend = st.checkbox("Show Legend", value=True, help="Show or hide the legend")

            # Submit button to trigger chart creation
            submit_button = st.form_submit_button("Generate 3D Surface Plot")

        # Move the chart rendering outside the st.form block
        if submit_button:
            # Configure legend visibility
            legend_visibility = show_legend

            # Ensure unique index values
            data = data.groupby([x_axis, y_axis])[z_axis].mean().reset_index()

            try:
                # Create the 3D surface plot using Plotly
                z_data = data.pivot(index=y_axis, columns=x_axis, values=z_axis)
                x = z_data.columns
                y = z_data.index
                z = z_data.values

                fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

                fig.update_layout(scene=dict(
                    xaxis_title=x_label,
                    yaxis_title=y_label,
                    zaxis_title=z_label
                ))

                # Set chart title
                fig.update_layout(title=chart_title)

                # Show or hide legend
                if not legend_visibility:
                    fig.update_layout(scene=dict(showlegend=False))

                # Display the plot with increased size
                st.plotly_chart(fig, use_container_width=True, width=1000, height=800)
                
                # Save the plot as an image
                fig.write_image("demo.png", format='png', width=800, height=600)

            except Exception as e:
                st.error(f"Error occurred: {str(e)}")




