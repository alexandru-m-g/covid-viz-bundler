import json
import requests

OUTPUT_FILE = 'out.json'

SOURCES = [
    {
        'name': 'national_data',
        'url': 'https://proxy.hxlstandard.org/data.objects.json?dest=data_edit&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vT9_g7AItbqJwDkPi55VyVhqOdB81c3FePhqAoFlIL9160mxqtqg-OofaoTZtdq39BATa37PYQ4813k%2Fpub%3Fgid%3D0%26single%3Dtrue%26output%3Dcsv'
    },
    {
        'name': 'subnational_data',
        'url': 'https://proxy.hxlstandard.org/data.objects.json?dest=data_edit&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vT9_g7AItbqJwDkPi55VyVhqOdB81c3FePhqAoFlIL9160mxqtqg-OofaoTZtdq39BATa37PYQ4813k%2Fpub%3Fgid%3D433791951%26single%3Dtrue%26output%3Dcsv'
    },
    {
        'name': 'sources_data',
        'url': 'https://proxy.hxlstandard.org/data.objects.json?dest=data_edit&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vT9_g7AItbqJwDkPi55VyVhqOdB81c3FePhqAoFlIL9160mxqtqg-OofaoTZtdq39BATa37PYQ4813k%2Fpub%3Fgid%3D1837381168%26single%3Dtrue%26output%3Dcsv'
    },
    {
        'name': 'vaccination_campaigns_data',
        'url': 'https://proxy.hxlstandard.org/data.objects.json?dest=data_edit&strip-headers=on&force=on&url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2Fe%2F2PACX-1vT8m53T3ITzFdJWWKkdRRVRjezgt6MeeU5c2tJWl9SNff7SYn3iJ9_7DZZ_tYSmYI67-vH7cqze1VE0%2Fpub%3Fgid%3D0%26single%3Dtrue%26output%3Dcsv'
    }
]

FILE_START = '{'
FILE_END = '}'
KEY_TEMPLATE = '"{}":'
SEPARATOR = ','


def pull_data(url):
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    data_dict = r.json()
    # return json.dumps(data_dict, separators=(',', ':'))
    return json.dumps(data_dict)


def create_file():
    first = True
    with open(OUTPUT_FILE, 'w') as out:
        out.write(FILE_START)
        for source in SOURCES:
            name = source.get('name')
            url = source.get('url')
            data = pull_data(url)
            if first:
                first = False
            else:
                out.write(SEPARATOR)
            # print(data)
            out.write(KEY_TEMPLATE.format(name))
            out.write(data)
        out.write(FILE_END)


if __name__ == '__main__':
    create_file()
