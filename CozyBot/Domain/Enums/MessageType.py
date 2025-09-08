from enum import Enum


class MessageType(Enum):
    ON_MEMBER_JOIN = 1
    ON_MEMBER_LEAVE = 2
    ON_GUILD_JOIN = 3
    ON_GUILD_LEAVE = 4