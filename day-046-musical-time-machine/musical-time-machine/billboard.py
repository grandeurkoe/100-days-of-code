from bs4 import BeautifulSoup
import requests


class Billboard:
    def __init__(self):
        self.top100_titles = []

    def get_content(self, time_travel_date):
        """Gets the top 100 tracks on the billboard at a given date."""

        billboard_endpoint = f"https://www.billboard.com/charts/hot-100/{time_travel_date}/"

        billboard_response = requests.get(url=billboard_endpoint)
        billboard_response.raise_for_status()
        billboard_data = billboard_response.text

        billboard_soup = BeautifulSoup(billboard_data, "html.parser")
        billboard_titles = billboard_soup.find_all(name="h3", id="title-of-a-story")

        if billboard_titles[0].get_text().strip() == 'Songwriter(s):':
            for title_index in range(5, len(billboard_titles) - 13, +4):
                self.top100_titles.append(billboard_titles[title_index].get_text().strip())
        else:
            for title_index in range(6, len(billboard_titles) - 13, +4):
                self.top100_titles.append(billboard_titles[title_index].get_text().strip())

        return self.top100_titles
