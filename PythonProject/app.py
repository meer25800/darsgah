import streamlit as st

# Set the app background color
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
    }
    .stButton > button {
        background-color: #008CBA;  /* Blue color for buttons */
        color: white;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton > button:hover {
        background-color: #007bb5; /* Darker color for hover effect */
    }
    .question {
        color: #1e88e5;
        font-weight: bold;
        font-size: 26px;  /* Larger font size */
    }
    .score {
        font-weight: bold;
        font-size: 22px;
        text-align: center;
    }
    .score-a {
        color: #4caf50; /* Green for Group A */
    }
    .score-b {
        color: #ff9800; /* Orange for Group B */
    }
    .score-c {
        color: #ff5722; /* Red for Group C */
    }
    .score-d {
        color: #673ab7; /* Purple for Group D */
    }
    .center-title {
        font-size: 30px;
        font-weight: bold;
        color: #1e88e5;
    }
    .group-button-a {
        background-color: #4caf50; /* Green for Group A */
    }
    .group-button-b {
        background-color: #ff9800; /* Orange for Group B */
    }
    .group-button-c {
        background-color: #ff5722; /* Red for Group C */
    }
    .group-button-d {
        background-color: #673ab7; /* Purple for Group D */
    }
    .group-button:hover {
        opacity: 0.8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Centered Title
st.markdown(
    """
    <div class="center-title">
        Darsgah Taleemul Quran wal Hadith Kongamdara
    </div>
    """,
    unsafe_allow_html=True
)

# Initialize session state for groups, questions, and scores
if "score" not in st.session_state:
    st.session_state["score"] = {"A": 0, "B": 0, "C": 0, "D": 0}

if "questions" not in st.session_state:
    st.session_state["questions"] = {
        "A": [
            {"key": "q1", "question": "خلفائے راشدین کون تھے؟", "answer": "حضرت ابوبکر، حضرت عمر، حضرت عثمان، حضرت علی رضی اللہ عنہم"},
            {"key": "q2", "question": "خلفائے راشدین کا دورانیہ کتنا تھا؟", "answer": "تقریباً 30 سال"},
            {"key": "q3", "question": "حضرت ابوبکر رضی اللہ عنہ کا لقب کیا تھا؟", "answer": "صدیق"},
        ],
        "B": [
            {"key": "q4", "question": "حضرت عمر رضی اللہ عنہ کا لقب کیا تھا؟", "answer": "فاروق"},
            {"key": "q5", "question": "حضرت عثمان رضی اللہ عنہ کا لقب کیا تھا؟", "answer": "ذوالنورین"},
            {"key": "q6", "question": "حضرت علی رضی اللہ عنہ کا لقب کیا تھا؟", "answer": "مرتضیٰ"},
        ],
        "C": [
            {"key": "q7", "question": "قرآن کی جمع آوری کس کے دور میں ہوئی؟", "answer": "حضرت ابوبکر رضی اللہ عنہ کے دور میں"},
            {"key": "q8", "question": "بیت المال کا نظام کس نے بنایا؟", "answer": "حضرت عمر رضی اللہ عنہ"},
            {"key": "q9", "question": "قرآنی نسخے کس نے یکجا کیے؟", "answer": "حضرت عثمان رضی اللہ عنہ"},
        ],
        "D": [
            {"key": "q10", "question": "حضرت علی رضی اللہ عنہ کا سب سے بڑا کارنامہ کیا تھا؟", "answer": "داخلی فتنوں کا خاتمہ"},
            {"key": "q11", "question": "حضرت عثمان کی شہادت کس سال ہوئی؟", "answer": "35 ہجری"},
            {"key": "q12", "question": "حضرت عمر رضی اللہ عنہ کو فاروق کیوں کہا جاتا ہے؟", "answer": "حق و باطل میں فرق کرنے کی وجہ سے"},
        ],
    }

if "asked_questions" not in st.session_state:
    st.session_state["asked_questions"] = {"A": [], "B": [], "C": [], "D": []}

if "current_questions" not in st.session_state:
    st.session_state["current_questions"] = {
        "A": st.session_state["questions"]["A"][0],
        "B": st.session_state["questions"]["B"][0],
        "C": st.session_state["questions"]["C"][0],
        "D": st.session_state["questions"]["D"][0],
    }

# Function to update score for correct or incorrect answers
def update_score(group, is_correct):
    if is_correct:
        st.session_state["score"][group] += 10
    else:
        st.session_state["score"][group] -= 2  # Change to reduce 2 points for incorrect answer


# Function to pick the next unasked question sequentially
def pick_next_question(group):
    # Find the index of the current question in the list
    current_index = next(
        (index for index, question in enumerate(st.session_state["questions"][group])
         if question["key"] == st.session_state["current_questions"][group]["key"]), None
    )

    if current_index is not None and current_index < len(st.session_state["questions"][group]) - 1:
        next_question = st.session_state["questions"][group][current_index + 1]
        st.session_state["current_questions"][group] = next_question
    else:
        st.session_state["current_questions"][group] = None  # No more questions available


# Render Group Buttons in a single row with different colors
st.markdown("### Select a Group to Attempt the Quiz:")

cols = st.columns(4)
groups = ["A", "B", "C", "D"]
group_buttons = [
    {"group": "A", "button_class": "group-button-a"},
    {"group": "B", "button_class": "group-button-b"},
    {"group": "C", "button_class": "group-button-c"},
    {"group": "D", "button_class": "group-button-d"},
]

for i, group in enumerate(group_buttons):
    with cols[i]:
        if st.button(f"Group {group['group']}", key=f"group_button_{group['group']}"):
            st.session_state["active_group"] = group["group"]
            st.session_state["active_score"] = st.session_state["score"][group["group"]]  # Save group score on selection

# Display Group Scores Vertically
st.markdown("### Group Scores:")

# Create a single column for the group scores
score_column = st.container()

# Display scores for all groups in a vertical line
with score_column:
    st.markdown(f"<div class='score score-a'>Group A Score: {st.session_state['score']['A']}</div>",
                unsafe_allow_html=True)
    st.markdown(f"<div class='score score-b'>Group B Score: {st.session_state['score']['B']}</div>",
                unsafe_allow_html=True)
    st.markdown(f"<div class='score score-c'>Group C Score: {st.session_state['score']['C']}</div>",
                unsafe_allow_html=True)
    st.markdown(f"<div class='score score-d'>Group D Score: {st.session_state['score']['D']}</div>",
                unsafe_allow_html=True)

# Check which group is selected
active_group = st.session_state.get("active_group", None)

if active_group:
    st.markdown(f"## Group {active_group} Quiz")

    # Display the current score for this group
    st.markdown(f"<h4 class='score'>Score: {st.session_state['score'][active_group]}</h4>", unsafe_allow_html=True)

    # Display the current question
    current_question = st.session_state["current_questions"][active_group]
    if current_question:  # Check if a valid question is available
        st.markdown(f"<p class='question'>{current_question['question']}</p>", unsafe_allow_html=True)

        # Answer dropdown
        correct_answer = current_question["answer"]
        answer = st.selectbox(
            "Select Your Answer:", ["", correct_answer, "غلط جواب"], key=f"answer_{active_group}"
        )

        # Submit button (styled attractively)
        if st.button(f"Submit Answer for Group {active_group}"):

            if answer == correct_answer:
                st.success("Correct Answer! +10 points.")
                update_score(active_group, is_correct=True)
            elif answer == "غلط جواب":
                st.error("غلط جواب! -2 points.")  # Display the reduced points message
                update_score(active_group, is_correct=False)
            else:
                st.warning("Please select an answer.")

            # Pick the next question after submission
            pick_next_question(active_group)
    else:
        st.write("All questions have been asked.")
