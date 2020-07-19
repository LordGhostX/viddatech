from paystackapi.paystack import Paystack
from paystackapi.transaction import Transaction
from flask import *

app = Flask(__name__)
paystack_secret_key = "sk_test_b04fca7ba5fee795292b159e9fe527dcaf222c8b"
paystack = Paystack(secret_key=paystack_secret_key)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/new-transacton/", methods=["POST"])
def new_transaction():
    reference = request.form.get("reference")
    amount = request.form.get("amount")
    email = request.form.get("email")
    response = Transaction.initialize(
        reference=reference, amount=amount, email=email)
    if response["status"]:
        return jsonify({
            "success": True,
            "payment_url": response["data"]["authorization_url"],
            "reference": response["data"]["reference"],
            "message": response["message"]
        }), 200
    else:
        return jsonify({
        "success": False,
        "message": response["message"],
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
