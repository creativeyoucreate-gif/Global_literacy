
# #1.Checking for missing values in the DataFrame. The isnull() function returns a DataFrame of the same shape as adult_df, where each cell contains True if the corresponding value in adult_df is null (missing) and False otherwise. The sum() function then counts the number of True values in each column, giving us the total count of missing values for each column.
# adult_df.isnull().sum()
# #2.Dropping the 'code' column from the DataFrame since it is having more than 40 % of null values not needed for our analysis.
# adult_df = adult_df.drop(columns=['code'])
# #3.Checking for duplicate rows in the DataFrame. The duplicated() function returns a Series of boolean values indicating whether each row is a duplicate of a previous row. The sum() function then counts the number of True values in this Series, giving us the total count of duplicate rows in the DataFrame.
# adult_df.duplicated().sum()
# #4.Cleaning the 'Country' column by removing leading and trailing whitespace and converting the text to title case (capitalizing the first letter of each word) for better readability and consistency.
# adult_df['Country'] = adult_df['Country'].str.strip().str.title()
# #5.Getting a concise summary of the DataFrame, including the number of non-null entries, data types of each column, and memory usage. This helps us understand the structure of the DataFrame and identify any potential issues with missing data or incorrect data types.
# adult_df.info()
# #6.Checking the number of rows and columns in the DataFrame. The shape attribute returns a tuple where the first element is the number of rows and the second element is the number of columns.
# adult_df.shape
# #7.Getting a statistical summary of the DataFrame, including count, mean, standard deviation, minimum, 25th percentile, median (50th percentile), 75th percentile, and maximum values for each numeric column. This helps us understand the distribution and central tendency of the data.
# adult_df.describe()
# #8.Renaming the columns 'entity' to 'Country' and 'adult_literacy_rate__population_15plus_years__both_sexes__pct__lr_ag15t99' to 'Adult_Literacy_Rate' for better readability and understanding of the data. The rename() function is used to change the column names in the DataFrame, and the inplace=True argument ensures that the changes are made directly to the original DataFrame without needing to assign it back to a new variable.      
# adult_df.rename(columns={'entity': 'Country', 'adult_literacy_rate__population_15plus_years__both_sexes__pct__lr_ag15t99': 'Adult_Literacy_Rate'}, inplace=True)


import streamlit as st
from streamlit_option_menu import option_menu
import sql_query_executor as sqe # import your file
import eda_visualization as edav # import your file
import country_profile_page as cpp # import your file

st.set_page_config(layout='wide')

col1, col2 = st.columns([1, 5])

with col1:
    st.image("C:\\Users\\hemhe\\Documents\\GUVIproject\\project1\\Create a transparent.png", width=450)




with st.sidebar:

    st.markdown("<h1 style='text-align:center; margin-bottom:0px; font-size:16px; color:blue;'>Main Menu</h1>", unsafe_allow_html=True)
         
    select = option_menu(None, ['SQL Query Executor', 'EDA Visualizations', 'Country Profile Page'],
     icons=['database', 'bar-chart', 'globe'], menu_icon='menu', default_index=0,
     styles={"container": {"text-align": "center"},
            "icon": {"color": "white", "font-size": "14px"},
            "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px"},
            "nav-link-selected": {"background-color": "blue"},})
 

if select == 'SQL Query Executor':
    sqe.run() # 👈 Call function from sql_query_executor.py

elif select == 'EDA Visualizations':
    edav.run()   # 👈 Call function from eda_visualization.py

elif select == 'Country Profile Page':
    cpp.run()  #👈 Call function from country_profile_page.py