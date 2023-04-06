from collections import deque
from pathlib import Path
from typing import Any, Optional

from ..dependencies import register_vue_component
from ..element import Element

register_vue_component(name='log', path=Path(__file__).parent.joinpath('log.js'))

class Log(Element):

    def __init__(self, max_lines: Optional[int] = None) -> None:
        """Log view

        Create a log view that allows to add new lines without re-transmitting the whole history to the client.

        :param max_lines: maximum number of lines before dropping oldest ones (default: `None`)
        """
        super().__init__('log')
        self._props['max_lines'] = max_lines
        self._props['lines'] = ''
        self._classes = ['nicegui-log']
        self.lines: deque[str] = deque(maxlen=max_lines)
        self.use_component('log')

    def push(self, line: Any) -> None:
        line = str(line)
        self.lines.extend(line.splitlines())
        self._props['lines'] = '\n'.join(self.lines)
        self.run_method('push', line)

    def clear(self) -> None:
        """Clear the log"""
        super().clear()
        self._props['lines'] = ''
        self.lines.clear()
        self.run_method('clear')
