# Program for running server for Guitar stock System.


# Import the relevant modules.
from flask import Flask,  request, abort, jsonify
from DAO import guitarDao


app = Flask(__name__, static_url_path='', static_folder='templates')


#Home Page
@app.route('/')
def index():
    return app.send_static_file('index.html')

# retrieve all the data from the stock database.
@app.route('/guitars')
def fetchAll():
    return jsonify(guitarDao.fetchAll())

# Update an existing stock record.
@app.route('/guitars/<int:id>', methods = ['PUT'])
def update(id):
    retrieveStock = guitarDao.searchForId(id)
    print(retrieveStock)
    if len(retrieveStock) == 0:
        return jsonify({}), 404      
    currentStock = retrieveStock
    if 'guitarmodel' in request.json:
        currentStock['guitarmodel'] = request.json['guitarmodel']
    if 'price' in request.json:
        currentStock['price'] = request.json['price']
    if 'quantity' in request.json:
        currentStock['quantity'] = request.json['quantity']
    if 'datereceived' in request.json:
        currentStock['datereceived'] = request.json['datereceived']
    if 'colour' in request.json:
        currentStock['colour'] = request.json['colour']
   
    guitarDao.update(currentStock)
    return jsonify(currentStock)


# Add a new guitar to the database.
@app.route('/guitars', methods = ['POST'])
def create():
    if not request.json:

        abort(400)
    stock = {
    "guitarmodel": request.json['guitarmodel'], 
    "price": request.json["price"], 
    "quantity": request.json["quantity"],
    "datereceived": request.json["datereceived"],
    "colour": request.json["colour"]
    }
    return jsonify(guitarDao.create(stock))

# Get a specific booking from the database.
@app.route('/guitars/<int:id>')
def searchForId(ISBN):
    return jsonify(guitarDao.searchForId(id))



# Delete a Stock record.
@app.route('/guitars/<int:id>', methods = ['DELETE'])
def delete(id):
    retrieveStock = guitarDao.searchForId(id)
    print(retrieveStock)
    if len(retrieveStock) == 0:
        return jsonify({}), 404
    guitarDao.delete(id)
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)