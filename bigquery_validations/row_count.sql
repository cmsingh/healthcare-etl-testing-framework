SELECT COUNT(*) AS row_count
FROM `project.dataset.patient_fact`
WHERE load_date = CURRENT_DATE();
