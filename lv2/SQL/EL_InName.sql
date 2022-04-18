SELECT ANIMAL_ID,NAME
  FROM ANIMAL_INS
 WHERE NAME LIKE '%el%'
   AND ANIMAL_TYPE LIKE 'Dog'
 ORDER BY NAME ASC
-- Table
ANIMAL_ID	ANIMAL_TYPE	DATETIME	INTAKE_CONDITION	NAME	SEX_UPON_INTAKE
A355753	Dog	2015-09-10 13:14:00	Normal	Elijah	Neutered Male
A352872	Dog	2015-07-09 17:51:00	Aged	Peanutbutter	Neutered Male
A353259	Dog	2016-05-08 12:57:00	Injured	Bj	Neutered Male
A373219	Cat	2014-07-29 11:43:00	Normal	Ella	Spayed Female
A382192	Dog	2015-03-13 13:14:00	Normal	Maxwell 2	Intact Male

-- Question
이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 
이때 결과는 이름 순으로 조회해주세요. 
단, 이름의 대소문자는 구분하지 않습니다.

-- RESULT
ANIMAL_ID	NAME
A355753	Elijah
A382192	Maxwell 2