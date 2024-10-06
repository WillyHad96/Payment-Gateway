#Libraries

from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
from EmailCheckerHeadless import email_checker
from CardValidator import check_card_details

# Create the Flask application
app = Flask(__name__)

# Enable template auto-reload for development
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Home page
@app.route("/")
def checkout():
    return render_template('Checkout.html')

# Loading Page
@app.route("/VerifyingPayment", methods=['POST'])
def payment_processing_screen():
    card_number = request.form.get('card_number')
    card_type = request.form.get('card_type')
    expiry_date = request.form.get('exp_date')
    email_address = request.form.get('email_address')
    
    # Pass the form data to the loading page
    return render_template('Loading.html', card_number=card_number, card_type=card_type, exp_date=expiry_date, email_address=email_address)

# Payment Processing in the Loading Page
@app.route("/processing_payment", methods=['POST'])
def payment_processing():
    card_number = request.form.get('card_number')
    card_type = request.form.get('card_type')
    email_address = request.form.get('email_address')
    expiry_date_str = request.form.get('exp_date') 

    # Email and card validation 
    email_valid = email_checker(email_address)
    card_valid = check_card_details(card_number, card_type, expiry_date_str)

    if email_valid and card_valid:
        return jsonify({'status': 'success', 'redirect_url': url_for('successful_payment')})
    else:
        return jsonify({'status': 'failure', 'redirect_url': url_for('failed_payment')}) 

# successful Payment
@app.route("/SuccessfulPayment/")
def successful_payment():
    return render_template('SuccessfulPayment.html')

# Failed Payment
@app.route("/FailedPayment/")
def failed_payment():
    return render_template('FailedPayment.html')

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
