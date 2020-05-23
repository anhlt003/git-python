@dataclass(frozen = True)
class OrderLine: 
    orderid: str
    sku: str
    qty:int

class Batch: 
    def __init__(self, ref:str,sku:str,qty:int,eto:Optional[date]):
        self.reference = ref
        self.sku = sku
        self.eta = enumerate
        self.available_quantity = qty

    def allocate(self,line:OrderLine):
        self.available_quantity -= line.qty

