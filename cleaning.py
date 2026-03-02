from column import deal_df, work_df
import pandas as pd
import numpy as np
import re

def normalize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

deal_df = normalize_columns(deal_df)
work_df = normalize_columns(work_df)

DEALS_NUMERIC = [
    "masked_deal_value",
    "closure_probability"
]

DEALS_DATES = [
    "created_date",
    "close_date_(a)",
    "tentative_close_date"
]

DEALS_CATEGORICAL = [
    "sector/service",
    "deal_stage",
    "deal_status"
]

DEALS_NUMERIC = [
    "masked_deal_value",
    "closure_probability"
]

DEALS_DATES = [
    "created_date",
    "close_date_(a)",
    "tentative_close_date"
]

DEALS_CATEGORICAL = [
    "sector/service",
    "deal_stage",
    "deal_status"
]

WORK_NUMERIC = [
    "amount_in_rupees_(excl_of_gst)_(masked)",
    "billed_value_in_rupees_(excl_of_gst.)_(masked)",
    "collected_amount_in_rupees_(incl_of_gst.)_(masked)",
    "amount_receivable_(masked)"
]

WORK_DATES = [
    "probable_start_date",
    "probable_end_date",
    "data_delivery_date",
    "collection_date"
]

WORK_CATEGORICAL = [
    "sector",
    "execution_status",
    "billing_status",
    "collection_status"
]
def clean_numeric_columns(df, numeric_cols):
    for col in numeric_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(",", "", regex=False)
                .str.replace("₹", "", regex=False)
                .str.replace(" ", "", regex=False)
            )
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

def clean_date_columns(df, date_cols):
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df

def clean_categorical_columns(df, cat_cols):
    for col in cat_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().str.strip()
    return df



def clean_all(deal_df, work_df):
    deal_df = clean_numeric_columns(deal_df, DEALS_NUMERIC)
    deal_df = clean_date_columns(deal_df, DEALS_DATES)
    deal_df = clean_categorical_columns(deal_df, DEALS_CATEGORICAL)
    
    work_df = clean_numeric_columns(work_df, WORK_NUMERIC)
    work_df = clean_date_columns(work_df, WORK_DATES)
    work_df = clean_categorical_columns(work_df, WORK_CATEGORICAL)

    # Fill missing
    deal_df.fillna({"masked_deal_value": 0, "closure_probability": 0, 
                    "sector/service": "unknown", "deal_stage": "unknown"}, inplace=True)
    work_df.fillna({"amount_in_rupees_(excl_of_gst)_(masked)": 0,
                    "billed_value_in_rupees_(excl_of_gst.)_(masked)": 0,
                    "collected_amount_in_rupees_(incl_of_gst.)_(masked)": 0,
                    "sector": "unknown"}, inplace=True)
    
    return deal_df, work_df

