# updated.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from datetime import datetime

st.set_page_config(page_title="UMéRA Investment Analytics Dashboard", layout="wide")
st.title("📊 Comprehensive UMéRA Investors Age Segmentation Analytics Dashboard")

st.markdown("---")

# Load data
df = pd.read_excel("processed_investment_data.xlsx")

# Data preprocessing
columns_to_keep = ['DOB', 'INVESTMENT YEAR', 'INVESTMENT MONTH', 'LAND', 'UNIT', 'AMOUNT']
df = df[columns_to_keep].copy()
df = df.dropna(subset=['DOB', 'AMOUNT'])
df['DOB'] = pd.to_datetime(df['DOB'], errors='coerce')
df = df.dropna(subset=['DOB'])
df['AGE'] = df['DOB'].apply(lambda x: 2025 - x.year if pd.notnull(x) else None)

month_order = ['JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER', 'JANUARY']
df['INVESTMENT MONTH'] = df['INVESTMENT MONTH'].astype(str).str.strip().str.upper()
df = df[df['INVESTMENT MONTH'].isin(month_order)]
df['INVESTMENT MONTH'] = pd.Categorical(df['INVESTMENT MONTH'], categories=month_order, ordered=True)

df['UNIT'] = pd.to_numeric(df['UNIT'], errors='coerce')
df['AMOUNT'] = pd.to_numeric(df['AMOUNT'], errors='coerce')
df = df.dropna()

bins = [18, 30, 40, 50, 60, 70, 100]
labels = ["18-29", "30-39", "40-49", "50-59", "60-69", "70+"]
df["AGE GROUP"] = pd.cut(df["AGE"], bins=bins, labels=labels, right=False)
df = df[df["INVESTMENT MONTH"].notna()]

# Sidebar filters
st.sidebar.header("🔎 Filter Data")
selected_year = st.sidebar.selectbox("Select Investment Year", sorted(df["INVESTMENT YEAR"].unique()), index=0)
selected_age_groups = st.sidebar.multiselect("Select Age Groups", options=df["AGE GROUP"].unique(), default=df["AGE GROUP"].unique())
selected_land_types = st.sidebar.multiselect("Select Land Types", options=df["LAND"].unique(), default=df["LAND"].unique())

filtered_df = df[(df["INVESTMENT YEAR"] == selected_year) &
                 (df["AGE GROUP"].isin(selected_age_groups)) &
                 (df["LAND"].isin(selected_land_types))]

# Key Metrics
total_investment = filtered_df['AMOUNT'].sum()
total_units = filtered_df['UNIT'].sum()
total_investors = filtered_df['DOB'].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Investment", f"₦{total_investment:,.0f}")
col2.metric("📦 Total Units", f"{total_units:,.0f}")
col3.metric("👥 Unique Investors", f"{total_investors}")

# Plotly Bar Chart: Total Investment by Age Group
age_amount_df = filtered_df.groupby("AGE GROUP")["AMOUNT"].sum().reset_index()
fig1 = px.bar(age_amount_df, x="AGE GROUP", y="AMOUNT", color="AGE GROUP", title="Total Investment by Age Group", text_auto=True)
st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# Seaborn Chart 1: Total Investment by Age Group
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x="AGE GROUP", y="AMOUNT", data=age_amount_df, palette="viridis", ax=ax2)
ax2.set_title("Total Investment by Age Group")
ax2.set_ylabel("Total Amount Paid (₦)")
ax2.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig2)

st.markdown("---")

# Distribution of Land Type by Age Group
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.countplot(data=filtered_df, x="AGE GROUP", hue="LAND", order=labels, palette="coolwarm", ax=ax3)
ax3.set_title("Distribution of Land Type Purchased by Age Group")
ax3.set_ylabel("Count of Investors")
ax3.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig3)

st.markdown("---")

# Units Purchased
age_units_df = filtered_df.groupby("AGE GROUP")["UNIT"].sum().reset_index()
fig4 = px.bar(age_units_df, x="AGE GROUP", y="UNIT", color="AGE GROUP", text_auto=True, title="Total Units Purchased by Age Group")
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")

# Pie Chart
fig5 = px.pie(age_amount_df, values="AMOUNT", names="AGE GROUP", title="Proportion of Investment by Age Group")
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")

# Trend Line
monthly_investment = filtered_df.groupby("INVESTMENT MONTH")["AMOUNT"].sum().reset_index()
fig6 = px.line(monthly_investment, x="INVESTMENT MONTH", y="AMOUNT", markers=True, title="Monthly Investment Trend")
st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")

# Trend by Age Group
fig7 = px.line(filtered_df, x="INVESTMENT MONTH", y="AMOUNT", color="AGE GROUP", markers=True, title="Investment Trend by Age Group")
st.plotly_chart(fig7, use_container_width=True)

st.markdown("---")

# Heatmap: Age Group vs. Month
heatmap_data = filtered_df.pivot_table(index="INVESTMENT MONTH", columns="AGE GROUP", values="AMOUNT", aggfunc="sum", fill_value=0)
fig8, ax8 = plt.subplots(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="coolwarm", linewidths=0.5, ax=ax8)
ax8.set_title("Heatmap of Investment Amount by Age Group and Month")
st.pyplot(fig8)

