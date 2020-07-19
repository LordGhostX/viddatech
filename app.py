from paystackapi.paystack import Paystack
from paystackapi.transaction import Transaction
from paystackapi.tcontrol import TransferControl
from paystackapi.misc import Misc
from flask import *

app = Flask(__name__)
paystack_secret_key = "sk_test_b04fca7ba5fee795292b159e9fe527dcaf222c8b"
paystack = Paystack(secret_key=paystack_secret_key)


@app.route("/")
def index():
    return jsonify({
        "success": True,
        "message": "Hello World!",
        "docs": "https://github.com/LordGhostX/viddatech/blob/master/README.md"
    }), 200


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


@app.route("/transactions/")
def get_transactions():
    response = Transaction.list()
    if response["status"]:
        return jsonify({
            "success": True,
            "total": response["meta"]["total"],
            "total_volume": response["meta"]["total_volume"],
            "message": response["message"],
            "transactions": response["data"]
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": response["message"],
        }), 400


@app.route("/verify-transaction/", methods=["POST"])
def verify_transaction():
    reference = request.form.get("reference")
    response = Transaction.verify(reference=reference)
    if response["status"]:
        return jsonify({
            "success": True,
            "message": response["message"],
            "data": response["data"]
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": response["message"],
        }), 400


@app.route("/get-balance/")
def get_balance():
    response = TransferControl.check_balance()
    if response["status"]:
        return jsonify({
            "success": True,
            "message": response["message"],
            "balance": response["data"][0]["balance"]
        }), 200
    else:
        return jsonify({
            "success": True,
            "message": response["message"]
        }), 400
    return response


@app.route("/get-banks/")
def get_banks():
    response = Misc.list_banks()
    if response["status"]:
        return jsonify({
            "success": True,
            "message": response["message"],
            "data": response["data"]
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": response["message"],
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
