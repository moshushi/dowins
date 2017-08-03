import requests
import requests_mock
import dowins

# def test_A():
#     with requests_mock.Mocker() as m:
#         m.get('http://test.com', text='resp')
#         assert requests.get('http://test.com').text=='respe'

@requests_mock.Mocker()
def test_funcion(m):
        m.get('http://test.com', text=data_small_p)
        return requests.get('http://test.com').text

# assert test_funcion() == 'resp'
print(test_funcion(data_small_p))
# print(type(test_funcion()))


