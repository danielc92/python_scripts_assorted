import bs4
import requests
import pandas

continent_list = ["africa", "asia", "europe", "oceania",
                  "north-america", "south-america"]

datadict = {"continent":[],
            "name":[],
            "full_link":[],
            "capital":[],
            "population":[],
            "square_km":[]
            }

for continent in continent_list:

    url = "http://flagpedia.net/continent/" + continent

    req = requests.get(url)
    soup = bs4.BeautifulSoup(req.text, "lxml")
    articles = soup.find_all("article")

    for article in articles:

        data_list = []

        print(":::: Start ::::")

        name = article.find("h2").text
        print(name)

        img_tag = article.find("div").find("a").find("img")
        link = img_tag.get("src")
        full_link = "http:" + link

        request = requests.get(full_link)
        with open(name +"_" +continent + ".png", "wb") as fileObject:
            fileObject.write(request.content)

        datadict["continent"].append(continent)
        datadict["name"].append(name)
        datadict["full_link"].append(full_link)

        temp_list = []
        labels = article.find_all("dd")
        for label in labels:
            text = label.text
            temp_list.append(text)

        datadict["capital"].append(temp_list[0])
        datadict["population"].append(temp_list[1])
        datadict["square_km"].append(temp_list[2])


data = pandas.DataFrame(datadict)
data.to_csv("country_data.csv")


