from .errors import *
from flask import jsonify
from app import db
from . import api, get_query_string
from app.main.models import *


# trader information section #############################################
@api.route('/traders', methods=['GET'])
def get_traders():
    qry_dict = get_query_string(Trader)
    if len(qry_dict) == 0:
        traders = Trader.query.all()
    else:
        traders = Trader.query.filter_by(**qry_dict).all()
    return jsonify([{"Oid": t.Oid, "Group": t.Group} for t in traders]), 200


@api.route('/traders/<string:Oid>', methods=['GET'])
def get_trader(Oid):
    trader = Trader.query.filter_by(Oid=Oid).first_or_404()
    return jsonify(trader.to_json()), 200


@api.route('/traders', methods=['POST'])
def create_trader():
    json_trader = request.json
    trader = Trader.from_json(json_trader)
    db.session.add(trader)
    db.session.commit()
    return jsonify(trader.to_json()), 201


'''
@api.route('/traders/<string:Oid>', methods=['DELETE'])
def delete_trader(Oid):
    trader = Trader.query.filter_by(Oid=Oid).first_or_404()
    res = trader.to_json()
    for email in trader.Person.Emails.all():
        db.session.delete(email)
    for phone in trader.Person.Phones.all():
        db.session.delete(phone)
    for address in trader.Person.Addresses.all():
        db.session.delete(address)
    db.session.delete(trader)
    db.session.commit()
    return jsonify(res), 200, {'Status': 'Deleted'}
'''


@api.route('/traders/<string:Oid>', methods=['PUT'])
def update_trader(Oid):
    json_trader_new = request.json
    trader = Trader.query.filter_by(Oid=Oid).first_or_404()
    trader.update(json_trader_new)
    db.session.commit()
    return jsonify(trader.to_json()), 200, {'Status': 'Updated'}


@api.route('/trader/updategsec', methods=['PUT'])
def update_trader_gsec():
    traderOid = request.json.get('TraderOid')
    gsecOid = request.json.get('GSECCodeOid')
    trader = Trader.query.filter_by(Oid=traderOid).first_or_404()
    gsec = GSECCode.query.filter_by(Oid=gsecOid).first_or_404()
    if gsec not in trader.gseccodes:
        trader.gseccodes.append(gsec)
        db.session.commit()
    else:
        trader.gseccodes.remove(gsec)
        db.session.commit()
    return jsonify(trader.to_json()), 200
