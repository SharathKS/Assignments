import psycopg2
import logging


class GetPGConnection:
    def __init__(self):
        print("Initializing Connection to Postgres")

    def get_pg_connection(self):
        """Establish Connection PostGres"""
        try:
            connection = psycopg2.connect(user="docker",
                                          password="docker",
                                          host="127.0.0.1",
                                          port="5434",
                                          database="docker")
            return connection
        except():
            logging.error("Postgres connection error")