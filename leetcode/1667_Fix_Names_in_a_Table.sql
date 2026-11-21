# # Table: Users

# # +----------------+---------+
# # | Column Name    | Type    |
# # +----------------+---------+
# # | user_id        | int     |
# # | name           | varchar |
# # +----------------+---------+
# # user_id is the primary key (column with unique values) for this table.
# # This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.


# # Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

# # Return the result table ordered by user_id.

# # The result format is in the following example.



# # Example 1:

# # Input:
# # Users table:
# # +---------+-------+
# # | user_id | name  |
# # +---------+-------+
# # | 1       | aLice |
# # | 2       | bOB   |
# # +---------+-------+
# # Output:
# # +---------+-------+
# # | user_id | name  |
# # +---------+-------+
# # | 1       | Alice |
# # | 2       | Bob   |
# # +---------+-------+
# #
# #
# #
# #
# #
# #
# #
# #
# # SQL Schema:
# Create table If Not Exists Users (user_id int, name varchar(40))
# Truncate table Users
# insert into Users (user_id, name) values ('1', 'aLice')
# insert into Users (user_id, name) values ('2', 'bOB')










# Pandas Schema:
#     data = [[1, 'aLice'], [2, 'bOB']]
#     users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})













# Solution:
### SQL Solution

sql

```sql
SELECT
    user_id,
    CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id;
```

### Pandas Solution

python

```python
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values('user_id')
```
