from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Marketplace API!"

@app.route('/user/add', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")
    balance = data.get("balance")
    if username and balance:
        # Add user logic (You can integrate UserManager here)
        return jsonify({"message": "User added successfully"}), 201
    return jsonify({"error": "Username and initial balance are required to add a user."}), 400

@app.route('/marketplace/add_item', methods=['POST'])
def add_item():
    data = request.get_json()
    item_name = data.get("item_name")
    price = data.get("price")
    if item_name and price:
        # Add item logic (You can integrate MarketplaceManager here)
        return jsonify({"message": "Item added successfully"}), 201
    return jsonify({"error": "Item name and price are required."}), 400

@app.route('/marketplace/view_item/<string:item_name>', methods=['GET'])
def view_item(item_name):
    # Sample logic to view item (integrate with actual MarketplaceManager)
    item = {"item_name": item_name, "price": 100}  # Mock item data
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

