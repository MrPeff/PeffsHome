import urllib

def main():
    url = 'https://infomentor.se/swedish/production/mentor/'
    values = {'login_ascx_txtNotandanafn': 'MrPeff', 'login_ascx_txtLykilord': 'wywfsw123'}

    r = session.post(url, data=values)


    r = requests.post(url, data=values)
    #print(r.content)
    url = 'https://hub.infomentor.se/#/homework'
    r = requests.post(url, data=values)
    print(r.content)

if __name__ == '__main__':
    main()
