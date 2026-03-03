from bi_functions import (
    sector_revenue,
    pipeline_health,
    work_execution_status,
    total_deal_value,
    average_closure_probability,
    collected_vs_billed
)

def handle_bi_query(user_input, deal_df, work_df):
    """Simple conversational mapping of queries to BI functions"""
    user_input = user_input.lower()

    if "sector" in user_input and "revenue" in user_input:
        return str(sector_revenue(deal_df))
    elif "pipeline" in user_input or "deal stage" in user_input:
        return str(pipeline_health(deal_df))
    elif "work execution" in user_input or "work status" in user_input:
        return str(work_execution_status(work_df))

    elif "pipeline" in user_input:
        return pipeline_health(deal_df).to_dict()
    elif "work status" in user_input:
        return work_execution_status(work_df).to_dict()
    elif "total deal value" in user_input:
        return total_deal_value(deal_df)
    elif "average closure" in user_input or "probability" in user_input:
        return average_closure_probability(deal_df)
    elif "collected vs billed" in user_input:
        return collected_vs_billed(work_df)
    else:
        return "Sorry, I didn't understand the query. Try asking about sector revenue, pipeline, work status, or totals."
    