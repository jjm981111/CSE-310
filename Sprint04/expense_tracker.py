import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='whwhwh89',
    database='expense_tracker'
)
cursor = conn.cursor()

# Create expenses table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        description TEXT,
        category_id INT,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
''')

# Create categories table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
''')

conn.commit()











# Function to insert a new expense
def insert_expense(id, date, amount, description, category_id):
    sql = '''
        INSERT INTO expenses (id, date, amount, description, category_id)
        VALUES (%s, %s, %s, %s, %s)
    '''
    values = (id, date, amount, description, category_id)
    cursor.execute(sql, values)
    conn.commit()

# Function to update an existing expense
def update_expense(expense_id, date, amount, description, category_id):
    sql = '''
        UPDATE expenses
        SET date = %s, amount = %s, description = %s, category_id = %s
        WHERE id = %s
    '''
    values = (date, amount, description, category_id, expense_id)
    cursor.execute(sql, values)
    conn.commit()

# Function to delete an expense
def delete_expense(expense_id):
    sql = '''
        DELETE FROM expenses
        WHERE id = %s
    '''
    cursor.execute(sql, (expense_id,))
    conn.commit()

# Function to retrieve all expenses
def get_all_expenses():
    cursor.execute('SELECT * FROM expenses')
    return cursor.fetchall()

# Function to retrieve expenses by category
def get_expenses_by_category(category_id):
    sql = '''
        SELECT * FROM expenses
        WHERE category_id = %s
    '''
    cursor.execute(sql, (category_id,))
    return cursor.fetchall()

# Function to retrieve spending summary
def get_spending_summary():
    sql = '''
        SELECT categories.name, SUM(expenses.amount) AS total_spent
        FROM expenses
        JOIN categories ON expenses.category_id = categories.id
        GROUP BY categories.name
    '''
    cursor.execute(sql)
    return cursor.fetchall()



delete_expense(7)
expenses = get_all_expenses()
print("All Expenses:")
for expense in expenses:
    print(expense)
print()

summary = get_spending_summary()
print("Spending Summary:")
for item in summary:
    print(f"{item[0]}: ${item[1]}")
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='whwhwh89',
    database='expense_tracker'
)
cursor = conn.cursor()

# Create expenses table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        description TEXT,
        category_id INT,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
''')

# Create categories table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    )
''')

conn.commit()











# Function to insert a new expense
def insert_expense(id, date, amount, description, category_id):
    sql = '''
        INSERT INTO expenses (id, date, amount, description, category_id)
        VALUES (%s, %s, %s, %s, %s)
    '''
    values = (id, date, amount, description, category_id)
    cursor.execute(sql, values)
    conn.commit()

# Function to update an existing expense
def update_expense(expense_id, date, amount, description, category_id):
    sql = '''
        UPDATE expenses
        SET date = %s, amount = %s, description = %s, category_id = %s
        WHERE id = %s
    '''
    values = (date, amount, description, category_id, expense_id)
    cursor.execute(sql, values)
    conn.commit()

# Function to delete an expense
def delete_expense(expense_id):
    sql = '''
        DELETE FROM expenses
        WHERE id = %s
    '''
    cursor.execute(sql, (expense_id,))
    conn.commit()

# Function to retrieve all expenses
def get_all_expenses():
    cursor.execute('SELECT * FROM expenses')
    return cursor.fetchall()

# Function to retrieve expenses by category
def get_expenses_by_category(category_id):
    sql = '''
        SELECT * FROM expenses
        WHERE category_id = %s
    '''
    cursor.execute(sql, (category_id,))
    return cursor.fetchall()

# Function to retrieve spending summary
def get_spending_summary():
    sql = '''
        SELECT categories.name, SUM(expenses.amount) AS total_spent
        FROM expenses
        JOIN categories ON expenses.category_id = categories.id
        GROUP BY categories.name
    '''
    cursor.execute(sql)
    return cursor.fetchall()



delete_expense(1)
expenses = get_all_expenses()
print("All Expenses:")
for expense in expenses:
    print(expense)
print()

summary = get_spending_summary()
print("Spending Summary:")
for item in summary:
    print(f"{item[0]}: ${item[1]}")
