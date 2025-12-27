# Healthcare ETL Testing & Validation Platform

## Overview
This project implements an enterprise-grade ETL testing and data validation framework for healthcare EMR / HL7 data pipelines. It ensures data reliability by validating row counts, schema drift, duplicates, NULL values, and transformation logic. All validations are automated and integrated into Airflow pipelines.

The solution supports both batch and streaming healthcare data pipelines and follows production best practices used in regulated healthcare environments.

---

## Key Features
- Automated ETL testing using Python and SQL
- Row count validation (source vs target)
- Schema drift detection
- Duplicate record detection
- NULL checks for mandatory healthcare fields
- Transformation logic validation (age, billing, PHI handling)
- Airflow-integrated validation gates
- Streaming validation support (HL7 → Pub/Sub)
- Production-ready, interview-ready design

---

## Architecture
Healthcare data from EMR / HL7 systems is ingested through batch (GCS) and streaming (Pub/Sub) pipelines. Data is transformed using Python or Dataflow and loaded into BigQuery. Post-load, Airflow executes automated validation tasks to ensure data quality before downstream consumption.

---

## Project Structure

healthcare-etl-testing-platform/
│
├── dags/
│ └── healthcare_etl_validation_dag.py
│
├── etl/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── validations/
│ ├── row_count_validation.py
│ ├── schema_validation.py
│ ├── duplicate_validation.py
│ ├── null_validation.py
│ └── transformation_validation.py
│
├── bigquery_validations/
│ ├── row_count.sql
│ ├── duplicates.sql
│ ├── null_checks.sql
│ └── schema_check.sql
│
├── streaming/
│ └── pubsub_stream_validation.py
│
├── data/
│ └── source_emr_data.json
│
├── config/
│ └── schema_config.py
│
├── tests/
│ └── test_etl_validations.py
│
├── requirements.txt
└── README.md


---

## Validations Implemented

### 1. Row Count Validation
Ensures no data loss between source and target systems.

### 2. Schema Drift Detection
Detects unexpected schema changes using immutable schema definitions.

### 3. Duplicate Detection
Validates uniqueness of healthcare business keys such as visit_id.

### 4. NULL Validation
Ensures mandatory EMR fields are never NULL.

### 5. Transformation Logic Validation
Validates age calculation, billing conversion, and PHI-safe handling.

---

## Airflow Integration
All validations are executed as a dedicated Airflow task. If any validation fails:
- The DAG fails immediately
- Downstream tasks are blocked
- Alerts can be triggered
- Bad data is isolated or routed to DLQ

---

## Streaming Validation (HL7)
For real-time HL7 pipelines:
- Window-based count validation
- Duplicate message detection
- Mandatory field validation
- Dead Letter Queue (DLQ) support

---

## How to Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
