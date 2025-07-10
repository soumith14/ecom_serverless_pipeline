# E-commerce Serverless Data Pipeline (AWS)

This project demonstrates a full end-to-end serverless pipeline on AWS for processing, transforming, and analyzing e-commerce orders.

---

## 📌 Tools Used

- **Amazon S3** – data lake for raw and processed data
- **AWS Lambda** – to enrich CSV orders and output JSON
- **AWS Glue** – to convert nested JSON → flat Parquet
- **AWS Athena** – to run SQL queries on Parquet tables
- **Python (PyAthena + matplotlib)** – to create visual dashboards

---

## 🔄 Workflow Summary

1. CSV uploaded to `s3://alloj-raw-orders`
2. Lambda enriches the data and writes JSON to `s3://alloj-processed-orders`
3. Glue crawler scans the JSON and creates a catalog table
4. Glue ETL job converts JSON → Parquet and writes to `s3://alloj-processed-orders/parquet/`
5. A second crawler scans the Parquet and creates a clean flat table
6. Athena queries the Parquet table efficiently
7. Dashboard pulls top-selling products into a bar chart using matplotlib

---

## 📁 Folder Structure

- `lambda/` – Lambda handler code
- `glue/` – Glue ETL script & crawler CLI commands
- `dashboard/` – PyAthena + matplotlib dashboard code
- `sample/` – Sample CSV for ingestion
