import re
import socket

wrongProtCount = 0
BANNER = BANNER = r"""
  _   _            _____         _ _       _     _     
 | \ | |          / ____|       (_) |     | |   | |    
 |  \| | ___  ___| (_____      ___| |_ ___| |__ | |__  
 | . ` |/ _ \/ _ \\___ \ \ /\ / / | __/ __| '_ \| '_ \ 
 | |\  |  __/ (_) |___) \ V  V /| | || (__| | | | | | |
 |_| \_|\___|\___/_____/ \_/\_/ |_|\__\___|_| |_|_| |_|
   NEO:// Client
"""

def urlParser(url: str):
    pattern = re.compile(
        r'^(?P<protocol>[a-zA-Z][a-zA-Z0-9+.-]*)://(?P<host>[^:/]+)(?::(?P<port>\d+))?(?P<path>/.*)?$'
    )

    match = pattern.match(url)
    if not match:
        raise ValueError(f"Invalid URL: {url}")

    protocol = match.group("protocol")
    host = match.group("host")
    port = int(match.group("port")) if match.group("port") else 6942
    path = match.group("path") or "/"
    res = {
        "protocol" : protocol,
        "host" : host,
        "port" : port,
        "path" : path,
    }
    return res

def fetchNeo(url: str):
    global wrongProtCount
    parsedUrl = urlParser(url)
    protocol = parsedUrl["protocol"]
    host = parsedUrl["host"]
    port = parsedUrl["port"]
    path = parsedUrl["path"]

    if protocol.lower() != "neo":
        if wrongProtCount == 0:
            wrongProtCount += 1    
            return "Wrong Protocol, Bro. No worries :)"
        elif wrongProtCount == 1:
            wrongProtCount += 1
            return "Bro, use the neo:// protocol please"
        elif wrongProtCount == 2:
            wrongProtCount += 1
            return "BRO NOT COOL, THIS IS YOUR LAST WARNING"
        else:
            print("ALRIGHT BRO IF YOU WANT TO USE OTHER THAN THE NEO PROTOCOL JUST USE POSTMAN OR YOUR BROWSER")
            exit()


    with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
        s.connect((host,port))
        request = f"GET {path} NEO/1.0\n"
        s.sendall(request.encode("utf-8"))
        response = s.recv(65536).decode("utf-8")
    
    return response

if __name__ == "__main__":
    print(BANNER)
    while True:
        url = input("Enter neo:// address (or 'quit' to exit): ").strip()
        if url.lower() in ["quit", "exit"]:
            print("Goodbye 👋")
            break
        try:
            print(fetchNeo(url))
        except Exception as e:
            print(f"Error: {e}")
