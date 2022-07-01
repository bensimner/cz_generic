from commitizen.cz.base import BaseCommitizen
from commitizen.defaults import Questions

from textwrap import dedent

class Kind:
    def __init__(self, name, doc):
        self.name = name
        self.doc = doc


class GenericCz(BaseCommitizen):
    """ a language-agnostic generic Commitizen style with more flexibility and a wider range of types.

    easily configurable to extend the rules
    """

    SCHEMA = dedent("""\
        ["(" <what> ")"] <kind> ":" <subject>

        <body>

        <footer>
    """)

    KINDS = [
        # functional changes
        Kind("add", "added something new"),
        Kind("remove", "took away something old"),
        Kind("update", "not new, not old, just different"),
        Kind("fix", "oopsy"),

        # refactoring
        Kind("move", "same old, just somewhere else"),
        Kind("rename", "same old, just with a new name"),
        Kind("refactor", "same old but in a new box"),

        # inclusion, dependencies and builds
        Kind("sync", "was old, now new"),
        Kind("revert", "was new, now old"),

        # styling
        Kind("style", "same, but looks different"),
    ]

    def questions(self) -> Questions:
        raise ValueError("Unsupported operation")

    def message(self, answers: dict) -> str:
        raise ValueError("Unsupported operation")

    def example(self) -> str:
        return (
            "(docs) fix: minor typo\n"
            "\n"
            "closes: #12"
        )

    def schema(self) -> str:
        return self.SCHEMA

    def schema_pattern(self) -> str:
        BODY_PATTERN = r"(\s.*)"
        PATTERN_PARTS = [r"(\(\S+\)\s)?", "(" + "|".join(kind.name for kind in self.KINDS) + ")", ":", BODY_PATTERN]
        PATTERN = "".join(PATTERN_PARTS)
        return PATTERN

    def info(self) -> str:
        raise ValueError("Unsupported operation")

    def process_commit(self, commit: str) -> str:
        raise ValueError("Unsupported operation")


discover_this = GenericCz  # used by the plug-in system
