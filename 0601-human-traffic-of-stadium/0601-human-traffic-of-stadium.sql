# Write your MySQL query statement below
WITH YourFilteredQuery AS (
    -- This is your exact query identifying the valid days
    SELECT id, visit_date, people 
    FROM Stadium 
    WHERE people >= 100
),
StreakGroups AS (
    SELECT *,
        -- We apply the sequential row number to find islands
        id - ROW_NUMBER() OVER (ORDER BY id) AS group_id
    FROM YourFilteredQuery
)
SELECT id, visit_date, people
FROM StreakGroups
WHERE group_id IN (
    SELECT group_id 
    FROM StreakGroups 
    GROUP BY group_id 
    HAVING COUNT(*) >= 3
)
ORDER BY id;
