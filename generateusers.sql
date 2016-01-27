CREATE USER testerAdmin WITH PASSWORD 'test_password';
GRANT ALL PRIVILEGES ON DATABASE "wypozyczalnia" to testerAdmin;

CREATE USER tester2 WITH PASSWORD 'test_password';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO tester2;
