CREATE TABLE students (
  registration_no VARCHAR(10) NOT NULL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  vaccination_status VARCHAR(5) NOT NULL
);

INSERT INTO students (registration_no, name, vaccination_status)
VALUES
  ('191155', 'rajashree', 'YES'),
  ('191166', 'tharani', 'NO'),
  ('191177', 'akshaya', 'YES');
