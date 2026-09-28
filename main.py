# Initialization.

if __name__ == '__main__':
    import src.mgweb.server as server
    server = server.Server()
    server.flask.run(debug=True)