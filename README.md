
# 📊 UMéRA Investment Analytics Dashboard

This project is a **fully interactive investment age-segmentation data analytics dashboard** built using **Streamlit** to visualize and analyze investment data for UMéRA Real Estate. It features advanced filtering, insightful metrics, and a range of compelling visualizations for stakeholder decision-making.

It was designed to analyze investor trends and age segmentation for UMéRA Real Estate Investment Portfolio. It transforms raw Excel data into meaningful insights through a rich blend of charts, filters, and metrics tailored for business leaders, analysts, and stakeholders.

---

This well detailed Investment Analytics Dashboard which I developed for UMéRA can be accessed live on streamlit [Here](https://umerainvestments.streamlit.app/)

---

## 📬 Author

**Gbenga Kajola**

[LinkedIn](https://www.linkedin.com/in/kajolagbenga)

[Certified_Data_Scientist](https://www.datacamp.com/certificate/DSA0012312825030)

[Certified_Data_Analyst](https://www.datacamp.com/certificate/DAA0018583322187)

[Certified_SQL_Database_Programmer](https://www.datacamp.com/certificate/SQA0019722049554)


---

## 📁 Dataset Used

The dataset used is [`processed_investment_data.xlsx`](./processed_investment_data.xlsx), due to security and to protect the sensitive informations of investors, and as a result encrepted file which contains anonymized records of investor transactions including:

- **Date of Birth (DOB)**
- **Investment Year and Month**
- **Land Types**
- **Units Purchased**
- **Investment Amount**

This data enables segmentation and trend analysis by investor age group, land type, and investment timelines.

---

## 🎯 Project Objectives

- Provide management with a clear **overview of investment patterns**.
- Visualize **age-based segmentation** of investors.
- Track **monthly and yearly investment trends**.
- Identify **popular land types** across demographics.
- Present a **comprehensive downloadable Word report** for offline insights.

---

## 🧑‍💼 Target Users

- UMéRA Executives & Investment Managers
- Marketing & Strategy Teams
- Data Analysts for internal reporting
- Potential Investors (as a case study)

---

## 📌 Key Features

### 🔍 Sidebar Filters
- **Investment Year** filter
- **Age Group** selection
- **Land Type** selection

### 📈 Visualizations
| Visualization Type                         | Description |
|-------------------------------------------|-------------|
| **Bar Charts**                             | Investment by Age Group and Units |
| **Seaborn & Matplotlib Charts**            | Grouped bar, boxplot, and trends |
| **Plotly Charts**                          | Interactive investment visuals |
| **Heatmaps**                               | Monthly vs. Age Group metrics |
| **Pie Chart**                              | Proportional investment distribution |
| **Bubble Chart**                           | Investment intensity by age & month |

### 📄 Report Export
- Downloadable `.docx` report via Streamlit interface.

---

## 🧠 Tech Stack

| Tool/Library    | Purpose                         |
|------------------|----------------------------------|
| `streamlit`      | Web framework for Python apps   |
| `pandas`         | Data cleaning & manipulation    |
| `openpyxl`       | Reading Excel files             |
| `matplotlib`     | Static visualizations           |
| `seaborn`        | Enhanced plotting with stats    |
| `plotly`         | Interactive charts              |
| `numpy`          | Numeric computations            |

---

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/prodigy234/prodigy234-UMeRA_Royal_Palm_Customer_Age_Segmentation_Data_Analytics_July_2024_to_January_2025.git
   cd umera-investment-dashboard
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run updated.py
   ```

4. **Upload the dataset** or ensure it's located as:
   ```
   ./processed_investment_data.xlsx
   ```

---

## 🧾 Project Structure

```bash
umera-investment-dashboard/
│
├── main.py                                       # Main Streamlit app
├── processed_investment_data.xlsx                # Dataset used
├── requirements.txt                              # Python dependencies
├── age_sementation.ipynb                         # The first Jupyter Notebook
├── age_sementation2.ipynb                        # The second Jupyter Notebook
├── age_sementation3.ipynb                        # The third Jupyter Notebook
├── Gbenga.jpg                                    # Developer's profile image
└── README.md                                     # Project documentation
```

---

## 📬 Contact

For feedback or collaborations, reach out at:

📧 **k.gbenga234@gmail.com**

---

## 📝 License

This project is licensed for academic, showcase, and internal business presentation use. Contact the developer for commercial use rights.
