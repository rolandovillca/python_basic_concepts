# The __init__.py files are required to make Python treat the directories as containing packages;
# this is done to prevent directories with a common name, such as string,
# from unintentionally hiding valid modules that occur later on the module search path.
# In the simplest case, __init__.py can just be an empty file,
# but it can also execute initialization code for the package or set the __all__ variable, described later.

# Summary:
# Files named __init__.py are used to mark directories on disk as Python package directories.
# If you remove the __init__.py file, Python will no longer look for submodules inside that directory, so attempts to import the module will fail.
# The __init__.py file is usually empty, but can be used to export selected portions of the package under more convenient name, hold convenience functions, etc.


# Files named __init__.py are used to mark directories on disk as Python package directories. If you have the files

# mydir/spam/__init__.py
# mydir/spam/module.py
# and mydir is on your path, you can import the code in module.py as

# import spam.module
# or

# from spam import module
# If you remove the __init__.py file, Python will no longer look for submodules inside that directory, so attempts to import the module will fail.

# The __init__.py file is usually empty, but can be used to export selected portions of the package under more convenient name, hold convenience functions, etc. Given the example above, the contents of the init module can be accessed as

# import spam
