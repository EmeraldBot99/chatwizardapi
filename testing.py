import requests

# The base URL of your server
BASE_URL = 'http://localhost:8787'  # Replace with your deployed server URL if needed

# Send GET request to /foo
def get_foo():
    response = requests.get(f'{BASE_URL}/foo')
    try:
        response.raise_for_status()
        data = response.json()
        print("[GET /foo] Response:", data)
    except requests.RequestException as e:
        print("[GET /foo] Error:", e)

# Send POST request to /bar
def post_bar():
    response = requests.post(f'{BASE_URL}/bar')
    try:
        response.raise_for_status()
        data = response.json()
        print("[POST /bar] Response:", data)
    except requests.RequestException as e:
        print("[POST /bar] Error:", e)

# Send DELETE request to /baz
def delete_baz():
    response = requests.delete(f'{BASE_URL}/baz')
    try:
        response.raise_for_status()
        data = response.json()
        print("[DELETE /baz] Response:", data)
    except requests.RequestException as e:
        print("[DELETE /baz] Error:", e)

if __name__ == "__main__":
    get_foo()
    post_bar()
    delete_baz()
