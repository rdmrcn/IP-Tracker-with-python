import requests

def getIP():
    """Fetch the public IP address of the current machine."""
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        ip = response.json()['ip']
        return ip
    except requests.RequestException as e:
        print(f"Error fetching IP: {e}")
        return None

def getCountry(ip, format='json'):
    """Fetch the country information for the given IP address."""
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/country')
        response.raise_for_status()
        country = response.text.strip()
        return country
    except requests.RequestException as e:
        print(f"Error fetching country: {e}")
        return None

def getGeodData(ip):
    """Fetch the geolocation data for the given IP address."""
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/geo')
        response.raise_for_status()
        geo_data = response.json()
        return geo_data
    except requests.RequestException as e:
        print(f"Error fetching geo data: {e}")
        return None

def showIpDetails(ip):
    """Print detailed information about the given IP address."""
    geo_data = getGeodData(ip)
    if geo_data:
        print(f"IP Details for {ip}:")
        for key, value in geo_data.items():
            print(f"{key}: {value}")

def showCountryDetails(ip):
    """Print the country details for the given IP address."""
    country = getCountry(ip, 'plain')
    if country:
        print(f"Country for IP {ip}: {country}")
