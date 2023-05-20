# Installation

- clone the repository: `git clone <this_repository_url>`
- create a virtual environment: `python -m venv rugby`
- activate the virtual environment: `source rugby/bin/activate`
- install the dependencies: `pip install -r requirements.txt`

# Usage

```
python __init__.py
```

This will launch a script that will check every minute the page of the world cup
rugby 2023 to see if a match is available for sale.

It will write down in the console the availability if any.
