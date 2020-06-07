from flask import Flask,jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from datetime import datetime
from finance import config
from finance.domain import model
from finance.adapters import orm 
from finance.adapters import repository
from finance.servicelayer import services
from finance.servicelayer import unit_of_work
from decimal import Decimal

orm.start_mappers()
get_session = sessionmaker(bind= create_engine(config.get_mysql_uri()))
app = Flask(__name__)

@app.route("/remove", methods=['POST'])
def allocate_del_endpoint(): 
    session = get_session()
    repo = repository.OrderSqlArchemyAbstractRepository(session)
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
    try: 
        services.remove_order(orderUnit,repo,session)
    except Exception as e: 
        return jsonify({" Exception's detail is ": str(e)}),400

    return True


# Test Data.
# {	
# 	"order_id":"order55", 
# 	"order_item": "E2E", 
# 	"order_start_time":"2020-05-26 14:53:47",
# 	"order_end_time":"2020-05-26 14:53:47",
# 	"order_price":1000.00,
# 	"order_lot":0.10,
# 	"order_margin":1,
# 	"order_stoploss":0.00,
# 	"order_takeprofit":100.00
# }


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

@app.route("/add_batch", methods=['POST'])
def add_batch():
    batch_time = request.json['batch_time']
    if batch_time is not None:
        batch_time = datetime.fromisoformat(batch_time).date()
    services.add_batch(
        request.json['batch_id'], request.json['batch_oder_item'], request.json['batch_total_money'], batch_time,
        unit_of_work.SqlAlchemyUnitOfWork(),
    )
    return 'OK', 201

    
# # Test Data.
# {	
# 	"batch_id":"batch_68", 
# 	"batch_oder_item": "UOW", 
# 	"batch_total_money":"1999",
# 	"batch_time":"2020-06-07 14:53:47"
# }
