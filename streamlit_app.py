import streamlit as st
import altair as alt
import pandas as pd

###############################################
# Percentage of surface waters in Glasgow City that have at least good water quality
surface_water_quality_target = 100.0 # Target percentage of surface waters with at least good water quality
surface_water_quality_baseline = 0.0  # Baseline percentage of surface waters with at least good water quality
surface_water_quality_current = 37.9  # Current percentage of surface waters with at least good water quality

# Percentage of Glasgow's surface waters assessed as having at least ‘good’ overall status
surface_water_overall_status_target = 100.0 # Target percentage of surface waters assessed as having at least ‘good’ overall status 
surface_water_overall_status_baseline = 0.0  # Baseline percentage of surface waters assessed as having at least ‘good’ overall status  
surface_water_overall_status_current = 27.6  # Current percentage of surface waters assessed as having at least ‘good’ overall status   

# Percentage of Glasgow's groundwaters assessed as having at least 'good' status
groundwater_quality_target = 100.0 # Target percentage of groundwaters assessed as having at least 'good' status    
groundwater_quality_baseline = 0.0  # Baseline percentage of groundwaters assessed as having at least 'good' status 
groundwater_quality_current = 66.7  # Current percentage of groundwaters assessed as having at least 'good' status 

tree_canopy_coverage_target = 20.0 # Target percentage of tree canopy coverage
tree_canopy_coverage_baseline = 0.0  # Baseline percentage of tree canopy coverage
tree_canopy_coverage_current = 18.0  # Current percentage of tree canopy coverage

peatlands_intact_restored_target = 100.0 # Target percentage of peatlands that are intact or restored
peatlands_intact_restored_baseline = 0.0  # Baseline percentage of peatlands that are intact or restored
peatlands_intact_restored_current = 79.6  # Current percentage of peatlands that are intact or restored

carbon_sequestration_target = 37000.0  # Target amount of carbon sequestrated in Glasgow in tonnes C per year
carbon_sequestration_baseline = 9000.5  # Baseline amount of carbon sequestrated in Glasgow in tonnes C per year
carbon_sequestration_current = 9625.9  # Current amount of carbon sequestrated in Glasgow in tonnes C per year

# Percentage of adults in Glasgow who engage in a volunteering work
volunteering_target = 25.0 # Target percentage of adults in Glasgow who engage in a volunteering work
volunteering_baseline = 0.0  # Baseline percentage of adults in Glasgow who engage in a volunteering work
volunteering_current = 14.7  # Current percentage of adults in Glasgow who engage in a volunteering work

# Percentage of people who rate their neighbourhood as very good or fairly good
neighbourhood_rating_target = 100.0 # Target percentage of people who rate their neighbourhood as very good or fairly good
neighbourhood_rating_baseline = 0.0  # Baseline percentage of people who rate their neighbourhood as very good or fairly good
neighbourhood_rating_current = 92.2  # Current percentage of people who rate their neighbourhood as very good or fairly good

# Percentage of people satisfied with local community centres
community_centre_satisfaction_target = 100.0 # Target percentage of people satisfied with local community centres
community_centre_satisfaction_baseline = 0.0  # Baseline percentage of people satisfied with local community centres
community_centre_satisfaction_current = 70.2  # Current percentage of people satisfied with local community centres 

# Percentage of adults in Glasgow who engage in cultural events
cultural_engagement_target = 76.0 # Target percentage of adults in Glasgow who engage in cultural events
cultural_engagement_baseline = 0.0  # Baseline percentage of adults in Glasgow who engage in cultural events
cultural_engagement_current = 63.83  # Current percentage of adults in Glasgow who engage in cultural events 

# Percentage of Glasgow residents who are satisfied with museums, libraries and theatres
cultural_facilities_satisfaction_target = 100.0 # Target percentage of Glasgow residents who are satisfied with museums, libraries and theatres
cultural_facilities_satisfaction_baseline = 0.0  # Baseline percentage of Glasgow residents who are satisfied with museums, libraries and theatres
cultural_facilities_satisfaction_current = 58.06  # Current percentage of Glasgow residents who are satisfied with museums, libraries and theatres

