# Payment Gateway

This Payment Gateway is a Flask-based project that integrates a custom 3D Secure (3DS) verification system and card validation functionalities. The application allows users to process transactions securely, validate card information (number, expiry date, CVC), and perform 3DS verification during checkout.


**GUI**

<img src="https://github.com/WillyHad96/Payment-Gateway/blob/main/PaymentGatewayImage.png" alt="Screenrecording" width="800" height="500">


**Testing**

The project can be tested in the following URL: 

[www.willyhad96.pythonanywhere.com ](https://willyhad96.pythonanywhere.com/)


**Features**

* **Custom 3D Secure (3DS) Verification**: A built-in 3DS system for authenticating cardholders during online payments without relying on third-party services.
* **Card Validation**: Validate card number, expiry date, and CVC against a stored database.
* **Email Verification**: Secure email-based authentication to add an extra layer of security.
* **Automatic Testing**: Ability to test up to 1000 credit cards automatically for processing efficiency.


**Code Overview**

The code snippet provided in Checkout.py is just the backbone of the full project, if you want to know more about the code, you can contact me and I can show you the whole project.


**Libraries**

```
Flask
Datetime
Requests
```


**License**

This project is licensed under the MIT License - see the LICENSE file for details.


**Acknowledgements**

* Python Software Foundation
* Flask Documentation
* Requests Documentation
