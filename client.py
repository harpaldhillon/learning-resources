import requests

# Path to your client certificate file
cert_file = '/path/to/client.crt'

# Path to your client key file
key_file = '/path/to/client.key'

# Make a GET request to a URL using SSL client authentication
response = requests.get('https://example.com', cert=(cert_file, key_file))

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.text)
else:
    # Print an error message if the request was not successful
    print('Error:', response.status_code)
