import requests

SERVER='192.168.1.200'
API='/api/predict?speed=2.2&cores=12&storage=2000&ram=32'

def test_api(server,api):
    
    response = requests.get('http://'+server+api)
    
    print('Server:        {}'.format(server))
    print('API Call:      {}'.format(api))
    print('Response Code: {:d}'.format(response.status_code))
    print('Response:      {}'.format(response.json()))
    
    return response.json()

def main():
    return test_api(SERVER,API)

if __name__ == '__main__':
    main()