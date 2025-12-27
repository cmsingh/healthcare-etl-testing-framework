SELECT column_name
FROM `project.dataset.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'patient_fact'
ORDER BY ordinal_position;
