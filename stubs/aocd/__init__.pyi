from typing import Any, Optional

def submit(
    answer: str,
    part: Optional[str] = None,
    day: Optional[int] = None,
    year: Optional[int] = None,
    session: Optional[Any] = None,
    reopen: Optional[bool] = True,
    quiet: Optional[bool] = False,
) -> Any: ...
def get_data(
    session: Any = None,
    day: Optional[int] = None,
    year: Optional[int] = None,
    block: bool = False,
) -> str: ...
