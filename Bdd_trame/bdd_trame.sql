CREATE TABLE test (
    id_test INT PRIMARY KEY NOT NULL, 
    nom_test VARCHAR(100), 
    date_execution DATETIME
)
CREATE TABLE trame (
    id_trame INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
    framedate DATETIME, 
    MID VARCHAR(100), 
    bench_3 INT, 
    bench_5 VARCHAR(100), 
    framesize INT, 
    mac_dest VARCHAR(100), 
    mac_src VARCHAR(100), 
    field_1 VARCHAR(100), 
    field_2 INT, 
    field_3 INT, 
    field_4 INT, 
    field_5 INT, 
    field_6 INT, 
    field_7 INT, 
    src_ip VARCHAR(100), 
    dest_ip VARCHAR(100), 
    field_9 INT,
    field_10 INT,
    field_11 INT, 
    field_14 VARCHAR(100), 
    field_16 INT, 
    field_17 VARCHAR(100), 
    field_18 VARCHAR(100), 
    field_20 INT, 
    field_21 INT, 
    field_23 VARCHAR(100), 
    field_25 VARCHAR(100), 
    field_26 INT, 
    field_28 VARCHAR(100), 
    field_29 VARCHAR(100), 
    field_30 INT,
    field_32 VARCHAR(100),
    packet_date DATETIME,
    mac_sender VARCHAR(100),
    sender_ip VARCHAR(100),
    mac_target VARCHAR(100),
    target_ip VARCHAR(100), 
    num_test INT, 
    FOREIGN KEY (num_test) REFERENCES test(id_test)
)