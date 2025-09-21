import socket
import os

HOST = "127.0.0.1"
PORT = 6942
ROOT_DIR = os.path.dirname(__file__)+"/docs"


def handleRequest(request: str):
    requestSplit = request.split(" ")
    if not requestSplit:
        return "NEO/1.0 400 Bad Request"
    
    if len(requestSplit) != 3 or requestSplit[0] != "GET":
        return "NEO/1.0 400 Bad Request"
    
    removeLeftSlash = requestSplit[1].lstrip("/")

    if removeLeftSlash == "":
        removeLeftSlash = "index.md"
    elif not removeLeftSlash.endswith(".md"):
        removeLeftSlash += ".md"

    filePath = os.path.join(ROOT_DIR, removeLeftSlash)

    if not os.path.exists(filePath) or not filePath.endswith(".md"):
        return "NEO/1.0 404 Not Found"

    with open(filePath, 'r', encoding="utf-8")as f:
        content = f.read()
        headers = [
        "NEO/1.0 200 OK",
        "Content-Type: text/markdown",
        f"Content-Length: {len(content)}",
        "",
        content
    ]
    return "\n".join(headers)

def startServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        print(f"NeoSwitchh server running at neo://{HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                dataRequest = conn.recv(4096).decode("utf-8")
                if not dataRequest:
                    continue
                response = handleRequest(dataRequest)
                conn.sendall(response.encode("utf-8"))

if __name__ == "__main__":
    startServer()