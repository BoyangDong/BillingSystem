from flask import Blueprint, jsonify, request
from flask_cors import CORS
api = Blueprint('api', __name__)
CORS(api, resources={r"/*": {"origins": "*"}})


def get_query_string(cls):
    res = {}
    for qry in request.query_string.split('&'):
        pair = qry.split('=')
        if len(pair) == 2:
            if pair[0] in cls.__table__.columns.keys():
                res[pair[0]] = pair[1].replace('+', ' ')
    return res


from .authentication import auth
import user_routes
import bill_routs
import breakdown_routes
import contact_routes
import vendor_routes
import gseccode_routes
import trader_routes
import dashboard_routes


@api.route('/')
def get():
    return jsonify({"message": "Welcome to SUMO Billing System",
                    "ip": request.remote_addr})


'''
# trader/vender services #######################################
# Subscribed Services
@api.route('/services/<string:Oid>', methods=['GET'])
def get_service(Oid):
    s = SubscribedService.query.filter_by(Oid=Oid).first_or_404()
    return jsonify(s.to_json()), 200


@api.route('/services/<string:Oid>', methods=['PUT'])
def update_service(Oid):
    json_service_new = request.json
    serv = SubscribedService.query.filter_by(Oid=Oid).first_or_404()
    serv.update(json_service_new)
    res = serv.to_json()
    db.session.commit()
    return jsonify(res), 200, {'Status': 'Updated'}


@api.route('/services/<string:Oid>', methods=['DELETE'])
def delete_service(Oid):
    serv = SubscribedService.query.filter_by(Oid=Oid).first_or_404()
    res = serv.to_json()
    db.session.delete(serv)
    db.session.commit()
    return jsonify(res), 200, {'Status': 'Deleted'}


@api.route('/services', methods=['GET'])
def get_services():
    return jsonify([
        s.to_json() for s in
        SubscribedService.query.filter_by(
            **get_query_string(SubscribedService)).all()]), 200


@api.route('/services', methods=['POST'])
def create_service():
    json_service = request.json
    serv = SubscribedService.from_json(json_service)

    try:
        db.session.add(serv)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify(serv.to_json()), 400, {"Error": "Not Created"}
    return jsonify(serv.to_json()), 201,
    {"Location": url_for('api.get_service', Oid=serv.Oid, _external=True)}
'''


'''
# Cash Card Section #################################################
@api.route('/cashcard', methods=['POST'])
def create_cashcards():
    json_cc = request.json
    cashcards = []
    if isinstance(json_cc, list):
        for cc in json_cc:
            cashcards.append(CashCard.from_json(cc))
    else:
        cashcards.append(CashCard.from_json(json_cc))

    for cashcard in cashcard:
        db.session.add(cashcard)
    db.commit()
    return jsonify({"message": "cash cards created"}), 201


@api.route('/cashcard', methods=['DELETE'])
def delete_cashcard():
    for cashcard in CashCard.query.all():
        db.session.delete(cashcard)
    db.session.commit()
    return jsonify({"message": "cash cards removed"}), 200


@api.route('/cashcard', methods=['GET'])
def get_cashcard():
    return jsonify([cashcard.to_json()
                    for cashcard in CashCard.query.all()]), 200


@api.route('/cashcard/<string:Oid>', methods=['POST'])
def move_to_cashcard(Oid):
    cc = []
    bill = Bill.query.filter_by(Oid=Oid).first()
    if bill:
        cc = bill.to_cash_card()
        for item in cc:
            db.session.add(item)
        db.session.commit()
    return jsonify({'message': 'put ' +
                    str(len(cc)) +
                    ' items in Cash Card'}), 201


@api.route('/cashcard/download', methods=['GET'])
def download_cashcards():
    cashcard = CashCard.getCashCardItems()
    xlsx_data = getCashCardReport(cashcard)
    # print xlsx_data
    return send_file(xlsx_data,
                     attachment_filename='test.xlsx',
                     as_attachment=True)


@api.route('/test_report/<string:code>', methods=['GET'])
def test_download_report(code):
    recon = GSECMonthlyRecon(code, '2017')
    data = {'gseccode': code, 'data': recon.report}
    report = GSECMonthlyReconReport()
    file_name = code + '_' + '2017.xlsx'
    return send_file(report.get_report_xlsx(data),
                     attachment_filename=file_name,
                     as_attachment=True)
'''
