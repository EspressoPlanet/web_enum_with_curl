# web_enum_with_curl
~ A Python script that takes in an argument of a TXT file containing a list of domains or subdomains. It will then run a curl on each domain listed and return the corresponding HTTP code. It will output all responses into a TXT into a directory of your choice.

# How to use
~ start the program with **python3 ./web_enum_with_curl <insert txt of domains here>**
~ To ensure the script runs properly, make sure the list of domains contains just one domain per line

# Output format
~ All responses will be recorded in the format **<HTTP CODE> ~~~ <DOMAIN>**
~ EX: **200 ~~~ Github.com**
