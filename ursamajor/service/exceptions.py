def contains(url: str) -> bool:
    exceptions = ('youtube.com',)
    for e in exceptions:
        if e in url:
            print(e, url, )
            return True
    return False
