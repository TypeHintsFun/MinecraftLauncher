from dataclasses import dataclass, field


@dataclass
class ProgressBar:
    max_value: int

    filling_symbols: list[str] = field(
        default_factory=lambda: ['█', ' ']
    )
    prefix: str = ''
    suffix: str = ''

    def render_progress_bar(self, value: int, relative_value: bool = True) -> str:
        pass
