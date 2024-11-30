"""File Handler"""

import requests
import json

class FileHandler:
    """Handles files"""

    def __init__(self, endpoint: str):
        """Initialize attributes"""

        self.endpoint = endpoint
        self.response = requests.get(json.load(open('endpoints.json'))['endpoints'][endpoint])

    def store(self):
        """Stores the file"""

        with open(self.endpoint + '.json', 'w') as file:
            file.write(json.dumps(self.response.json(), indent=2))

    def read(self):
        """Reads the file"""

        with open(self.endpoint + '.json', 'r') as file:
            return json.load(file)

    def update(self):
        """Regularly updates the file given a time interval"""

        pass


def main():
    pass

if __name__ == '__main__':
    main()