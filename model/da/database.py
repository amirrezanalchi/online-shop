from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from shop.model.entity import User, Store, Product, Order, OrderProduct
from shop.config import Config

class DatabaseManager:
    def __init__(self, database_url=None):
        if database_url is None:
            database_url = Config.SQLALCHEMY_DATABASE_URI
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
        self.create_tables()

    def create_tables(self):
        User.metadata.create_all(self.engine)
        Store.metadata.create_all(self.engine)
        Product.metadata.create_all(self.engine)
        Order.metadata.create_all(self.engine)
        OrderProduct.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()

    def add(self, instance):
        session = self.get_session()
        session.add(instance)
        session.commit()
        session.close()

    def query(self, model):
        session = self.get_session()
        result = session.query(model).all()
        session.close()
        return result

    def filter(self, model, **kwargs):
        session = self.get_session()
        result = session.query(model).filter_by(**kwargs).all()
        session.close()
        return result

    def delete(self, instance):
        session = self.get_session()
        session.delete(instance)
        session.commit()
        session.close()

    def update(self):
        session = self.get_session()
        session.commit()
        session.close()