# Percentage of Glasgow residents satisfied with sports and leisure centres
sports_leisure_satisfaction_target = 100.0 # Target percentage of Glasgow residents satisfied with sports and leisure centres
sports_leisure_satisfaction_baseline = 0.0  # Baseline percentage of Glasgow residents satisfied with sports and leisure centres
sports_leisure_satisfaction_current = 78.47  # Current percentage of Glasgow residents satisfied with sports and leisure centres

# Percentage of households that are satisfied with housing
housing_satisfaction_target = 100.0 # Target percentage of households that are satisfied with housing
housing_satisfaction_baseline = 0.0  # Baseline percentage of households that are satisfied with housing
housing_satisfaction_current = 86.78  # Current percentage of households that are satisfied with housing 

# Percentage of people who consider rent cost among the 2-3 biggest financial concern for their household
rent_cost_financial_concerns_target = 0.0 # Target percentage of people who consider rent cost among the 2-3 biggest financial concern for their household
rent_cost_financial_concerns_baseline = 100.0  # Baseline percentage of people who consider rent cost among the 2-3 biggest financial concern for their household
rent_cost_financial_concerns_current = 25.03  # Current percentage of people who consider rent cost among the 2-3 biggest financial concern for their household

# Percentage of homes with an EPC band at B/C or above
epc_band_target = 100.0 # Target percentage of homes with an EPC band at B/C or above
epc_band_baseline = 0.0  # Baseline percentage of homes with an EPC band at B/C or above
epc_band_current = 76.1  # Current percentage of homes with an EPC band at B/C or above

# Percentage of households that experience fuel poverty
fuel_poverty_target = 0.0 # Target percentage of households that experience fuel poverty
fuel_poverty_baseline = 100.0  # Baseline percentage of households that experience fuel poverty
fuel_poverty_current = 31.65  # Current percentage of households that experience fuel poverty

# Percentage of people who consider the cost and gas and electricity as their 2 or 3 biggest financial concerns for their household
energy_cost_financial_concerns_target = 0.0 # Target percentage of people who consider the cost and gas and electricity as their 2 or 3 biggest financial concerns for their household
energy_cost_financial_concerns_baseline = 100.0  # Baseline percentage of people who consider the cost and gas and electricity as their 2 or 3 biggest financial concerns for their household
energy_cost_financial_concerns_current = 59.76  # Current percentage of people who consider the cost and gas and electricity as their 2 or 3 biggest financial concerns for their household

# Percentage of homes with electric or communal heating in Glasgow
electric_heating_target = 100.0 # Target percentage of homes with electric or communal heating in Glasgow
electric_heating_baseline = 0.0  # Baseline percentage of homes with electric or communal heating in Glasgow
electric_heating_current = 19.7  # Current percentage of homes with electric or communal heating in Glasgow 

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
st.header("Cycle Water indicators")
st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)
surface_water_quality_target = st.number_input("Target percentage of surface waters with at least good water quality (%)", min_value=0.0, max_value=100.0, value=surface_water_quality_target, step=0.1)    
surface_water_quality_baseline = st.number_input("Baseline percentage of surface waters with at least good water quality (%)", min_value=0.0, max_value=100.0, value=surface_water_quality_baseline, step=0.1)      
surface_water_quality_current = st.slider("Current percentage of surface waters with at least good water quality (%)", min_value=0.0, max_value=100.0, value=surface_water_quality_current, step=0.1)   
surface_water_quality_overshoot_value = min(100,100*(surface_water_quality_target - surface_water_quality_current)/(surface_water_quality_target - surface_water_quality_baseline))     
altair_horizontal_bar_chart(
    x=[surface_water_quality_overshoot_value],
    y=["Surface Water Quality"],
    title="Surface Water Quality Overshoot",
    xlabel="Category",
    y_min=0,
    y_max=100
)

surface_water_overall_status_target = st.number_input("Target percentage of surface waters assessed as having at least ‘good’ overall status (%)", min_value=0.0, max_value=100.0, value=surface_water_overall_status_target, step=0.1)         
surface_water_overall_status_baseline = st.number_input("Baseline percentage of surface waters assessed as having at least ‘good’ overall status (%)", min_value=0.0, max_value=100.0, value=surface_water_overall_status_baseline, step=0.1)   
surface_water_overall_status_current = st.slider("Current percentage of surface waters assessed as having at least ‘good’ overall status (%)", min_value=0.0, max_value=100.0, value=surface_water_overall_status_current, step=0.1)    
surface_water_overall_status_overshoot_value = min(100,100*(surface_water_overall_status_target - surface_water_overall_status_current)/(surface_water_overall_status_target - surface_water_overall_status_baseline))  
altair_horizontal_bar_chart(
    x=[surface_water_overall_status_overshoot_value],
    y=["Surface Water Overall Status"],
    title="Surface Water Overall Status Overshoot",
    xlabel="Category",
    y_min=0,
    y_max=100
)

