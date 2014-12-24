#! python

import collections
import io
import json
import urllib2

"""Problem 1: download data, aggregate it, pretty-print it.

This file will write JSON to standard out if run as a script from the command
line.

This URL...

    http://api.sba.gov/geodata/city_county_links_for_state_of/in.json

...fetches county and geolocation data for the state of Indiana in JSON format.

Given the following list of abbreviated state names...

    states = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]

Set up a loop to iterate through the list above to change the state name
abbreviation in the URL, then fetch the data for each state, and populate
a text file with the results. Please provide inline commentary and/or
docstrings for your code, and set up your answer as a standard Python module
that can be executed from the command line.  Use any Python library you
like to make your API call. Make your code as simple and elegant as
possible."""

def load_state(state_abbreviation, retry_total=4):
    """Load an individual state's JSON data from the provided
       web site. Allow downloads to retry if there's a loading/parsing
       failure.
    """
    url_pattern = ("http://api.sba.gov/geodata/"
                   "city_county_links_for_state_of/{0}"
                   ".json").format(state_abbreviation.lower())
    # Retry download up to 4 times
    retry_count = 0
    while True:
        retry_count += 1
        try:
            return json.load(urllib2.urlopen(url_pattern))
        except Exception as e:
            if retry_count >= retry_total:
                raise
    raise RuntimeError("This should never happen.")

def load_states():
    """A generator that yields abbreviation/dict pairs, suitable for
       assembling into a dictionary.
    """
    states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL",
        "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME",
        "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH",
        "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",
        "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI",
        "WY"
    ]
    for state in states:
        yield (state, load_state(state))

def load_states_dict():
    """Loop through the list of states, returning a JSON-like struct that
       contains information for *all* the states.
    """
    # Use an ordereddict so state abbreviation keys stay in alphabetical order
    state_struct = collections.OrderedDict()
    for abbreviation, state_data in load_states():
        state_struct[abbreviation] = state_data
    return state_struct

def get_states_json():
    """Returns a JSON string incorporating all states' data.

       This script uses the io module for the sake of "future-proofing":
       by explicitly handling the bytes/unicode divide we make it easier
       to port to Python 3 (if it ever happens) and makes the code a little
       more modern.
    """
    state_data = load_states_dict()
    string_handle = io.BytesIO()
    with string_handle:
        json.dump(state_data, string_handle, indent=2)
        return string_handle.getvalue().decode("utf-8")

def print_states():
    """Calls load_states, prettyprints JSON to standard out.
    """
    print get_states_json()

if __name__ == "__main__":
    print_states()
