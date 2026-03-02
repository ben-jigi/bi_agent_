from column import fetch_boards, convert_to_dfs
from cleaning import normalize_columns, clean_numeric_columns, clean_date_columns, clean_categorical_columns
from bi_functions import sector_revenue, pipeline_health, work_execution_status, merge_boards

board_ids = [5026915383, 5026909152]
raw_data = fetch_boards(board_ids)

board_dfs = convert_to_dfs(raw_data)

deal_df = normalize_columns(board_dfs["Sales_Intelligence_Board_1772354616"])
work_df = normalize_columns(board_dfs["Work_Order_Tracker Data"])


DEALS_NUMERIC = ["masked_deal_value", "closure_probability"]
DEALS_DATES = ["created_date", "close_date_(a)", "tentative_close_date"]
DEALS_CATEGORICAL = ["sector/service", "deal_stage", "deal_status"]

WORK_NUMERIC = [
    "amount_in_rupees_(excl_of_gst)_(masked)",
    "billed_value_in_rupees_(excl_of_gst.)_(masked)",
    "collected_amount_in_rupees_(incl_of_gst.)_(masked)",
    "amount_receivable_(masked)"
]
WORK_DATES = ["probable_start_date", "probable_end_date", "data_delivery_date", "collection_date"]
WORK_CATEGORICAL = ["sector", "execution_status", "billing_status", "collection_status"]

deal_df = clean_numeric_columns(deal_df, DEALS_NUMERIC)
deal_df = clean_date_columns(deal_df, DEALS_DATES)
deal_df = clean_categorical_columns(deal_df, DEALS_CATEGORICAL)

work_df = clean_numeric_columns(work_df, WORK_NUMERIC)
work_df = clean_date_columns(work_df, WORK_DATES)
work_df = clean_categorical_columns(work_df, WORK_CATEGORICAL)

# Merge if needed
merged_df = merge_boards(deal_df, work_df)

