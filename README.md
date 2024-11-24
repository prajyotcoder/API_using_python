This project is a simple REST API built using Flask and pyODBC to interact with a SQL Server database. 
The API provides basic CRUD (Create, Read, Update, Delete) functionality for managing records in the MOCK_DATA table.
The API supports retrieving all records, adding new records, fetching a specific record by ID, and deleting records from the database.

Key Features:
GET /mock_data: Fetch all records from the MOCK_DATA table.
GET /mock_data/<id>: Fetch a specific record by its id.
POST /mock_data: Add a new record to the MOCK_DATA table (requires id, first_name, last_name, gender, and ip_address).
DELETE /mock_data/<id>: Delete a record by its id.
Database: Connects to an SQL Server database using pyODBC for executing SQL queries.

(Happy Coding !!)
