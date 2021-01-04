import django_subcommands

from leon.management.subcommands.docs import DocsCommand
from leon.management.subcommands.setup import SetupCommand
from leon.management.subcommands.scaffold import ScaffoldCommand


class Command(django_subcommands.SubCommands):
    
    subcommands = {
        "docs": DocsCommand,
        "setup": SetupCommand,
        "scaffold": ScaffoldCommand,
    }