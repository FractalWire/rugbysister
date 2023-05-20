import time
from datetime import datetime
from signal import signal, SIGINT
from sys import exit

from lxml.html import fromstring
import requests

def check_availability():
    r = requests.get(
        "https://tickets.rugbyworldcup.com/fr",
        headers={"User-Agent": "Mozilla/5.0"}
    )

    html = fromstring(r.content)

    for el in html.find_class("list-ticket-content"):
        info = el.find_class("match-label")
        s = info[0].text_content()
        official_ticket = el.find_class("ticketing-info")
        availability = []
        if len(official_ticket[0].find_class("unavailable")) == 0:
            availability.append("Official ticket available")
        resale_ticket = el.find_class("resale-info")
        if len(resale_ticket[0].find_class("unavailable")) == 0:
            availability.append("Resale ticket available")

        if availability:
            print(f'{s}: {availability}')
        else:
            print('No availability')


def sigint_handler(signal_received, frame):
    exit(0)


if __name__ == '__main__':
    signal(SIGINT, sigint_handler)

    minute = 60
    while True:
        print(datetime.now())
        check_availability()
        time.sleep(1 * minute)
