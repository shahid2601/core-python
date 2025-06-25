# Define configuration variables for a web server
server_name = "my_server"
port = 80
is_https_enabled = True
max_connection = 1000

# Print the configuration
print(f"Server Name: {server_name}")
print(f"Port: {port}")
print(f"HTTPS Enabled: {is_https_enabled}")
print(f"Max Connection: {max_connection}")

# Update configuration values
port = 3303
is_https_enabled = False

# Print the Updated configuration
print(f"Updated Port: {port}")
print(f"Updated HTTPS Enabled: {is_https_enabled}")