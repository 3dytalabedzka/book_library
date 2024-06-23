from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_books(request: Request, db: Session = Depends(get_db)):
    books = crud.get_books(db)
    return templates.TemplateResponse("books.html", {"request": request, "books": books})

@app.post("/books/")
def create_book(title: str = Form(...), author: str = Form(...), year: int = Form(...), genre: str = Form(...), db: Session = Depends(get_db)):
    book = schemas.BookCreate(title=title, author=author, year=year, genre=genre)
    crud.create_book(db=db, book=book)
    return RedirectResponse(url="/", status_code=303)

@app.post("/books/update/{book_id}")
def update_book(book_id: int, title: str = Form(...), author: str = Form(...), year: int = Form(...), genre: str = Form(...), db: Session = Depends(get_db)):
    book = schemas.BookCreate(title=title, author=author, year=year, genre=genre)
    crud.update_book(db=db, book_id=book_id, book=book)
    return RedirectResponse(url="/", status_code=303)

@app.post("/books/delete/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    crud.delete_book(db=db, book_id=book_id)
    return RedirectResponse(url="/", status_code=303)
