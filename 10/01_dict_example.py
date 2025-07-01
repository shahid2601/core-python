# Create a server configuration dictionary
server_config = {
    "server1": {
        "ip": "192.168.1.1",
        "port": 8080,
        "status": "active"
    },
    "server2": {
        "ip": "192.168.1.2",
        "port": 8000,
        "status": "inactive"
    },
    "server3": {
        "ip": "192.168.1.3",
        "port": 9000,
        "status": "active"
    }
}

def get_server_status(server_name):
    """Get the status of a server by its name."""
    return server_config.get(server_name, {}).get("status", "server not found")

server_name = "server2"
server_status = get_server_status(server_name)
print(f"The status of {server_name} is: {server_status}")