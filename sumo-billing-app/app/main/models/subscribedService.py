from datetime import datetime
import uuid
from ... import db
from app.exceptions import ValidationError
from flask import url_for




class SubscribedService(db.Model):
    __tablename__ = 'subscribedservice'
    Oid = db.Column(db.String(38), primary_key=True, index=True)
    ServiceName = db.Column(db.String(64))
    TraderOid = db.Column(db.String(38), db.ForeignKey('trader.Oid'))
    #trader backref defined in Trader class
    VendorShortcut = db.Column(db.String(16), db.ForeignKey('vendor.Shortcut'), index=True)

    #vendor backref defined in Vendor class
    GSECCode = db.Column(db.String(38), db.ForeignKey('gseccode.Code'), index=True)
    GSECCodeObj = db.relationship('GSECCode')
    StartDate = db.Column(db.DateTime)
    EndDate = db.Column(db.DateTime)
    Created = db.Column(db.DateTime)
    CreatedBy = db.Column(db.String(38))

    def __init__(self, ServiceName, TraderOid, VendorShortcut, GSECCode, StartDate=None, EndDate=None):
        self.Oid = str(uuid.uuid4())
        self.ServiceName = ServiceName
        self.TraderOid = TraderOid
        self.VendorShortcut = VendorShortcut
        self.GSECCode = GSECCode
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.Created = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")


    def update(self, sub_json):
        ServiceName = sub_json.get('ServiceName')
        TraderOid = sub_json.get('TraderOid')
        VendorShortcut = sub_json.get('VendorShortcut')
        GSECCode = sub_json.get('GSECCode')
        StartDate = sub_json.get('StartDate')
        EndDate = sub_json.get('EndDate')

        if ServiceName is not None:
            self.ServiceName = ServiceName
        if TraderOid is not None:
            self.TraderOid = TraderOid
        if VendorShortcut is not None:
            self.VendorShortcut = VendorShortcut
        if GSECCodeOid is not None:
            self.GSECCode = GSECCode
        if StartDate is not None:
            self.StartDate = StartDate
        if EndDate is not None:
            self.EndDate = EndDate
        



    def to_json(self):

        sub_json = {
        'Oid' : self.Oid,
        'ServiceName' : self.ServiceName,
        'TraderOid' : self.TraderOid,
        'VendorShortcut' :self.VendorShortcut,
        'GSECCode' : self.GSECCode,
        'StartDate' : self.StartDate,
        'EndDate' : self.EndDate,
        'Created' : self.Created
        }

        return sub_json

    @staticmethod
    def from_json(json_sub):
        TraderOid = json_sub.get('TraderOid')
        if TraderOid is None or TraderOid is "":
            raise ValidationError("Trader Not Found")
        Vendor = json_sub.get('VendorShortcut')
        if Vendor is None or Vendor is "":
            raise ValidationError("Vendor Not Found")
        GSECCode = json_sub.get('GSECCodeOid')
        if GSECCode is None or GSECCode is "":
            raise ValidationError("GSEC Code Not Found")
        ServiceName = json_sub.get('ServiceName')
        StartDate = json_sub.get('StartDate')
        EndDate = json_sub.get('EndDate')

        return SubscribedService(ServiceName, TraderOid, Vendor, GSECCode, StartDate, EndDate)

        