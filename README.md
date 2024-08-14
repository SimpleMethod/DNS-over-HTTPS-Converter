# DNS over HTTPS Converter

This repository contains a Python script that facilitates querying DNS records over HTTPS using Cloudflare's DNS service. It allows users to encode DNS queries into Base64 format, send them to a DNS-over-HTTPS (DoH) server, and decode DNS queries for analysis. The tool supports various DNS record types such as A, AAAA, CNAME, MX, NS, SOA, and SRV.

## Features

- **Domain Validation**: Ensures that the domain names provided by the user are valid according to standard DNS name conventions.
- **DNS Query Encoding**: Converts DNS queries into a Base64url encoded format suitable for transmission to a DoH server.
- **DoH Request Handling**: Sends encoded DNS queries to Cloudflare's DNS-over-HTTPS server and retrieves the DNS response.
- **DNS Query Decoding**: Allows users to decode Base64url encoded DNS queries back into their human-readable format for inspection or debugging.
- **Support for Multiple Record Types**: Users can request DNS records of various types, including A, AAAA, CNAME, MX, NS, SOA, and SRV.

## How to Use

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/SimpleMethod/DNS-over-HTTPS-Converter.git
   cd dns-over-https-converter
   ```

2. Ensure you have the necessary Python dependencies installed:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:
   ```bash
   python main.py
   ```

4. Follow the on-screen menu to either:
   - Fetch a DNS record for a domain by encoding the query and sending it to the DoH server.
   - Decode an already encoded DNS query.

## Example

To fetch an A record for `mlodaw.ski`:

```
Menu:
1. Get DNS record
2. Decode DNS query
3. Exit
Choose an option: 1
Enter domain: mlodaw.ski
Enter record type (e.g. 'A', 'AAAA', 'CNAME', 'MX', 'NS', 'SOA', 'SRV'): A
Encoded query: cZYBAAABAAAAAAAABm1sb2RhdwNza2kAAAEAAQ
id 29078
opcode QUERY
rcode NOERROR
flags QR RD RA
;QUESTION
mlodaw.ski. IN A
;ANSWER
mlodaw.ski. 300 IN A 188.114.96.11
mlodaw.ski. 300 IN A 188.114.97.11
;AUTHORITY
;ADDITIONAL

Menu:
1. Get DNS record
2. Decode DNS query
3. Exit
Choose an option: 
```

## Requirements

- Python 3.x
- `requests` library
- `dnspython` library

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork this repository and open a pull request with your changes. For significant changes, it's recommended to open an issue first to discuss what you would like to improve.

## Support

If you encounter any issues or have questions, feel free to open an issue in this repository.
