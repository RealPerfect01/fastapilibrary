from fastapi import FastAPI
from database import Base, engine
from routers import books, users, loans, dashboard, auth
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles



Base.metadata.create_all(bind=engine)


app = FastAPI(title="Library Management API (Secure)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify frontend origins like ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(loans.router, prefix="/loans", tags=["Loans"])

port = int(os.environ.get("PORT", 8000))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
