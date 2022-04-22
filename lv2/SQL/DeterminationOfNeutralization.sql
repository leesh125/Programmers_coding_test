-- My turn
SELECT ANIMAL_ID, NAME, 
  CASE WHEN SEX_UPON_INTAKE LIKE '%Neutered%'
         OR SEX_UPON_INTAKE LIKE '%Spayed' THEN 'O' -- OR 사용가능
       ELSE 'X' END AS 중성화
  -- CASE WHEN 조건 THEN (실행문, 조건에 맞다면)
  -- ELSE (나머지 처리) 
  -- CASW WHEN은 꼭 END로 마무리!!!
  FROM ANIMAL_INS
 ORDER BY ANIMAL_ID

-- Good Explanation
SELECT ANIMAL_ID, NAME, 
    CASE WHEN 
    SEX_UPON_INTAKE in('%Spayed Female%','%Neutered Male%') -- in 사용하기
    THEN 'O' 
    ELSE 'X' 
    END AS 중성화 
        FROM ANIMAL_INS ORDER BY ANIMAL_ID ASC
-- Table
ANIMAL_ID	ANIMAL_TYPE	DATETIME	INTAKE_CONDITION	NAME	SEX_UPON_INTAKE
A355753	Dog	2015-09-10 13:14:00	Normal	Elijah	Neutered Male
A373219	Cat	2014-07-29 11:43:00	Normal	Ella	Spayed Female
A382192	Dog	2015-03-13 13:14:00	Normal	Maxwell 2	Intact Male

-- Result
ANIMAL_ID	NAME	중성화
A355753	Elijah	O
A373219	Ella	O
A382192	Maxwell 2	X

-- Question
동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 
이때 중성화가 되어있다면 'O', 아니라면 'X