from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import StreamingResponse

from schemas.presentation import CreatePresentation
from engine.pptx_engine import PresentationGenerator
import uvicorn
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to md2pptx converter!"}

@app.post("/generate")
async def generate(presentation: CreatePresentation):
    presentation_generator = PresentationGenerator(presentation.content)
    presentation_generator.unparse()

    new_presentation = presentation_generator.export()
    return StreamingResponse(
        new_presentation,
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        headers={"Content-Disposition": f"attachment; filename={presentation.presentation_name}.pptx"}
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=5627,
        reload=True
    )