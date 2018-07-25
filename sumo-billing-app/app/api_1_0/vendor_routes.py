from .errors import *
from flask import jsonify, request
from app import db
from . import api, get_query_string
from app.main.models import *
from app.main.controllers import VendorMonthlyRecon


# vendor section ##############################################################
@api.route('/vendors', methods=['GET'])
def get_vendors():
    param = get_query_string(Vendor)
    if 'shortcutonly' in request.query_string:
        return jsonify([vendor.Shortcut for vendor in Vendor.query.all()]), 200
    return jsonify([v.to_json() for v in
                    Vendor.query.filter_by(**param).all()]), 200


@api.route('/vendors', methods=['PUT'])
def update_vendor():
    json_vendor = request.json
    vendor = Vendor.query.filter_by(
        Shortcut=json_vendor.get('Shortcut')).first_or_404()
    vendor.update(json_vendor)
    db.session.commit()
    return jsonify(vendor.to_json()), 200, {'Status': 'Updated'}


@api.route('/vendors/<string:Shortcut>', methods=['GET'])
def get_vendor(Shortcut):
    vendor = Vendor.query.filter_by(Shortcut=Shortcut).first_or_404()
    return jsonify(vendor.to_json()), 200


@api.route('/vendors/<string:Shortcut>/<int:n>')
def get_previous_bills(Shortcut, n):
    bills = Bill.query.filter_by(VendorShortcut=Shortcut).all()
    bills.sort()
    return jsonify([b.to_json() for b in bills[-3:]])


@api.route('/vendors/<string:Shortcut>', methods=['DELETE'])
def delete_vendor(Shortcut):
    vendor = Vendor.query.filter_by(Shortcut=Shortcut).first_or_404()
    for contact in vendor.Contacts.all():
        for addr in contact.Addresses.all():
            db.session.delete(addr)
        for phone in contact.Phones.all():
            db.session.delete(phone)
        for em in contact.Emails.all():
            db.session.delete(em)
        db.session.delete(contact)
    for acct in vendor.traderaccounts.all():
        db.session.delete(acct)
    db.session.delete(vendor)
    db.session.commit()
    return jsonify({"Shortcut": Shortcut}), 200, {'Status': 'Deleted'}


@api.route('/vendors', methods=['POST'])
def create_vendor():
    json_vendor = request.json
    vendor = Vendor.from_json(json_vendor)
    db.session.add(vendor)
    db.session.commit()
    res = vendor.to_json()
    return jsonify(res), 201


@api.route('/vendors/accounts/<string:Oid>', methods=['GET'])
def get_vendor_account(Oid):
    account = TraderAccount.query.filter_by(Oid=Oid).first_or_404()
    return jsonify(account.to_json()), 200


@api.route('/vendors/<string:Shortcut>/report/<string:Year>', methods=['GET'])
def get_vendor_report(Shortcut, Year):
    report = VendorMonthlyRecon()
    vendor = Vendor.query.filter_by(Shortcut=Shortcut).first_or_404()
    return jsonify(report.getReport(vendor, Year)), 200


@api.route('/vendors/report/<string:Year>', methods=['GET'])
def get_annual_vendor_report(Year):
    report = VendorMonthlyRecon()
    return jsonify(report.getAllReports(Year)), 200


@api.route('/vendors/report/<string:year>/download')
def download_annual_vendor_report(year):
    report = VendorMonthlyRecon()
    data = report.getAllReports(year)
    report = VendorMonthlyReconReport()
    file_name = "vendors_report" + '_' + year + '.xlsx'
    return send_file(report.get_report_xlsx(data),
                     mimetype='application/vnd.ms-excel',
                     attachment_filename=file_name, as_attachment=True)
# vendor report download started, but not done
