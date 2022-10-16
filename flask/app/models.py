from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from . import login_manager

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    
    @property
    def password(self):
        raise AttributeError("password is a not a readable attribute")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password=password)

class Customer(db.Model):
    
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    status = db.Column(db.String(17))
    cars = db.relationship("Car", backref="customer")
   
class Color(db.Model):
    
    __tablename__ = "colors"
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(6), unique=True)
    cars = db.relationship("Car", backref="color")
    
class Model(db.Model):
    
    __tablename__ = "car_models"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(11), unique=True)
    cars = db.relationship("Car", backref="model")
    
class Car(db.Model):
    
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    color_id = db.Column(db.Integer, db.ForeignKey("colors.id"))
    model_id = db.Column(db.Integer, db.ForeignKey("car_models.id"))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))