groundwater_quality_target = st.number_input("Target percentage of groundwaters assessed as having at least 'good' status (%)", min_value=0.0, max_value=100.0, value=groundwater_quality_target, step=0.1) 
groundwater_quality_baseline = st.number_input("Baseline percentage of groundwaters assessed as having at least 'good' status (%)", min_value=0.0, max_value=100.0, value=groundwater_quality_baseline, step=0.1)   
groundwater_quality_current = st.slider("Current percentage of groundwaters assessed as having at least 'good' status (%)", min_value=0.0, max_value=100.0, value=groundwater_quality_current, step=0.1)    
groundwater_quality_overshoot_value = min(100,100*(groundwater_quality_target - groundwater_quality_current)/(groundwater_quality_target - groundwater_quality_baseline))   
altair_horizontal_bar_chart(
    x=[groundwater_quality_overshoot_value],
    y=["Groundwater Quality"],
    title="Groundwater Quality Overshoot",
    xlabel="Category",
    y_min=0,
    y_max=100
)


st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)
st.header("Store Carbon indicators")
st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)
tree_canopy_coverage_target = st.number_input("Target percentage of tree canopy coverage (%)", min_value=0.0, max_value=100.0, value=tree_canopy_coverage_target, step=0.1)
tree_canopy_coverage_baseline = st.number_input("Baseline percentage of tree canopy coverage (%)", min_value=0.0, max_value=100.0, value=tree_canopy_coverage_baseline, step=0.1)   
tree_canopy_coverage_current = st.slider("Current percentage of tree canopy coverage (%)", min_value=0.0, max_value=100.0, value=tree_canopy_coverage_current, step=0.1)
tree_canopy_coverage_overshoot_value = min(100,100*(tree_canopy_coverage_target - tree_canopy_coverage_current)/(tree_canopy_coverage_target - tree_canopy_coverage_baseline))
altair_horizontal_bar_chart(
    x=[tree_canopy_coverage_overshoot_value],
    y=["Tree Canopy Coverage"],
    title="Tree Canopy Coverage Overshoot",
    xlabel="Category",
    y_min=0,
    y_max=100
)  

peatlands_intact_restored_target = st.number_input("Target percentage of peatlands that are intact or restored (%)", min_value=0.0, max_value=100.0, value=peatlands_intact_restored_target, step=0.1)
peatlands_intact_restored_baseline = st.number_input("Baseline percentage of peatlands that are intact or restored (%)", min_value=0.0, max_value=100.0, value=peatlands_intact_restored_baseline, step=0.1)
peatlands_intact_restored_current = st.slider("Current percentage of peatlands that are intact or restored (%)", min_value=0.0, max_value=100.0, value=peatlands_intact_restored_current, step=0.1) 
peatlands_intact_restored_overshoot_value = min(100,100*(peatlands_intact_restored_target - peatlands_intact_restored_current)/(peatlands_intact_restored_target - peatlands_intact_restored_baseline))
altair_horizontal_bar_chart(
    x=[peatlands_intact_restored_overshoot_value],
    y=["Peatlands Intact or Restored"],
    title="Peatlands Intact or Restored Overshoot",
    xlabel="Category",
    y_min=0,
    y_max=100
)

carbon_sequestration_target = st.number_input("Target amount of carbon sequestrated in Glasgow in tonnes C per year", min_value=0.0, max_value=100000.0, value=carbon_sequestration_target, step=0.1)   
carbon_sequestration_baseline = st.number_input("Baseline amount of carbon sequestrated in Glasgow in tonnes C per year", min_value=0.0, max_value=100000.0, value=carbon_sequestration_baseline, step=0.1)
carbon_sequestration_current = st.slider("Current amount of carbon sequestrated in Glasgow in tonnes C per year", min_value=0.0, max_value=100000.0, value=carbon_sequestration_current, step=0.1)
carbon_sequestration_overshoot_value = min(100,100*(carbon_sequestration_target - carbon_sequestration_current)/(carbon_sequestration_target - carbon_sequestration_baseline))
altair_horizontal_bar_chart(
    x=[carbon_sequestration_overshoot_value],
    y=["Carbon Sequestration"],
    title="Carbon Sequestration Overshoot",
    xlabel="Category",
    y_min=0,
    y_max=100
)


