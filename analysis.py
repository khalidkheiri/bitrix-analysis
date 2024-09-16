import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


df = pd.read_excel("data.xlsx")
df_resp = df["Responsible"].value_counts().reset_index()

Piplines = ["Tele Sales المبيعات الهاتفية", "Data Rotation إعادة تدوير الطالب",
           "Logistic Services الخدمات اللوجيستية", "After Sales Serv. خدمات ما بعد البيع"]

Tele_Sales = [
    "New Students الطلاب الجدد",
    "2024 Students Target [1-1]",
    "Student Inquiry استفسار",
    "Student Documents الحصول على الأوراق",
    "تسجيل الطالب بالجامعات الخاصة",
    "مهتم ( فقط مصطفى )",
    "الحصول على قبول مبدأي",
    "[غلق البيع أونلاين] الحصول على قبول نهائي",
    "No Answer لم يتم الرد 1 (24 H) [2-2]",
    "No Answer لم يتم الرد 2 (48 H)  [3-4]",
    "No Answer لم يتم الرد 3 (48 H) [4-6]",
    "No Answer لم يتم الرد 4 (3 D) [5-9]",
    "No Answer لم يتم الرد 5 (3 D) [6-12]",
    "Data Rotation إعادة التدوير",
    "Not a Student غير طالب",
    "FILTER TARGET",
    "New Pesrian Students",
    "2023 Students target",
    "Agent وكيل",
    "متابعة2023",
    "غير مهتم",
    "Delete Cards",
    "Job Applicants طلب توظيف",
    "[التسجيل على المنحة]",
    "[طالب حكومي]",
    "موعد زيارة مع الطالب",
    "زيارة للجامعات ١",
    "زيارة للجامعات ٢",
    "[غلق البيع أوفلاين] الحصول على قبول نهائي",
    "الإنتقال إلى الخدمات اللوجيستية",
    "Registered With Other Co. سجل مع شركة أخرى",
    "Asked to stop contacting طلب عدم التواصل مرة أخرى",
    "Deal won"
]

Data_Rotation = [
    "New student / Waiting for 7 daysطالب جديد / إنتظار 7 يوم",
    "Contact in [8-22 D] تواصل",
    "Contact in [9-1 M] تواصل في",
    "Contact in [10-1M7D ] تواصل في",
    "Contact in [11-1M15D ] تواصل في",
    "Contact in [12-1M22D ] تواصل في",
    "Contact in [13-2 M] تواصل في"
]

Logisitic_Services = [
    "New Clients العملاء الجدد",
    "Student's Arrival Date موعد وصول الطالب",
    "VIP Services خدمات ال",
    "مكالمة قبل الوصول باسبوع",
    "مكالمة قبل الوصول بيومين",
    "استقبال المطار",
    "تحصيل السكن",
    "إتمام معادلة شهادة الطالب",
    "تسجيل الطالب بالجامعة",
    "اتمام امتحان اللغة",
    "أخذ موعد إقامة للطالب",
    "التواصل مع الطالب بعد شهر 11",
    "مشكلات خاصة للطلاب",
    "Ask For Review طلب تقييم",
    "Positive Review تقييم إيجابي",
    "Negative Review تقييم سلبي"
]

After_Sales = [
    "الطلاب المسجلين الجدد (اسم + سنة التسجيل)",
    "التواصل مع الطالب قبل امتحانات نصف العام الأول",
    "التواصل مع الطالب بعد امتحانات نصف العام الأول",
    "التواصل مع الطالب قبل امتحانات  العام الأول",
    "التواصل مع الطالب بعد امتحانات  العام الأول",
    "التواصل مع الطالب قبل امتحانات نصف العام الثاني",
    "التواصل مع الطالب بعد امتحانات نصف العام الثاني",
    "التواصل مع الطالب قبل امتحانات  العام الثاني",
    "التواصل مع الطالب بعد امتحانات  العام الثاني",
    "التواصل مع الطالب بعد امتحانات نصف العام الثالث",
    "التواصل مع الطالب بعد امتحانات  العام الثالث",
    "التواصل مع الطالب بعد امتحانات نصف العام الرابع",
    "التواصل مع الطالب بعد امتحانات  العام الرابع",
    "التواصل مع الطالب بعد امتحانات  العام الخامس",
    "حضور حفل التخرج / نشر صور للطلاب",
    "التواصل مع الطالب بعد التخرج",
    "طلابنا الخريجين ❤️"
]

#print(df["Pipeline"].value_counts())
stages = df[["Pipeline", "Stage"]].groupby(["Pipeline", "Stage"]).value_counts()

index_df = pd.DataFrame({
    'Pipeline': (["Tele Sales المبيعات الهاتفية"] * len(Tele_Sales) +
                 ["Data Rotation إعادة تدوير الطالب"] * len(Data_Rotation) +
                 ["Logistic Services الخدمات اللوجيستية"] * len(Logisitic_Services) +
                 ["After Sales Serv. خدمات ما بعد البيع"] * len(After_Sales)),
    'Stage': Tele_Sales + Data_Rotation + Logisitic_Services + After_Sales
})

