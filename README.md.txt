# 🛒 Serverless E-commerce Order Processing Pipeline on AWS

This project demonstrates a **fully serverless data processing pipeline** for e-commerce order files using key AWS services like **S3, Lambda, Glue, and Athena**. The goal is to transform raw CSV order files into enriched, queryable JSON data for analytics — all without managing any servers.

---

## 📌 Problem Statement

E-commerce platforms frequently receive order data in CSV format. Before this data can be queried or analyzed, it must be:
- Validated and transformed
- Stored in a structured format
- Made queryable via SQL

This project solves that problem **end-to-end using serverless architecture.**

---

## 🧰 Tech Stack (AWS Services Used)

| Service        | Purpose |
|----------------|---------|
| **Amazon S3**  | Raw and processed order data storage (CSV → JSON) |
| **AWS Lambda** | Triggered on new uploads, transforms and enriches CSV data |
| **AWS Glue**   | Crawls processed JSON to detect schema and catalog the table |
| **Amazon Athena** | Executes SQL queries on the processed data in S3 |

---

## 🧱 Architecture Diagram
![Architecture Diagram](./assets/architecture.png)


### 📊 Flow Summary:
1. User uploads `orders.csv` to S3 (`raw/` folder).
2. Lambda is triggered automatically → parses, enriches, and writes a JSON to S3 (`processed/` folder).
3. AWS Glue crawler scans `processed/` data to infer schema and create a table.
4. Athena queries the table directly using SQL for insights like revenue, top products, etc.

---

## ⚙️ How It Works

### Lambda Function
- Reads the uploaded `.csv` from the raw S3 bucket
- Adds a `total_amount = price * quantity` column
- Writes the enriched output as `.json` into a processed S3 bucket

### Glue Crawler
- Detects schema of the JSON files
- Registers the metadata as a table in the AWS Glue Data Catalog

### Athena Query Example
```sql
SELECT product_id, 
       SUM(total_amount) AS total_revenue
FROM yourprefix_processed_orders
GROUP BY product_id
ORDER BY total_revenue DESC
LIMIT 10;
