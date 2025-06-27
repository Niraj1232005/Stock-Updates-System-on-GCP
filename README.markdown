# 💹 Stock Updates System on Google Cloud Platform

This project implements a stock updates system using Google Cloud Platform (GCP) services to process and store real-time stock market data.

## 📋 Features

- **Pub/Sub**: Handles incoming messages with stock updates.
- **Cloud Run**: Decodes and processes stock data.
- **BigQuery**: Stores processed data for analysis.
- **[4th Service Placeholder]**: Add any fourth GCP service in the future.

## 🛠️ Setup Guide

### 1. Create a BigQuery Dataset and Table

- Navigate to **BigQuery** in the GCP Console.
- Go to **Datasets** > **Create Dataset**.
  - **Dataset ID**: `stock_data`
  - **Data location**: `asia-south1`
- Create a table in this dataset with the following schema:
  - `ticker` (STRING, Nullable)
  - `price` (FLOAT, Nullable)
  - `timestamp` (TIMESTAMP, Nullable)

### 2. Create a Pub/Sub Topic and Subscription

- Navigate to **Pub/Sub** in the GCP Console.
- Go to **Topics** > **Create Topic**.
  - **Topic ID**: `stock-updates`
- Create a subscription:
  - **Subscription ID**: `stock-sub`
  - **Delivery type**: Pull

### 3. Deploy Cloud Run

- Open your **GCP Cloud Shell**.
- Ensure the project directory contains:
  - `main.py`
  - `requirements.txt`
- Deploy the app to **Cloud Run**:
  - **Region**: `asia-south1`
  - **Authentication**: Allow unauthenticated access
  - Command:
    ```bash
    gcloud run deploy stock-updates-service --source . --region asia-south1 --allow-unauthenticated
    ```

### 4. Test the System

- Publish a test message to Pub/Sub:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"message": {"data": "eyJ0aWNrZXIiOiAiQUFQTCIsICJwcmljZSI6IDE1MC4yNSwgInRpbWVzdGFtcCI6ICIyMDI1LTA2LTI3VDE3OjMwOjAwWiJ9", "attributes": {}}, "subscription": "projects/propane-melody-462107-p0/subscriptions/stock-sub"}' https://<your-cloud-run-url>.asia-south1.run.app
  ```
- Decode the message to verify:
  ```bash
  echo "eyJ0aWNrZXIiOiAiQUFQTCIsICJwcmljZSI6IDE1MC4yNSwgInRpbWVzdGFtcCI6ICIyMDI1LTA2LTI3VDE3OjMwOjAwWiJ9" | base64 --decode
  ```
- Check **Cloud Logs** for processing results.
- Verify that **BigQuery** contains the processed stock data.

## 📂 File Structure

```
cloud-run-app/
├── main.py
├── requirements.txt
```

## ✨ Services Used

- **Pub/Sub**
- **Cloud Run**
- **BigQuery**
- **CloudStorage**
