from pydantic import BaseModel

class Followers(BaseModel):
    id: int
    user_id: int
    follower_id: int

    class Config:
        from_attributes = True


