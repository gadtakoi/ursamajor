def contains(url: str) -> bool:
    exceptions = ('youtube.com',)
    for e in exceptions:
        if e in url:
            return True
    return False
