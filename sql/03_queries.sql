-- View all machines
SELECT * FROM machines;

-- View feeders with their machine names
SELECT f.feeder_id, f.material_type, f.fill_level, m.name AS machine_name
FROM feeders AS f
JOIN machines AS m ON f.machine_id = m.machine_id;

-- View inspections with high defect scores
SELECT inspection_id, machine_id, defect_score, status
FROM inspections
WHERE defect_score >= 0.70
ORDER BY defect_score DESC;

-- Count inspections per machine
SELECT machine_id, COUNT(*) AS inspection_count
FROM inspections
GROUP BY machine_id
ORDER BY inspection_count DESC;

-- Update a feeder fill level
UPDATE feeders
SET fill_level = 35.00
WHERE feeder_id = 'F-200';

-- Verify the feeder update
SELECT feeder_id, fill_level
FROM feeders
WHERE feeder_id = 'F-200';

-- Close an alert
UPDATE alerts
SET is_open = FALSE
WHERE alert_id = 'A-400';

-- Delete a low-value review inspection example
DELETE FROM inspections
WHERE inspection_id = 'I-301';