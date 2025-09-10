import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import logging

class DatabaseManager:
    def __init__(self):
        load_dotenv()
        self.engine = None
        self.connection = None
        self.host = os.getenv("DB_HOST")
        self.name = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.port = os.getenv("DB_PORT")
        self.password = os.getenv('DB_PASSWORD')
        self.coonection_string = f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


    def connect(self):
        """Set database connection"""
        try:
            self.engine = create_engine(self.coonection_string,
                                        echo=False, pool_size=5,
                                        max_overflow=10)
            self.connection = self.engine.connect()
            logging.info("Database connection established")
            return self.connection
        except Exception as e:
            logging.error("Database connection failed: %s", e)
            raise e


    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed")


    def execute_query(self, query:str, params=None):
        """Execute a query safely"""
        if not self.connection:
            self.connect()
        try:
            query_result = self.connection.execute(text(query), params or {})
            return query_result.all()
        except SQLAlchemyError as e:
            logging.error("Query execution failed: %s", e)
            raise e

if __name__ == "__main__":
    db = DatabaseManager()
    db.connect()
    print(db.execute_query("select 'hello db, I am working'"))
    db.disconnect()
 