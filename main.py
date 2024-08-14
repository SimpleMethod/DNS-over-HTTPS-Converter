import base64
import dns.message
import dns.rdatatype
import requests
import re


def is_valid_domain(domain):
    """
    :param domain: A string representing the domain name to be validated.
    :return: A boolean value indicating whether the domain name is valid or not.
    """
    # Simple regex for validating a domain name
    regex = re.compile(
        r'^(?:[a-zA-Z0-9]'  # First character of the domain
        r'(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)'  # Sub domain + hostname
        r'+[a-zA-Z]{2,6}$'  # First level TLD
    )
    return re.match(regex, domain) is not None


def get_dns_record(domain, record_type):
    """
    :param domain: The domain name for which to fetch the DNS record.
    :return: None

    This method takes a domain name as input and retrieves the DNS record for that domain. If the domain name is invalid, an error message is printed. The method sends a DNS query to the Cloudflare DNS server and receives the response. The response is then parsed and displayed.

    Example usage:
        get_dns_record('example.com')
    """
    if not is_valid_domain(domain):
        print("Error: Invalid domain name")
        return

    try:
        # Determine the appropriate DNS record type.
        # dns.rdatatype has attributes corresponding to DNS record types, which we will use for lookup.
        rdtype = getattr(dns.rdatatype, record_type.upper(), None)
        if rdtype is None:
            print(f'Error: Unsupported record type "{record_type}"')
            return

        # Create a DNS query
        q = dns.message.make_query(domain, rdtype)

        # Get the wire format representation
        wire_data = q.to_wire()

        # Encode in Base64url
        encoded_data = base64.urlsafe_b64encode(wire_data).decode('utf-8').rstrip('=')

        # Display the encoded query
        print("Encoded query:", encoded_data)

        # Send the query to the DNS server
        response = requests.get('https://cloudflare-dns.com/dns-query?dns=' + encoded_data, timeout=5)

        # Check if the response is valid
        if response.status_code == 200:
            # Parse the response
            try:
                dns_response = dns.message.from_wire(response.content)
                print(dns_response)
            except dns.exception.DNSException:
                print("Error: Invalid DNS response")
        else:
            print("Error:", response.status_code)
    except requests.RequestException as e:
        print(f"Error: {e}")


def decode_dns_query(encoded_query):
    """
    Decodes an encoded DNS query and prints its content.
    """
    try:
        # Decode from Base64url
        wire_data = base64.urlsafe_b64decode(encoded_query + '===')

        # Parse the DNS query
        dns_query = dns.message.from_wire(wire_data)
        print(dns_query)
    except (base64.binascii.Error, dns.exception.DNSException):
        print("Error: Invalid encoded DNS query")


def main():
    while True:
        print("\nMenu:")
        print("1. Get DNS record")
        print("2. Decode DNS query")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            domain = input("Enter domain: ").strip()
            record_type = input("Enter record type (e.g. 'A', 'AAAA', 'CNAME', 'MX', 'NS', 'SOA', 'SRV'): ").strip()
            get_dns_record(domain, record_type)
        elif choice == '2':
            encoded_query = input("Enter encoded DNS query: ").strip()
            decode_dns_query(encoded_query)
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
