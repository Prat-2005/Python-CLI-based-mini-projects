from decimal import Decimal
import mysql.connector

# Create a connection between Python and MySQL database
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '@Prat_3103',
    database = 'transaction_handling'
)

# Create a cursor with alias name 'cur'
cur = conn.cursor()

# Create 'accounts' table: 'account_id', 'name' and 'balance'
try:
    cur.execute(
        # Here, 'decimal (10, 2)' where precision = 10 & scale = 2 
        # Precision - Total number of digits (both before and after the decimal point)
        # Scale - Number of digits after the decimal point    
        '''Create table accounts (
            account_id varchar(10) not null,
            name text,
            balance decimal (10, 2),  
            primary key (account_id));'''
    )

    print("Table created successfully!\n")

except mysql.connector.Error as e:
    print(f"Table creation failed! {e}.\n")

# Insert two sample user's account data into 'accounts' table
cur.execute(
    '''Insert into accounts(account_id, name, balance) values
        ('hdfc0913', 'Priyansh', 1000.00),
        ('icici0871', 'Shreyas', 500.00);'''
)

print("Records inserted successfully!\n")

def transfer_money(from_account, to_account, amount):
    try:
        # Start transaction
        cur.execute("START TRANSACTION")
        
        # Check if source account has sufficient balance
        cur.execute("SELECT balance FROM accounts WHERE account_id = %s FOR UPDATE", (from_account,))
        balance = cur.fetchone()[0] # 0 - indexing on selected column 'balance'
        
        if balance < amount:
            raise ValueError("Insufficient funds")
        
        # Perform transfers
        cur.execute("UPDATE accounts SET balance = balance - %s WHERE account_id = %s", 
                    (amount, from_account))
        cur.execute("UPDATE accounts SET balance = balance + %s WHERE account_id = %s", 
                    (amount, to_account))
        
        # Commit if all went well
        conn.commit()
        print("Transaction completed successfully!")
        
    except Exception as e:
        conn.rollback()
        print(f"Transaction failed: {str(e)}")

# Usage
print("Welcome to our Bank service!")
print("Choose transfer direction:")
print("1. From HDFC to ICICI")
print("2. From ICICI to HDFC")

ch = int(input("Enter your choice (1 or 2): "))

if ch in (1, 2):
    try:
        amount = Decimal(input("Enter amount: "))
        if ch == 1:
            transfer_money('hdfc0913', 'icici0871', amount)
        else:
            transfer_money('icici0871', 'hdfc0913', amount)
    except ValueError as e:
        print(f"Invalid input: {str(e)}")
else:
    print("Invalid choice!")

# Save the changes in the database
conn.commit()

# Close the connection
conn.close()