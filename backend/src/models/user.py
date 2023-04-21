
from datetime import datetime
import uuid
from . import db
# create user table
class User(db.Model):
    """ The User Model """
    __tablename__ = "users"

    id = db.Column(db.String(200), primary_key=True, default=str(uuid.uuid4()))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    role = db.Column(db.String(50))
    picture = db.Column(db.String(100))
    shared_opportunities = db.relationship('Opportunity', backref='user', lazy=True)
    
    def set_role(self, role):
        self.role = role