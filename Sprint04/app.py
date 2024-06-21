from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# MySQL Connection Configuration
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='whwhwh89',
    database='expense_tracker'
)

# Function to fetch categories
def get_categories():
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM categories')
        return cursor.fetchall()

# Function to fetch all expenses
def get_expenses():
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM expenses')
        expenses = cursor.fetchall()
        return expenses
    

# Route to display home page and add expenses
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        date = request.form['date']
        amount = float(request.form['amount'])
        description = request.form['description']
        category_id = int(request.form['categories'])

        cursor = conn.cursor()
        sql = '''
            INSERT INTO expenses (date, amount, description, category_id)
            VALUES (%s, %s, %s, %s)
        '''
        values = (date, amount, description, category_id)
        cursor.execute(sql, values)
        conn.commit()

        return redirect(url_for('home'))

    categories = get_categories()
    expenses = get_expenses()

    return render_template('index.html', categories=categories, expenses=expenses)

@app.route('/delete_expense/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    cursor = conn.cursor()
    sql = 'DELETE FROM expenses WHERE id = %s'
    cursor.execute(sql, (expense_id,))
    conn.commit()
    
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)





