-- Animal_ins Table

-- NAME	TYPE	NULLABLE
-- ANIMAL_ID	VARCHAR(N)	FALSE
-- ANIMAL_TYPE	VARCHAR(N)	FALSE
-- DATETIME	DATETIME	FALSE
-- INTAKE_CONDITION	VARCHAR(N)	FALSE
-- NAME	VARCHAR(N)	TRUE
-- SEX_UPON_INTAKE	VARCHAR(N)	FALSE

-- Result

-- ANIMAL_ID	NAME
-- A367012	Miller
-- A381217	Cherokee

SELECT ANIMAL_ID, NAME
  FROM ANIMAL_INS
 WHERE INTAKE_CONDITION = 'Sick'
 ORDER BY ANIMAL_ID ASC;