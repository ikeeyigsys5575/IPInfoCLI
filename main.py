import requests

url = "http://ip-api.com/json/?fields=status,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,asname,reverse,mobile,proxy,hosting,query"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # print(f"Status:\t{data['status']}\n\n")
    print("Summary:")
    print(f"\tIP:\t\t{data['query']}")
    print(f"\tAS:\t\t{data['as']}")
    print(f"\tHostname:\t{data['reverse']}")
    print(f"\tCompany:\t{data['isp']}")

    print("\nGeolocation:")
    print(f"\tCity:\t\t{data['city']}")
    print(f"\tRegion:\t\t{data['region']}")
    print(f"\tCountry:\t{data['country']}")
    print(f"\tPostal:\t\t{data['zip']}")
    print(f"\tTimezone:\t{data['timezone']}")
    print(f"\tCoordinates:\t{data['lat']}, {data['lon']}")

    print("\nDevice:")
    print(f"\tMobile:\t{data['mobile']}")
    print(f"\tProxy:\t{data['proxy']}")
    print(f"\tHosting\t{data['hosting']}")

    asn = data['as'].split(' ')[0][2:]


    # ipResponse = requests.get(f"https://api.bgpview.io/ip/{data['query']}")
    # ipResponseData = ipResponse.json()
    upstreamResponse = requests.get(f"https://api.bgpview.io/asn/{asn}/upstreams")
    upstreamResponseData = upstreamResponse.json()

    print("\nRouting:")
    upstreams4 = upstreamResponseData['data']['ipv4_upstreams']
    print("\tIPv4 Upstreams:")
    for upstream in upstreams4:
        print(f"\t\t{upstream['asn']} - {upstream['description']} ({upstream['country_code']})")

    upstreams6 = upstreamResponseData['data']['ipv6_upstreams']
    print("\tIPv6 Upstreams:")
    for upstream in upstreams6:
        print(f"\t\t{upstream['asn']} - {upstream['description']}")


else:
    print("Failed, try again")
