
from pssh.clients import ParallelSSHClient
from pssh.config import HostConfig

# split the host list with comma
def split_hosts(host_list):
  new_host_list = []
  for value in host_list.split(','):
    new_host_list.append(value)
  return new_host_list

# output seperator
def seperator(host):
  print(host + " -------------------------------------------------------------------> execution completed")

# need to create hostconfig for pssh
def create_config(host_list):
  new_host_list = []
  host_config_list = []
  for host in host_list:
    split_host = host.split('@')
    host_config_list.append(HostConfig(user=split_host[0]))
    new_host_list.append(split_host[1])
  return (new_host_list, host_config_list)

# output controller to show desired level of verbose
def output_controller(output):
  for host_ip in output.keys():
    seperator(host_ip)
  check_ouptut = input("print output for (y/n): ")
  for host_ip, value in output.items():
    seperator(host_ip)
    if check_ouptut == "y":
      for stdout in value['stdout']:
        print(host_ip + " :: " + stdout)
    else:
      print("Proceeding without printing output")

# creates a host based dictionary to store ssh execution property data
def output_formatter(host_outputs):
  output_dict = {}
  for host_output in host_outputs:
    output_dict[host_output.host] = {'exit_code': host_output.exit_code, 'stdout': list(host_output.stdout)}
  return output_dict

# executes command on multiple hosts simultaneously
def exec_command(host_string, command):
  host_tuple = create_config(split_hosts(host_string))
  host_list = host_tuple[0]
  host_config = host_tuple[1]
  client = ParallelSSHClient(host_list, host_config=host_config)
  output = client.run_command(command)
  output_controller(output_formatter(output))

def run():
  option = "y"
  while option == "y":
    host_string = input("Enter comma seperated hosts example (username@host1,username@host2): ")
    command = input("Enter command to execute: ")
    if command != "exit":
      print("executing command: ")
      output = exec_command(host_string, command)
      
    option = input("Press (y/n) to start again : ")

if __name__ == '__main__':
  run()