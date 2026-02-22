from fastapi import FastAPI
from database import agent_collection, customer_collection, newspaper_collection, subsciption_collection # Custom file
from models import AgentCreate, CustomerCreate , AddNewspaper, SubscriptionCostumerwise# Custom file

from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId

app = FastAPI(title="PaperSetu API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "PaperSetu FastAPI running 🚀"}

@app.delete("/agents/{agent_id}")
def delete_agent(agent_id: str):
    result = agent_collection.delete_one(
        {"_id": ObjectId(agent_id)}
    )

    if result.deleted_count == 0:
        return {"message": "Agent not found"}

    return {"message": "Agent deleted successfully"}

@app.put("/agents/{agent_id}")
def update_agent(agent_id: str, agent: AgentCreate):
    result = agent_collection.update_one(
        {"_id": ObjectId(agent_id)},
        {"$set": agent.dict()}
    )

    if result.matched_count == 0:
        return {"message": "Agent not found"}

    return {"message": "Agent updated successfully"}

@app.get("/dashboard/agents_summary")
def dashboard_summary():
    total_agents = agent_collection.count_documents({})

    return {
        "total_agents": total_agents
    }

# Add an Agent
@app.post("/agents/register")
def register_agent(agent: AgentCreate):
    if agent_collection.find_one({"mobile": agent.mobile}):
        return {
            "success": False,
            "message": "Agent already exists"
        }

    agent_collection.insert_one(agent.dict())

    return {
        "success": True,
        "message": "Agent registered successfully"
    }

# ========================== END Add Agent ==========================

# View Agents List
@app.get("/agents")
def get_agents():
    agents = []
    for a in agent_collection.find():
        agents.append({
            "id": str(a["_id"]),
            "name": a["full_name"],
            "mobile": a["mobile"],
            "email": a["email"],
            "address": a["address"],
            "upi_id": a.get("upi_id", ""),      # ✅ ADD
            "aadhaar": a.get("aadhaar", ""),    # ✅ ADD
            "commType": a["commtype"],
            "commVal": a["commval"],
        })
    return agents
# Add customer 
@app.post("/customer/register")
def register_customer(customer: CustomerCreate):
    if customer_collection.find_one({"mobile": customer.mobile}):
        return {
            "success": False,
            "message": "Customer already exists"
        }

    customer_collection.insert_one(customer.dict())

    return {
        "success": True,
        "message": "Customer registered successfully"
    }
# View customer list 
@app.get("/customer")
def get_customer():
    customer = []
    for a in customer_collection.find():
        customer.append({
            "id": str(a["_id"]),
            "name": a["full_name"],
            "mobile": a["mobile"],
            "email": a["email"],
            "address": a["address"],
            "News_name": a.get("News_name", ""),      # ✅ ADD
            "Del_date": a.get("Del_date", ""),      # ✅ ADD
            
        })
    return customer

# Operations of costumer

@app.delete("/customer/{customer_id}")
def delete_customer(customer_id: str):
    result = customer_collection.delete_one(
        {"_id": ObjectId(customer_id)}
    )

    if result.deleted_count == 0:
        return {"message": "Customer not found"}

    return {"message": "Customer deleted successfully"}

@app.put("/customer/{customer_id}")
def update_customer(customer_id: str, customer: CustomerCreate):
    result = customer_collection.update_one(
        {"_id": ObjectId(customer_id)},
        {"$set": customer.dict()}
    )

    if result.matched_count == 0:
        return {"message": "Customer not found"}

    return {"message": "Customer updated successfully"}

@app.get("/dashboard/customers_summary")
def dashboard_summary():
    total_customers = customer_collection.count_documents({})

    return {
        "total_customers": total_customers
    }
    
# Add newspaper 
@app.post("/newspapers/add")
def add_newspaper(newspaper: AddNewspaper):
    if newspaper_collection.find_one({"news_name": newspaper.news_name}):
        return {
            "success": False,
            "message": "Newspaper already exists"
        }

    newspaper_collection.insert_one(newspaper.dict())

    return {
        "success": True,
        "message": "Newspaper added successfully"
    }
# View newspaper list
@app.get("/newspapers")
def get_newspapers():
    newspapers = []
    for a in newspaper_collection.find():
        newspapers.append({
            "id": str(a["_id"]),
            "news_name": a["news_name"],
            "price": a["price"],
            "status": a["status"]
        })
    return newspapers
# Newspaper edit / delete

@app.delete("/newspaper/{newspaper_id}")
def delete_newspaper(newspaper_id: str):
    result = newspaper_collection.delete_one(
        {"_id": ObjectId(newspaper_id)}
    )

    if result.deleted_count == 0:
        return {"message": "Newspaper not found"}

    return {"message": "Newspaper deleted successfully"}

@app.put("/newspaper/{newspaper_id}")
def update_newspaper(newspaper_id: str, newspaper: AddNewspaper):
    result = newspaper_collection.update_one(
        {"_id": ObjectId(newspaper_id)},
        {"$set": newspaper.dict()}
    )

    if result.matched_count == 0:
        return {"message": "Newspaper not found"}

    return {"message": "Newspaper updated successfully"}

@app.get("/dashboard/newspapers_summary")
def dashboard_summary():
    total_newspapers = newspaper_collection.count_documents({})

    return {
        "total_newspapers": total_newspapers
    }

# Add subscription for customer
@app.post("/subscription/add")
def add_subscription(subscription: SubscriptionCostumerwise):
    if subsciption_collection.find_one({"customer_id": subscription.customer_id, "newspaper_id": subscription.newspaper_id}):
        return {
            "success": False,
            "message": "Subsciption already exists"
        }

    subsciption_collection.insert_one(subscription.dict())

    return {
        "success": True,
        "message": "Subscription added successfully"
    }
# view subscription list
@app.get("/subscription")
def get_subscriptions():
    subscriptions = []
    for a in subsciption_collection.find():
        subscriptions.append({
            "id": str(a["_id"]),
            "customer_id": a["customer_id"],
            "newspaper_id": a["newspaper_id"],
            "agent_id": a["agent_id"],
            "start_date": a["start_date"],
            "price_type": a["price_type"],
            "price": a["price"],
        })
    return subscriptions
