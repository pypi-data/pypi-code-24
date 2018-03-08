from .command import Command

from poetry.masonry import Builder


class BuildCommand(Command):
    """
    Builds a package, as a tarball and a wheel by default.

    build
        { --f|format=* : Limit the format to either wheel or sdist}
    """

    def handle(self):
        fmt = 'all'
        if self.option('format'):
            fmt = self.option('format')

        package = self.poetry.package
        self.line(f'Building <info>{package.pretty_name}</> '
                  f'(<comment>{package.version}</>)')

        builder = Builder(self.poetry, self.output)
        builder.build(fmt)
