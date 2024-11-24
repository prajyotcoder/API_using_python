


#REST_API Demonstration Script
#Author: Prajyot Talkar
#Date: [24/11/2024]

import pyodbc
from flask import Flask, jsonify, request

# Flask app initialization
app = Flask(__name__)

# SQL Server connection string
connection_string = (
    r"Driver={SQL Server};"
    r"Server=DESKTOP-ECI9CJ4\SQLEXPRESS01;"
    r"Database=PRAJYOT;"
    r"Trusted_Connection=yes;"
    r"Encrypt=no;"
)

# Function to execute SQL queries
def execute_query(query, params=None):
    try:
        with pyodbc.connect(connection_string) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()
                else:
                    conn.commit()
                    return None
    except Exception as e:
        print(f"Database error: {e}")
        return []

# API endpoint: Get all rows from MOCK_DATA
@app.route('/mock_data', methods=['GET'])
def get_mock_data():
    query = "SELECT id, first_name, last_name, gender, ip_address FROM MOCK_DATA"
    results = execute_query(query)
    mock_data = [
        {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "gender": row[3],
            "ip_address": row[4]
        } for row in results
    ]
    return jsonify(mock_data)

# API endpoint: Get a specific row by ID
@app.route('/mock_data/<int:record_id>', methods=['GET'])
def get_mock_data_by_id(record_id):
    query = "SELECT id, first_name, last_name, gender, ip_address FROM MOCK_DATA WHERE id = ?"
    results = execute_query(query, (record_id,))
    if results:
        row = results[0]
        return jsonify({
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "gender": row[3],
            "ip_address": row[4]
        })
    else:
        return jsonify({"error": "Record not found"}), 404

# API endpoint: Add a new record
@app.route('/mock_data', methods=['POST'])
def add_mock_data():
    data = request.get_json()
    if "id" in data and "first_name" in data and "last_name" in data and "gender" in data and "ip_address" in data:
         query = "INSERT INTO MOCK_DATA (id, first_name, last_name, gender, ip_address) VALUES (?, ?, ?, ?, ?)"
         execute_query(query, (data["id"], data["first_name"], data["last_name"], data["gender"], data["ip_address"]))
         return jsonify({"message": f"Record with id {data['id']} added successfully"}), 201  # 201 = Created status
    else:
        return jsonify({"error": "Invalid data, all fields are required"}), 400  # 400 = Bad Request status


# API endpoint: Delete a record by ID
@app.route('/mock_data/<int:record_id>', methods=['DELETE'])
def delete_mock_data(record_id):
    query = "DELETE FROM MOCK_DATA WHERE id = ?"
    results = execute_query(query, (record_id,))
    return jsonify({"message": "Record deleted successfully"}) if results is None else jsonify({"error": "Record not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
