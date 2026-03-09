-- 1. Machine + feeder overview
SELECT m.machine_id,
       m.name,
       m.location,
       f.feeder_id,
       f.material_type,
       f.fill_level
FROM machines AS m
LEFT JOIN feeders AS f ON m.machine_id = f.machine_id
ORDER BY m.machine_id;

-- 2. Inspection summary per machine
SELECT i.machine_id,
       COUNT(*) AS inspection_count,
       ROUND(AVG(i.defect_score), 2) AS avg_defect_score,
       SUM(CASE WHEN i.status = 'defective' THEN 1 ELSE 0 END) AS defective_count
FROM inspections AS i
GROUP BY i.machine_id
ORDER BY defective_count DESC, avg_defect_score DESC;

-- 3. Open alerts with readable source label
SELECT a.alert_id,
       a.source_type,
       a.source_id,
       a.severity,
       a.is_open,
       CASE
           WHEN a.source_type = 'inspection' THEN 'Quality issue'
           WHEN a.source_type = 'feeder' THEN 'Material issue'
           ELSE 'Other issue'
       END AS alert_category
FROM alerts AS a
WHERE a.is_open = TRUE
ORDER BY a.severity DESC, a.created_at DESC;

-- 4. Latest inspection per machine using window function
WITH ranked_inspections AS (
    SELECT i.*,
           ROW_NUMBER() OVER (
               PARTITION BY i.machine_id
               ORDER BY i.created_at DESC
           ) AS row_num
    FROM inspections AS i
)
SELECT machine_id,
       inspection_id,
       defect_score,
       status,
       created_at
FROM ranked_inspections
WHERE row_num = 1
ORDER BY machine_id;

-- 5. Machines needing attention
WITH inspection_summary AS (
    SELECT i.machine_id,
           COUNT(*) AS inspection_count,
           ROUND(AVG(i.defect_score), 2) AS avg_defect_score,
           SUM(CASE WHEN i.status = 'defective' THEN 1 ELSE 0 END) AS defective_count
    FROM inspections AS i
    GROUP BY i.machine_id
)
SELECT m.machine_id,
       m.name,
       f.fill_level,
       s.avg_defect_score,
       s.defective_count,
       CASE
           WHEN f.fill_level < 20 OR s.defective_count > 0 THEN TRUE
           ELSE FALSE
       END AS needs_attention
FROM machines AS m
LEFT JOIN feeders AS f ON m.machine_id = f.machine_id
LEFT JOIN inspection_summary AS s ON m.machine_id = s.machine_id
ORDER BY needs_attention DESC, m.machine_id;