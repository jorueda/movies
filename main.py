from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from utils import clean_no_release_date, get_director, clean_related_movies_data
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Montar la carpeta static
app.mount("/static", StaticFiles(directory="static"), name="static")

API_KEY = os.environ.get('API_KEY')
# https://developer.themoviedb.org/reference/intro/authentication
suffix = f"api_key={API_KEY}&language=es-mx"


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/search")
async def search_movie(request: Request, query: str = "", page: int = 1):
    # https://developer.themoviedb.org/reference/search-movie
    url = f"https://api.themoviedb.org/3/search/movie?{
        suffix}&query={query}&page={page}"
    response = requests.get(url)
    data = response.json()
    # Clean no release date
    data = clean_no_release_date(data)

    return templates.TemplateResponse(
        "results.html",
        {
            "request": request,
            "movies": data["results"],
            "query": query,
            "page": page
        }
    )


@app.get("/cast/{movie_id}", response_class=HTMLResponse)
async def cast(request: Request, movie_id: int, title: str):
    # https://developer.themoviedb.org/reference/movie-credits
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?{suffix}"
    response = requests.get(url)
    data = response.json()

    return templates.TemplateResponse("cast.html",
                                      {
                                          "request": request,
                                          "persons": data["cast"],
                                          "title": title
                                      }
                                      )


@app.get("/director/{movie_id}", response_class=HTMLResponse)
async def director(request: Request, movie_id: int, title: str):
    # https://developer.themoviedb.org/reference/movie-credits
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?{suffix}"
    response = requests.get(url)
    data = response.json()

    director = get_director(data)

    return templates.TemplateResponse("director.html",
                                      {
                                          "request": request,
                                          "directors": director,
                                          "title": title
                                      }
                                      )


@app.get("/related-movies/{person_id}")
async def related_movies(request: Request, person_id: int, name: str):
    # https://developer.themoviedb.org/reference/person-movie-credits
    url = f"https://api.themoviedb.org/3/person/{
        person_id}/movie_credits?{suffix}"
    response = requests.get(url)
    data = response.json()
    # Clean from empty character or job
    data = clean_related_movies_data(data)

    return templates.TemplateResponse(
        "related-movies.html",
        {
            "request": request,
            "movies": data,
            "name": name
        }
    )
