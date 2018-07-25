from .errors import *
from flask import jsonify
from app import db
from . import api, get_query_string
from app.main.models import *


@api.route('/bills', methods=['GET'])
def get_bills():
    bills = Bill.query.filter_by(**get_query_string(Bill)).all()
    return jsonify([bill.to_json() for bill
                    in sorted(bills,
                              key=lambda x: (x, x.VendorShortcut, x.Type),
                              reverse=True)]), 200


@api.route('/bills/<string:Oid>', methods=['GET'])
def get_bill(Oid):
    bill = Bill.query.filter_by(Oid=Oid).first_or_404()
    return jsonify(bill.to_json()), 200


@api.route('/newbills', methods=['POST'])
def create_newbill():
    # json_bill = request.json
    pass


@api.route('/bills', methods=['POST'])
def create_bill():
    json_bill = request.json
    bill = Bill.from_json(json_bill)

    json_breakdowns = json_bill.get("Breakdowns")
    if json_breakdowns is not None:
        breakdowns = []
        total = Decimal('0.0')
        if isinstance(json_breakdowns, list):
            for json_breakdown in json_breakdowns:
                if isinstance(json_breakdown, dict):
                    json_breakdown['BillOid'] = bill.Oid
                    breakdowns.append(Breakdown.from_json(json_breakdown))
            for bkd in breakdowns:
                total += Decimal(bkd.Amount)
                bill.Breakdowns.append(bkd)
                db.session.add(bkd)
    if total >= bill.Total:
        bill.IsCompleted = True
    db.session.add(bill)
    db.session.commit()
    return jsonify(bill.to_json()), 201,
    {'Location': url_for('api.get_bill', Oid=bill.Oid, _external=True)}


@api.route('/bills/<string:Oid>', methods=['DELETE'])
def delete_bill(Oid):
    res = {}
    bill = Bill.query.filter_by(Oid=Oid).first_or_404()
    if bill.IsPaid:
        return jsonify(breakdown.to_json()), 304,
        {'Status': 'Not Modified', 'Message': 'Paid bill cannot be modified'}
    breakdowns = bill.Breakdowns.all()
    if breakdowns is not None and isinstance(breakdowns, list):
        for bkd in breakdowns:
            bkd.tradergseccode.SortingScore -= 1
            db.session.delete(bkd)
    if bill is not None:
        res = bill.to_json()
        db.session.delete(bill)

    db.session.commit()
    return jsonify(res), 200


@api.route('/bills/<string:Oid>', methods=['PUT'])
def update_bill(Oid):
    json_bill_new = request.json
    bill = Bill.query.filter_by(Oid=Oid).first_or_404()
    if bill.IsPaid:
        return jsonify(breakdown.to_json()), 304,
        {'Status': 'Not Modified', 'Message': 'Paid bill cannot be modified'}
    bill.update(json_bill_new)
    res = bill.to_json()
    bill.check_breakdown_completion()
    db.session.commit()
    return jsonify(res), 200


@api.route('/bills/approve', methods=['PUT'])
def approve_bill():
    Oid = request.json.get('Oid')
    bill = Bill.query.filter_by(Oid=Oid).first_or_404()
    bill.IsApproved = True
    db.session.commit()
    bill = Bill.query.filter_by(Oid=Oid).first_or_404()
    return jsonify(bill.to_json()), 200, {'Status': 'Updated'}


@api.route('/bills/pay', methods=['PUT'])
def pay_bill():
    Oid = request.json.get('Oid')
    bill = Bill.query.filter_by(Oid=Oid).first_or_404()
    ref = request.json.get('BillPayRef')
    if ref is not None:
        bill.BillPayRef = ref
        bill.IsPaid = True
        db.session.commit()
        return jsonify(bill.to_json()), 200, {'Status': 'Updated'}
    else:
        return jsonify(bill.to_json()), 304, {'Status': 'Not Updated'}


@api.route('/bills/reject', methods=['PUT'])
def reject_bill():
    Oid = request.json.get('Oid')
    bill = Bill.query.filter_by(Oid=Oid).first_or_404()
    if bill.IsPaid is not False:
        return jsonify(bill.to_json()), 304, {'Status': 'Not Modified'}
    bill.IsCompleted = False
    db.session.commit()
    return jsonify(bill.to_json()), 200, {'Status': 'Updated'}
