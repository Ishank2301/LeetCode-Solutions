-- Last updated: 15/9/2026, 11:35:09 pm
# Write your MySQL query statement bel
# Write your MySQL query statement below
SELECT 
    actor_id, 
    director_id
FROM 
    ActorDirector
GROUP BY 
    actor_id, 
    director_id
HAVING 
    COUNT(*) >= 3;