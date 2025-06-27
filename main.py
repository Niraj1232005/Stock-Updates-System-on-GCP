import base64
import json
from google.cloud import bigquery

def process_message(message):
    client = bigquery.Client()
    table_id = "your-project-id.stock_data.stock_updates"
    rows_to_insert = [message]
    errors = client.insert_rows_json(table_id, rows_to_insert)

    if errors:
        print(f"Failed to insert rows: {errors}")
    else:
        print("Message successfully written to BigQuery.")

def handle_pubsub(request):
    try:
        envelope = request.get_json()
        pubsub_message = envelope["message"]
        data = base64.b64decode(pubsub_message["data"]).decode("utf-8")
        message = json.loads(data)
        process_message(message)
    except Exception as e:
        print(f"Error: {e}")
    return ("", 204)
