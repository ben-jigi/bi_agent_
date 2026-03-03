import pandas as pd
import numpy as np



def sector_revenue(deals_df):
    rev = deals_df.groupby("sector/service")["masked_deal_value"].sum()
    # Convert to dict of plain numbers
    return {sector: float(amount) for sector, amount in rev.items()}

def pipeline_health(deals_df):
    stage_sum = deals_df.groupby("deal_stage")["masked_deal_value"].sum()
    return {stage: float(amount) for stage, amount in stage_sum.items()}

def total_deals_value(deals_df):
    return float(deals_df["masked_deal_value"].sum())


def work_execution_status(work_df):
    status_sum = work_df.groupby("execution_status")["amount_in_rupees_(excl_of_gst)_(masked)"].sum()
    return {status: float(amount) for status, amount in status_sum.items()}

def work_billed_total(work_df):
    return float(work_df["billed_value_in_rupees_(excl_of_gst.)_(masked)"].sum())

def work_collected_total(work_df):
    return float(work_df["collected_amount_in_rupees_(incl_of_gst.)_(masked)"].sum())

