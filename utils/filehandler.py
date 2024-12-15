"""File Handler"""

import requests
import json

class FileHandler:
    """Handles files"""

    def __init__(self, endpoint: str=''):
        """Initialize attributes"""

        self.endpoint = endpoint
        if endpoint:
            self.response = requests.get(json.load(open(r'data\endpoints.json'))['endpoints'][endpoint])

    def store(self, filename=None, data=None):
        """Stores the file"""
        
        if not filename:
            with open(f'data/{self.endpoint}.json', 'w') as file:
                file.write(json.dumps(self.response.json(), indent=2))

        elif filename and data:
            with open(filename, 'w') as file:
                file.write(json.dumps(data, indent=2))

        else:
            with open(filename, 'w') as file:
                file.write(json.dumps(self.response.json(), indent=2))

    def read(self, filename=None):
        """Reads the file"""

        if not filename:
            with open(self.endpoint + '.json', 'r') as file:
                return json.load(file)
            
        else:
            with open(filename, 'r') as file:
                return json.load(file)


def main():
    pass

if __name__ == '__main__':
    main()