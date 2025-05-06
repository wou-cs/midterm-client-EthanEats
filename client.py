import requests

api_url = "http://chrisbrooks.pythonanywhere.com/api/programmers"

def get_programmer_count():
    """
    Return the number of programmers return from the plural programmers API
    :return: An integer indicating the number of programmers in the plural list.
    """
    response = requests.get(api_url, timeout=5).json()
    programmers = response["programmers"]
    return len(programmers)


def get_programmer_by_id(pid):
    """
    Return the single programmer referenced by the specified programmer id (pid)
    :param pid: Unique identifier for the programmer to lookup
    :return: A dictionary containing the matched programmer. Return an empty dictionary if not found
    """
    url = api_url + f"/{pid}"

    try:
        programmer = requests.get(url, timeout=5).json()
        return programmer
    except:
        return {}


def get_full_name_from_first(first_name):
    """
    Return the full name of the *first* programmer having the provided first name, concatenating the first and last name with a space between.
    :param first_name:
    :return: A string containing the first and last name of the first programmer in the list of matches.
    """
    url = api_url + f"/by_first_name/{first_name}"


    response = requests.get(url, timeout=5).json()
    programmers = response["programmers"]

    programmer = next(((p["first"] + " " + p["last"]) for p in programmers), None)

    return programmer