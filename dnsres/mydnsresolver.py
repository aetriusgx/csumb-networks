import dns.resolver
import sys

# two inputs:
# 	- domain name
# 	- a type
def resolver(domain, type):
	try:
		valid_types = ["A", "NS", "MX"]

		# check if type is valid
		if (type not in valid_types):
			print("error")
			return
		
		# use resolver
		answer = dns.resolver.resolve(domain, type)
		# open file to write
		file = open("mydnsresolver_output.txt", "a")
		# write arg info into file & cmd
		file.write(str("name: " + domain + "\ttype: " + type + "\n"))
		print("name: " + domain + "\ttype: " + type + "\n")
		
		for a in answer:
			# write response into file and cmd
			file.write(str(a))
			file.write("\n")
			print(a)
		# newline to separate entries
		file.write("\n")
		file.close()
	# if fail
	except:
		print("failed to execute")
		

def main():
	domain = sys.argv[1]
	type = sys.argv[2]

	resolver(domain, type)

main()