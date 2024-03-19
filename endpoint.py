import requests

def url_check(url):
    isUp=True
    try:
        #resp = requests.get('http://cnn.com')
        resp = requests.get(url)
    except:
        print('please double check your url')
    else:
        status = resp.status_code
        #print(status)
        if status == 200:
            #print('site is up')
            isUp=True
        else:
            #print('site is down')
            isUp=False
    return isUp
a = url_check('http://google.com')
print(a)