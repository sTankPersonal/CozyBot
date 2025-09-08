from Config import Settings

class ValidateSettingsService:
    @staticmethod
    def validate(settings: dict) -> bool:
        required_keys = ['TOKEN', 'PREFIX', 'DB_CONNECTION_STRING', 'BOT_NAME', 'FOOTER']

        for key in required_keys:
            if key not in settings or not settings[key]:
                raise ValueError(f"Missing or empty required setting: {key}")

        return True