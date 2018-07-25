from .errors import *
from flask import jsonify
from app import db
from . import api, get_query_string
from app.main.models import *


# contact information ####################################################
@api.route('/contacts', methods=['GET'])
def get_contacts():
    return jsonify([
        p.to_json() for p in
        Person.query.filter_by(**get_query_string(Person)).all()]), 200


@api.route('/contacts', methods=['POST'])
def create_contact():
    json_contact = request.json
    person = Person.from_json(json_contact)
    phones = json_contact.get('Phones')
    emails = json_contact.get('Emails')
    addresses = json_contact.get('Addresses')
    if phones is not None:
        for phone in phones:
            phone['PersonOid'] = person.Oid
            f = Phone.from_json(phone)
            db.session.add(f)
    if emails is not None:
        for email in emails:
            email['PersonOid'] = person.Oid
            e = Email.from_json(email)
            db.session.add(e)
    if addresses is not None:
        for address in addresses:
            address['PersonOid'] = person.Oid
            a = Address.from_json(address)
            db.session.add(a)
    db.session.add(person)
    db.session.commit()
    return jsonify(person.to_json()), 201


@api.route('/contacts/<string:Oid>', methods=['GET'])
def get_contact(Oid):
    contact = Person.query.filter_by(Oid=Oid).first_or_404()
    return jsonify(contact.to_json()), 200


@api.route('/contacts/<string:Oid>', methods=['DELETE'])
def delete_contact(Oid):
    contact = Person.query.filter_by(Oid=Oid).first_or_404()
    res = contact.to_json()
    for phone in contact.Phones.all():
        db.session.delete(phone)
    for email in contact.Emails.all():
        db.session.delete(email)
    for address in contact.Addresses.all():
        db.session.delete(address)
    db.session.delete(contact)
    db.session.commit()
    return jsonify(res), 200, {'Status': 'Deleted'}
