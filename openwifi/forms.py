
from wtforms import Form, TextField, IntegerField

class AccessPointAddForm(Form):
    name = TextField('name')
    hardware = TextField('hardware')
    address = TextField('address')
    radios_2g = IntegerField('2ghz Radios')
    radios_5g = IntegerField('5ghz Radios')

class AccessPointEditForm(Form):
    name = TextField('name')
    hardware = TextField('hardware')
    address = TextField('address')
    sshkey = TextField('sshkey') # private key to access this ap
    sshhostkey = TextField('sshhostkey') # remote host key

class OpenWrtEditForm(Form):
    name = TextField('name')
    address = TextField('address')
    distribution = TextField('distrubtion')
    version = TextField('version') # private key to access this ap
    uuid = TextField('uuid') # remote host key
    configured = TextField('configured')
    login = TextField('login')
    password = TextField('password')
    configuration = TextField('configuration')
