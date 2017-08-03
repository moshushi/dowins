import dowins

def save_cookie_string():
    """
    get and save cookie string for fixture pytest
    """
    cookie_string = dowins.PostsExtractor.get_csrf_and_cookie_string()[1]
#     cookie_string = "headers = { 'Set-Cookie: '" + cookie_string + "'}"
    with open('cookie_string.txt','w') as f:
        f.write(cookie_string)


if __name__ == '__main__':
    save_cookie_string()
