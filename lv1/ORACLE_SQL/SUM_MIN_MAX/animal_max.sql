-- Animal_ins Table

-- NAME	TYPE	NULLABLE
-- ANIMAL_ID	VARCHAR(N)	FALSE
-- ANIMAL_TYPE	VARCHAR(N)	FALSE
-- DATETIME	DATETIME	FALSE
-- INTAKE_CONDITION	VARCHAR(N)	FALSE
-- NAME	VARCHAR(N)	TRUE
-- SEX_UPON_INTAKE	VARCHAR(N)	FALSE

-- Result

-- 2013-11-18 17:03:00
SELECT MAX(DATETIME)
  FROM ANIMAL_INS;