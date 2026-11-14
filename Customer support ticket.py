import streamlit as st
import pandas as pd
import plotly.express as px
import spacy
from spacy.matcher import Matcher

# ---------------------------------------------------
# LOAD NLP MODEL
# ---------------------------------------------------

nlp = spacy.load("en_core_web_md")

# ---------------------------------------------------
# CREATE MATCHER
# ---------------------------------------------------

matcher = Matcher(nlp.vocab)

matcher.add(
    "TECHNICAL",
    [
        [{"LOWER": "error"}],
        [{"LOWER": "crash"}],
        [{"LOWER": "bug"}],
        [{"LOWER": "slow"}],
        [{"LOWER": "sync"}],
        [{"LOWER": "issue"}],
        [{"LOWER": "working"}]
    ]
)

matcher.add(
    "BILLING",
    [
        [{"LOWER": "payment"}],
        [{"LOWER": "charged"}],
        [{"LOWER": "invoice"}],
        [{"LOWER": "billing"}],
        [{"LOWER": "declined"}],
        [{"LOWER": "deducted"}]
    ]
)

matcher.add(
    "ACCOUNT",
    [
        [{"LOWER": "login"}],
        [{"LOWER": "password"}],
        [{"LOWER": "account"}],
        [{"LOWER": "locked"}],
        [{"LOWER": "reset"}]
    ]
)

matcher.add(
    "SHIPPING",
    [
        [{"LOWER": "delivery"}],
        [{"LOWER": "shipment"}],
        [{"LOWER": "tracking"}],
        [{"LOWER": "damaged"}],
        [{"LOWER": "arrived"}]
    ]
)

matcher.add(
    "REFUND",
    [
        [{"LOWER": "refund"}],
        [{"LOWER": "return"}],
        [{"LOWER": "cancel"}],
        [{"LOWER": "reimbursement"}]
    ]
)

matcher.add(
    "FEEDBACK",
    [
        [{"LOWER": "love"}],
        [{"LOWER": "great"}],
        [{"LOWER": "awesome"}],
        [{"LOWER": "feature"}],
        [{"LOWER": "feedback"}],
        [{"LOWER": "suggestion"}],
        [{"LOWER": "misbehave"}],
        [{"LOWER": "rude"}],
        [{"LOWER": "asked tip"}]
    ]
)


# ---------------------------------------------------
# TEXT SIMILARITY REFERENCE DOCUMENTS
# ---------------------------------------------------

categories = {

    "Technical Issue":
        nlp(
            "error crash bug slow sync issue "
            "technical problem not working"
        ),

    "Billing":
        nlp(
            "payment billing invoice charged "
            "deducted money transaction declined"
        ),

    "Account":
        nlp(
            "account login password locked "
            "sign in two factor authentication reset"
        ),

    "Shipping":
        nlp(
            "delivery shipment package "
            "tracking damaged courier arrived"
        ),

    "Refund":
        nlp(
            "refund return cancel "
            "money back reimbursement"
        ),

    "Feedback":
        nlp(
            "love great awesome feedback "
            "feature suggestion improvement"
        )
}

# ---------------------------------------------------
# PRIORITY DETECTION
# ---------------------------------------------------

def get_priority(text):

    text = text.lower()

    high_priority_keywords = [
        "urgent",
        "critical",
        "failed",
        "immediately",
        "not working",
        "misbehave"
    ]

    for word in high_priority_keywords:

        if word in text:
            return "High"

    return "Normal"

# ---------------------------------------------------
# ROUTING FUNCTION
# ---------------------------------------------------

def route_ticket(ticket):

    doc = nlp(ticket)

    entities = []

    for ent in doc.ents:

        entities.append(
            f"{ent.text} ({ent.label_})"
        )

    matches = matcher(doc)

    if matches:

        match_id, start, end = matches[0]

        category = nlp.vocab.strings[match_id]

        mapping = {
    "TECHNICAL": "Technical Issue",
    "BILLING": "Billing",
    "ACCOUNT": "Account",
    "SHIPPING": "Shipping",
    "REFUND": "Refund",
    "FEEDBACK": "Feedback"
}

        return (
            mapping[category],
            entities
        )

    scores = {}

    for team, ref_doc in categories.items():

        similarity_score = doc.similarity(ref_doc)

        scores[team] = similarity_score

    best_team = max(
        scores,
        key=scores.get
    )

    return best_team, entities

# ---------------------------------------------------
# STREAMLIT PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Customer Support Router",
    page_icon="🎫",
    layout="wide"
)

st.title(
    "🎫 AI Customer Support Ticket Routing System"
)

st.markdown("""
### Features

✅ NLP Pipeline  
✅ Matcher  
✅ Named Entity Recognition  
✅ Text Similarity  
✅ CSV Upload  
✅ Dashboard Analytics
""")

# ---------------------------------------------------
# SINGLE TICKET ROUTING
# ---------------------------------------------------

st.header("Single Ticket Routing")

ticket = st.text_area(
    "Enter Customer Ticket"
)

if st.button("Route Ticket"):

    if ticket:

        department, entities = route_ticket(ticket)

        priority = get_priority(ticket)

        st.success(
            f"Department : {department}"
        )

        st.warning(
            f"Priority : {priority}"
        )

        st.subheader("Entities")

        if entities:

            for item in entities:

                st.write(item)

        else:

            st.write(
                "No entities found"
            )

# ---------------------------------------------------
# BULK CSV ROUTING
# ---------------------------------------------------

st.header("Bulk Ticket Routing")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(
        uploaded_file
    )

    st.subheader(
        "Uploaded Data"
    )

    st.dataframe(df)

    if "ticket" not in df.columns:

        st.error(
            "CSV must contain 'ticket' column"
        )

    else:

        departments = []
        priorities = []
        entities_column = []

        for ticket in df["ticket"]:

            department, entities = route_ticket(
                str(ticket)
            )

            priority = get_priority(
                str(ticket)
            )

            departments.append(
                department
            )

            priorities.append(
                priority
            )

            entities_column.append(
                ", ".join(entities)
            )

        df["Department"] = departments

        df["Priority"] = priorities

        df["Entities"] = entities_column

        st.subheader(
            "Routing Results"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        csv_data = df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="Download Results",
            data=csv_data,
            file_name="routed_tickets.csv",
            mime="text/csv"
        )

        # ----------------------------------
        # ANALYTICS
        # ----------------------------------

        st.subheader(
            "Department Distribution"
        )

        dept_count = (
            df["Department"]
            .value_counts()
        )

        st.bar_chart(
            dept_count
        )

        fig = px.pie(
            values=dept_count.values,
            names=dept_count.index,
            title="Ticket Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
        
