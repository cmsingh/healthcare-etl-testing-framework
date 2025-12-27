SELECT COUNT(*) AS null_count
FROM `project.dataset.patient_fact`
WHERE patient_id IS NULL
   OR gender IS NULL
   OR visit_id IS NULL;
