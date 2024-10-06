#Libraries

from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
#from ThreeDSwindow import threeds_verification
from EmailCheckerHeadless import email_checker
from CardValidator import check_card_details
#from PMDatabase import save_card_details
#import OOP
#from APM import check_klarna_details, check_paypal_details, check_ideal_details, check_wallet_details, willet
#import schedule #This is for subscriptions
#import mysql.connector  # this is to connect the cards with the database for the machine learning Radar tool(Fraudar)
#Credit Card Fraud Detection Kaggle Database: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data
#Supported Radar Attributes: https://docs.stripe.com/radar/rules/supported-attributes 
#Library for creating fake data: https://faker.readthedocs.io/en/master/
#Encrypt Data using Javascript on the checkout to go to the database, so that it can't be intercepted

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

    # Debugging print statements
    print(f"Received form data in payment_processing_screen(): - Email: {email_address}, Card Number: {card_number}, Card Type: {card_type}, Expiry Date: {expiry_date}")
    
    # Pass the form data to the loading page
    return render_template('Loading.html', card_number=card_number, card_type=card_type, exp_date=expiry_date, email_address=email_address)

# Payment Processing in the Loading Page
@app.route("/processing_payment", methods=['POST'])
def payment_processing():
    card_number = request.form.get('card_number')
    card_type = request.form.get('card_type')
    email_address = request.form.get('email_address')
    expiry_date_str = request.form.get('exp_date') #or '2026-05-01' if we want to harcode for testing

    # Log received data
    print(f"Received form data in payment_processing(): - Card Number: {card_number}, Card Type: {card_type}, Expiry Date: {expiry_date_str}, Email: {email_address}")

    # if not expiry_date:
    #     print("Error: Expiry date is missing in payment processing()!")
    #     return jsonify({'status': 'failure', 'redirect_url': url_for('failed_payment')})

    # Since expiry_date is already in 'yyyy-MM-dd', no need for conversion
    print(f"Expiry Date in original format: {expiry_date_str}")

    # Email and card validation (dummy check for illustration)
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

# Uncomment and implement the Setup mode and Subscription mode as needed
# Setup mode
# @app.route("/SetupButton/", methods=['POST'])
# def setup_button():
#     card_number = request.form.get('card_number')
#     card_type = request.form.get('card_type')
#     expiry_date = request.form.get('exp_date')
#     email_address = request.form.get('email_address')
#     current_date = datetime.now()

#     email_valid = email_checker(email_address)
#     card_valid = check_card_details(card_number, card_type, expiry_date, current_date)

#     if email_valid and card_valid:
#         # save_card_details()
#         return render_template('SuccessfulSetup.html')
#     else:
#         return render_template('FailedSetup.html')

# Subscription mode
# @app.route("/SubscriptionButton/", methods=['POST'])
# def subscription_button():
#     card_number = request.form.get('card_number')
#     card_type = request.form.get('card_type')
#     expiry_date = request.form.get('exp_date')
#     email_address = request.form.get('email_address')
#     current_date = datetime.now()

#     email_valid = email_checker(email_address)
#     card_valid = check_card_details(card_number, card_type, expiry_date, current_date)

#     if email_valid and card_valid:
#         # save_card_details()
#         # payment()
#         # schedule(payment())  # Schedule as needed
#         return render_template('SuccessfulPayment.html')
#     else:
#         return render_template('FailedPayment.html')

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
