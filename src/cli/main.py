#!/usr/bin/env python


def cli():
    """
    The Gist CLI for executing remote and local py gists.
    \b
    Note: the remote server defaults to https://github.com.
    If a different remote server access is required e.g. (Github
    Enterprise) then run `gist host add https://server.com`.
    
    Github:

    \b
    Gist Commands:
        create      Create a py gist                      # authentication required..
        update      Update a py gist                      # authentication required..
        delete      Delete a py gist                      # authentication required..
        fork        Fork a py gist                        # authentication required..
        ... others

    Gisteren:

    \b
    Query Commands:
        list        Shows indexed py gists                # (global/local)
        add         Add one or many py gists              # (global/local)
        remove      Remove one or many py gists           # (global/local)

    \b
    Action Commands:
        use         Set a py gist as active               # (py gist/file)
        describe    Describe a py gist                    # (py gist/file)

    \b 
    File Commands:
        exec        Execute a file/function in a py gist  # (file/function)
    
    \b
    Helper Commands:
        auth        Authenticate user and generate Gist token

    \b
    Other Commands:
        config      Modify Gisteren configuration
        test        Test Gisteren configuration
        version     Print the cli version information
        alias       Make an alias name for a local py gist

    """
    pass
