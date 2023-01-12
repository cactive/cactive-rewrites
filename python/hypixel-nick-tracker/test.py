from cactive_hypixel_nick_tracker import Client

client = Client(
    key="MY_API_KEY", # replace this field.
    cache=False
)

try:
    data = client.nickname_history("nickname").data
    print(data)
    ''' [
        {
            "uuid": "eea2d4fda8b8413b9439f06faaf7e109",
            "nickname": "angry_and_free",
            "active": false,
            "created_at": "2022-04-11T09:00:27.933Z",
            "voided_at": "1970-01-01T00:00:00.000Z"
        }
    ] '''
except Exception as e:
    print(e)
    ''' [
        {
            "type": "no-identifier",
            "code": 400,
            "message": "You didn't provide a 'nickname' parameter in your request"
        }
    ] '''