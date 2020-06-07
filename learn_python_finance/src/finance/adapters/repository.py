import abc 
from finance.domain import model

# define command maker class that auto generate command follow object model
class ICommandExecuter(abc.ABC):
    pass

# repositories abstract class.
class ISqlArchemyAbstractRepository(abc.ABC):
    
    @abc.abstractmethod
    def add(self, obj):
        raise NotImplementedError("Subclass will implement this method")

    @abc.abstractmethod
    def getAll(self,obj):
        raise NotImplementedError("Subclass will implement this method")
    
    # @abc.abstractmethod
    # def getById(self, ModelName):
    #     raise NotImplementedError("Subclass will implement this method")
    
    # @abc.abstractmethod
    # def delAll(self, obj):
    #     raise NotImplementedError("Subclass will implement this method")
    
    # @abc.abstractmethod
    # def delById(self, ModelName):
    #     raise NotImplementedError("Subclass will implement this method")
    
class SqlArchemyAbstractRepository(ISqlArchemyAbstractRepository):
    def __init__(self,session): 
        self.session = session

    def add(self,obj):
        self.session.add(obj)

    def getAll(self,ModelName):
        return self.session.query(ModelName).all()
    

class BatchSqlArchemyAbstractRepository(SqlArchemyAbstractRepository):
    def __init__(self, session):
        self.session = session
    
    def get(self, batch_id):
        return self.session.query(model.Batch).filter_by(batch_id=batch_id).one()

    def delele(self,batch: model.Batch):
        return self.session.delete(batch)

    def list(self):
        return self.session.query(model.Batch).all()


class OrderSqlArchemyAbstractRepository(SqlArchemyAbstractRepository):
    def __init__(self, session):
        self.session = session
    
    def get(self, order_id):
        return self.session.query(model.OrderUnit).filter_by(order_id=order_id).one()

    def delele(self,orderItem: model.OrderUnit):
        deleteItem = self.get(orderItem.order_id)
        return self.session.delete(deleteItem)

    def list(self):
        return self.session.query(model.OrderUnit).all()