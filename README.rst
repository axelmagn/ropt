Ropt
====

Ropt is a tool that helps you interact with REST APIs from the command line.
Curl already does this, and I think everyone should learn to use Curl before
they use Ropt.  It's one of the most powerful tools in the 'nix toolbox.
However, for day to day use, using Curl on REST APIs can feel like driving a
race car to the grocery store.  Think of Ropt as the scooter you drive around
town for errands.  it just feels a little more convenient sometimes.

Note
----

Ropt is in **extremely** early development.  It would be a horrible idea to use
this tool right now.

Url Mode
--------

At its most basic, ropt can be used to craft a HTTP request to a specific URL.::

    Usage:
      ropt [options] [post|put|delete] <url> [<args>...]

This lets you craft HTTP requests with relative ease.
