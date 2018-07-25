from flask import jsonify
from app.main.models import *
from app.main.controllers import *
from . import api


@api.route('/bill-summary/<string:year>', methods=['GET'])
def get_bill_summary(year):
    res = BillSummary(year)
    return jsonify(res.summary), 200


@api.route('/bill-summary/<string:year>/barchart', methods=['GET'])
def get_bill_summary_barchartdata(year):
    res = BillSummary(year)
    return jsonify(res.get_summary_barchart_data()), 200


@api.route('/bill-summary/<string:year>/amounts', methods=['GET'])
def get_bill_summary_amounts(year):
    res = BillSummary(year)
    return jsonify(res.get_payment_amounts()), 200
