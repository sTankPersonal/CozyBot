import discord

class IntentBuilder:
    def __init__(self):
        self.intents = discord.Intents.none()

    def enable_default(self):
        self.intents = discord.Intents.default()
        return self

    def enable_all(self):
        self.intents = discord.Intents.all()
        return self

    def members(self, value=True):
        self.intents.members = value
        return self

    def presences(self, value=True):
        self.intents.presences = value
        return self

    def message_content(self, value=True):
        self.intents.message_content = value
        return self

    def guilds(self, value=True):
        self.intents.guilds = value
        return self

    def reactions(self, value=True):
        self.intents.reactions = value
        return self

    def messages(self, value=True):
        self.intents.messages = value
        return self

    def voice_states(self, value=True):
        self.intents.voice_states = value
        return self

    def emojis(self, value=True):
        self.intents.emojis = value
        return self

    def typing(self, value=True):
        self.intents.typing = value
        return self

    def build(self):
        return self.intents