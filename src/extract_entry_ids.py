import requests
import re
import datetime
import os
# import getopt
# import sys
from bs4 import BeautifulSoup

page_headers = {"User-Agent": "eksi-dumper"}

# pageHeaders = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) '
#                              'AppleWebKit/601.1.46 (KHTML, like Gecko) '
#                              'Version/9.0 Mobile/13B137 Safari/601.1'}


def starting_date(file_name) -> None:
    date_format = "%d-%m-%Y %H:%M:%S"
    now = datetime.datetime.now()
    date = now.strftime(date_format)
    try:
        file = open("dumps/{}.txt".format(file_name), "w")
    except FileNotFoundError:
        print("'dumps' directory is not found. creating...")
        os.mkdir("dumps")
        file = open("dumps/{}.txt".format(file_name), "w")

    file.write(date + "\n\n")
    file.close()


def detect_pages(username) -> int:  # make callable with user name
    user_last_entries = "https://eksisozluk.com/basliklar/istatistik/{}/son-entryleri?p=2".format(username)

    eksi_sozluk_response_text = requests.get(user_last_entries, headers=page_headers).text
    soup = BeautifulSoup(eksi_sozluk_response_text, features="lxml")
    pager = str((soup.find("div", {"class": "pager"})))

    try:
        page_number = int(re.findall(r'(?<=data-pagecount=")\d+(?=")', pager)[0])
    except IndexError:
        page_number = 1

    return page_number


def extract_entries_from_page(username, page, _file) -> None:
    # _file.write("\n" + "{}".format(page).center(10, "-") + "\n")
    user_last_entries = "https://eksisozluk.com/basliklar/istatistik/{}/son-entryleri?p={}".format(username, page)

    with requests.Session() as session:
        eksi_sozluk_response_text = session.get(user_last_entries, headers=page_headers).text
        soup = BeautifulSoup(eksi_sozluk_response_text, features="lxml")
        entry_section = str((soup.find("section", {"id": "content-body"})))

    extracted_entries = re.findall(r"(?<=#)\d+", entry_section)
    print("Page {} contains {} entries".format(page, len(extracted_entries)))

    for i in extracted_entries:
        _file.write(i + "\n")


def main(user) -> None:
    starting_date(user)

    file = open("dumps/{}.txt".format(user), "a")

    page_number = detect_pages(user)

    print("User: {}, Total pages: {}".format(user, page_number))

    for current_page in range(1, page_number+1):
        extract_entries_from_page(user, current_page, file)
        print("Page {}/{} is done.".format(current_page, page_number))

    file.close()


if __name__ == '__main__':
    main("example")
