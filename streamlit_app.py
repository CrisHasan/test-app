import streamlit as st
import altair as alt
import pandas as pd

###############################################
no2_concentration_target = 10.0 # Target levels of annual concentration of NO2 (µg/m³)
no2_concentration_baseline = 43.07  # Baseline levels of annual concentration of NO2 (µg/m³)
no2_concentration_current = 20.12  # Current levels of annual concentration of NO2 (µg/m³)

pm10_concentration_target = 15.0 # Target levels of annual concentration of PM10 (µg/m³)
pm10_concentration_baseline = 15.95  # Baseline levels of annual concentration of PM10 (µg/m³)
pm10_concentration_current = 10.52  # Current levels of annual concentration of PM10 (µg/m³) 

pm25_concentration_target = 5.0 # Target levels of annual concentration of PM2.5 (µg/m³)
pm25_concentration_baseline = 15.28  # Baseline levels of annual concentration of PM2.5 (µg/m³)
pm25_concentration_current = 6.09  # Current levels of annual concentration of PM2.5 (µg/m³)

pop_weighted_pm25_concentration_target = 5.0 # Target levels of population-weighted annual concentration of PM2.5 (µg/m³)
pop_weighted_pm25_concentration_baseline = 8.7  # Baseline levels of population-weighted annual concentration of PM2.5 (µg/m³)
pop_weighted_pm25_concentration_current = 5.24  # Current levels of population-weighted annual concentration of PM2.5 (µg/m³)

percentage_households_financially_manage_well_target = 100.0 # Target percentage of households financially managing well
percentage_households_financially_manage_well_baseline = 0.0  # Baseline percentage (2015)
percentage_households_financially_manage_well_current = 89.74  # Current percentage of households financially managing well

percentage_children_low_income_families_target = 0.0 # Target percentage of children living in relative low-income families
percentage_children_low_income_families_baseline = 100.0  # Baseline percentage (2015)
percentage_children_low_income_families_current = 26.25  # Current percentage of children living in relative low-income families

unemployment_rate_target = 5.0 # Target unemployment rate
unemployment_rate_baseline = 100.0  # Baseline unemployment rate (2015)
unemployment_rate_current = 7.52  # Current unemployment rate

percentage_experince_any_event_food_insecurity_target = 0.0 # Target percentage of people who experienced any event of food insecurity over the last 12 months
percentage_experince_any_event_food_insecurity_baseline = 100.0  # Baseline percentage (2015)
percentage_experince_any_event_food_insecurity_current = 21.8  # Current percentage of people who experienced any event of food insecurity over the last 12 months

gap_in_food_insecurity_target = 0.0  # Gap in the percentage of people who experienced any event of food insecurity over the last 12 months between the bottom 15% deprived and other areas of Glasgow
gap_in_food_insecurity_baseline = 100.0  # Baseline gap in the percentage of people who experienced any event of food insecurity over the last 12 months between the bottom 15% deprived and other areas of Glasgow
gap_in_food_insecurity_current = 12.2  # Current gap in the percentage of people who experienced any event of food insecurity over the last 12 months between the bottom 15% deprived and other areas of Glasgow

percentage_people_food_cost_financial_concerns_target = 0.0 # Target percentage of people who consider food cost among the two or three biggest financial concerns for their household
percentage_people_food_cost_financial_concerns_baseline = 100.0  # Baseline percentage (2015)
percentage_people_food_cost_financial_concerns_current = 58.72  # Current percentage of people who consider food cost among the two or three biggest financial concerns for their household

percentage_people_unable_to_eat_healthy_food_target = 0.0 # Target percentage of people who were unable to eat healthy and nutritious food because of a lack of money or other resources in the last 12 months
percentage_people_unable_to_eat_healthy_food_baseline = 100.0  # Baseline percentage (2015)
percentage_people_unable_to_eat_healthy_food_current = 15.9  # Current percentage of people who were unable to eat healthy and nutritious food because of a lack of money or other resources in the last 12 months

active_travel_target = 50.0 # Target percentage of the population using active travel modes
active_travel_baseline = 5.0  # Baseline percentage (2015)
active_travel_mode_current = 10.0  # Current value of active travel mode

