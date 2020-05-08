#import library
library(bigrquery)

# Use your project ID here
project_id <- "physionet-data"
# Example query
sql_string <- "SELECT * FROM `mimiciii_clinical.admissions` LIMIT 1000"
# Execute the query and store the result
query_results <- query_exec(sql_string, project = project_id, useLegacySql = FALSE)
