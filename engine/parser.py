"""Very simple command parser."""

class Parser:
    def parse(self, command: str) -> tuple[str, list[str]]:
        """Parse a raw string into a verb and list of arguments."""
        parts = command.strip().lower().split()
        if not parts:
            return "", []
        verb, *args = parts
        return verb, args
