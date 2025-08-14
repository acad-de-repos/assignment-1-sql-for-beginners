import unittest
import pandas as pd
from sqlalchemy import create_engine, text
from assignment import run_sql_queries

class TestSQLQueries(unittest.TestCase):
    def setUp(self):
        """Set up a temporary in-memory SQLite database for testing"""
        self.engine = create_engine('sqlite:///:memory:')
        self.connection = self.engine.connect()

        # Create tables
        self.connection.execute(text("""
        CREATE TABLE departments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
        """))
        self.connection.execute(text("""
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            salary INTEGER,
            department_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments (id)
        );
        """))

        # Insert sample data
        self.connection.execute(text("INSERT INTO departments (id, name) VALUES (1, 'IT'), (2, 'HR'), (3, 'Finance');"))
        self.connection.execute(text("""
        INSERT INTO employees (id, name, age, salary, department_id) VALUES
        (1, 'Alice', 30, 80000, 1),
        (2, 'Bob', 45, 95000, 2),
        (3, 'Charlie', 28, 72000, 1),
        (4, 'David', 52, 120000, 3),
        (5, 'Eve', 38, 110000, 1),
        (6, 'Frank', 41, 60000, 2),
        (7, 'Grace', 35, 150000, 3),
        (8, 'Henry', 48, 90000, 1);
        """))
        self.connection.commit()

    def tearDown(self):
        """Close the database connection after each test"""
        self.connection.close()

    def test_run_sql_queries_returns_dict(self):
        """Test that the function returns a dictionary"""
        results = run_sql_queries(self.connection)
        self.assertIsInstance(results, dict)

    def test_task_1_all_employees(self):
        """Test that task 1 returns all employees"""
        results = run_sql_queries(self.connection)
        df = results.get('task_1')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 8)

    def test_task_2_it_department(self):
        """Test that task 2 returns employees from the IT department"""
        results = run_sql_queries(self.connection)
        df = results.get('task_2')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 4)
        self.assertTrue(all(df['department_id'] == 1))

    def test_task_3_average_salary(self):
        """Test that task 3 calculates the average salary correctly"""
        results = run_sql_queries(self.connection)
        df = results.get('task_3')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertAlmostEqual(df['average_salary'].iloc[0], 97125.0, places=2)

    def test_task_4_top_5_salaries(self):
        """Test that task 4 returns the top 5 highest-paid employees"""
        results = run_sql_queries(self.connection)
        df = results.get('task_4')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 5)
        self.assertEqual(df['salary'].iloc[0], 150000)
        self.assertEqual(df['salary'].iloc[4], 80000)

    def test_task_5_join_tables(self):
        """Test that task 5 correctly joins the employees and departments tables"""
        results = run_sql_queries(self.connection)
        df = results.get('task_5')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('department_name', df.columns)
        self.assertEqual(len(df), 8)

if __name__ == '__main__':
    unittest.main()
