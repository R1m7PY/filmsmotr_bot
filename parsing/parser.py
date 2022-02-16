import json
import requests
from bs4 import BeautifulSoup
import lxml
from .config import headers, url_films


async def connect(url, headers) -> BeautifulSoup|bool:
    try:
        req = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(req.text, "lxml")
        return soup
    except:
        return False

async def parsing_films():
    films_info = []
    for page in range(1, 69+1):
        # print(f"{page}/69 page parsing...")
        url = url_films + f"page/{page}"
        page_film = await connect(url, headers)
        if page_film != False:
            films = page_film.find("div", {"id": "allEntries"}).find_all("a")
            for film in films:
                film_url = film.get("href")
                film_title = str(film.find("div", class_="vid-t").text)
                film_search_title = film_title.lower()
                film_description = film.find("div", class_="vid-mes").text
                films_info.append(
                    {
                        "URL": film_url,
                        "Title": film_title,
                        "Search title": film_search_title,
                        "Description": film_description
                    }
                )
        else:
            print("connect error")
    with open("parsing/films.json", "w", encoding="utf-8") as file:
        json.dump(films_info, file, indent=4, ensure_ascii=False)


async def search_film(search: str) -> list|bool:
    with open("parsing/films.json", "r", encoding="utf-8") as file:
        films = json.load(file)
        answer = []
        for film in films:
            if search in film["Search title"]:
                answer.append(film)
        if len(answer) != 0:
            return answer
        else:
            return False
