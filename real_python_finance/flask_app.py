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
# print(config.get_mysql_uri())

@app.route("/allocate", methods=['POST'])
def allocate_endpoint(): 
    session = get_session()
    repo = repository.BatchSqlArchemyAbstractRepository(session)
    orderUnit = model.OrderUnit(
        request.json["order_id"],
        request.json["order_item"], 
        request.json["order_start_time"], 
        request.json["order_end_time"], 
        request.json["order_price"], 
        request.json["order_lot"], 
        request.json["order_margin"], 
        request.json["order_stoploss"],  
        request.json["order_takeprofit"]
    )
    # batches = repo.list()
    # batch = batches[0]
    try: 
        batchId = services.allocate(orderUnit,repo,session)
        # batchId = services.allocate_and_save_order_unit(orderUnit,repo,session)
    except Exception as e: 
        # return jsonify({"OrderUnit":orderUnit}),201 #,
        # return jsonify({"batch":batch}),201 #,
        return jsonify({'message': str(e)}), 400

    return jsonify({'batchId is ': batchId}), 201

@app.route("/", methods=['GET'])
def index(): 
    return "Go to chapter 4 / repository and service."
    # return str(get_session)
