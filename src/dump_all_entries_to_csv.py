import requests
import csv
import os
from bs4 import BeautifulSoup

page_headers = {"User-Agent": "eksi-dumper"}

field_names = ["entry_id", "title", "text", "date", "time", "edited_date", "edited_time"]

entry_list = []


def dict_to_csv(entries, username):
    try:
        try:
            open("dumps/{}.txt".format(username),"r")
        except FileNotFoundError:
            os.mkdir("dumps")

        with open('dumps/{}.csv'.format(username), 'w') as f:
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()

            for entry in entries:
                writer.writerow(entry)
    except IOError as e:
        print("I/O error: {}".format(e))


def entry_to_dict(eid, title, text, date_time) -> dict:
    # 08.05.2021 17:50 ~ 17:53    entry_date_time = entry_date_time.split(" ~ ")
    date_time = date_time.replace(" ~ ", " ").split()
    items = len(date_time)
    date, time, edited_date, edited_time = "", "", "", ""

    if items==2:
        date, time = date_time
    elif items==3:
        date, time, edited_date = date_time
    elif items==4:
        date, time, edited_date, edited_time = date_time

    return {"entry_id": eid,
            "title": title,
            "text": text,
            "date": date,
            "time": time,
            "edited_date": edited_date,
            "edited_time": edited_time
            }


def extract_entry(entry_id) -> dict:
    print("Getting entry: {}".format(entry_id))
    link = "https://eksisozluk.com/entry/{}".format(entry_id)
    with requests.Session() as session:
        content = session.get(link, headers=page_headers).text
        soup = BeautifulSoup(content, features="lxml").find("div", {"id": "topic"})

    #h1 id="title" data-title="sevgili ile beraber tatil yapmak"
    entry_title = soup.find_next("h1", {"id": "title"}).get_text().strip()
    entry_text = soup.find_next("div", {"class": "content"}).get_text().strip()

    #<a class="entry-date permalink" href="/entry/122973468"></a>
    entry_date_time = soup.find_next("a", {"class": "entry-date permalink"}).get_text().strip()

    print("{} is finished.\n".format(entry_id))
    return entry_to_dict(entry_id, entry_title, entry_text, entry_date_time)


def main(username):

    file = open("dumps/{}.txt".format(username), "r")
    entry_ids = file.readlines()[2:]
    file.close()

    for entry in entry_ids:
        entry = entry.strip()
        current_entry = extract_entry(entry)
        entry_list.append(current_entry)
    dict_to_csv(entry_list, username)


if __name__ == '__main__':
    main("example")
