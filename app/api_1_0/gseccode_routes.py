from .errors import *
from flask import jsonify, send_file
from app import db
from . import api, get_query_string
from app.main.models import *
from app.main.controllers import GSECMonthlyRecon, GSECMonthlyReconReport


# gsec code section #############################################
@api.route('/gseccodes', methods=['GET'])
def get_gseccodes():
    return jsonify([g.to_json() for g in
                    sorted(
                        GSECCode.query
                        .filter_by(**get_query_string(GSECCode)).all(),
                        key=lambda x: x.SortingScore,
                        reverse=True)]), 200


@api.route('/gseccodelist', methods=['GET'])
def get_gseccodelist():
    gseccodes = sorted(GSECCode.query.all(),
                       key=lambda x: x.SortingScore, reverse=True)
    return jsonify([g.Code for g in gseccodes]), 200


@api.route('/gseccodes/<string:Oid_or_Code>', methods=['GET'])
def get_gseccode(Oid_or_Code):
    if len(Oid_or_Code) > 20:
        code = GSECCode.query.filter_by(Oid=Oid_or_Code).first_or_404()
    else:
        code = GSECCode.query.filter_by(Code=Oid_or_Code).first_or_404()
    return jsonify(code.to_json()), 200


@api.route('/gseccodes', methods=['POST'])
def create_gseccode():
    json_gcode = request.json
    code = GSECCode.from_json(json_gcode)
    db.session.add(code)
    db.session.commit()
    return jsonify(code.to_json()), 201


@api.route('/gseccodes/<string:code>/recon/<int:year>', methods=['GET'])
def get_monthly_recon(code, year):
    recon = GSECMonthlyRecon(code, year)
    return jsonify(recon.report), 200


@api.route('/gseccodes/<string:code>/recon/<string:year>/report',
           methods=['GET'])
def get_monthly_recon_report(code, year):
    code = code.upper()
    recon = GSECMonthlyRecon(code, year)
    data = {'gseccode': code, 'data': recon.report}
    report = GSECMonthlyReconReport()
    file_name = code + '_' + year + '.xlsx'
    return send_file(report.get_report_xlsx(data),
                     mimetype='application/vnd.ms-excel',
                     attachment_filename=file_name,
                     as_attachment=True)
