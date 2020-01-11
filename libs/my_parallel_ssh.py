from pssh.pssh_client import ParallelSSHClient
from pssh.exceptions import AuthenticationException, UnknownHostException, ConnectionErrorException

client = ParallelSSHClient(['10.2.6.19', '10.2.6.20'], user='em7admin', password='em7admin')

try:
    output = client.run_command('ls -ltrh ~/')
except (AuthenticationException, UnknownHostException, ConnectionErrorException) as ex:
    print ex

print '============ Result ==========='
print output