st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)
st.header("Community indicators")
st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)

volunteering_target = st.number_input("Target percentage of adults in Glasgow who engage in a volunteering work (%)", min_value=0.0, max_value=100.0, value=volunteering_target, step=0.1)
volunteering_baseline = st.number_input("Baseline percentage of adults in Glasgow who engage in a volunteering work (%)", min_value=0.0, max_value=100.0, value=volunteering_baseline, step=0.1)    
volunteering_current = st.slider("Current percentage of adults in Glasgow who engage in a volunteering work (%)", min_value=0.0, max_value=100.0, value=volunteering_current, step=0.1)
volunteering_shortfall_value = min(100,100*(volunteering_target - volunteering_current)/(volunteering_target - volunteering_baseline))
altair_horizontal_bar_chart(
    x=[volunteering_shortfall_value],
    y=["Volunteering"],
    title="Volunteering Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100
)

neighbourhood_rating_target = st.number_input("Target percentage of people who rate their neighbourhood as very good or fairly good (%)", min_value=0.0, max_value=100.0, value=neighbourhood_rating_target, step=0.1)
neighbourhood_rating_baseline = st.number_input("Baseline percentage of people who rate their neighbourhood as very good or fairly good (%)", min_value=0.0, max_value=100.0, value=neighbourhood_rating_baseline, step=0.1)
neighbourhood_rating_current = st.slider("Current percentage of people who rate their neighbourhood as very good or fairly good (%)", min_value=0.0, max_value=100.0, value=neighbourhood_rating_current, step=0.1)
neighbourhood_rating_shortfall_value = min(100,100*(neighbourhood_rating_target - neighbourhood_rating_current)/(neighbourhood_rating_target - neighbourhood_rating_baseline))
altair_horizontal_bar_chart(
    x=[neighbourhood_rating_shortfall_value],
    y=["Neighbourhood Rating"],
    title="Neighbourhood Rating Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100
)

community_centre_satisfaction_target = st.number_input("Target percentage of people satisfied with local community centres (%)", min_value=0.0, max_value=100.0, value=community_centre_satisfaction_target, step=0.1)
community_centre_satisfaction_baseline = st.number_input("Baseline percentage of people satisfied with local community centres (%)", min_value=0.0, max_value=100.0, value=community_centre_satisfaction_baseline, step=0.1)
community_centre_satisfaction_current = st.slider("Current percentage of people satisfied with local community centres (%)", min_value=0.0, max_value=100.0, value=community_centre_satisfaction_current, step=0.1)
community_centre_satisfaction_shortfall_value = min(100,100*(community_centre_satisfaction_target - community_centre_satisfaction_current)/(community_centre_satisfaction_target - community_centre_satisfaction_baseline))
altair_horizontal_bar_chart(
    x=[community_centre_satisfaction_shortfall_value],
    y=["Community Centre Satisfaction"],
    title="Community Centre Satisfaction Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100
)

st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)
st.header("Culture indicators")
st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)

cultural_engagement_target = st.number_input("Target percentage of adults in Glasgow who engage in cultural events (%)", min_value=0.0, max_value=100.0, value=cultural_engagement_target, step=0.1)
cultural_engagement_baseline = st.number_input("Baseline percentage of adults in Glasgow who engage in cultural events (%)", min_value=0.0, max_value=100.0, value=cultural_engagement_baseline, step=0.1)
cultural_engagement_current = st.slider("Current percentage of adults in Glasgow who engage in cultural events (%)", min_value=0.0, max_value=100.0, value=cultural_engagement_current, step=0.1)
cultural_engagement_shortfall_value = min(100,100*(cultural_engagement_target - cultural_engagement_current)/(cultural_engagement_target - cultural_engagement_baseline))
altair_horizontal_bar_chart(
    x=[cultural_engagement_shortfall_value],
    y=["Cultural Engagement"],
    title="Cultural Engagement Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100
)

