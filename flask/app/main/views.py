from flask import render_template
from flask_login import login_required
from . import main
from .forms import CustomersForm, CarsForm
from .. import db
from ..models import Car, Color, Customer, Model, User

@main.route("/", methods=["GET", "POST"])
def index():
    
    db.create_all()
    
    user_query = db.session.query(User).first()
    if user_query is None:
        user = User(username="admin", password="qiskit")
        db.session.add(user)
        db.session.commit()
    
    color_query = db.session.query(Color).first()
    if color_query is None:
        colors_list = ["blue", "gray", "yellow"]
        for color in colors_list:
            car_color = Color(color=color)
            db.session.add(car_color)
            db.session.commit()
        
    model_query = db.session.query(Model).first()
    if model_query is None:
        models_list = ["convertible", "hatch", "sedan"]
        for model in models_list:
            car_model = Model(model=model)
            db.session.add(car_model)
            db.session.commit()
    
    return render_template("index.html")

@main.route("/customer_registration", methods=["GET", "POST"])
@login_required
def customer_registration():
    
    message = ''
    form = CustomersForm()
    
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        
        query_customer = db.session.query(Customer).filter_by(name=name).first()
        if query_customer is None:
            customer = Customer(name=name, status="opportunity")
            db.session.add(customer)
            db.session.commit()
            message = f"The customer whose name is {name} has been registered with success!"
        else:
            message = "This customer already exists in the database!"
        
    return render_template("customer_registration.html", form=form, message=message)

@main.route("/car_registration", methods=["GET", "POST"])
@login_required
def car_registration():
    
    message = ''
    error_message = ''
    form = CarsForm()
        
    if form.validate_on_submit():
        
        customer_name = form.customer.data
        color = form.color.data
        model = form.model.data
        
        customer = db.session.query(Customer).filter_by(name=customer_name).first()
        if customer is None:
            error_message = f"The person called {customer_name} is not in the database!"
        else:
            customer_id = customer.id
            customer_number_of_cars = db.session.query(Car).filter_by(customer_id=customer_id).count()
        
            if customer_number_of_cars < 3:
                
                query_customer = db.session.query(Customer).filter_by(name=customer_name).first()
                query_customer.status = "already has a car"
                db.session.add(query_customer)
                
                car_color = db.session.query(Color).filter_by(color=color).first()
                color_id = car_color.id
                car_model = db.session.query(Model).filter_by(model=model).first()
                model_id = car_model.id
                car = Car(customer_id=customer_id, color_id=color_id, model_id=model_id)
                db.session.add(car)
                db.session.commit()
                
                message = f"A {car_color.color} car of the model {car_model.model}, that belongs to {customer.name}, has been registered with success!"
            else:
                error_message = f"The customer {customer.name} can't buy another car due city rules! (already has 3 cars)"
    
    return render_template("car_registration.html", form=form, message=message, error_message=error_message)
