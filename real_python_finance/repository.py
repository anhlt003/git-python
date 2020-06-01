import abc 
import model 

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

    def list(self):
        return self.session.query(model.Batch).all()