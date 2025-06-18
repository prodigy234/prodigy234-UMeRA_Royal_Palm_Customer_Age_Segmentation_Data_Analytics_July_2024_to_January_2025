
# 📊 UMéRA Investment Analytics Dashboard

This project is a **fully interactive data analytics dashboard** built using **Streamlit** to visualize and analyze investment data for UMéRA Real Estate. It features advanced filtering, insightful metrics, and a range of compelling visualizations for stakeholder decision-making.

## 📁 Dataset Used

The dataset used is [`processed_investment_data.xlsx`](./processed_investment_data.xlsx), which contains anonymized records of investor transactions including:

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
   git clone https://github.com/your-username/umera-investment-dashboard.git
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

```
.
├── updated.py                     # Main Streamlit app
├── processed_investment_data.xlsx # Dataset used
├── requirements.txt               # Python dependencies
├── .streamlit/
│   └── runtime.txt                # Python version specification
└── README.md                      # This file
```

---

## 📸 Screenshots

> *(Add screenshots here if available)*

---

## 👨‍💻 About the Developer

**Kajola Gbenga**

- 🎓 Certified Data Analyst | Certified Data Scientist
- 📱 Mobile App Developer | AI/ML Engineer
- 🌐 [Portfolio](https://kajolagbenga.netlify.app/)
- 💼 [LinkedIn](https://www.linkedin.com/in/kajolagbenga)
- 🧾 [Certifications](https://www.datacamp.com/portfolio/kgbenga234)
- 💻 [GitHub](https://github.com/prodigy234)

---

## 📬 Contact

For feedback or collaborations, reach out at:

📧 **k.gbenga234@gmail.com**

---

## 📝 License

This project is licensed for academic, showcase, and internal business presentation use. Contact the developer for commercial use rights.
