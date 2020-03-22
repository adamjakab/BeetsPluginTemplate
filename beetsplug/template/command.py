#  Copyright: Copyright (c) 2020., Adam Jakab
#
#  Author: Adam Jakab <adam at jakab dot pro>
#  Created: 3/21/20, 11:28 AM
#  License: See LICENSE.txt

from optparse import OptionParser
from beets.library import Library, Item, parse_query_parts
from beets.ui import Subcommand, decargs
from beets.util.confit import Subview

from beetsplug.template import common

# The plugin
__PLUGIN_NAME__ = u'template'
__PLUGIN_SHORT_DESCRIPTION__ = u'a plugin template'


class TemplateCommand(Subcommand):
    config: Subview = None
    lib: Library = None
    query = None
    parser: OptionParser = None

    def __init__(self, cfg):
        self.config = cfg

        self.parser = OptionParser(usage='beet template [options] [QUERY...]')

        self.parser.add_option(
            '-v', '--version',
            action='store_true', dest='version', default=False,
            help=u'show plugin version'
        )

        # Keep this at the end
        super(TemplateCommand, self).__init__(
            parser=self.parser,
            name=__PLUGIN_NAME__,
            help=__PLUGIN_SHORT_DESCRIPTION__
        )

    def func(self, lib: Library, options, arguments):
        self.lib = lib
        self.query = decargs(arguments)

        if options.version:
            self.show_version_information()
            return

        self.handle_main_task()

    def handle_main_task(self):
        self._say("Well done!")

    def show_version_information(self):
        from beetsplug.template.version import __version__
        self._say("Plot(beets-{}) plugin for Beets: v{}".format(__PLUGIN_NAME__, __version__))

    def _say(self, msg, log_only=False):
        common.say(msg, log_only)