cultural_facilities_satisfaction_target = st.number_input("Target percentage of Glasgow residents who are satisfied with museums, libraries and theatres (%)", min_value=0.0, max_value=100.0, value=cultural_facilities_satisfaction_target, step=0.1)
cultural_facilities_satisfaction_baseline = st.number_input("Baseline percentage of Glasgow residents who are satisfied with museums, libraries and theatres (%)", min_value=0.0, max_value=100.0, value=cultural_facilities_satisfaction_baseline, step=0.1)
cultural_facilities_satisfaction_current = st.slider("Current percentage of Glasgow residents who are satisfied with museums, libraries and theatres (%)", min_value=0.0, max_value=100.0, value=cultural_facilities_satisfaction_current, step=0.1)
cultural_facilities_satisfaction_shortfall_value = min(100,100*(cultural_facilities_satisfaction_target - cultural_facilities_satisfaction_current)/(cultural_facilities_satisfaction_target - cultural_facilities_satisfaction_baseline))
altair_horizontal_bar_chart(
    x=[cultural_facilities_satisfaction_shortfall_value],
    y=["Cultural Facilities Satisfaction"],
    title="Cultural Facilities Satisfaction Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100
)

sports_leisure_satisfaction_target = st.number_input("Target percentage of Glasgow residents satisfied with sports and leisure centres (%)", min_value=0.0, max_value=100.0, value=sports_leisure_satisfaction_target, step=0.1)
sports_leisure_satisfaction_baseline = st.number_input("Baseline percentage of Glasgow residents satisfied with sports and leisure centres (%)", min_value=0.0, max_value=100.0, value=sports_leisure_satisfaction_baseline, step=0.1)
sports_leisure_satisfaction_current = st.slider("Current percentage of Glasgow residents satisfied with sports and leisure centres (%)", min_value=0.0, max_value=100.0, value=sports_leisure_satisfaction_current, step=0.1)
sports_leisure_satisfaction_shortfall_value = min(100,100*(sports_leisure_satisfaction_target - sports_leisure_satisfaction_current)/(sports_leisure_satisfaction_target - sports_leisure_satisfaction_baseline))
altair_horizontal_bar_chart(
    x=[sports_leisure_satisfaction_shortfall_value],
    y=["Sports and Leisure Satisfaction"],
    title="Sports and Leisure Satisfaction Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100
)

st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)
st.header("Housing indicators")
st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)

housing_satisfaction_target = st.number_input("Target percentage of households that are satisfied with housing (%)", min_value=0.0, max_value=100.0, value=housing_satisfaction_target, step=0.1)
housing_satisfaction_baseline = st.number_input("Baseline percentage of households that are satisfied with housing (%)", min_value=0.0, max_value=100.0, value=housing_satisfaction_baseline, step=0.1)
housing_satisfaction_current = st.slider("Current percentage of households that are satisfied with housing (%)", min_value=0.0, max_value=100.0, value=housing_satisfaction_current, step=0.1)
housing_satisfaction_shortfall_value = min(100,100*(housing_satisfaction_target - housing_satisfaction_current)/(housing_satisfaction_target - housing_satisfaction_baseline))
altair_horizontal_bar_chart(
    x=[housing_satisfaction_shortfall_value],
    y=["Housing Satisfaction"],
    title="Housing Satisfaction Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100
)

rent_cost_financial_concerns_target = st.number_input("Target percentage of people who consider rent cost among the 2-3 biggest financial concern for their household (%)", min_value=0.0, max_value=100.0, value=rent_cost_financial_concerns_target, step=0.1)
rent_cost_financial_concerns_baseline = st.number_input("Baseline percentage of people who consider rent cost among the 2-3 biggest financial concern for their household (%)", min_value=0.0, max_value=100.0, value=rent_cost_financial_concerns_baseline, step=0.1)
rent_cost_financial_concerns_current = st.slider("Current percentage of people who consider rent cost among the 2-3 biggest financial concern for their household (%)", min_value=0.0, max_value=100.0, value=rent_cost_financial_concerns_current, step=0.1)
rent_cost_financial_concerns_shortfall_value = min(100,100*(rent_cost_financial_concerns_current - rent_cost_financial_concerns_target)/(rent_cost_financial_concerns_baseline - rent_cost_financial_concerns_target))  
altair_horizontal_bar_chart(
    x=[rent_cost_financial_concerns_shortfall_value],
    y=["Rent Cost Financial Concerns"],
    title="Rent Cost Financial Concerns Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100
)

