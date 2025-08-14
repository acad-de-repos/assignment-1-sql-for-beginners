import pandas as pd

def run_sql_queries(db_connection):
  """
  Executes a series of SQL queries and returns the results.

  This function practices fundamental SQL skills:
  1. Basic data retrieval
  2. Filtering with WHERE
  3. Aggregation with AVG()
  4. Sorting and limiting results
  5. Joining tables

  Args:
    db_connection: An active database connection object.

  Returns:
    A dictionary of pandas DataFrames, where each key is the task number.
  """
  results = {}

  # Task 1: Select all records from the employees table
  # Hint: Use pd.read_sql_query() to execute the query
  # Example: pd.read_sql_query("SELECT * FROM table_name", db_connection)
  # SQL Syntax: SELECT * FROM employees
  results['task_1'] = None
  # Your code here
  # Write your SQL query to select all employees
  # results['task_1'] = pd.read_sql_query("YOUR_QUERY_HERE", db_connection)

  # Task 2: Select employees in the 'IT' department
  # Hint: Use a WHERE clause to filter by department
  # You need to find the department_id for 'IT' first, then filter employees
  # Option 1: Use a subquery: WHERE department_id = (SELECT id FROM departments WHERE name = 'IT')
  # Option 2: Use a JOIN: JOIN departments ON employees.department_id = departments.id WHERE departments.name = 'IT'
  results['task_2'] = None
  # Your code here
  # Write your SQL query to select IT department employees
  # results['task_2'] = pd.read_sql_query("YOUR_QUERY_HERE", db_connection)

  # Task 3: Calculate the average salary of all employees
  # Hint: Use the AVG() aggregate function
  # SQL Syntax: SELECT AVG(column_name) as alias_name FROM table_name
  # Example: SELECT AVG(salary) as average_salary FROM employees
  results['task_3'] = None
  # Your code here
  # Write your SQL query to calculate average salary
  # results['task_3'] = pd.read_sql_query("YOUR_QUERY_HERE", db_connection)

  # Task 4: Find the top 5 highest-paid employees
  # Hint: Use ORDER BY and LIMIT to get the top results
  # SQL Syntax: SELECT columns FROM table ORDER BY column DESC LIMIT number
  # Example: SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 5
  results['task_4'] = None
  # Your code here
  # Write your SQL query to get top 5 highest-paid employees
  # results['task_4'] = pd.read_sql_query("YOUR_QUERY_HERE", db_connection)

  # Task 5: Join employees and departments tables
  # Hint: Use an INNER JOIN to combine the tables
  # SQL Syntax: 
  # SELECT table1.column, table2.column as alias
  # FROM table1 
  # INNER JOIN table2 ON table1.foreign_key = table2.primary_key
  # Example:
  # SELECT e.name, d.name as department_name
  # FROM employees e
  # INNER JOIN departments d ON e.department_id = d.id
  results['task_5'] = None
  # Your code here
  # Write your SQL query to join employees and departments
  # results['task_5'] = pd.read_sql_query("YOUR_QUERY_HERE", db_connection)

  return results
