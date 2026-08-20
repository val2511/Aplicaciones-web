def conectar_api(url, timeout=30, retries=3, use_ssl=True):

    return f"{url} - {timeout} - {retries} - {use_ssl}"


print(conectar_api("https://api.com"))
