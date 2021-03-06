-- Animal_ins Table

-- NAME	TYPE	NULLABLE
-- ANIMAL_ID	VARCHAR(N)	FALSE
-- ANIMAL_TYPE	VARCHAR(N)	FALSE
-- DATETIME	DATETIME	FALSE
-- INTAKE_CONDITION	VARCHAR(N)	FALSE
-- NAME	VARCHAR(N)	TRUE
-- SEX_UPON_INTAKE	VARCHAR(N)	FALSE

-- Result

-- ANIMAL_TYPE	count
-- Cat	2
-- Dog	1

SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE)
  FROM ANIMAL_INS
 WHERE ANIMAL_TYPE = 'Cat'
   OR ANIMAL_TYPE = 'Dog'
 GROUP BY ANIMAL_TYPE
 ORDER BY ANIMAL_TYPE ASC;