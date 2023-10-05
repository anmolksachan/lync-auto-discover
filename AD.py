#!/bin/bash
echo "asachan_ADS_Enum_Auto_Fuxx"

echo "
                                                           
 |     ._   _  / /\     _|_  _ __ _| o  _  _  _      _  ._ 
 |_ \/ | | (_ / /--\ |_| |_ (_)  (_| | _> (_ (_) \/ (/_ |  
    /                                                      
      Dumb script to detect AD [Lync & auto]
                                           "

if [ $# -ne 1 ]; then
    echo "Usage: $0 domain.txt"
    exit 1
fi

domain_file="$1"

# Define colors for output
GREEN="\033[0;32m"
RED="\033[0;31m"
NC="\033[0m" # No color

while read -r subdomain; do
    urls=("http://lyncdiscover.${subdomain}"
          "https://lyncdiscover.${subdomain}"
          "http://autodiscover.${subdomain}/rpc"
          "https://autodiscover.${subdomain}/rpc")

    echo "Testing subdomain: ${subdomain}"
    
    for url in "${urls[@]}"; do
        status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")
        if [ "$status_code" = "200" ]; then
            echo -e "${GREEN}URL exists: $url${NC}"
        else
            echo -e "${RED}URL does not exist or returned status code $status_code: $url${NC}"
        fi
    done

    echo # Add an empty line for better readability between subdomains
done < "$domain_file"
