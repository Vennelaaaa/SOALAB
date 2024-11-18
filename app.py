from flask import Flask, request, render_template
import json

app = Flask(__name__)

# Load data from JSON file
with open('data.json', 'r') as f:
    mutual_funds = json.load(f)

# Route 1: Show all mutual funds
@app.route('/')
def list_funds():
    return render_template('funds.html', funds=mutual_funds)

# Route 2: Get returns for a specific fund
@app.route('/mutualfunds/returns', methods=['GET'])
def get_returns():
    fund_name = request.args.get('fund')  # Get the fund name from query params

    # Handle case where the user doesn't enter a fund name
    if not fund_name:
        return render_template('funds.html', funds=mutual_funds, error="Fund name is required!")

    # Search for the fund
    for fund in mutual_funds:
        if fund["name"].lower() == fund_name.lower():  # Case-insensitive comparison
            return render_template("returns.html", fund=fund)

    # Handle case where the fund is not found
    return render_template('funds.html', funds=mutual_funds, error="Fund not found!")

if __name__ == '__main__':
    app.run(debug=True)