st.markdown("---")

# Stacked Bar Chart
df_grouped = filtered_df.groupby(["INVESTMENT MONTH", "AGE GROUP"])["AMOUNT"].sum().unstack().reindex(columns=labels)
fig9, ax9 = plt.subplots(figsize=(12, 6))
df_grouped.plot(kind="bar", stacked=True, colormap="viridis", ax=ax9)
ax9.set_title("Stacked Bar Chart: Investment by Age Group and Month")
ax9.set_xlabel("Investment Month")
ax9.set_ylabel("Total Investment Amount")
ax9.legend(title="Age Group")
ax9.set_xticklabels(df_grouped.index, rotation=45)
st.pyplot(fig9)

st.markdown("---")

# Grouped Bar Chart
fig10, ax10 = plt.subplots(figsize=(12, 6))
df_grouped.plot(kind="bar", stacked=False, colormap="coolwarm", ax=ax10)
ax10.set_title("Grouped Bar Chart: Investment by Age Group and Month")
ax10.set_xlabel("Investment Month")
ax10.set_ylabel("Total Investment Amount")
ax10.legend(title="Age Group")
ax10.set_xticklabels(df_grouped.index, rotation=45)
st.pyplot(fig10)

st.markdown("---")

# Bubble Chart
fig11, ax11 = plt.subplots(figsize=(12, 6))
sns.scatterplot(data=filtered_df, x="INVESTMENT MONTH", y="AGE GROUP", size="AMOUNT", hue="AGE GROUP", sizes=(20, 1000), palette="coolwarm", alpha=0.6, ax=ax11)
ax11.set_title("Bubble Chart: Investment Amount by Age Group and Month")
ax11.set_xlabel("Investment Month")
ax11.set_ylabel("Age Group")
ax11.legend(title="Investment Amount", bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig11)

st.markdown("---")

# Chart: Boxplot - Investment Amount Distribution by Age Group
st.subheader("📦 Boxplot: Investment Amount Distribution by Age Group")
fig_box, ax_box = plt.subplots(figsize=(10, 6))
sns.boxplot(data=filtered_df, x="AGE GROUP", y="AMOUNT", palette="coolwarm", hue="AGE GROUP", ax=ax_box, legend=False)
ax_box.set_xlabel("Age Group")
ax_box.set_ylabel("Investment Amount (₦)")
ax_box.set_title("Investment Amount Distribution by Age Group")
ax_box.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig_box)

st.markdown("---")

# Chart: Bar Chart - Total Investment by Year (from filtered_df)
st.subheader("📅 Total Investment by Year")
yearly_df = df[df["AGE GROUP"].isin(selected_age_groups) & df["LAND"].isin(selected_land_types)]
yearly_grouped = yearly_df.groupby("INVESTMENT YEAR")["AMOUNT"].sum().reset_index()
fig_year, ax_year = plt.subplots(figsize=(10, 6))
sns.barplot(data=yearly_grouped, x="INVESTMENT YEAR", y="AMOUNT", palette="viridis", ax=ax_year)
ax_year.set_xlabel("Investment Year")
ax_year.set_ylabel("Total Investment Amount (₦)")
ax_year.set_title("Investment Trends Over the Years")
ax_year.set_xticklabels(ax_year.get_xticklabels(), rotation=45)
ax_year.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig_year)

st.markdown("---")

# Cross-tabulation Heatmap
age_month_ct = pd.crosstab(filtered_df["INVESTMENT MONTH"], filtered_df["AGE GROUP"])
fig12, ax12 = plt.subplots(figsize=(10, 6))
sns.heatmap(age_month_ct, annot=True, cmap="coolwarm", linewidths=0.5, fmt="d", ax=ax12)
ax12.set_title("Investment Distribution Across Months and Age Groups")
ax12.set_xlabel("Age Group")
ax12.set_ylabel("Investment Month")
st.pyplot(fig12)

st.markdown("---")

# Sidebar extra info
st.sidebar.markdown("---")
st.sidebar.markdown("**Unique Investment Months:**")
st.sidebar.write(df["INVESTMENT MONTH"].unique())



# Word Report Download
st.markdown("### \U0001F4DD Download Full UMéRA Portfolio Analytics Report")
with open("UMéRA Royal Palm Data Analytics Report.docx", "rb") as doc_file:
    st.download_button(
        label="\U0001F4E5 Download Full Word Report",
        data=doc_file,
        file_name="UMeRA_RoyalPalm_Analytics_Report.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

# Footer
st.markdown("---")
st.markdown("# About the Developer")

st.image("Gbenga.jpg", width=300)
st.markdown("## **Kajola Gbenga**")

st.markdown(
    """
\U0001F4C7 Certified Data Analyst | Certified Data Scientist | Certified SQL Programmer | Mobile App Developer | AI/ML Engineer

\U0001F517 [LinkedIn](https://www.linkedin.com/in/kajolagbenga)  
\U0001F4DC [View My Certifications & Licences](https://www.datacamp.com/portfolio/kgbenga234)  
\U0001F4BB [GitHub](https://github.com/prodigy234)  
\U0001F310 [Portfolio](https://kajolagbenga.netlify.app/)  
\U0001F4E7 k.gbenga234@gmail.com
"""
)