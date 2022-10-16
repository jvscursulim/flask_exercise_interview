import unittest
from app import create_app, db
from app.models import Car, Color, Customer, Model

class TestModels(unittest.TestCase):
    
    def setUp(self) -> None:
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_color_db(self) -> None:
        color_list = ["blue", "gray", "yellow"]
        for color in color_list:
            car_color = Color(color=color)
            db.session.add(car_color)
        db.session.commit()
        
        self.assertFalse(db.session.query(Color).all() is None)
    
    def test_model_db(self) -> None:
        model_list = ["convertible", "hatch", "sedan"]
        for model in model_list:
            car_model = Model(model=model)
            db.session.add(car_model)
        db.session.commit()
        
        self.assertFalse(db.session.query(Model).all() is None)
    
    def test_customer_db(self) -> None:
        status = "opportunity"
        name_list = ["Alice", "Bob", "Charlie"]
        for name in name_list:
            customer = Customer(name=name, status=status)
            db.session.add(customer)
        db.session.commit()
        
        self.assertFalse(db.session.query(Customer).all() is None)
        
    def test_car_db(self) -> None:
        customer_name = "Alice"
        status = "opportunity"
        customer = Customer(name=customer_name, status=status)
        db.session.add(customer)
        customer = db.session.query(Customer).filter_by(name=customer_name).first()
        customer_id = customer.id
        model_list = ["convertible", "hatch", "sedan"]
        for model in model_list:
            car_model = Model(model=model)
            db.session.add(car_model)
        color_list = ["blue", "gray", "yellow"]
        for color in color_list:
            car_color = Color(color=color)
            db.session.add(car_color)
        for tp in zip(model_list, color_list):
            car_color = db.session.query(Color).filter_by(color=tp[1]).first()
            color_id = car_color.id
            car_model = db.session.query(Model).filter_by(model=tp[0]).first()
            model_id = car_model.id
            car = Car(customer_id=customer_id, color_id=color_id, model_id=model_id)
            db.session.add(car)
            db.session.commit()
            
        self.assertFalse(db.session.query(Car).all() is None)
        