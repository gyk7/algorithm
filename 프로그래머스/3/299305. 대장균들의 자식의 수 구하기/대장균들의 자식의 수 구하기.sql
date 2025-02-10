SELECT
      ID
    , IFNULL(
        (SELECT 
            COUNT(*)
        FROM ECOLI_DATA A
        WHERE A.PARENT_ID = B.ID), 0) AS CHILD_COUNT
FROM ECOLI_DATA B
ORDER BY ID;