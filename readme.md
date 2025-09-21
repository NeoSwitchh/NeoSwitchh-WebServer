# NeoSwitchh Protocol (NEO/1.0)

A fun experiment to serve and fetch Markdown files over a custom protocol called **NEO/1.0**.  
It consists of two parts:

- **neoServer.py** → a simple Python socket server that serves Markdown files.
- **neoClient.py** → a client that can fetch Markdown files from the server using the `neo://` protocol.

---

## 🚀 Features

- Custom **NEO/1.0** protocol (inspired by HTTP).
- Server serves only `.md` files from the `docs/` folder.
- Client validates the `neo://` scheme
- ASCII banner for the client.

---

## 📂 Project Structure

```

.
├── neoServer.py # The server
├── neoClient.py # The client
├── docs/ # Markdown files served by the server
│ ├── index.md
└── README.md

```

---

## 🖥️ Running the Server

1. Make sure you have **Python 3.8+** installed.
2. Create a `docs/` folder with at least an `index.md` file:

```

docs/index.md

```

3. Run the server:

```
python neoServer.py
```

4. You should see:

```
NeoSwitchh server running at neo://127.0.0.1:6942
```

---

## 📡 Running the Client

1. Start the client:

```
python neoClient.py
```

2. You’ll see the ASCII banner:

```
 _   _            _____         _ _       _     _
| \ | |          / ____|       (_) |     | |   | |
|  \| | ___  ___| (_____      ___| |_ ___| |__ | |__
| . ` |/ _ \/ _ \\___ \ \ /\ / / | __/ __| '_ \| '_ \
| |\  |  __/ (_) |___) \ V  V /| | || (__| | | | | | |
|_| \_|\___|\___/_____/ \_/\_/ |_|\__\___|_| |_|_| |_|
    NEO:// Client
```

3. Enter a `neo://` URL:

```
Enter neo:// address (or 'quit' to exit): neo://127.0.0.1/
```

4. The client will fetch `docs/index.md` and display the content.

---

## 🌐 URL Rules

- `neo://127.0.0.1/` → serves `docs/index.md`

---

## 📑 Protocol Specification (NEO/1.0)

### Request

```
GET /readme NEO/1.0
```

### Response

```
NEO/1.0 200 OK
Content-Type: text/markdown
Content-Length: 1234

# Markdown Content Here
```

### Error Responses

- `NEO/1.0 400 Bad Request`
- `NEO/1.0 404 Not Found`

---

## 🤯 Fun Feature

The NEO client has a little personality of its own.  
Try giving it something _it doesn’t quite expect_ — maybe the wrong kind of URL —  
and see how patient (or impatient) it can be with you. 😉

(Pro tip: stick to `neo://` unless you enjoy being scolded.)

---

## 📜 License

MIT
