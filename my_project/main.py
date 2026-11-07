import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import plotly.graph_objects as go

st.set_page_config(page_icon=":dollar:",
                   page_title="Personal Finance Analysis",
                   layout="wide")
st.title("Personal Finance Analysis")
df=pd.read_csv("cleaned_dataset.csv")
df2=pd.read_csv("Monthly_summary.csv")

with st.sidebar:
    op=option_menu("Option Menu",["Home","Dataset","Preprocessing","Categorical Analysis","Monthly Analysis","Saving Analysis","Summary","About"],
                   icons=["house","bar-chart","gear","graph-up","graph-down","cash-coin","journal-text","info-circle"])

if op=="Home":
    st.title("💰 Personal Finance Analysis")
    st.subheader("Understand your money. Improve your habits.")
    st.write(
        "Welcome to your personal finance dashboard. "
        "Track your expenses, monitor your savings, and "
        "understand your financial patterns."
    )
    st.divider()
    st.markdown("""
        <style>
        .kpi-card{
        border-radius:12px;
        padding:2rem;
        text-align:center;
        background-color:rgba(31, 138, 219, 0.62);
        margin:1px;
        transition:transform 0.1s;
        border:2px solid;
        }
        .kpi-label{
        font-size:2rem;
        font-weight:500;
        }
        .kpi-value{
        font-size:1.5rem;
        font-weight:250;
        }
        .kpi-card:hover{
        transform:scale(1.05);
        # box-shadow:0 6px 16px rgba(0,0,0,0.3);
        background-color:rgba(26, 194, 248, 0.62);
        }
        </style>
        """,unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="kpi-card">
        <div class="kpi-label">💸 Total Expenses</div>
        <div class="kpi-value">₹50,000</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="kpi-card">
        <div class="kpi-label">💰 Total Savings</div>
        <div class="kpi-value">₹35,000</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="kpi-card">
        <div class="kpi-label">📊 Average Expense</div>
        <div class="kpi-value">₹5,000</div>
        </div>
        """, unsafe_allow_html=True)
    st.divider()

    st.header("📊 Explore Your Finances")
    st.write(
        "Explore different aspects of your financial data "
        "using the analysis sections below."
    )

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📅 Monthly Analysis")
        st.write(
            "Analyze your financial activity month by month."
        )
        st.write("""
        • Monthly expenses  
        • Monthly savings  
        • Month-wise comparison  
        • Identify high and low spending months
        """)

    with col2:
        st.subheader("🗂️ Categorical Analysis")
        st.write(
            "Understand how your money is distributed across "
            "different categories."
        )

        st.write("""
        • Category-wise expenses  
        • Company-wise spending  
        • Subscription analysis  
        • Compare expense categories
        """)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💸 Expense Analysis")
        st.write(
            "Get a detailed understanding of your overall "
            "spending and expenses."
        )
        st.write("""
        • Total expenses  
        • Average expenses  
        • Major expenses  
        • Spending patterns
        """)
    with col2:
        st.subheader("💰 Saving Analysis")
        st.write(
            "Monitor your savings and understand how effectively "
            "you manage your income."
        )
        st.write("""
        • Total savings  
        • Monthly savings  
        • Saving rate  
        • Highest and lowest saving periods
        """)
    st.divider()
    st.header("🎯 Why use this dashboard?")
    st.info(
        "This dashboard provides a simple way to understand your "
        "financial situation. Analyze your expenses, compare "
        "different categories, track monthly changes, and "
        "monitor your savings to make better financial decisions."
    )
    st.divider()
    st.header("🚀 Explore Your Finances")
    st.write(
        "Select an analysis section from the navigation menu "
        "to explore your financial data in detail."
    )
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("📅")
        st.caption("Monthly Analysis")

    with col2:
        st.write("🗂️")
        st.caption("Categorical Analysis")

    with col3:
        st.write("💸")
        st.caption("Expense Analysis")

    with col4:
        st.write("💰")
        st.caption("Saving Analysis")

    st.divider()
    st.caption(
        "Personal Finance Analysis Dashboard | "
        "Built with Python • Pandas • Streamlit • Plotly"
    )

elif op=="Dataset":
    st.header("📂 DATASET OVERVIEW")
    st.write("This dataset is based upon the personal expenses of a person on different areas.It classifies the data in different categories and analyse them.It helps to give further recommendations for saving money based on that analysis.")
    st.subheader("DATASET PREVIEW")
    st.dataframe(df.head())
    st.subheader("DATASET SHAPE")
    c1,c2=st.columns(2)
    with c1:
        st.metric("No. of rows are:",df.shape[0])
    with c2:
        st.metric("No. of columns are:",df.shape[1])
    st.subheader("More About The Columns")
    st.markdown("- Date\n - Description\n - Amount\n- Transaction type\n- Category\n- Account name\n- Month\n- New Category")
    st.subheader("Datatype")
    st.dataframe(
        pd.DataFrame(
            df.dtypes,
            columns=["Data Type"]
        )
    )
    st.subheader("Statistical summary")
    with st.expander("Click to view statistical summary"):
        st.dataframe(df.describe())
    st.subheader("Dataset importance")
    st.markdown("""
                - Provides insights into employee mental health.
                - Enables workplace trend analysis.
                - Supports burnout and productivity assessment.
                - Facilitates data-driven decision making.
                - Forms the basis for all dashboard visualizations""")

elif op=="Preprocessing":
    st.header("⚙️Data Preprocessing")
    st.markdown("Data preprocessing is the process of preparing raw data so it is clean, organized, and suitable for analysis or for training a machine learning model.It typically includes steps such as:")
    st.markdown("""
                    - Cleaning data: Removing errors, duplicates, and handling missing values.
                    - Transforming data: Converting data into the required format (for example, changing text to numbers).
                    - Normalizing or scaling: Adjusting numerical values to a common range.
                    - Encoding categorical data: Converting categories (like "Male" or "Female") into numerical values.
                    - Feature selection: Choosing the most relevant variables for analysis.""")
    st.subheader("Missing Values")
    st.dataframe(pd.DataFrame(df.isna().sum()))
    st.subheader("Data Cleaning Steps ")
    st.markdown("""
                    - Verified and handled missing values.
                    - Checked for duplicate records.
                    - Ensured consistency across categorical variables.
                    - Validated numerical attributes for analysis.
                    - Confirmed appropriate data types for all features.
                    - Removed data inconsistencies and anomalies.
                    - Prepared the dataset for interactive visualization.
                    - Final dataset is clean, structured, and analysis-ready.""")
    st.subheader("Preprocessing Outcome")
    st.write("After completing the preprocessing phase, the dataset was found to be suitable for exploratory data analysis (EDA)," \
                " relationship analysis, and dashboard development. The cleaned dataset enables organizations and stakeholders to derive " \
                "actionable insights regarding employee mental health and workplace well-being.")

elif op=="Categorical Analysis":
    st.header("Categorical Analysis")
    st.write("Here is a simple bar graph showing Categorical expenses")
    filtered21=df.groupby(["New_Category"])["Amount"].sum().reset_index()
    filtered21.columns=["New_Category","TAmount"]
    fig21=px.bar(
        filtered21,
        x="New_Category",
        y="TAmount",
        title="Expenses including credit card payment",
        labels={"New_Category":"Category",
                "TAmount":"Total Amount"},
        color_discrete_sequence=["red"]
    )
    filtered22=df.groupby(["New_Category"])["Amount"].sum().reset_index()
    filtered22=filtered22[filtered22["New_Category"]!="Credit Card Payment"]
    filtered22.columns=["New_Category","TAmount"]
    fig22=px.bar(
        filtered22,
        x="New_Category",
        y="TAmount",
        title="Expenses excluding credit card payment",
        labels={"New_Category":"Category",
                "TAmount":"Total Amount"},
        color_discrete_sequence=["red"]
    )
    c21,c22=st.columns(2)
    with c21:
        st.plotly_chart(fig21,use_container_width=True)
    with c22:
        st.plotly_chart(fig22,use_container_width=True)

    st.header("Expenses for selected categories")
    m21=st.multiselect("Select the categories whose expenses you want to see",options=df["New_Category"].unique())
    filtered23=df[df["New_Category"].isin(m21)].reset_index()
    filtered23=filtered23.groupby(["New_Category"])["Amount"].sum().reset_index()
    filtered23.columns=["Category","Amount"]
    fig23=px.pie(
        filtered23,
        labels="Category",
        values="Amount",
        title="Deep category wise analysis",
        hover_data="Category"
    )
    st.plotly_chart(fig23,use_container_width=True)
    st.header("Detailed expenses list for all categories")
    filtered24=df[df["New_Category"]!="Credit Card Payment"].reset_index()
    filtered24=filtered24.groupby(["Category"])["Amount"].sum().reset_index()
    filtered24.columns=["Category","Amount"]
    fig24=px.bar(
        filtered24,
        x="Category",
        y="Amount",
        title="Deep category wise analysis",
        hover_data="Category"
    )
    st.plotly_chart(fig24,use_container_width=True)

# monthly analysis
elif op=="Monthly Analysis":
    st.header("Monthly Expenses")
    st.write("Here is a simple bar graph showing monthly expenses form JAN2018 to SEP2019")
    # fig1df=df2.groupby(["Monthly"])["Monthly_expense"]
    fig11=px.bar(
        df2,
        x="Monthly",
        y="Monthly_expense",
        labels={
            "Monthly":"Month",
        }
    )
    st.plotly_chart(fig11,use_container_width=True)
    st.header("Selected Month wise expenses")
    m11=st.multiselect("Select the months whose expenses you want from Jan18 to Sep19",options=df2["Monthly"].unique())
    if m11:
        filtered11=df2[df2["Monthly"].isin(m11)]
    else:
        filtered11=df2
    fig12=px.bar(
        filtered11,
        x="Monthly",
        y="Monthly_expense" ,
        labels={
                "Monthly":"Month",
            }   
    )
    st.plotly_chart(fig12,use_container_width=True,key="chart1")
    st.header("Month wise detailed expenses chart")
    m12=st.selectbox("Enter the month whose detailed study you want",options=df2["Monthly"].unique())
    if m12:
        filtered12=df[df["Month"]==m12].reset_index()
    else:
        st.write("Please select a month here!!")
    filtered12=filtered12.groupby(["New_Category"])["Amount"].sum().reset_index()
    filtered12.columns=["New_Category","TAmount"]
    fig13=px.pie(
        filtered12,
        labels="New_Category",
        values="TAmount",
        title="expenses including credit card" ,
        hover_data="New_Category"   
    )
    filtered13=df[(df["Month"]==m12) & (df["New_Category"]!="Credit Card Payment")].reset_index()
    filtered13=filtered13.groupby(["New_Category"])["Amount"].sum().reset_index()
    filtered13.columns=["New_Category","TAmount"]
    fig14=px.pie(
        filtered13,
        labels="New_Category",
        values="TAmount",
        title="expenses excluding credit card" ,
        hover_data="New_Category"     
    )
    c11,c12=st.columns(2)
    with c11:
        st.plotly_chart(fig13,use_container_width=True)
    with c12:
        st.plotly_chart(fig14,use_container_width=True)
# saving analysis
elif op=="Saving Analysis":
    # for Saving analysis with a checkbox
    st.header("Savings Analysis")
    st.markdown("""
    <style>
    .kpi-card{
    border-radius:12px;
    padding:2rem;
    text-align:center;
    background-color:rgba(31, 138, 219, 0.62);
    margin:auto;
    transition:transform 0.1s;      
    border:2px solid;
    width:fit-content;
    }
    .kpi-label{
    font-size:2rem;
    font-weight:500;
    }
    .kpi-value{
    font-size:1.5rem;
    font-weight:250;
    }
    .kpi-card:hover{
    transform:scale(1.05);
    # box-shadow:0 6px 16px rgba(0,0,0,0.3);
    background-color:rgba(26, 194, 248, 0.62);
    }
    </style>
    """,unsafe_allow_html=True)



    c1,c2,c3,c4=st.columns(4)
    with c1:
        st.markdown("""
        <div class="kpi-card">
        <div class="kpi-label"> Total Salary</div>
        <div class="kpi-value">$17,000</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
            <div class="kpi-card">
            <div class="kpi-label"> Max saving</div>
            <div class="kpi-value">$9,364</div>
            </div>
            """, unsafe_allow_html=True) 

    with c3:
        st.markdown("""
            <div class="kpi-card">
            <div class="kpi-label"> Min saving</div>
            <div class="kpi-value">$486</div>
            </div>
            """, unsafe_allow_html=True) 

    with c4:
        st.markdown("""
            <div class="kpi-card">
            <div class="kpi-label"> Average saving</div>
            <div class="kpi-value">$6,507</div>
            </div>
            """, unsafe_allow_html=True) 

    st.divider()
    fig31=px.bar(
        data_frame=df2,
        x="Monthly",
        y="Saving",
        labels={
        "Monthly":"Month"
        }
    )
    st.header("Savings Month wise")
    st.plotly_chart(fig31,use_container_width=True)

    st.divider()
    st.header("What should be the avg amount spend on each category?")
    st.write("For each cateogry there should be an idle amount of money expenditure to maximise the savings")
    filtered32=df.groupby(["New_Category"])["Amount"].mean().reset_index()
    filtered32.columns=["cat","amount"]
    fig32=px.line(
    data_frame=filtered32,
    x="cat",
    y="amount",
    labels={
        "cat":"Category",
        "amount":"Avg. expenditure"
    },
    markers="diamond"
    )
    st.plotly_chart(fig32,use_container_width=True)

    st.header("Realtion b/w idle and actual amount spent")
    m31=st.selectbox("Select a month below to check the idle and actual amount spent on category for that month",options=df2["Monthly"].unique())
    if m31:
        filtered33=df[df["Month"]==m31].reset_index()
    else:
        st.write("Please select a month here!!")
    idle_df=df.groupby(["Month","New_Category"])["Amount"].sum().reset_index()
    idle_df=idle_df.groupby("New_Category")["Amount"].mean().reset_index()
    actual_df=df[df["Month"]==m31]
    actual_df=actual_df.groupby("New_Category")["Amount"].sum().reset_index()
    fig=go.Figure()
    fig.add_trace(go.Scatter(
        x=idle_df["New_Category"],
        y=idle_df["Amount"],
        name="Idle expenditure on each category"
    ))
    fig.add_trace(go.Scatter(
         x=actual_df["New_Category"],
         y=actual_df["Amount"],
         name="Actual expenditure on each category"
     ))
    st.plotly_chart(fig,use_container_width=True)

elif op=="Summary":

    st.title("📊 Project Summary")
    st.markdown("---")

    st.header("💰 Personal Finance Analysis")

    st.write("""
    Personal Finance Analysis is an interactive web-based application
    developed using Python and Streamlit. It is designed to help users
    manage, track and understand their financial activities by analyzing
    daily transactions, monthly expenses and savings.

    The application converts raw financial data into meaningful insights
    through data processing, statistical calculations and interactive
    visualizations. It helps users identify their spending habits,
    understand category-wise expenses and monitor their savings.

    Using Pandas, Plotly and Matplotlib, the application presents financial
    information in an organized and visually understandable format,
    making personal financial management easier and more effective.
    """)

    st.markdown("---")

    st.header("✨ Key Features")

    st.subheader("1. 📅 Monthly Analysis")
    st.write("""
    Provides month-wise expense analysis and helps users understand
    changes in their spending patterns over different periods.
    """)

    st.subheader("2. 📂 Categorical Analysis")
    st.write("""
    Analyzes expenses across different categories and identifies
    which categories consume the largest portion of the user's money.
    """)

    st.subheader("3. 💸 Expense Analysis")
    st.write("""
    Provides detailed insights into expenditure and helps users
    understand how their money is distributed among different categories.
    """)

    st.subheader("4. ⚖️ Ideal vs Actual Spending")
    st.write("""
    Compares the average monthly spending of each category, calculated
    using the entire year's data, with the actual spending of a selected
    month. This comparison helps users identify variations in their
    monthly spending habits.
    """)

    st.subheader("5. 🏦 Saving Analysis")
    st.write("""
    Focuses on monthly savings and helps users understand their saving
    patterns and evaluate their financial management.
    """)

    st.markdown("---")

    st.header("🎯 Project Objectives")

    st.write("""
    - To organize and analyze personal financial transactions.
    - To understand monthly and category-wise spending patterns.
    - To compare average and actual monthly expenses.
    - To monitor savings and improve financial awareness.
    - To present financial information through interactive visualizations.
    - To support better budgeting and financial decision-making.
    """)

    st.markdown("---")

    st.header("🛠️ Technologies Used")

    st.write("""
    - **Python:** Main programming language.
    - **Streamlit:** Development of the interactive web application.
    - **Pandas:** Data cleaning, grouping and manipulation.
    - **Plotly:** Interactive charts and graphs.
    - **Matplotlib:** Data visualization and graphical representation.
    """)

    st.markdown("---")

    st.header("🚀 Future Scope")

    st.write("""
    The project can be further enhanced by introducing expense prediction,
    automated budget planning, personalized saving recommendations,
    financial alerts and automated transaction tracking.

    These improvements can make the application more intelligent and
    help users manage their finances more efficiently.
    """)

    st.markdown("---")

    st.success(
        "Manage Your Money Better | Understand Your Spending | Save Smarter"
    )


elif op=="About":
    st.header("About Project")
    c41,c42=st.columns([4,1])
    with c41:
        st.markdown("---")
        st.subheader("Project Description")
        st.write("""
        Personal Finance Analysis is a data analysis and visualization project developed using Python,
        Pandas, Streamlit, and Plotly. The project helps users understand and analyze their personal 
        spending patterns through an interactive dashboard.

        It provides insights into monthly expenses, spending categories, transaction trends, and overall
        financial behavior. Users can select specific months and categories to view detailed expense breakdowns
        through interactive charts and visualizations. The dashboard makes it easier to identify major spending 
        areas, compare expenses across months, and understand where money is being spent.
        """)
        st.markdown("---")
        st.subheader("Project Objectives")
        st.write("""
        1.To analyze personal financial data and understand overall spending patterns.\n
        2.To track monthly expenses and identify changes in spending from one month to another.\n
        3.To categorize expenses into different spending categories for better financial understanding.\n
        4.To identify major spending areas and determine which categories contribute most to total expenses.\n
        5.To provide interactive data visualization using charts and graphs for easier interpretation of financial data.\n
        6.To develop an interactive dashboard using Streamlit that allows users to filter and explore their financial data.\n
        7.To provide detailed month-wise analysis so users can examine their expenses for a particular month.\n
        8.To help users make better financial decisions by providing clear insights into their spending habits.\n
        9.To demonstrate practical use of Python and data analysis techniques such as Pandas, Plotly, and Streamlit in a real-world project.\n
        """)

        st.markdown("---")
        st.subheader("Future Scope")
        st.write("""
        📱 Develop a mobile application for easier access to financial analysis.\n
        🤖 Add AI/ML-based expense predictions to forecast future spending.\n
        🔔 Implement budget and spending alerts when expenses exceed predefined limits.\n
        💳 Integrate bank and digital payment data for automatic transaction tracking.\n
        📊 Add more advanced financial dashboards and visualizations.\n
        🎯 Introduce personalized budgeting and savings recommendations.\n
        📈 Provide future expense and savings forecasts based on previous spending patterns.\n
        🔐 Improve data security and privacy for storing personal financial information.\n
        📄 Add options to generate and download financial reports in PDF or Excel format.\n
        ☁️ Enable cloud storage and synchronization so users can access their financial data across devices.\n
        """)
    st.markdown("---")
    st.info(
        "This project demonstrates the application of Python and Data Analytics "
        "techniques to address real-world challenges related to employee mental health."
    )
    with c42:
        st.subheader("Project Info")
        st.write("**Student Name:** Vanshika choudhary")
        st.write("**Program:** B.Tech (Computer Science)")
        st.write("**College:** DAVIET, Jalandhar")
        st.write("**Project Title:** Personal Finance Analysis")
        st.write("**Tools Used:** Python, Pandas, Plotly, Streamlit")
        st.write("**Domain:** Data Science & Data Analytics")
