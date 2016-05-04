import logging

# EXAMPLE 1: Tracking events in a software application, this is known as logging
# ==============================================================================
# print a log message to the console.
logging.warning('This is a wanting message!')
print


# EXAMPLE 2: We can easily output to a file:
# ==============================================================================
logging.basicConfig(filename='program.log',level=logging.DEBUG)
logging.warning('An example message.')
logging.warning('Another message')
print


# EXAMPLE 3: Level of severity:
# ==============================================================================
# These are the levels of severity:
# DEBUG     Information only for problem diagnostics    
# INFO      The program is running as expected
# WARNING   Indicate something went wrong
# ERROR     The software will no longer be able to function
# CRITICAL  Very serious eror
#
# The default logging level is warning, which implies that other messages are ignored.

logging.basicConfig(level=logging.DEBUG)
print


# EXAMPLE 4: Time in Log:
# ==============================================================================

# You can enable time for logging using this line of code:
logging.basicConfig(format='%(asctime)s %(message)s')

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.info('Logging app started')
logging.warning('An example logging message.')
logging.warning('Another log message')
print