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
    response = requests.get(api_url, timeout=5).json()
    programmers = response["programmers"]
    programmer = next((p for p in programmers if p["id"] == pid), {})

    return programmer


def get_full_name_from_first(first_name):
    """
    Return the full name of the *first* programmer having the provided first name, concatenating the first and last name with a space between.
    :param first_name:
    :return: A string containing the first and last name of the first programmer in the list of matches.
    """
    response = requests.get(api_url, timeout=5).json()
    programmers = response["programmers"]

    # 'next' grabs the first element that succeeds at the following:
    # we're testing each programmer to see if the first name matches the input name (first_name)
    # if we find one, the succeeding element will be the first and last name appended.
    # the 'None' at the very end is for defaulting (if there isn't a programmer by the inputted name)
    programmer = next(((p["first"] + " " + p["last"]) for p in programmers if p["first"].upper() == first_name.upper()), None)

    return programmer