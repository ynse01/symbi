import argparse
from common.commands import *

def main() -> None:
    my_parser = argparse.ArgumentParser(prog='symbi',
                                        description='List the available subcommands',
                                        add_help=True)
    commands = my_parser.add_subparsers(dest="command",
                                        required=True,
                                        metavar="command",
                                        description="Subcommands")

    # Build command parsing
    build_parser = commands.add_parser("build", help="Build the specified project")
    build_parser.add_argument("project-file", type=str)
    # Lint command parsing
    lint_parser = commands.add_parser("lint", help="Lint the specified project")
    lint_parser.add_argument("project", type=str)
    # Test command parsing
    test_parser = commands.add_parser("test", help="Test the specified project")
    test_parser.add_argument("project", type=str)
    # Deploy command parsing
    deploy_parser = commands.add_parser("deploy", help="Deploy the specified project")
    deploy_parser.add_argument("project", type=str)

    args = my_parser.parse_args()

    print(args)
    runProcess(["python", "--version"])
    

if __name__ == "__main__":
    main()
