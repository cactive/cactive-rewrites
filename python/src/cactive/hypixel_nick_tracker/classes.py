from json import dumps

from typing import Union, Literal

StaffRank = Literal["ADMINISTRATOR", "GAME_MASTER"]
PunishmentType = Literal["ban", "mute", "kick", "warning"]
FilterType = Literal["all", "online", "offline"]

class NicknameHistory:
    def __init__(self, uuid: str, nickname: str, active: bool, created_at: str, voided_at: str) -> None:
        self.uuid = uuid
        self.nickname = nickname
        self.active = active
        self.created_at = created_at
        self.voided_at = voided_at

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class PlayerDataNicknameHistory:
    def __init__(self, nickname: str, active: Union[bool, None], created_at: str, voided_at: Union[str, None]) -> None:
        self.nickname = nickname
        self.active = active
        self.created_at = created_at
        self.voided_at = voided_at

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class PlayerDataInfractions:
    def __init__(self, id: str, punishment_type: PunishmentType, executor: Union[str, None], reason: str, length: Union[float, None]) -> None:
        self.id = id
        self.punishment_type = punishment_type
        self.executor = executor
        self.reason = reason
        self.length = length

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class PlayerDataTracker:
    def __init__(self, server: Union[str, None], map: Union[str, None], proxy: Union[str, None], last_login: Union[str, None]) -> None:
        self.server = server
        self.map = map
        self.proxy = proxy
        self.last_login = last_login

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class PlayerDataIPHistory:
    def __init__(self, ip: str, login_at: str, logout_at: Union[str, None], connection_proxy: Union[str, None]) -> None:
        self.ip = ip
        self.login_at = login_at
        self.logout_at = logout_at
        self.connection_proxy = connection_proxy

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class PlayerData:
    def __init__(self, uuid: str, nickname_history: list[PlayerDataNicknameHistory], infractions: list[PlayerDataInfractions], tracker: PlayerDataTracker, ip_history: Union[list[PlayerDataIPHistory], None] = None) -> None:
        self.uuid = uuid
        self.nickname_history = nickname_history
        self.infractions = infractions
        self.tracker = tracker
        self.ip_history = ip_history

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class StaffTracker:
    def __init__(self, uuid: str, rank: StaffRank, online: Union[bool, None]) -> None:
        self.uuid = uuid
        self.rank = rank
        self.online = online

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class PunishmentData:
    def __init__(self, id: str, punishment_type: PunishmentType, uuid: str, executor: Union[str, None], reason: str, length: Union[float, None]) -> None:
        self.id = id
        self.punishment_type = punishment_type
        self.uuid = uuid
        self.executor = executor
        self.reason = reason
        self.length = length

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class KeyEndpoints:
    def __init__(self, id: str, version: float, status: bool) -> None:
        self.id = id
        self.version = version
        self.status = status

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class KeyData:
    def __init__(self, key: str, valid: bool, active: bool, created_at: Union[str, None], expires_at: Union[str, None], owner_cactiveconnections_id: Union[str, None], endpoints: list[KeyEndpoints]) -> None:
        self.key = key
        self.valid = valid
        self.active = active
        self.created_at = created_at
        self.expires_at = expires_at
        self.owner_cactiveconnections_id = owner_cactiveconnections_id
        self.endpoints = endpoints

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class InternalError:
    def __init__(self, type: str, code: float, message: str, internal: bool) -> None:
        self.type = type
        self.code = code
        self.message = message
        self.internal = internal

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class APINicknameResponse:
    def __init__(self, success: bool, id: Union[str, None] = None, data: Union[list[NicknameHistory], None] = None, errors: Union[list[InternalError], None] = None) -> None:
        self.success = success
        self.id = id
        self.data = data
        self.errors = errors

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class APIPlayerData:
    def __init__(self, success: bool, id: Union[str, None] = None, data: Union[PlayerData, None] = None, errors: Union[list[InternalError], None] = None) -> None:
        self.success = success
        self.id = id
        self.data = data
        self.errors = errors

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class APIKeyData:
    def __init__(self, success: bool, id: Union[str, None] = None, data: Union[KeyData, None] = None, errors: Union[list[InternalError], None] = None) -> None:
        self.success = success
        self.id = id
        self.data = data
        self.errors = errors

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class APIStaffTracker:
    def __init__(self, success: bool, id: Union[str, None] = None, data: Union[list[StaffTracker], None] = None, errors: Union[list[InternalError], None] = None) -> None:
        self.success = success
        self.id = id
        self.data = data
        self.errors = errors

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

class APIPunishmentData:
    def __init__(self, success: bool, id: Union[str, None] = None, data: Union[PunishmentData, None] = None, errors: Union[list[InternalError], None] = None) -> None:
        self.success = success
        self.id = id
        self.data = data
        self.errors = errors

    def __str__(self) -> str:
        return dumps(self.__dict__, indent=2, separators=(",", ": "))

APIResponseTypes = Union[APINicknameResponse, APIPlayerData, APIKeyData, APIStaffTracker, APIPunishmentData]