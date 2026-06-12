from pydantic import BaseModel

class DocumentResponse(BaseModel):

    id: int 

    tenant_id: int 

    title: str 

    file_path: str 

    status: str 

    class Config:

        from_attributes = True