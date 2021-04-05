from communicator import Client, Server


client_obj = Client("localhost", 8081)
server_obj = Server("localhost", 8082)

client_obj.generate_prime()
server_obj.get_prime(client_obj.prime)
print('Client prime:', client_obj.prime)
print('Server prime:', server_obj.prime)
print(80*'#')

client_obj.generate_base()
server_obj.get_base(client_obj.base)
print('Client base:', client_obj.base)
print('Server base:', server_obj.base)
print(80*'#')

client_s = client_obj.generate_local_secret()
server_s = server_obj.generate_local_secret()
print('Client secret: ', client_s)
print('Server secret: ', server_s)
client_obj.get_secret(server_s)
server_obj.get_secret(client_s)
print(80*'#')


print('Client shared secret:', client_obj._Connector__shared_secret)
print('Server shared secret:', server_obj._Connector__shared_secret)

