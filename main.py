from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY = ""


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/search")
async def search_movie(query: str, request: Request):
    # https://www.themoviedb.org/
    url = f"https://api.themoviedb.org/3/search/movie?query={
        query}&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    movies = [{key: value for key, value in item.items()
               if key in ["id", "original_title", "title", "release_date"]}
              for item in data["results"]]

    # return data
    return templates.TemplateResponse("movie_list.html",
                                      {"request": request, "items": movies})


@app.get("/item/{movie_id}", response_class=HTMLResponse)
async def get_item(movie_id: int, request: Request):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}"
    response = requests.get(url)
    data2 = response.json()
    cast = [{key: value for key, value in item.items()
                     if key in ["name", "character"]}
                    for item in data2["cast"]]

    return templates.TemplateResponse("cast.html", 
                                      {"request": request, "items": cast})
