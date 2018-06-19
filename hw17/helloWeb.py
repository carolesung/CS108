#!/usr/bin/python3

# File: helloWeb.py
# Author: Aaron Stevens (azs@bu.edu)
# Description: Our first Python web application.

# The main section of the program:
if __name__ == "__main__":
    # HTTP headers
    print("Content-type: text/html")
    print()
    print(
"""
<html>
<head>
<title>Our first Python web application</title>
</head>

<body>
Hello, world!
</body>

</html>

""")
