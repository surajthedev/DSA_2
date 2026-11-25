Table: Employees

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id is the column with unique values for this table.
This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null).


For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.

Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer.

Return the result table ordered by employee_id.

The result format is in the following example.



Example 1:

Input:
Employees table:
+-------------+---------+------------+-----+
| employee_id | name    | reports_to | age |
+-------------+---------+------------+-----+
| 9           | Hercy   | null       | 43  |
| 6           | Alice   | 9          | 41  |
| 4           | Bob     | 9          | 36  |
| 2           | Winston | null       | 37  |
+-------------+---------+------------+-----+
Output:
+-------------+-------+---------------+-------------+
| employee_id | name  | reports_count | average_age |
+-------------+-------+---------------+-------------+
| 9           | Hercy | 2             | 39          |
+-------------+-------+---------------+-------------+
Explanation: Hercy has 2 people report directly to him, Alice and Bob. Their average age is (41+36)/2 = 38.5, which is 39 after rounding it to the nearest integer.
Example 2:

Input:
Employees table:
+-------------+---------+------------+-----+
| employee_id | name    | reports_to | age |
|-------------|---------|------------|-----|
| 1           | Michael | null       | 45  |
| 2           | Alice   | 1          | 38  |
| 3           | Bob     | 1          | 42  |
| 4           | Charlie | 2          | 34  |
| 5           | David   | 2          | 40  |
| 6           | Eve     | 3          | 37  |
| 7           | Frank   | null       | 50  |
| 8           | Grace   | null       | 48  |
+-------------+---------+------------+-----+
Output:
+-------------+---------+---------------+-------------+
| employee_id | name    | reports_count | average_age |
| ----------- | ------- | ------------- | ----------- |
| 1           | Michael | 2             | 40          |
| 2           | Alice   | 2             | 37          |
| 3           | Bob     | 1             | 37          |
+-------------+---------+---------------+-------------+
















SQL Schema:
Create table If Not Exists Employees(employee_id int, name varchar(20), reports_to int, age int)
Truncate table Employees
insert into Employees (employee_id, name, reports_to, age) values ('9', 'Hercy', NULL, '43')
insert into Employees (employee_id, name, reports_to, age) values ('6', 'Alice', '9', '41')
insert into Employees (employee_id, name, reports_to, age) values ('4', 'Bob', '9', '36')
insert into Employees (employee_id, name, reports_to, age) values ('2', 'Winston', NULL, '37')




PAndas Schema:
    data = [[9, 'Hercy', None, 43], [6, 'Alice', 9, 41], [4, 'Bob', 9, 36], [2, 'Winston', None, 37]]
    employees = pd.DataFrame(data, columns=['employee_id', 'name', 'reports_to', 'age']).astype({'employee_id':'Int64', 'name':'object', 'reports_to':'Int64', 'age':'Int64'})













Solution:
    ### SQL Solution

    sql

    ```sql
    SELECT
        e.employee_id,
        e.name,
        COUNT(r.employee_id) AS reports_count,
        ROUND(AVG(r.age)) AS average_age
    FROM Employees e
    JOIN Employees r
        ON e.employee_id = r.reports_to
    GROUP BY e.employee_id, e.name
    ORDER BY e.employee_id;
    ```

    ### Pandas Solution

    python

    ```python
    import pandas as pd

    def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
        result = (
            employees
            .dropna(subset=['reports_to'])
            .groupby('reports_to')
            .agg(
                reports_count=('employee_id', 'count'),
                average_age=('age', 'mean')
            )
            .reset_index()
            .rename(columns={'reports_to': 'employee_id'})
        )

        result = result.merge(
            employees[['employee_id', 'name']],
            on='employee_id'
        )

        result['average_age'] = result['average_age'].round().astype(int)

        return result[
            ['employee_id', 'name', 'reports_count', 'average_age']
        ].sort_values('employee_id')
    ```