epc_band_target = st.number_input("Target percentage of homes with an EPC band at B/C or above (%)", min_value=0.0, max_value=100.0, value=epc_band_target, step=0.1)
epc_band_baseline = st.number_input("Baseline percentage of homes with an EPC band at B/C or above (%)", min_value=0.0, max_value=100.0, value=epc_band_baseline, step=0.1)
epc_band_current = st.slider("Current percentage of homes with an EPC band at B/C or above (%)", min_value=0.0, max_value=100.0, value=epc_band_current, step=0.1)
epc_band_shortfall_value = min(100,100*(epc_band_target - epc_band_current)/(epc_band_target - epc_band_baseline))  
altair_horizontal_bar_chart(
    x=[epc_band_shortfall_value],
    y=["EPC Band B/C or above"],
    title="EPC Band B/C or above Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100
)   

st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)
st.header("Energy indicators")
st.markdown("<hr style='border: 2px solid #0343DF;'>", unsafe_allow_html=True)

fuel_poverty_target = st.number_input("Target percentage of households that experience fuel poverty (%)", min_value=0.0, max_value=100.0, value=fuel_poverty_target, step=0.1)
fuel_poverty_baseline = st.number_input("Baseline percentage of households that experience fuel poverty (%)", min_value=0.0, max_value=100.0, value=fuel_poverty_baseline, step=0.1)
fuel_poverty_current = st.slider("Current percentage of households that experience fuel poverty (%)", min_value=0.0, max_value=100.0, value=fuel_poverty_current, step=0.1)
fuel_poverty_shortfall_value = min(100,100*(fuel_poverty_current - fuel_poverty_target)/(fuel_poverty_baseline - fuel_poverty_target))  
altair_horizontal_bar_chart(
    x=[fuel_poverty_shortfall_value],
    y=["Fuel Poverty"],
    title="Fuel Poverty Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100
)   

energy_cost_financial_concerns_target = st.number_input("Target percentage of people who consider the cost and gas and electricity as their 2 or 3 biggest financial concerns for their household (%)", min_value=0.0, max_value=100.0, value=energy_cost_financial_concerns_target, step=0.1)
energy_cost_financial_concerns_baseline = st.number_input("Baseline percentage of people who consider the cost and gas and electricity as their 2 or 3 biggest financial concerns for their household (%)", min_value=0.0, max_value=100.0, value=energy_cost_financial_concerns_baseline, step=0.1)
energy_cost_financial_concerns_current = st.slider("Current percentage of people who consider the cost and gas and electricity as their 2 or 3 biggest financial concerns for their household (%)", min_value=0.0, max_value=100.0, value=energy_cost_financial_concerns_current, step=0.1)
energy_cost_financial_concerns_shortfall_value = min(100,100*(energy_cost_financial_concerns_current - energy_cost_financial_concerns_target)/(energy_cost_financial_concerns_baseline - energy_cost_financial_concerns_target))  
altair_horizontal_bar_chart(
    x=[energy_cost_financial_concerns_shortfall_value],
    y=["Energy Cost Financial Concerns"],
    title="Energy Cost Financial Concerns Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100
)   

electric_heating_target = st.number_input("Target percentage of homes with electric or communal heating in Glasgow (%)", min_value=0.0, max_value=100.0, value=electric_heating_target, step=0.1)
electric_heating_baseline = st.number_input("Baseline percentage of homes with electric or communal heating in Glasgow (%)", min_value=0.0, max_value=100.0, value=electric_heating_baseline, step=0.1)
electric_heating_current = st.slider("Current percentage of homes with electric or communal heating in Glasgow (%)", min_value=0.0, max_value=100.0, value=electric_heating_current, step=0.1)
electric_heating_shortfall_value = min(100,100*(electric_heating_target - electric_heating_current)/(electric_heating_target - electric_heating_baseline))
altair_horizontal_bar_chart(
    x=[electric_heating_shortfall_value],   
    y=["Electric or Communal Heating"],
    title="Electric or Communal Heating Shortfall",
    xlabel="Category",
    y_min=0,
    y_max=100
)

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