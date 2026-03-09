INSERT INTO machines (machine_id, name, location, is_active) VALUES
('M-100', 'Smart Feeder Line A', 'Aachen Plant 1', TRUE),
('M-101', 'Smart Feeder Line B', 'Aachen Plant 1', TRUE),
('M-102', 'Smart Feeder Line C', 'Aachen Plant 2', TRUE);

INSERT INTO feeders (feeder_id, machine_id, material_type, fill_level) VALUES
('F-200', 'M-100', 'powder', 15.00),
('F-201', 'M-101', 'granules', 52.00),
('F-202', 'M-102', 'powder', 18.00);

INSERT INTO inspections (inspection_id, machine_id, defect_score, image_path, status, created_at) VALUES
('I-300', 'M-100', 0.82, 'data/raw/m100_01.jpg', 'defective', '2026-03-01 09:00:00'),
('I-301', 'M-100', 0.61, 'data/raw/m100_02.jpg', 'review', '2026-03-01 15:00:00'),
('I-302', 'M-101', 0.22, 'data/raw/m101_01.jpg', 'ok', '2026-03-01 09:30:00'),
('I-303', 'M-102', 0.80, 'data/raw/m102_01.jpg', 'defective', '2026-03-01 14:30:00');

INSERT INTO alerts (alert_id, source_type, source_id, message, severity, is_open) VALUES
('A-400', 'feeder', 'F-200', 'Feeder fill level is below threshold.', 'medium', TRUE),
('A-401', 'inspection', 'I-300', 'Defect score exceeded threshold.', 'high', TRUE),
('A-402', 'inspection', 'I-303', 'Repeated defect detected.', 'high', TRUE); 