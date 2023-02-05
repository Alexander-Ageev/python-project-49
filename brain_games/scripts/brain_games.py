#!/usr/bin/env python3
import brain_games.tools.cli as cli


def main():
    cli.welcome()
    name = cli.username_request()
    cli.hello(name)


if __name__ == '__main__':
    main()
