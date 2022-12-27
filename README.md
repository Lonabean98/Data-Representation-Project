Welcome to the Data Representation Project 2021 repository!

This repository contains the code and data for a web application built with Flask and RESTful APIs that connects to a database table and allows for CRUD (create, read, update, delete) operations through a web page. The application is a guitar shop inventory system for a fictional store called String Theory. It allows users to view the list and details of the current stock, create new stock with the option to select guitar model and colour, update existing stock, and delete stock. All of these actions are interfaced with a stock table in a MySQL database.

In order to run the program, you will need to have Python, MySQL, and Flask installed on your machine. If you do not have Python installed, it is recommended to install Anaconda, which includes a full Python installation and all necessary libraries. MySQL can be downloaded and installed from the MySQL website, and Flask can be installed using the command pip install Flask.

To set up the database, run the createdb.py program to create a schema called datarepresentation, then run createtable.py to create a table called guitars in the datarepresentation schema. Finally, run the main server program server.py and navigate to http://127.0.0.1:5000/ in a web browser to access the shop system.

Note: The user and password for the MySQL database in this instance are set to 'root' and 'root', respectively. If your system has different login credentials, you will need to update the db class in DAO.py with your own user and password.

To use the guitar shop system:

On the main page, you will see a table of current stock (which will be empty if there is no stock yet).
To create a new item, select "Create new stock" and fill out the form with the Guitar model, price, quantity, dat received and colour. The stock ID will be automatically updated. Click "Create Entry" to save the guitar and return to the main page, or "Cancel" to clear the form and return to the main page without creating a new item.
To update an item, select "Update Stock" in the corresponding guitar record and make any desired changes on the update form. Click "Update" to save the changes and return to the main page, or "Cancel" to discard the changes and return to the main page.
To delete an item, select "Delete Stock" in the corresponding stock record. This will remove the stock from the table and the database.