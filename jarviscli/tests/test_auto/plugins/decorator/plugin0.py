from plugin import plugin, alias, complete


@plugin()
def plugin0(jarvis, s):
    """
    Doku
    """
    jarvis.say("exec")


@plugin(network=True, native="native", python="python", plattform="plattform")
@complete("complete")
@alias("alias")
def plugin1(jarvis, s):
    """help"""
    pass
