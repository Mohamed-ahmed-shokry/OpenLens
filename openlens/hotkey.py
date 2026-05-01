"""Global hotkey listener boundary."""

from collections.abc import Callable
from typing import Any

DEFAULT_HOTKEY = "<ctrl>+<shift>+s"
HOTKEY_WARNING = (
    "Warning: global hotkey listener could not start. "
    "This may happen on Wayland or restricted desktop sessions."
)


class GlobalHotkeyListener:
    """Manage a background pynput global hotkey listener."""

    def __init__(
        self,
        callback: Callable[[], None],
        hotkey: str = DEFAULT_HOTKEY,
    ) -> None:
        self.callback = callback
        self.hotkey = hotkey
        self._listener: Any | None = None

    def start(self) -> bool:
        """Start listening for the configured hotkey."""
        if self._listener is not None:
            return True

        try:
            # Import lazily so unsupported desktop sessions can still open the app.
            from pynput import keyboard

            self._listener = keyboard.GlobalHotKeys({self.hotkey: self.callback})
            self._listener.start()
        except Exception as exc:
            self._listener = None
            print(f"{HOTKEY_WARNING} ({exc})")
            return False

        return True

    def stop(self) -> None:
        """Stop the listener if it was started."""
        if self._listener is None:
            return

        self._listener.stop()
        self._listener = None
