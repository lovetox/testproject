from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    from testproject.second_module import Bar


class Foo:
    def method(self, bar: Bar) -> None:
        pass
