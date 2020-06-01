from flask import Flask,jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import datetime,decimal
import config
import model
import orm 
import repository
import services

orm.start_mappers()
get_session = sessionmaker(bind= create_engine(config.get_mysql_uri()))
app = Flask(__name__)

@app.route("/allocate", methods=['POST'])
def allocate_endpoint(): 
    session = get_session()
    repo = repository.BatchSqlArchemyAbstractRepository(session)
    orderUnit = model.OrderUnit("order77", "E2E", 
                        datetime(2020,5, 26, 14, 53, 46),
                        datetime(2020, 5, 26, 14, 53, 46),
                        1000,
                        decimal.Decimal("0.10"),
                        1,
                        decimal.Decimal("0.00"),
                        decimal.Decimal("100.00")
    )
    try: batchId = services.allocate(orderUnit,repo,session)
    except : 
        return jsonify({'message': str('Fail on endpoint')}), 400

    return jsonify({'batchId is ': batchId}), 201




@app.route("/", methods=['GET'])
def index(): 
    return "Hello, Flask"
