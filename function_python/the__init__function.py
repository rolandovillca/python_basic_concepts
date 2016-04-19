'''
The primary use of __init__.py is to initialize Python packages.

The __init__.py files are required to make Python treat the directories as
containing packages; this is done to prevent directories with a common name,
such as string, from unintentionally hiding valid modules that occur later
(deeper) on the module search path. In the simplest case, __init__.py can just
be an empty file, but it can also execute initialization code for the package
or set the __all__ variable, described later.

__init__.py will treat the directory it is in as a loadable module.

__init__.py can be empty, as long as it exists.
It indicates that the directory should be regarded as a package.
Of course, __init__.py can also set the appropriate content.

The __init__.py file makes Python treat directories containing it as modules.
Furthermore, this is the first file to be loaded in a module, so you can use it
to execute code that you want to run each time a module is loaded, or specify
the submodules to be exported.

In addition to labeling a directory as a Python package and defining __all__,
__init__.py allows you to define any variable at the package level. Doing so is
often convenient if a package defines something that will be imported
frequently, in an API-like fashion. This pattern promotes adherence
to the Pythonic "flat is better than nested" philosophy.
'''

# Files named __init__.py are used to mark directories on disk as Python package
# directories. If you have the files

# mydir/spam/__init__.py
# mydir/spam/module.py

# Where the mydir is on your path, you can import the code in module.py as

'''
import spam.module

or

from spam import module
'''

# If you remove the __init__.py file, Python will no longer look for submodules
# inside that directory, so attempts to import the module will fail.

# The __init__.py file is usually empty, but can be used to export selected
# portions of the package under more convenient name, hold convenience functions,
# etc. Given the example above, the contents of the init module can be accessed as

'''
import spam
'''