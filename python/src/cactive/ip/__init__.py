from requests import get, Response
from json import loads, dumps

from typing import Union


class IPData:
    '''
    The class which holds all IPData
    '''

    def __init__(
        self,
        ip: str,
        city: Union[str, None],
        state: Union[str, None],
        state_code: Union[str, None],
        country: Union[str, None],
        country_code: Union[str, None],
        country_currency: Union[str, None],
        continent: Union[str, None],
        continent_code: Union[str, None],
        post_code: Union[str, None],
        time_zone: Union[str, None],
        latitude: Union[float, None],
        longitude: Union[float, None],
        reverse_dns: Union[str, None],
        isp: Union[str, None],
        isp_org: Union[str, None],
        as_number: Union[str, None],
        as_name: Union[str, None],
        as_org: Union[str, None],
        detection_vpn: bool,
        detection_server: bool,
        detection_mobile: bool,
    ) -> None:
        self.ip = ip
        self.city = city
        self.state = state
        self.state_code = state_code
        self.country = country
        self.country_code = country_code
        self.country_currency = country_currency
        self.continent = continent
        self.continent_code = continent_code
        self.post_code = post_code
        self.time_zone = time_zone
        self.latitude = latitude
        self.longitude = longitude
        self.reverse_dns = reverse_dns
        self.isp = isp
        self.isp_org = isp_org
        self.as_number = as_number
        self.as_name = as_name
        self.as_org = as_org
        self.detection_vpn = detection_vpn
        self.detection_server = detection_server
        self.detection_mobile = detection_mobile

    def __str__(self) -> str:
        return dumps(self.__dict__)


class IPError(Exception):
    '''
    Custom exception for errors in IPData
    '''

    def __init__(self, error: str) -> None:
        Exception.__init__(self, error)


def fetch(ip: Union[str, None]) -> IPData:
    '''
    Do not call this function directly. Please use self or retrieve
    '''

    ip = ip if ip is not None else ""

    r: Response = get(f"https://ip.cactive.co/api/lookup/{ip}")
    d: dict = loads(r.text)

    if "errors" in d:
        raise IPError(d["errors"][0]["message"])
    return IPData(*d.values())


def self() -> IPData:
    '''
    Get the IP data for yourself
    '''

    return fetch(None)


def retrieve(ip: str) -> IPData:
    '''
    Get IP data for another IP address
    '''

    return fetch(ip)