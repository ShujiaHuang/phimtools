"""Work with Minimac commands.

Author: Shujia Huang
Date: 2019-05-22
"""
from phimtools.log import Log
from phimtools.launch import do


class Minimac(object):
    """A class for Minimac3/Minimac4 program"""

    def __init__(self, config, toolstore, reference_panel):
        """basical setting for Minimac"""

        if reference_panel is None:
            return

        self.minimac = toolstore["minimac"]
        self.ref_panel = config["minimac"]["reference_panel"][reference_panel]
        
    def help(self):
        """Help information for Minimac program"""
        return do.run("%s --help" % self.minimac)

    def run(self, **kwargs):
        """Run a Minimac commands with provided options.

        Parameters:
            ``kwargs``: A dict like
                key world parameter for minimac
        """
        if "chr" not in kwargs:
            Log.error("Missing 'chr' for reference panel in the Minimac command")
            return False

        chrom = kwargs["chr"]
        # minimac4: Non-zero value of "--start" required parameter if using "--chr" parameter.
        if "start" not in kwargs:
            del kwargs['chr'] 

        cmd = " ".join([self.minimac] + 
                       ["--refHaps %s" % self.ref_panel[chrom]] +
                       ["--%s %s" % (k, v) for k, v in kwargs.items()])
        do.run(cmd)
        return True
