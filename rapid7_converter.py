#!/usr/bin/python3

import ipaddress
import fileinput

total = 0

# Let's standardize the format some
for line in fileinput.input(['rapid7.txt'], inplace=True):
	print(line.replace(', ', '\n'), end='') # Replace commas with newlines
for line in fileinput.input(['rapid7.txt'], inplace=True):
	print(line.replace(' - ', '-'), end='') # Remove spaces around the dashes
for line in fileinput.input(['rapid7.txt'], inplace=True):
	if line.strip() != '': 					# Remove blank lines
		print(line.strip())

with open('rapid7.txt') as f:
	print("----- Space Delimited (Nmap/masscan) ----")
	lines = f.readlines()
	last = lines[-1]
	for line in lines:
		if "-" in line:
			begin = line.split('-')[0]
			begin = begin.strip()
			end = line.split('-')[1]
			end = end.strip()

			begin = ipaddress.IPv4Address(begin) - 1
			end = ipaddress.IPv4Address(end) + 1

			subnets = [ipaddr for ipaddr in ipaddress.summarize_address_range(begin,end)]

			for subnet in subnets:
				total += ipaddress.ip_network(subnet).num_addresses
				if line is last:
					print(subnet, end='')
				else:
					print(subnet, end=' ')


		else:
			total += 1
			if line is last:
				print(line.strip(), end='')
			else:
				print(line.strip(), end=' ')

	print('\n\n')

with open('rapid7.txt') as f:
	print("----- Comma Delimited ----")
	lines = f.readlines()
	last = lines[-1]
	for line in lines:
		if "-" in line:
			begin = line.split('-')[0]
			begin = begin.strip()
			end = line.split('-')[1]
			end = end.strip()

			begin = ipaddress.IPv4Address(begin) - 1
			end = ipaddress.IPv4Address(end) + 1

			subnets = [ipaddr for ipaddr in ipaddress.summarize_address_range(begin,end)]

			for subnet in subnets:
				if line is last:
					print(subnet, end='')
				else:
					print(subnet, end=',')


		else:
			if line is last:
				print(line.strip(), end='')
			else:
				print(line.strip(), end=',')

	print('\n\n')


with open('rapid7.txt') as f:
	print("----- Newline Delimited ----")
	lines = f.readlines()
	for line in lines:
		if "-" in line:
			begin = line.split('-')[0]
			begin = begin.strip()
			end = line.split('-')[1]
			end = end.strip()

			begin = ipaddress.IPv4Address(begin) - 1
			end = ipaddress.IPv4Address(end) + 1

			subnets = [ipaddr for ipaddr in ipaddress.summarize_address_range(begin,end)]

			for subnet in subnets:
				print(subnet)


		else:
			print(line.strip())
	print('\n')

print("Total addresses = " + str(total))
