from pydantic import BaseModel, ConfigDict, Field

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100, example="My First Post")
    content: str = Field(min_length=1, example="My First Post")
    author: str = Field(min_length=1, max_length=50, example="John Doe")

class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str

    
