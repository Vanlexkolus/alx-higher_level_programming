#!/bin/bash
#	Takes a URL, sends a request to that URL, and displays the size of the body of the response
curl -s $1 | wc -c
#!/bin/bash

# Check if the URL argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the URL using curl in silent mode and count the bytes
response_size=$(curl -s "$1" | wc -c)

# Display the size of the response body in bytes
echo "$response_size"

