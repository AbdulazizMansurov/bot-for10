from bs4 import BeautifulSoup
import requests

class Marvel_News():
    def show_marvel_new(self):
        req = requests.get("https://pluggedin.ru/keywords/Marvel").text
        soup = BeautifulSoup(req, "html.parser")
        last_news = soup.find("li", style="margin-bottom: 15px")
        name = last_news.find("a", class_="search_title").get_text()
        link = "pluggedin.ru" + last_news.find("a").get("href")
        new = {
            "name": name,
            "link": link,
            "set": "pluggedin.ru"
        }
        return new

class Anime_parser():
    def show_anime_new(self):
        req = requests.get("https://kg-portal.ru/news/anime/").text
        soup = BeautifulSoup(req, "html.parser")
        all = soup.find("div", class_="news_box anime_cat")
        all_too = all.find_all("a")[1]
        text = all_too.get_text()
        link = "kg-portal.ru" + (all_too.get("href"))
        new = {
            "name": text,
            "link": link,
            "set": "kg-portal.ru"
        }
        return new

class Genshin_parser():
    def show_genshin_new(self):
        req = requests.get("https://www.goha.ru/games/genshin-impact/news").text
        soup = BeautifulSoup(req, "html.parser")
        all = soup.find("div", class_="component-article-tile")
        text = all.find("div", class_="shortly").get_text()
        link = all.find("div", class_="title")
        link = link.find("a").get("href")
        new = {
            "name": text,
            "link": link,
            "set": "kg-portal.ru"
        }
        return new
