CREATE TABLE machines (
    machine_id VARCHAR(20) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE feeders (
    feeder_id VARCHAR(20) PRIMARY KEY,
    machine_id VARCHAR(20) NOT NULL,
    material_type VARCHAR(50) NOT NULL,
    fill_level NUMERIC(6,2) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_feeders_machine
        FOREIGN KEY (machine_id)
        REFERENCES machines(machine_id)
        ON DELETE CASCADE
);

CREATE TABLE inspections (
    inspection_id VARCHAR(20) PRIMARY KEY,
    machine_id VARCHAR(20) NOT NULL,
    defect_score NUMERIC(4,2) NOT NULL,
    image_path TEXT NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    CONSTRAINT fk_inspections_machine
        FOREIGN KEY (machine_id)
        REFERENCES machines(machine_id)
        ON DELETE CASCADE
);

CREATE TABLE alerts (
    alert_id VARCHAR(20) PRIMARY KEY,
    source_type VARCHAR(20) NOT NULL,
    source_id VARCHAR(20) NOT NULL,
    message TEXT NOT NULL,
    severity VARCHAR(20) NOT NULL,
    is_open BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_feeders_machine_id ON feeders(machine_id);
CREATE INDEX idx_inspections_machine_id ON inspections(machine_id);
CREATE INDEX idx_inspections_status ON inspections(status);
CREATE INDEX idx_alerts_source_type ON alerts(source_type);