# SQL for Beginners Assignment

## Problem Description

In this assignment, you will practice fundamental SQL queries to retrieve and manipulate data from a relational database. Your tasks are to connect to a database, execute a series of SQL queries to extract specific information, and return the results in a structured format. This assignment introduces core data retrieval techniques essential for any data professional.

## Learning Objectives

By completing this assignment, you will learn:
- How to connect to a SQLite database using Python
- How to execute basic SELECT queries with filtering conditions
- How to use aggregate functions to perform calculations
- How to join multiple tables to retrieve related data
- Best practices for writing clean and efficient SQL queries

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make sure you have the following packages installed:
   - pandas (>=1.3.0)
   - sqlalchemy (>=1.4.0)

## Instructions

1. Open the `assignment.py` file.
2. You will find a function definition: `run_sql_queries(db_connection)`.
3. The function takes a database connection object as input.
4. Your tasks are to:
   *   **Task 1**: Write a SQL query to select all records from the `employees` table.
   *   **Task 2**: Write a SQL query to select employees who work in the 'IT' department.
   *   **Task 3**: Write a SQL query to calculate the average salary of all employees.
   *   **Task 4**: Write a SQL query to find the top 5 highest-paid employees and return their names and salaries.
   *   **Task 5**: Write a SQL query to join the `employees` and `departments` tables to get the department name for each employee.

## Hints

*   Use `pd.read_sql_query()` to execute SQL queries and return a DataFrame.
*   Use a `with` statement to ensure the database connection is properly managed.
*   For Task 4, use the `ORDER BY` and `LIMIT` clauses.
*   For Task 5, use an `INNER JOIN` to combine the two tables on the `department_id` column.
*   Remember to return a dictionary of DataFrames, where each key corresponds to a task.

## Testing Your Solution

Run the test file to verify your implementation:
```bash
python test.py
```

The tests will check:
- That your function returns a dictionary with the correct keys
- That each returned DataFrame has the expected columns and data types
- That the query results are accurate based on the test data
- That the database connection is handled correctly

## Expected Output

Your function should return a dictionary of pandas DataFrames, where each key is the task number (e.g., 'task_1', 'task_2', etc.) and the value is the resulting DataFrame from the corresponding SQL query.

## Sample Data Format

The database will contain two tables: `employees` and `departments`.

### `employees` table:
- `id` (INTEGER, PRIMARY KEY)
- `name` (TEXT)
- `age` (INTEGER)
- `salary` (INTEGER)
- `department_id` (INTEGER, FOREIGN KEY)

### `departments` table:
- `id` (INTEGER, PRIMARY KEY)
- `name` (TEXT)

## Troubleshooting

### Common Errors
- `DatabaseError: execution failed on statement`: Check your SQL syntax for errors.
- `KeyError`: Ensure your returned dictionary has the correct keys ('task_1', 'task_2', etc.).
- `AssertionError`: Your query results do not match the expected output. Double-check your logic.

## Further Exploration (Optional)

*   Try using other aggregate functions like `SUM()`, `COUNT()`, `MIN()`, and `MAX()`.
*   Explore different types of joins, such as `LEFT JOIN` and `RIGHT JOIN`.
*   How would you modify the queries to handle more complex filtering conditions (e.g., employees with salaries above a certain threshold in a specific department)?
*   Can you write a query to find the department with the highest average salary?
*   Look into using subqueries to perform more advanced data retrieval.

## Resources

- [SQL for Beginners Guide](https://www.w3schools.com/sql/)
- [Pandas `read_sql_query` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)
- [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/14/tutorial/)
- [Introduction to SQL Joins](https://www.geeksforgeeks.org/sql-join-and-different-types-of-joins/)
