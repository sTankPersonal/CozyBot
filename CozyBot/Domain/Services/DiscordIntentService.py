from typing import Any, Dict, Optional


class DiscordIntentService:
    def build_intent(
        self,
        name: str,
        description: Optional[str] = None,
        options: Optional[list] = None,
        default_permission: bool = True,
        type_: int = 1,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Builds a Discord intent
        """
        intent = {
            "name": name,
            "description": description or "",
            "options": options or [],
            "default_permission": default_permission,
            "type": type_,
        }
        intent.update(kwargs)
        return intent

    # Add more intent-related methods as needed