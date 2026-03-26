#!/usr/bin/env python3

"""
User Dashboard Project

A simple command-line user dashboard application.

Usage:
    user_dashboard.py <command> [<args>]

Commands:
    create_user
    list_users
    delete_user
    update_user

Options:
    -h --help     Show this screen.
    --version     Show version.
"""

import docopt

def main():
    arguments = docopt.docopt(__doc__, version='1.0')
    print(arguments)

if __name__ == '__main__':
    main()