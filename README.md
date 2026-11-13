# 🎓 EduPro Learner Analytics Dashboard

An interactive, data-driven web application designed to analyze learner demographics, course enrollments, and behavioral patterns on the EduPro online learning platform. 

Built with **Python**, **Streamlit**, and **Plotly**, this dashboard transforms raw educational data into actionable insights, enabling stakeholders to make informed decisions regarding curriculum design, targeted marketing, and platform inclusivity.

---

## 📸 Features at a Glance

- **Auto-Loading Data Pipeline:** The app automatically detects and merges relational datasets (`Users`, `Courses`, `Transactions`, `Teachers`) on startup without requiring manual uploads.
- **Dynamic Global Filters:** A fully interactive sidebar allows users to filter the entire dashboard by **Age Group, Gender, Course Category, and Course Level**.
- **5 Analytical Modules:**
  1. **📊 Overview:** High-level KPIs and macro-level distributions (Free vs. Paid, Course Levels, Ratings).
  2. **👥 Demographics:** Detailed breakdown of the learner base by age and gender.
  3. **📚 Course Analysis:** Identification of the most popular categories and the Top 10 most enrolled courses.
  4. **🎯 Preferences:** Advanced heatmaps cross-referencing demographics with course attributes to uncover hidden preferences.
  5. **📈 Insights:** Behavioral KPIs, enrollment concentration metrics (Power Users), and monthly enrollment trends over time.
- **Modern UI/UX:** A sleek, fully responsive dark-mode interface featuring bold typography and a custom Violet/Blue gradient color palette for high visual contrast.

---

## 📂 Project Structure

For the application to run correctly, ensure your project directory is structured exactly like this:

```text
edupro_analytics/
│
├── app.py                  # The main Streamlit application code
├── README.md               # Project documentation (this file)
├── requirements.txt        # List of required Python packages
├── Research_Paper.pdf      # EDA, Insights, and Recommendations
├── Executive_Summary.pdf   # Stakeholder summary
│
└── data/                   # The folder containing your datasets
    ├── Users.csv
    ├── Courses.csv
    ├── Transactions.csv
    └── Teachers.csv
