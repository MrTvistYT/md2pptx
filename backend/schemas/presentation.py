from pydantic import BaseModel


class CreatePresentation(BaseModel):
    presentation_name: str
    content: str