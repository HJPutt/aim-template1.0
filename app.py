import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Collaboration Hub | Aim Builder",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 Developing your aim")

st.write(
    "Complete the sections below to build a clear improvement aim."
)

# ---------------------------------------------------------
# WHY?
# ---------------------------------------------------------

st.header("1. Why?")

st.write("What are you trying to improve?")

improve_health = st.checkbox("Improve health outcomes")

improve_experience = st.checkbox("Improve patient experience")

improve_colleague = st.checkbox("Improve colleague satisfaction")

lower_costs = st.checkbox("Lower costs")

# ---------------------------------------------------------
# WHAT?
# ---------------------------------------------------------

st.header("2. What?")

direction = st.radio(
    "What type of change are you aiming for?",
    ["Improve", "Increase", "Decrease"],
    horizontal=True
)

measure_name = st.text_input(
    "What do you want to change?",
    placeholder="e.g. average waiting time"
)

measure_type = st.radio(
    "How will it be measured?",
    ["Number", "Amount", "Percentage"],
    horizontal=True
)

# ---------------------------------------------------------
# FOR WHOM?
# ---------------------------------------------------------

st.header("3. For whom?")

stakeholder = st.text_input(
    "Who is affected by the improvement?",
    placeholder="e.g. patients attending the Surgical Decisions Unit"
)

# ---------------------------------------------------------
# SYSTEM / SCOPE
# ---------------------------------------------------------

st.header("4. System / scope")

system = st.text_input(
    "Where does this improvement apply?",
    placeholder="e.g. Surgical Decisions Unit, Musgrove Park Hospital"
)

# ---------------------------------------------------------
# HOW MUCH?
# ---------------------------------------------------------

st.header("5. How much?")

col1, col2 = st.columns(2)

with col1:
    baseline = st.text_input(
        "Current position",
        placeholder="e.g. 120 minutes"
    )

with col2:
    target = st.text_input(
        "Target position",
        placeholder="e.g. 90 minutes"
    )

# ---------------------------------------------------------
# BY WHEN?
# ---------------------------------------------------------

st.header("6. By when?")

target_date = st.date_input(
    "Target date",
    value=date.today()
)

# ---------------------------------------------------------
# AIM STATEMENT
# ---------------------------------------------------------

st.divider()

st.header("Your Aim Statement")

if measure_name and stakeholder and baseline and target:

    formatted_date = target_date.strftime("%d/%m/%Y")

    aim_statement = (
        f"We will {direction.lower()} {measure_name} "
        f"for {stakeholder}"
    )

    if system:
        aim_statement += f" within {system}"

    aim_statement += (
        f" from {baseline} to {target} "
        f"by {formatted_date}."
    )

    st.success(aim_statement)

else:
    st.info(
        "Complete the fields above and your aim statement will appear here."
    )

