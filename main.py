#Ip Location Tracker
import geo

def track_ip(ip):
    """Track and display information for the given IP address."""
    try:
        # Get the IP address if none is provided
        if not ip:
            ip = geo.getIP()
        if not ip:
            print("Unable to fetch IP address.")
            return

        print(f"Tracking information for IP: {ip}")

        # Get country information
        country = geo.getCountry(ip, 'plain')
        if country:
            print(f"Country: {country}")
        else:
            print("Unable to fetch country information.")

        # Get geo data
        geo_data = geo.getGeodData(ip)
        if geo_data:
            print(f"Geo Data: {geo_data}")
        else:
            print("Unable to fetch geo data.")

        # Show IP details
        geo.showIpDetails(ip)

        # Show country details
        geo.showCountryDetails(ip)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Interactive part
    ip_to_track = input("Enter the IP address to track (leave empty to track your own IP): ")
    track_ip(ip_to_track)

# sample IP that can be tested