connectivity_target = 85.0 # Target percentage of the population with good connectivity
connectivity_baseline = 75.0  # Baseline percentage (2015)
connectivity_current = 80.0  # Current percentage of the population with good connectivity

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
    chart = alt.Chart(data).mark_bar(color='#FF4500').add_selection(
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
st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)
st.header("Cleanse the Air indicators")
st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)

no2_concentration_target = st.number_input("Target levels of annual concentration of NO2 (µg/m³)", min_value=0.0, max_value=100.0, value=no2_concentration_target, step=0.1)     
no2_concentration_baseline = st.number_input("Baseline levels of annual concentration of NO2 (µg/m³)", min_value=0.0, max_value=100.0, value=no2_concentration_baseline, step=0.1)
no2_concentration_current = st.slider("Current levels of annual concentration of NO2 (µg/m³)", min_value=0.0, max_value=100.0, value=no2_concentration_current, step=0.1)
no2_concentration_overshoot_value = min(100,100*(no2_concentration_current - no2_concentration_target)/(no2_concentration_baseline - no2_concentration_target))  
altair_horizontal_bar_chart(
    x=[no2_concentration_overshoot_value],
    y=["NO2 Concentration"],
    title="NO2 Concentration Overshoot",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)   
pm10_concentration_target = st.number_input("Target levels of annual concentration of PM10 (µg/m³)", min_value=0.0, max_value=100.0, value=pm10_concentration_target, step=0.1)
pm10_concentration_baseline = st.number_input("Baseline levels of annual concentration of PM10 (µg/m³)", min_value=0.0, max_value=100.0, value=pm10_concentration_baseline, step=0.1)
pm10_concentration_current = st.slider("Current levels of annual concentration of PM10 (µg/m³)", min_value=0.0, max_value=100.0, value=pm10_concentration_current, step=0.1)
pm10_concentration_overshoot_value = min(100,100*(pm10_concentration_current - pm10_concentration_target)/(pm10_concentration_baseline - pm10_concentration_target))  
altair_horizontal_bar_chart(
    x=[pm10_concentration_overshoot_value],
    y=["PM10 Concentration"],
    title="PM10 Concentration Overshoot",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)   

pm25_concentration_target = st.number_input("Target levels of annual concentration of PM2.5 (µg/m³)", min_value=0.0, max_value=100.0, value=pm25_concentration_target, step=0.1)
pm25_concentration_baseline = st.number_input("Baseline levels of annual concentration of PM2.5 (µg/m³)", min_value=0.0, max_value=100.0, value=pm25_concentration_baseline, step=0.1)
pm25_concentration_current = st.slider("Current levels of annual concentration of PM2.5 (µg/m³)", min_value=0.0, max_value=100.0, value=pm25_concentration_current, step=0.1)
pm25_concentration_overshoot_value = min(100,100*(pm25_concentration_current - pm25_concentration_target)/(pm25_concentration_baseline - pm25_concentration_target))  
altair_horizontal_bar_chart(
    x=[pm25_concentration_overshoot_value],
    y=["PM2.5 Concentration"],
    title="PM2.5 Concentration Overshoot",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)

pop_weighted_pm25_concentration_target = st.number_input("Target levels of population-weighted annual concentration of PM2.5 (µg/m³)", min_value=0.0, max_value=100.0, value=pop_weighted_pm25_concentration_target, step=0.1)
pop_weighted_pm25_concentration_baseline = st.number_input("Baseline levels of population-weighted annual concentration of PM2.5 (µg/m³)", min_value=0.0, max_value=100.0, value=pop_weighted_pm25_concentration_baseline, step=0.1)
pop_weighted_pm25_concentration_current = st.slider("Current levels of population-weighted annual concentration of PM2.5 (µg/m³)", min_value=0.0, max_value=100.0, value=pop_weighted_pm25_concentration_current, step=0.1)
pop_weighted_pm25_concentration_overshoot_value = min(100,100*(pop_weighted_pm25_concentration_current - pop_weighted_pm25_concentration_target)/(pop_weighted_pm25_concentration_baseline - pop_weighted_pm25_concentration_target))  
altair_horizontal_bar_chart(
    x=[pop_weighted_pm25_concentration_overshoot_value],
    y=["Population-weighted PM2.5 Concentration"],
    title="Population-weighted PM2.5 Concentration Overshoot",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)



