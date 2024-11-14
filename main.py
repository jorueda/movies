from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY = ""
# https://developer.themoviedb.org/reference/intro/authentication
suffix = f"api_key={API_KEY}&language=es-es"


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

    # Formatear los resultados
    results = [
        {
            "id": item["id"],
            "title": item["title"],
            "original_title": item["original_title"],
            "release_date": item["release_date"]
        }
        for item in data['results']
        if item["release_date"]
    ]

    return templates.TemplateResponse(
        "results.html",
        {
            "request": request,
            "items": results,
            "query": query,
            "page": page
        }
    )


@app.get("/cast/{movie_id}", response_class=HTMLResponse)
async def get_cast(request: Request, movie_id: int, title: str):
    # https://developer.themoviedb.org/reference/movie-credits
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?{suffix}"
    response = requests.get(url)
    data = response.json()
    cast = [
        {
            "id": item["id"],
            "character": item["character"],
            "name": item["name"]
        }
        for item in data["cast"]
    ]

    return templates.TemplateResponse("cast.html",
                                      {
                                          "request": request,
                                          "items": cast,
                                          "title": title
                                      }
                                      )


@app.get("/director/{movie_id}", response_class=HTMLResponse)
async def get_director(request: Request, movie_id: int, title: str):
    # https://developer.themoviedb.org/reference/movie-credits
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?{suffix}"
    response = requests.get(url)
    data = response.json()
    director = [
        {
            "id": item["id"],
            "name": item["name"]
        }
        for item in data["crew"]
        if item["job"] == "Director"
    ]

    return templates.TemplateResponse("director.html",
                                      {
                                          "request": request,
                                          "items": director,
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

    cast = [
        {
            "id": item["id"],
            "title": item["title"],
            "original_title": item["original_title"],
            "release_date": item["release_date"]
        }
        for item in data["cast"]
        if item["release_date"]
    ]
    crew = [
        {
            "id": item["id"],
            "title": item["title"],
            "original_title": item["original_title"],
            "release_date": item["release_date"]
        }
        for item in data["crew"]
        if item["release_date"] and item["job"] == "Director"
    ]

    results = cast + crew
    return templates.TemplateResponse(
        "related-movies.html",
        {
            "request": request,
            "items": results,
            "name": name
        }
    )
