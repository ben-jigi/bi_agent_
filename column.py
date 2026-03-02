import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

MONDAY_API_KEY = os.getenv("monday_api_token")


def fetch_board(board_ids):  
    
    
    if isinstance(board_ids, list):
        ids_string = ",".join(str(i) for i in board_ids)
        ids_part = f"[{ids_string}]"
    else:
        ids_part = str(board_ids)

    query = f"""
    query {{
    boards(ids: {ids_part}) {{
      id
      name

    items_page(limit: 500) {{
      items {{
        id
        name
        column_values {{
          text
          column {{
            title
          }}
        }}
      }}
    }}
  }}
}}
"""

    response = requests.post(
        "https://api.monday.com/v2",
        json={"query": query},
        headers={"Authorization": MONDAY_API_KEY}
    )

    return response.json()
board_ids = [5026915383, 5026909152]

deals_raw = fetch_board(board_ids)

print(fetch_board(board_ids))

def convert_boards_to_dfs(deals_raw):

    board_dfs = {}

    boards = deals_raw["data"]["boards"]

    for board in boards:

        board_name = board["name"]
        items = board["items_page"]["items"]

        rows = []

        for item in items:

            row = {
                "Item ID": item["id"],
                "Item Name": item["name"]
            }

            for col in item["column_values"]:
                column_name = col["column"]["title"]
                row[column_name] = col["text"]

            rows.append(row)

        df = pd.DataFrame(rows)
        board_dfs[board_name] = df

    return board_dfs

board_dataframes = convert_boards_to_dfs(deals_raw)


print(board_dataframes.keys())

deal_df=board_dataframes['Sales_Intelligence_Board_1772354616']  
work_df=board_dataframes["Work_Order_Tracker Data"]

print(deal_df.head())
print(work_df.head())

deal_df.columns=deal_df.columns.str.lower().str.replace(" ", "_")
work_df.columns=work_df.columns.str.lower().str.replace(" ", "_")



COLUMN_MAPPING = {
    "deals": {
        "sector": "sector/service",
        "value": "masked_deal_value",
        "stage": "deal_stage",
        "status": "deal_status",
        "close_date": "close_date_(a)",
        "tentative_close": "tentative_close_date",
        "probability": "closure_probability",
        "created_date": "created_date"
    },

    "work_orders": {
        "sector": "sector",
        "value": "amount_in_rupees_(excl_of_gst)_(masked)",
        "billed": "billed_value_in_rupees_(excl_of_gst.)_(masked)",
        "collected": "collected_amount_in_rupees_(incl_of_gst.)_(masked)",
        "receivable": "amount_receivable_(masked)",
        "execution_status": "execution_status",
        "billing_status": "billing_status",
        "collection_status": "collection_status",
        "start_date": "probable_start_date",
        "end_date": "probable_end_date",
        "collection_date": "collection_date"
    }
}


