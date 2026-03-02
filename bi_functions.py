import pandas as pd
import numpy as np

import pandas as pd



import pandas as pd

# ----------------------------
# Core BI functions
# ----------------------------

def sector_revenue(df):
    """Revenue by sector"""
    if "sector/service" in df.columns:
        return df.groupby("sector/service")["masked_deal_value"].sum()
    elif "sector" in df.columns:
        return df.groupby("sector")["amount_in_rupees_(excl_of_gst)_(masked)"].sum()
    else:
        return pd.Series()

def pipeline_health(df):
    """Pipeline health by deal stage"""
    if "deal_stage" in df.columns:
        return df.groupby("deal_stage")["masked_deal_value"].sum()
    return pd.Series()

def work_execution_status(df):
    """Work Orders execution status summary"""
    if "execution_status" in df.columns:
        return df.groupby("execution_status")["amount_in_rupees_(excl_of_gst)_(masked)"].sum()
    return pd.Series()

def total_deal_value(df):
    return f"Total Deal Value: ₹{df['masked_deal_value'].sum():,.2f}" if "masked_deal_value" in df.columns else "No deal value column"

def average_closure_probability(df):
    if "closure_probability" in df.columns:
        avg_prob = df['closure_probability'].mean()
        return f"Average Closure Probability: {avg_prob:.2f}%"
    return "No closure probability column"

def collected_vs_billed(df):
    if all(col in df.columns for col in [
        "collected_amount_in_rupees_(incl_of_gst)_(masked)",
        "billed_value_in_rupees_(excl_of_gst.)_(masked)"]):
        total_collected = df["collected_amount_in_rupees_(incl_of_gst)_(masked)"].sum()
        total_billed = df["billed_value_in_rupees_(excl_of_gst.)_(masked)"].sum()
        return f"Total Collected: ₹{total_collected:,.2f}, Total Billed: ₹{total_billed:,.2f}"
    return "Required columns missing"

