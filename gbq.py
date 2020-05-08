from google.cloud import bigquery
from google.oauth2 import service_account


credentials = service_account.Credentials.from_service_account_file("./gbq_mimic_service_account.json")
project_id = 'mimic-276423'
client = bigquery.Client(credentials=credentials, project=project_id)


query_job = client.query(
"""
  SELECT *
  FROM `physionet-data.mimiciii_clinical.admissions` 
  LIMIT 1000
""")
results = query_job.result()  # Waits for job to complete.
