from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, UnknownHostException, ConnectionErrorException

client = ParallelSSHClient(['1.1.1.1', '2.2.2.2'], user='user', password='pass')

try:
    output = client.run_command('ls -ltrh ~/')
except (AuthenticationException, UnknownHostException, ConnectionErrorException) as ex:
    print ex

print '============ Result ==========='
print output
