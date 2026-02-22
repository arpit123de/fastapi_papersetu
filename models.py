from ast import List
from pydantic import BaseModel, EmailStr

class AgentCreate(BaseModel):
    # agent_id :str
    full_name: str
    mobile: str
    email: EmailStr
    address: str
    upi_id: str
    aadhaar: str
    commtype: str
    commval: float
    status: int
# Add Customer
class CustomerCreate(BaseModel):
    # customer_id : str
    full_name: str
    mobile: str
    email: EmailStr
    address: str
    # News_name: str
    # Del_date: str
    agent_id: str
    status : int

# Master Newspaper
class AddNewspaper(BaseModel):
    # newspaper_id: str
    news_name: str
    price: float
    status : int
    
# master subs
# class SubscriptionItem(BaseModel):
#     subscription_id: str
#     newspaper_id: str
# Subs for Customer
class SubscriptionCostumerwise(BaseModel):
    # subscription_id: str
    customer_id: str
    newspaper_name: str
    agent_id: str
    start_date: str
    price_type: str
    price: float
    status:int
    
    # newspapers: List[SubscriptionItem]