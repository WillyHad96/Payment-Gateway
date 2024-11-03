# Payment Gateway

This Payment Gateway is a Flask-based project featuring a custom 3D Secure (3DS) verification system, card validation, and reCAPTCHA functionalities. The application supports various payment methods, including Klarna, PayPal, and Google Pay, allowing users to securely process transactions and validate card information (number, expiry date, CVC) while performing 3DS verification during checkout.


**GUI**

<img src="https://github.com/WillyHad96/Payment-Gateway/blob/main/PaymentGatewayImage3.png" alt="Screenrecording" width="800" height="500">


**Testing**

The project can be tested in the following URL: 

[www.willyhad96.pythonanywhere.com ](https://willyhad96.pythonanywhere.com/)


**Features**

* **Custom 3D Secure (3DS) Verification**: A built-in 3DS system for authenticating cardholders during online payments without relying on third-party services.
* **Card Validation**: Validate card number, expiry date, and CVC against a stored database.
* **Email Verification**: Secure email-based authentication to add an extra layer of security.
* **Automatic Testing**: Ability to test up to 1000 credit cards automatically for processing efficiency.
* **Payment Method Integrations**:
  - **Google Pay**: Convenient mobile and online payment integration.
  - **PayPal**: Widely recognized payment option for secure transactions.
  - **Klarna**: Buy-now-pay-later functionality for enhanced flexibility at checkout.


**Code Overview**

The code snippet provided in Checkout.py is just the backbone of the full project, if you want to know more about the code, you can contact me and I can show you the whole project.


**Libraries**

```
Flask
Datetime
Requests
Paypalrestsdk
Flask_wtf
```


**License**

This project is licensed under the MIT License - see the LICENSE file for details.


**Acknowledgements**

* Python Software Foundation
* Flask Documentation
* Requests Documentation
* Google Pay Documentation
* Paypal Documentation
* Klarna Documentation
