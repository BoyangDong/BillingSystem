from .errors import *
from flask import jsonify
from app import db
from . import api, get_query_string
from app.main.models import *


# breakdowns####################################
@api.route('/bills/breakdowns', methods=['GET'])
def get_breakdowns():
    return jsonify([
        breakdown.to_json() for breakdown
        in Breakdown.query.filter_by(**get_query_string(Breakdown)).all()]),
    200


@api.route('/bills/breakdowns/<string:Oid>', methods=['GET'])
def get_bill_breakdown(Oid):
    breakdown = Breakdown.query.filter_by(Oid=Oid).first_or_404()
    return jsonify(breakdown.to_json()), 200


@api.route('/bills/breakdowns/<string:Oid>', methods=['PUT'])
def update_breakdown(Oid):
    breakdown = Breakdown.query.filter_by(Oid=Oid).first_or_404()
    bill = breakdown.Bill
    if bill.IsPaid:
        return jsonify(breakdown.to_json()),
        304,
        {'Status': 'Not Modified', 'Message': 'Paid bill cannot be modified'}
    json_breakdown_new = request.json
    breakdown.update(json_breakdown_new)
    res = breakdown.to_json()
    db.session.commit()
    bill.check_breakdown_completion()
    db.session.commit()
    return jsonify(res), 200


@api.route('/bills/breakdowns/<string:Oid>', methods=['DELETE'])
def delete_breakdown(Oid):
    res = {}
    breakdown = Breakdown.query.filter_by(Oid=Oid).first_or_404()
    bill = breakdown.Bill
    if bill.IsPaid:
        return jsonify(breakdown.to_json()),
        304,
        {'Status': 'Not Deleted', 'Message': 'Paid bill cannot be modified'}
    breakdown.update_monthlyexpenses()
    breakdown.tradergseccode.SortingScore -= 1
    res = breakdown.to_json()
    bill.Breakdowns.remove(breakdown)
    db.session.delete(breakdown)
    if bill.IsCompleted:
        if bill.check_breakdown_completion() is False:
            bill.IsCompleted = False
    db.session.commit()
    return jsonify(res), 200


@api.route('/bills/<string:Oid>/breakdowns', methods=['GET'])
def get_bill_breakdowns(Oid):
    bill = Bill.query.filter_by(Oid=Oid).first_or_404()
    breakdowns = bill.Breakdowns.all()
    return jsonify([bkd.to_json() for bkd in breakdowns]), 200


@api.route('/bills/<string:Oid>/breakdowns', methods=['POST'])
def creat_bill_breakdowns(Oid):
    res = []
    json_breakdowns = request.json
    if type(json_breakdowns) != list:
        return jsonify({"message": "not created"}), 400
    for json_breakdown in json_breakdowns:
        json_breakdown['BillOid'] = Oid
        res.append(bkd.to_json())
        db.session.add(bkd)
    db.session.commit()
    bill = Bill.query.filter_by(Oid=Oid).first_or_404()
    if bill.IsCompleted is False:
        if bill.check_breakdown_completion() is True:
            bill.IsCompleted = True
            db.session.commit()
    return jsonify(res), 201


@api.route('/bills/<string:Oid>/breakdown', methods=['POST'])
def create_bill_breakdown(Oid):

    json_breakdown = request.json
    json_breakdown['BillOid'] = Oid
    breakdown = Breakdown.from_json(json_breakdown)
    res = breakdown.to_json()
    db.session.add(breakdown)
    db.session.commit()
    bill = Bill.query.filter_by(Oid=Oid).first_or_404()
    if bill.IsCompleted is False:
        if bill.check_breakdown_completion() is True:
            bill.IsCompleted = True
            db.session.commit()
    return jsonify(res), 201
