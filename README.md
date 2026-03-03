# The_founder_bi_agent_

The Founder BI Agent is an AI-powered conversational business intelligence (BI) assistant that integrates directly with monday.com boards to provide founders and executives with quick, accurate insights about their Deals and Work Orders. It removes the need for manual data cleaning and cross-board analysis, allowing users to ask questions in natural language and get actionable responses.

This project was developed as part of a technical challenge, focused on live BI queries and conversational interaction.

## Features
### 1. Live monday.com Integration

Connects to monday.com boards via API.

Supports multiple boards: Deals and Work Orders.

Pulls live data without caching, ensuring up-to-date insights.

Handles messy and inconsistent board data.

### 2. Data Cleaning & Transformation

Normalizes column names and data types.

Handles missing/null values.

Converts numeric columns and dates to proper formats.

Cleans categorical columns for consistent querying.

### 3. Conversational AI Interface

Users can ask founder-level questions in natural language.

Chat history is maintained to allow follow-up questions.

Provides conversational insights into:

Sector Revenue – total revenue per sector.

Pipeline Health – deal value distribution across stages.

Work Execution Status – value of work by execution status.

Fully supports multi-turn queries using Streamlit session state.

### 4. Business Intelligence Functions

Implemented BI functions include:

sector_revenue(df) – calculates revenue by sector.

pipeline_health(df) – calculates deal value by deal stage.

work_execution_status(df) – calculates work execution value by status.

Additional BI functions for summarizing deals and work orders in numeric, categorical, and date-based insights.

### 5. Deployment

Streamlit app provides a browser-based conversational interface.

Can be run locally or deployed to Streamlit Cloud for public access.

## Technical Stack

Python – data processing and BI functions.

pandas / numpy – data cleaning and manipulation.

Streamlit – conversational UI for founder queries.

monday.com API – live board integration.

No external LLM required – all queries are answered using processed board data.

## Live Demo Link:https://biagent-2gc4ezcghzspzhzgh5bqmy.streamlit.app/
