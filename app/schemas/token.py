from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class TokenPayload(BaseModel):
    access_token: str
    token_type: str

