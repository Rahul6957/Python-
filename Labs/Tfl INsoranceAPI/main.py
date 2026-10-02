from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

with open("list.json", "r") as file:
   policies = json.load(file)

# ----------------------------------
# 1. Create FastAPI Application
# ----------------------------------

app = FastAPI( title="TFLInsurance API", description="Simple Insurance Policy Management REST API", version="1.0")

# ----------------------------------
# 2. Define Policy Model
# ----------------------------------

class Policy(BaseModel):
    name: str
    description: str
    maturity: str
    premium: float

# ----------------------------------
# 4. Helper Function
# ----------------------------------

def find_policy(policy_id: int):
    for policy in policies:
        if policy["id"] == policy_id:
            return policy

    return None


# ----------------------------------
# 5. READ - Get All Policies
# HTTP GET
# ----------------------------------

@app.get("/api/get_all_policies")
def get_all_policies():
    return {
        "message": "Policies retrieved successfully",
        "count": len(policies),
        "data": policies
    }


# ----------------------------------
# 6. READ - Get Policy By ID
# HTTP GET
# ----------------------------------

@app.get("/api/get_all_policies_byid/{policy_id}")
def get_policy(policy_id: int):
    policy = find_policy(policy_id)
    if policy is None:
        raise HTTPException( status_code=404, detail="Policy not found" )
    return policy


# ----------------------------------
# 7. CREATE - Add New Policy
# HTTP POST
# ----------------------------------

@app.post("/api/add_policies", status_code=201)
def create_policy(policy: Policy):
    new_id = max((p["id"] for p in policies), default=0) + 1
    new_policy = {
        "id": new_id,
        **policy.model_dump()
    }

    policies.append(new_policy)

    return {
        "message": "Policy created successfully",
        "data": new_policy
    }


# ----------------------------------
# 8. UPDATE - Modify Existing Policy
# HTTP PUT
# ----------------------------------

@app.put("/api/policies/{policy_id}")
def update_policy(policy_id: int, updated_policy: Policy):
    policy = find_policy(policy_id)
    if policy is None:
        raise HTTPException( status_code=404, detail="Policy not found" )
    policy.update(updated_policy.model_dump())
    return {
        "message": "Policy updated successfully",
        "data": policy
    }


# ----------------------------------
# 9. DELETE - Remove Policy
# HTTP DELETE
# ----------------------------------

@app.delete("/api/policies/{policy_id}")
def delete_policy(policy_id: int):
    policy = find_policy(policy_id)
    if policy is None:
        raise HTTPException( status_code=404, detail="Policy not found" )
    policies.remove(policy)
    return {
        "message": "Policy deleted successfully",
        "deleted_policy": policy
    }


# ----------------------------------
# 10. Root Endpoint
# ----------------------------------

@app.get("/")
def home():
    return {
        "application": "TFLInsurance",
        "message": "Welcome to TFLInsurance REST API",
        "docs": "/docs"
    }