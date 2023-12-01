import uvicorn
from fastapi import FastAPI,APIRouter
from fastapi.responses import RedirectResponse
from app.api.router import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_root():
    """
    The API root, redirects to docs.

    :returns: Redirection to the redoc page.
    """
    return RedirectResponse(url="docs/")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
