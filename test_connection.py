import pyodbc

# Replace with your actual server and database details
conn = pyodbc.connect("DRIVER={SQL Server};SERVER=HITHESH\\SQLEXPRESS1;DATABASE=sales;Trusted_Connection=yes;")

try:
    cursor = conn.cursor()
    cursor.execute("SELECT 1")  # Test query
    print("Database connected:", cursor.fetchone())  # Should return (1,)
    conn.close()
except Exception as e:
    print("Error connecting to database:", e)
