CREATE DATABASE IF NOT EXISTS hospital_db;
USE hospital_db;

CREATE TABLE hospital (
    age INT,
    gender VARCHAR(10),
    blood_type VARCHAR(5),
    medical_condition VARCHAR(100),
    billing_amount DOUBLE,
    admission_type VARCHAR(50),
    medication VARCHAR(50),
    test_results VARCHAR(50)
);