from bs4 import BeautifulSoup
import requests

class Marvel_News():
    def show_marvel_new(self):
        req = requests.get("https://pluggedin.ru/keywords/Marvel").text
        soup = BeautifulSoup(req, "html.parser")
        last_news = soup.find("li", style="margin-bottom: 15px")
        # print(last_news)
        link_1 = str(last_news.find("a", href=str)).split(" ")
        name = (last_news.find("a", href=str)).get_text()
        link = link_1[2].split("=")[1].split(">")[0].split("/")
        linker = f"https://pluggedin.ru/keywords/Marvel/open{link[1]}/{link[2]}"
        new = {
            "name": name,
            "link": linker,
            "set": "pluggedin.ru"
        }
        return new

class Anime_parser():
    def show_anime_new(self):
        req = requests.get("https://kg-portal.ru/news/anime/").text
        soup = BeautifulSoup(req, "html.parser")
        all = soup.find("div", class_="news_box anime_cat")
        all_too = all.find_all("a")
        text = all_too[2].get_text()
        link_1 = str(all_too[2]).split(" ")[1].split("=")[1].split(">")[0].split("/")
        link = f"https://kg-portal.ru/news/anime/{link_1[1]}/{link_1[2]}"
        new = {
            "name": text,
            "link": link,
            "set": "kg-portal.ru"
        }
        return new
