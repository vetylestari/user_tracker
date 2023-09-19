from typing import Union
import decouple 
import psycopg2
from user_agents import parse
from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, ORJSONResponse
from src import tool as src_tool
from sqlalchemy.orm import Session
from fastapi import FastAPI, Request, Depends
from model.database import UserResponse, SessionLocal

tags_metadata = [
    {"name": "Internal Tools", "description": "One other way around"}
]

middleware = [
    Middleware(
        CORSMiddleware
        , allow_origins=['*']
        , allow_headers=['application/json']
        , allow_methods=['*']
    )
]

app = FastAPI(
    openapi_tags=tags_metadata
    , middleware=middleware
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/user")
def read_user(request: Request, db: Session = Depends(get_db)):
    user_agent = request.headers['user-agent']
    user_agent_parsed = parse(user_agent)
    return {
        # 'headers-unparsed': request.headers,  
        'headers': {
            'host': request.headers['host']
            ,'user-agent': user_agent
            ,'client-host': request.client.host
            ,'client-port': request.client.port
            ,'client-browser': f"{user_agent_parsed.browser.family} {user_agent_parsed.browser.version_string}"
            ,'client-os': f"{user_agent_parsed.os.family} {user_agent_parsed.os.version_string}"
            ,'client-device': f"{user_agent_parsed.device.family} {user_agent_parsed.device.model}"
            ,'is-bot': user_agent_parsed.is_bot
            ,'is-email-client': user_agent_parsed.is_email_client
            ,'is-mobile': user_agent_parsed.is_mobile
            ,'is-pc': user_agent_parsed.is_pc
            ,'is-tablet': user_agent_parsed.is_tablet
            ,'is-touch-capable': user_agent_parsed.is_touch_capable
        }, 
        'body': decouple.config('CUSTOMUSER')
    }
    
    user_response = UserResponse(**response_data)
    
    # Add the UserResponse instance to the database session and commit it
    db.add(user_response)
    db.commit()
    return response_data