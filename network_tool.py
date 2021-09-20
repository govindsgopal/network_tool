import os
interface_lst = []
def menu():
	print("1.Assign ip address")
	print("2.Delete IP address")
	print("3.Display ip address")
	print("4.Display all interface")
	print("5.Configure routing")
	print("6.Turn on/off interface")
	print("7.Add ARP entry")
	print("8.Delete ARP entry")
	print("9.Restart network")
	print("10.Change host name")
	print("11.Add DNS server entry")
	print("12.Exit")

def ip_assign():
	ip = input('\tEnter ip address to add on interface \t ')
#	interface = os.popen('ip l | cut -d":" -f2 | tr -d " "').read()
#	interfaces = interface.split('\n')
#	interfaces.remove('altnameenp2s1')
#	interface_lst = interfaces[0:-2:2]
#	print(interface_lst)
	display_interface()
	choice = input("\tEnter your choice of interface \t  ")
	command = f'sudo ip addr add {ip} dev {choice}'
	result = os.popen(command).read() 
	print(result)
	print("\tIP changed succesfully!!")

def delete_ip():
	display_ip()
	ip = input("Enter ip address to delete from interface : ")
	display_interface()
	choice = input("Enter the interface to delete ip from :  ")
	command = f'sudo ip address del {ip} dev {choice}'
	result = os.popen(command).read() 
	print(result)
	print("\tIP deleted succesfully!!")
	
def display_ip():
	command = f'ip -c -br address'
	result = os.popen(command).read()
	print(result)
def display_interface():
	interface = os.popen('ip l | cut -d":" -f2 | tr -d " "').read()
	interfaces = interface.split('\n')
	interfaces.remove('altnameenp2s1')
	interface_lst = interfaces[0:-2:2]
	print(interface_lst)
def config_routing():
	network_addr = input('\tEnter network Address with /mask : ')
	getway_ip = input('\tEnter Gateway ip address : ')
	command = f'ip r add {network_addr} via {getway_ip}'
	result = os.popen(command).read()
	print(result)
	print("\tRouting configuration completed successfully!!")
def switch_interface():
	print("\t1.Turn on interface ")
	print("\t2.Turn off interface ")
	choice = input("\tEnter your choice :  ")
	display_interface()
	interface = input("\tEnter the interface to turn on or off :  ")
	if choice == '1':
		command = f'sudo ip link set dev {interface}  up'
		result = os.popen(command).read()
		print(result)
		print(f"\t\tInterface {interface} has been turned on succesfully!!")
	elif choice == '2':
		command = f'sudo ip link set dev {interface}  down'
		result = os.popen(command).read()
		print(result)
		print(f"\t\tInterface {interface} has been turned off succesfully!!")
def add_arp():
	ip = input('Enter ip address  : ')
	display_interface()
	interface = input("Enter your choice of interface :")
	arp_cache = os.popen('ip n show | cut -d " " -f5').read()
	command = f'ip n add {ip} lladdr {arp_cache} dev {interface} nud permanent'
	res = os.popen(command).read()
	print("\t\tARP ENTRY added succesfully!!")
def delete_arp():
	ip = input("Enter ip address  : ")
	display_interface()
	interface = input("Enter your choice of interface :  ")
	arp_cache = os.popen('ip n show | cut -d " " -f5').read()
	command = f'ip n del {ip} dev {interface}'
	res = os.popen(command).read()
	print("\t\tARP Entry deleted successfully")
def restart_network():
	cmd = 'sudo systemctl restart networking'
	os.popen(cmd).read()
	print("Network restarted succesfully")
	cmd2 = 'sudo systemctl status networking'
	print(os.popen(cmd2).read())
def change_host_name():
	host_name = input("Enter new host name :")
	cmd = f'hostnamectl set-hostname {host_name}'
	os.popen(cmd).read()
	print(f"New host name {host_name} was applied succesfully")
def add_DNS_entry():
	 print('adding dns server.....')
	 pass
while True:
	menu()
	ch = input("Enter the choice\t")
	if ch == '1':
		ip_assign()
		
	elif ch == '2':
		delete_ip()
	elif ch == '3':
		display_ip()
	elif ch == '4':
		display_interface()
	elif ch == '5':
		config_routing()
	elif ch == '6':
		switch_interface()
	elif ch == '7':
		add_arp()
	elif ch == '8':
		delete_arp()
	elif ch == '9':
		restart_network()
	elif ch == '10':
		change_host_name()
	elif ch == '11':
		add_DNS_entry()
	elif ch == '12':
		break
	else:
		print("Invalid input, try again!")
