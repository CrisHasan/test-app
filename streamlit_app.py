import streamlit as st
import altair as alt
import pandas as pd

###############################################
active_travel_baseline_year = 2015
active_travel_target = 50.0 # Target percentage of the population using active travel modes
active_travel_baseline = 5.0  # Baseline percentage (2015)
active_travel_mode_current = 10.0  # Current value of active travel mode

connectivity_baseline_year = 2015
connectivity_target = 85.0 # Target percentage of the population with good connectivity
connectivity_baseline = 75.0  # Baseline percentage (2015)
connectivity_current = 80.0  # Current percentage of the population with good connectivity

GHG_emissions_baseline_year = 2005
GHG_emissions_target = 0.0  # Target of GHG emissions in tCO2e per capita
GHG_emissions_baseline = 8.9  # Baseline value (2005)
GHG_emissions_current = 5.0  # Current value


def altair_horizontal_bar_chart(x, y, xlabel=None, title="Horizontal Bar Chart", y_min=0, y_max=110, save_as=None):
    """
    Create horizontal bar chart with Altair and custom Y-axis limits
    
    Parameters:
    - x: list of values for bar lengths
    - y: list of labels for bars
    - xlabel: X-axis label
    - title: Chart title 
    - y_min, y_max: Y-axis limits (actually X-axis since it's horizontal)
    """
    # Prepare data
    labels = y if y else [""]
    data = pd.DataFrame({
        'category': labels * len(x) if len(labels) == 1 else labels,
        'value': x
    })
    
    # Create Altair chart with Y-axis limits
    chart = alt.Chart(data).mark_bar().add_selection(
        alt.selection_interval(bind='scales', encodings=['x'])  # Only allow X-axis interaction
    ).encode(
        y=alt.Y('category:N', title=xlabel),
        x=alt.X('value:Q', 
                title="Value", 
                scale=alt.Scale(domain=[y_min, y_max]),  # Set X-axis limits for horizontal bar
                axis=alt.Axis(grid=True)),
        tooltip=['category', 'value']
    ).properties(
        title=title,
        width=400,
        height=150
    ).configure_axis(
        labelFontSize=10,
        titleFontSize=12
    ).interactive(bind_y=False)  # Disable Y-axis interaction
    
    # Display the chart
    st.altair_chart(chart, use_container_width=True)


###############################################
st.title("Indicator Workshop Interactive Tool")
active_travel_baseline_year = st.number_input("Baseline year for active travel modes", min_value=1980, max_value=2025, value=active_travel_baseline_year, step=1)
active_travel_baseline = st.number_input("Baseline percentage of the population using active travel modes in {} (%)".format(active_travel_baseline_year), min_value=0.0, max_value=100.0, value=active_travel_baseline, step=0.1)
active_travel_target = st.number_input("Desired (minimum) percentage of the population using active travel modes (%)", min_value=0.0, max_value=100.0, value=active_travel_target, step=0.1) 
active_travel_mode_current = st.slider("Current value of percentage of the population using active travel modes (%)", min_value=0.0, max_value=100.0, value=active_travel_mode_current, step=0.1)
active_travel_shortfall_value = min(100,100*(active_travel_target - active_travel_mode_current)/(active_travel_target - active_travel_baseline))

altair_horizontal_bar_chart(
    x=[active_travel_shortfall_value],
    y=["Active Travel"],
    title="Active Travel Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)

connectivity_baseline_year = st.number_input("Baseline year for connectivity", min_value=1980, max_value=2025, value=connectivity_baseline_year, step=1)
connectivity_baseline = st.number_input("Baseline percentage of the population with good connectivity in {} (%)".format(connectivity_baseline_year), min_value=0.0, max_value=100.0, value=connectivity_baseline, step=0.1)
connectivity_target = st.number_input("Desired (minimum) percentage of the population with good connectivity (%)", min_value=0.0, max_value=100.0, value=connectivity_target, step=0.1)
connectivity_current = st.slider("Current percentage of the population with good connectivity (%)", min_value=0.0, max_value=100.0, value=connectivity_current, step=0.1)
connectivity_shortfall_value = min(100,100*(connectivity_target - connectivity_current)/(connectivity_target - connectivity_baseline))

altair_horizontal_bar_chart(
    x=[connectivity_shortfall_value],
    y=["Connectivity"],
    title="Connectivity Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)


GHG_emissions_baseline_year = st.number_input("Baseline year for GHG emissions", min_value=1980, max_value=2025, value=GHG_emissions_baseline_year, step=1)
GHG_emissions_baseline = st.number_input("Baseline GHG emissions in {} (tCO2e per capita)".format(GHG_emissions_baseline_year), min_value=0.0, max_value=100.0, value=GHG_emissions_baseline, step=0.1)
GHG_emissions_target = st.number_input("Desired (maximum) GHG emissions (tCO2e per capita)", min_value=0.0, max_value=100.0, value=GHG_emissions_target, step=0.1)
GHG_emissions_current = st.slider("Current GHG emissions (tCO2e per capita)", min_value=0.0, max_value=15.0, value=GHG_emissions_current, step=0.1)
GHG_emissions_overshoot_value = min(100,100*(GHG_emissions_current - GHG_emissions_target)/(GHG_emissions_baseline - GHG_emissions_target))

altair_horizontal_bar_chart(
    x=[GHG_emissions_overshoot_value],
    y=["GHG Emissions"],
    title="GHG Emissions Overshoot",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)   

