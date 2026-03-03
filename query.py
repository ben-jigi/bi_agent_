from bi_functions import (
    sector_revenue,
    pipeline_health,
    work_execution_status,
    total_deals_value,
    work_billed_total,
    work_collected_total
)

def handle_bi_query(user_input, deal_df, work_df):
    """Simple conversational mapping of queries to BI functions"""
    user_input = user_input.lower()

    if "sector" in user_input and "revenue" in user_input:
        return sector_revenue(deal_df)
    if "pipeline" in user_input or "stage" in user_input:
        return pipeline_health(deal_df)
    if "total deals" in user_input or "deals value" in user_input:
        return total_deals_value(deal_df)

    
    if "execution status" in user_input:
        return work_execution_status(work_df)
    if "billed total" in user_input:
        return work_billed_total(work_df)
    if "collected total" in user_input:
        return work_collected_total(work_df)

    return "Sorry, I didn't understand the query. Try asking about sector revenue, pipeline, work status, or totals."




