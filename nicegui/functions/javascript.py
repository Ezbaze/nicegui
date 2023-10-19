from typing import Optional

from .. import globals  # pylint: disable=redefined-builtin
from ..awaitable_response import AwaitableResponse


def run_javascript(code: str, *,
                   respond: Optional[bool] = None,  # DEPRECATED
                   timeout: float = 1.0, check_interval: float = 0.01) -> AwaitableResponse:
    """Run JavaScript

    This function runs arbitrary JavaScript code on a page that is executed in the browser.
    The asynchronous function will return after the command(s) are executed.
    The client must be connected before this function is called.
    To access a client-side object by ID, use the JavaScript function `getElement()`.

    :param code: JavaScript code to run
    :param timeout: timeout in seconds (default: `1.0`)
    :param check_interval: interval in seconds to check for a response (default: `0.01`)

    :return: response from the browser, or `None` if `respond` is `False`
    """
    if respond is True:
        globals.log.warning('The "respond" argument of run_javascript() has been removed. '
                            'Now the function always returns an AwaitableResponse that can be awaited. '
                            'Please remove the "respond=True" argument.')
    if respond is False:
        raise ValueError('The "respond" argument of run_javascript() has been removed. '
                         'Now the function always returns an AwaitableResponse that can be awaited. '
                         'Please remove the "respond=False" argument and call the function without awaiting.')

    client = globals.get_client()
    if not client.has_socket_connection:
        raise RuntimeError('Cannot run JavaScript before client is connected; '
                           'try "await client.connected()" or "client.on_connect(...)".')

    return client.run_javascript(code, timeout=timeout, check_interval=check_interval)