stages = stages.reindex(index_df.set_index(['Pipeline', 'Stage']).index, fill_value=0)
stages = stages.reset_index()


sources = df["Source"].value_counts().reset_index()

sources["Source"] = sources["Source"].replace({
    "Instagram Direct - Open Channel": "Instagram Direct",
    "Facebook - Open Channel": "Facebook",
    "Facebook: Comments - Open Channel": "Facebook Comments"
})

##############################################################################################################################################

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

st.markdown(
"""
<style>
div.st-emotion-cache-jkfxgf.e1nzilvr5 > p {
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True
)

with st.sidebar:
    st.header("Noqta Plus")

st.title("Passyos Bitrix24 Analysis")
st.header(":blue[Responsible Analysis]", divider="rainbow")

rows = len(df_resp)
cols = st.columns(6)
for i in range(0, rows, 6):
    for row, col in zip(range(i, rows), cols):
        col.metric(df_resp.loc[row,"Responsible"],f"{df_resp.loc[row,'count']:,}")




st.header(":blue[Stages Analysis]", divider="rainbow")
col1, col2, col3, col4 = st.columns(4)
# Display captions
col1.caption("**Tele Sales:** Has 33 stages as in Bitrix24")
col2.caption("**Data Rotation:** Has 7 stages as in Bitrix24")
col3.caption("**Logistic Services:** Has 16 stages as in Bitrix24")
col4.caption("**After Sales Services:** Has 17 stages as in Bitrix24")
# Data for the bar graphs
categories1 = [str(x) for x in range(1, len(Tele_Sales)+1)]
values1 = stages[stages["Pipeline"] == Piplines[0]]["count"]
categories2 = [str(x) for x in range(1, len(Data_Rotation)+1)]
values2 = stages[stages["Pipeline"] == Piplines[1]]["count"]
categories3 = [str(x) for x in range(1, len(Logisitic_Services)+1)]
values3 = stages[stages["Pipeline"] == Piplines[2]]["count"]
categories4 = [str(x) for x in range(1, len(After_Sales)+1)]
values4 = stages[stages["Pipeline"] == Piplines[3]]["count"]

# Create a figure and define three subplots
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(9, 6))  # 1 row, 3 columns

# Adjust space between subplots
plt.subplots_adjust(hspace=0.3)

bars1 = ax1.bar(categories1, values1, color='#347deb')
bars2 = ax2.bar(categories2, values2, color='#34eb59')
bars3 = ax3.bar(categories3, values3, color='#eb5934')
bars4 = ax4.bar(categories4, values4, color='#ebc034')

ax1.tick_params(axis='x', labelsize=8)
ax2.tick_params(axis='x', labelsize=8)
ax3.tick_params(axis='x', labelsize=8)
ax4.tick_params(axis='x', labelsize=8)

ax1.tick_params(axis='y', labelleft=False)
ax2.tick_params(axis='y', labelleft=False)
ax3.tick_params(axis='y', labelleft=False)
ax4.tick_params(axis='y', labelleft=False)

ax1.set_ylabel('Tele Sales', rotation=0, labelpad=30, va='center')
ax2.set_ylabel('Data\nRotation', rotation=0, labelpad=30, va='center')
ax3.set_ylabel('Logistic\nServices', rotation=0, labelpad=30, va='center')
ax4.set_ylabel('After Sales\nServices', rotation=0, labelpad=30, va='center')

# Function to add labels on bars
def add_value_labels(ax, bars):
    for bar in bars:
        height = bar.get_height()
        # Set y position of label
        y_position = height if height != 0 else ax.get_ylim()[0]  # Place zero text at x-axis line
        ax.text(bar.get_x() + bar.get_width() / 2, y_position, f'{height}', 
                ha='center', va='bottom', fontsize=8)

# Add value labels to each bar chart
add_value_labels(ax1, bars1)
add_value_labels(ax2, bars2)
add_value_labels(ax3, bars3)
add_value_labels(ax4, bars4)

# Show the plot
fig



st.header(":blue[Sources]", divider="rainbow")
categories1 = sources["Source"]
values1 = sources["count"]

# Function to split category labels into multiple lines
def format_labels(labels):
    return [label.replace(' ', '\n') for label in labels]

# Format category labels
categories1 = format_labels(categories1)

# Create a figure
fig, ax1 = plt.subplots(1, 1, figsize=(6, 2))

bars1 = ax1.bar(categories1, values1, color='#347deb')

ax1.tick_params(axis='x', labelsize=5)
ax1.tick_params(axis='y', labelsize=4)

# Function to add labels on bars
def add_value_labels(ax, bars):
    for bar in bars:
        height = bar.get_height()
        # Set y position of label
        y_position = height if height != 0 else ax.get_ylim()[0]  # Place zero text at x-axis line
        ax.text(bar.get_x() + bar.get_width() / 2, y_position, f'{height:,}', 
                ha='center', va='bottom', fontsize=5)

# Add value labels to each bar chart
add_value_labels(ax1, bars1)

# Show the plot
fig
