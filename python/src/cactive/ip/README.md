# Cactive IP API (Python)

---

### API Information:

This is a free to use API hosted in Melbourne, Australia that provides detailed information of IP addresses.

You can request the API through the HTTP or HTTPS protocol and the `GET` method at [ip.cactive.co/api/lookup/](https://ip.cactive.co/api/lookup/).

You can either provide an IP address with `/api/lookup/[ip]` or leave it blank to get the IP address of the requester.

**Example:** https://ip.cactive.co/api/lookup/8.8.8.8

---

### Installation:

```bash
pip install cactive-ip
```

### Usage:

```python
import cactive.ip as ip

def examples():
    # Get the IP address of the client
    self = ip.self()
    print(self.ip) # eg: 192.168.0.1

    # Get the time zone of a domain, IPv4 or IPv6
    external = ip.retrieve("cactive.cloud")
    print(external.time_zone) # eg: Australia/Melbourne

examples()
```

### Data Schema:

| Field              | Type           | Example             |
|--------------------|----------------|---------------------|
| `ip`               | String         | `8.8.8.8`           |
| `city`             | String or None | `Ashburn`           |
| `state`            | String or None | `Virginia`          |
| `state_code`       | String or None | `VA`                |
| `country`          | String or None | `United States`     |
| `country_code`     | String or None | `US`                |
| `country_currency` | String or None | `USD`               |
| `continent`        | String or None | `North America`     |
| `continent_code`   | String or None | `NA`                |
| `post_code`        | String or None | `20149`             |
| `time_zone`        | String or None | `America/New_York`  |
| `latitude`         | Number or None | `39.03`             |
| `longitude`        | Number or None | `-77.5`             |
| `reverse_dns`      | String or None | `dns.google`        |
| `isp`              | String or None | `Google LLC`        |
| `isp_org`          | String or None | `Google Public DNS` |
| `as_number`        | String or None | `AS15169`           |
| `as_name`          | String or None | `GOOGLE`            |
| `as_org`           | String or None | `Google LLC`        |
| `detection_vpn`    | Boolean        | `false`             |
| `detection_server` | Boolean        | `true`              |
| `detection_mobile` | Boolean        | `false`             |