##########################################
st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)
st.header("Income and Work indicators")
st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)

percentage_households_financially_manage_well_target = st.number_input("Target percentage of households financially managing well (%)", min_value=0.0, max_value=100.0, value=percentage_households_financially_manage_well_target, step=0.1)
percentage_households_financially_manage_well_baseline = st.number_input("Baseline percentage of households financially managing well (%)", min_value=0.0, max_value=100.0, value=percentage_households_financially_manage_well_baseline, step=0.1)
percentage_households_financially_manage_well_current = st.slider("Current percentage of households financially managing well (%)", min_value=0.0, max_value=100.0, value=percentage_households_financially_manage_well_current, step=0.1)
percentage_households_financially_manage_well_shortfall_value = min(100,100*(percentage_households_financially_manage_well_target - percentage_households_financially_manage_well_current)/(percentage_households_financially_manage_well_target - percentage_households_financially_manage_well_baseline))  
altair_horizontal_bar_chart(
    x=[percentage_households_financially_manage_well_shortfall_value],
    y=["Households Financially Managing Well"],
    title="Financially Managing Well Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)  
percentage_children_low_income_families_target = st.number_input("Target percentage of children living in relative low-income families (%)", min_value=0.0, max_value=100.0, value=percentage_children_low_income_families_target, step=0.1) 
percentage_children_low_income_families_baseline = st.number_input("Baseline percentage of children living in relative low-income families (%)", min_value=0.0, max_value=100.0, value=percentage_children_low_income_families_baseline, step=0.1)
percentage_children_low_income_families_current = st.slider("Current percentage of children living in relative low-income families (%)", min_value=0.0, max_value=100.0, value=percentage_children_low_income_families_current, step=0.1)
percentage_children_low_income_families_shortfall_value = min(100,100*(percentage_children_low_income_families_current - percentage_children_low_income_families_target)/(percentage_children_low_income_families_baseline - percentage_children_low_income_families_target))  
altair_horizontal_bar_chart(
    x=[percentage_children_low_income_families_shortfall_value],
    y=["Children in Low-income Families"],
    title="Children in Low-income Families Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)

unemployment_rate_target = st.number_input("Target unemployment rate (%)", min_value=0.0, max_value=100.0, value=unemployment_rate_target, step=0.1)
unemployment_rate_baseline = st.number_input("Baseline unemployment rate (%)", min_value=0.0, max_value=100.0, value=unemployment_rate_baseline, step=0.1)
unemployment_rate_current = st.slider("Current unemployment rate (%)", min_value=0.0, max_value=100.0, value=unemployment_rate_current, step=0.1)
unemployment_rate_shortfall_value = min(100,100*(unemployment_rate_current - unemployment_rate_target)/(unemployment_rate_baseline - unemployment_rate_target))  
altair_horizontal_bar_chart(
    x=[unemployment_rate_shortfall_value],
    y=["Unemployment Rate"],
    title="Unemployment Rate Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)

##########################################
# Change color of markdown lines
st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)
st.header("Food indicators")
st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)


percentage_experince_any_event_food_insecurity_target = st.number_input("Target percentage of people who experienced any event of food insecurity over the last 12 months (%)", min_value=0.0, max_value=100.0, value=percentage_experince_any_event_food_insecurity_target, step=0.1)
percentage_experince_any_event_food_insecurity_baseline = st.number_input("Baseline percentage of people who experienced any event of food insecurity over the last 12 months (%)", min_value=0.0, max_value=100.0, value=percentage_experince_any_event_food_insecurity_baseline, step=0.1)
percentage_experince_any_event_food_insecurity_current = st.slider("Current percentage of people who experienced any event of food insecurity over the last 12 months (%)", min_value=0.0, max_value=100.0, value=percentage_experince_any_event_food_insecurity_current, step=0.1)
percentage_experince_any_event_food_insecurity_shortfall_value = min(100,100*(percentage_experince_any_event_food_insecurity_current - percentage_experince_any_event_food_insecurity_target)/(percentage_experince_any_event_food_insecurity_baseline - percentage_experince_any_event_food_insecurity_target))  
altair_horizontal_bar_chart(
    x=[percentage_experince_any_event_food_insecurity_shortfall_value],
    y=["Food Insecurity"],
    title="Food Insecurity Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)           


gap_in_food_insecurity_target = st.number_input("Target gap in the percentage of people who experienced any event of food insecurity over the last 12 months between the bottom 15% deprived and other areas of Glasgow (%)", min_value=0.0, max_value=100.0, value=gap_in_food_insecurity_target, step=0.1)
gap_in_food_insecurity_baseline = st.number_input("Baseline gap in the percentage of people who experienced any event of food insecurity over the last 12 months between the bottom 15% deprived and other areas of Glasgow (%)", min_value=0.0, max_value=100.0, value=gap_in_food_insecurity_baseline, step=0.1)
gap_in_food_insecurity_current = st.slider("Current gap in the percentage of people who experienced any event of food insecurity over the last 12 months between the bottom 15% deprived and other areas of Glasgow (%)", min_value=0.0, max_value=100.0, value=gap_in_food_insecurity_current, step=0.1)
gap_in_food_insecurity_shortfall_value = min(100,100*(gap_in_food_insecurity_current - gap_in_food_insecurity_target)/(gap_in_food_insecurity_baseline - gap_in_food_insecurity_target))        
altair_horizontal_bar_chart(
    x=[gap_in_food_insecurity_shortfall_value],
    y=["Food Insecurity Gap"],
    title="Food Insecurity Gap Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)   

percentage_people_food_cost_financial_concerns_target = st.number_input("Target percentage of people who consider food cost among the two or three biggest financial concerns for their household (%)", min_value=0.0, max_value=100.0, value=percentage_people_food_cost_financial_concerns_target, step=0.1)
percentage_people_food_cost_financial_concerns_baseline = st.number_input("Baseline percentage of people who consider food cost among the two or three biggest financial concerns for their household (%)", min_value=0.0, max_value=100.0, value=percentage_people_food_cost_financial_concerns_baseline, step=0.1)
percentage_people_food_cost_financial_concerns_current = st.slider("Current percentage of people who consider food cost among the two or three biggest financial concerns for their household (%)", min_value=0.0, max_value=100.0, value=percentage_people_food_cost_financial_concerns_current, step=0.1)
percentage_people_food_cost_financial_concerns_shortfall_value = min(100,100*(percentage_people_food_cost_financial_concerns_current - percentage_people_food_cost_financial_concerns_target)/(percentage_people_food_cost_financial_concerns_baseline - percentage_people_food_cost_financial_concerns_target))  
altair_horizontal_bar_chart(
    x=[percentage_people_food_cost_financial_concerns_shortfall_value],
    y=["Food Cost Financial Concerns"],
    title="Food Cost Financial Concerns Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)   

percentage_people_unable_to_eat_healthy_food_target = st.number_input("Target percentage of people who were unable to eat healthy and nutritious food because of a lack of money or other resources in the last 12 months (%)", min_value=0.0, max_value=100.0, value=percentage_people_unable_to_eat_healthy_food_target, step=0.1)
percentage_people_unable_to_eat_healthy_food_baseline = st.number_input("Baseline percentage of people who were unable to eat healthy and nutritious food because of a lack of money or other resources in the last 12 months (%)", min_value=0.0, max_value=100.0, value=percentage_people_unable_to_eat_healthy_food_baseline, step=0.1)
percentage_people_unable_to_eat_healthy_food_current = st.slider("Current percentage of people who were unable to eat healthy and nutritious food because of a lack of money or other resources in the last 12 months (%)", min_value=0.0, max_value=100.0, value=percentage_people_unable_to_eat_healthy_food_current, step=0.1)
percentage_people_unable_to_eat_healthy_food_shortfall_value = min(100,100*(percentage_people_unable_to_eat_healthy_food_current - percentage_people_unable_to_eat_healthy_food_target)/(percentage_people_unable_to_eat_healthy_food_baseline - percentage_people_unable_to_eat_healthy_food_target))  
altair_horizontal_bar_chart(
    x=[percentage_people_unable_to_eat_healthy_food_shortfall_value],
    y=["Unable to Eat Healthy Food"],
    title="Unable to Eat Healthy Food Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100  # Set maximum value for the axis
)       