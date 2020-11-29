"""

rofitmux entrypoint
"""
from rofi import Rofi
import libtmux

def main():
    """

    main entrypoint
    """
    server = libtmux.Server()
    sessions = server.sessions
    current_session = sessions[0]
    windows = current_session.windows
    rofi = Rofi()
    options = [f"""{item['window_index']}: {item['window_name']}"""
               f"""({len(item.panes)} panes)"""
               for item in windows]
    idx, _ = rofi.select("Select tmux window", options)
    if idx == -1:
        return
    option = options[idx]
    option_splitted = option.split(":")
    if len(option_splitted) == 0:
        raise Exception(f"Can't find {idx} in windows")
    current_session.select_window(int(option_splitted[0]))

if __name__ ==  "__main__":
    main()
