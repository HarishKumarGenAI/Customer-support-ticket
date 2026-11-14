🎫 AI Customer Support Ticket Routing System

📌 Project Overview

The AI Customer Support Ticket Routing System automates the process of classifying customer support tickets into the correct department using Natural Language Processing (NLP).

The application uses:

✦SpaCy NLP Pipeline
✦Rule-based Keyword Matching
✦Named Entity Recognition (NER)
✦Semantic Text Similarity
✦Priority Detection
✦Streamlit Dashboard
✦CSV Bulk Processing

The system intelligently routes customer queries to the appropriate department and identifies ticket priority levels to improve support efficiency.

🚀 Features

✅ Single Ticket Classification

✅ Bulk Ticket Routing via CSV Upload

✅ Rule-Based Ticket Categorization

✅ Named Entity Recognition (NER)

✅ Semantic Text Similarity Classification

✅ Priority Detection

✅ Download Processed Results

✅ Interactive Analytics Dashboard

✅ Department Distribution Charts

🛠 Technologies Used
✦Python
✦Streamlit
✦SpaCy
✦Pandas
✦Plotly
✦NLP
✦Machine Learning Concepts

📂 Departments Supported

Department	Examples
✦Technical Issue	Error, crash, bug, sync issue
✦Billing	Payment, invoice, charged
✦Account	Login, password reset, locked account
✦Shipping	Delivery, shipment, tracking
✦Refund	Refund, return, cancellation
✦Feedback	Suggestions, compliments, complaints

🧠 NLP Techniques Used

1. Matcher
SpaCy Matcher is used to identify predefined customer keywords.

Example:
"My app is crashing repeatedly."

Output:
Technical Issue

2. Named Entity Recognition (NER)

Extracts entities such as:
✦Names
✦Organizations
✦Locations
✦Dates

Example:
Amazon charged me twice on 12 June.

Entities:
✦Amazon (ORG)
✦12 June (DATE)

3. Text Similarity

If no rule-based match is found, semantic similarity is used to compare the customer ticket with department reference documents.

Example:
"My package arrived damaged."

Output:
Shipping

4. Priority Detection

High-priority tickets are detected using critical keywords.

Keywords:
✦urgent
✦critical
✦failed
✦immediately
✦not working
✦misbehave

Priority Levels:
✦High
✦Normal

📊 System Workflow
Customer Ticket
      │
      ▼
SpaCy NLP Processing
      │
      ▼
Keyword Matcher
      │
      ▼
If No Match
      │
      ▼
Text Similarity Analysis
      │
      ▼
Department Assignment
      │
      ▼
Priority Detection
      │
      ▼
NER Extraction
      │
      ▼
Dashboard Analytics

🎯 Example Inputs

➤Technical Issue
Application crashes whenever I upload a file.

Output:
Department: Technical Issue
Priority: Normal

➤Billing
My payment was deducted twice.

Output:
Department: Billing
Priority: Normal

➤Account
I forgot my password and cannot login.

Output:
Department: Account
Priority: Normal

➤Shipping
My package arrived damaged.

Output:
Department: Shipping
Priority: Normal

➤Refund
I would like a refund for my order.

Output:
Department: Refund
Priority: Normal

📁 CSV Input Format
Upload a CSV file containing a column named:

ticket
My app is crashing
Payment deducted twice
Reset my password
Package arrived damaged

📤 Output Format
ticket,Department,Priority,Entities
My app is crashing,Technical Issue,Normal,
Payment deducted twice,Billing,Normal,

📊 Dashboard Analytics
The application provides:

✦Department Distribution Bar Chart
✦Ticket Distribution Pie Chart
✦Ticket Analytics Dashboard
✦Downloadable Processed Results

📸 Project Interface

Features included:

✦Single Ticket Routing
✦Bulk CSV Processing
✦NLP-based Classification
✦NER Extraction
✦Analytics Dashboard
✦Download Results Button

🔮 Future Enhancements
✦Deep Learning Ticket Classification
✦Sentiment Analysis
✦Multi-language Support
✦LLM Integration (OpenAI/Gemini/Ollama)
✦Email Ticket Automation
✦Database Storage
✦Real-Time Customer Support Dashboard

👨‍💻 Author
Harish
AI & NLP Project built using SpaCy and Streamlit for intelligent customer support automation.
