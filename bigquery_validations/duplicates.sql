SELECT visit_id, COUNT(*)
FROM `project.dataset.patient_fact`
GROUP BY visit_id
HAVING COUNT(*) > 1;
