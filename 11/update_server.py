# This script updates a configuration file for a server application.
# It searches for a specific key and updates its value.
# Example usage:

# A function to update a server configuration file
# It reads the file, modifies the specified key, and writes it back.
def update_server_config(file_path, key, value):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:  # Read each line in the file
            if key in line:
                # Update the line with the new value
                file.write(f"{key} = {value}\n")
            else:
                # Write the line unchanged
                file.write(line)

update_server_config('server.conf', 'MAX_CONNECTIONS', '600') # This will change the value of MAX_CONNECTIONS to 600 in the server.conf file.