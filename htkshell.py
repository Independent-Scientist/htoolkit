from IPython.frontend.terminal.embed import InteractiveShellEmbed
from IPython.config.loader import Config
import modules.torrific as torrific


def interact():
    cfg = Config()
    ipshell = InteractiveShellEmbed(config=cfg, banner1="Hacking Toolkit")
    ipshell()


def main():
    interact()


if __name__ == '__main__':
    main()



