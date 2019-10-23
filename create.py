from openstack import connection
import time


def list_flavors(conn,name):
    # print("List Flavors:")

    for flavor in conn.compute.flavors():
        if(flavor.name == name):
            return flavor

def list_images(conn,name):
    # print("List Images:")

    for image in conn.compute.images():
        if(image.name == name):
            return image


def create_instance(conn,instance_name,flavor_name,image_name,network_id):


    return conn.create_server(instance_name, image=image, flavor=flavor, auto_ip=True,
                ips=None, ip_pool=None, root_volume=None, 
                terminate_volume=False, wait=False, timeout=180,
                reuse_ips=True, network=network_id, boot_from_volume=False,
                volume_size='50', boot_volume=None, volumes=None, 
                nat_destination=None, group=None)



conn = connection.Connection(
    region_name='RegionOne',
    auth=dict(
        auth_url='http://192.168.0.18:5000/v3',
        username='admin',
        password='ahKieng2cuhul7Cu',
        project_id='5a55fd1d28ec42fdb71441fccfb62c65',
        user_domain_id='998162117f9148e98d5f519524df217f'),
    compute_api_version='2',
    identity_interface='internal')



instance_name = 'python_sdk'

flavor_name = 'm1.tiny'
flavor = list_flavors(conn,flavor_name)

image_name = 'bionic'
image = list_images(conn,image_name)

network_id = '91b6ab5d-e189-4783-8e1f-a1f3d8360d32'


instance = create_instance(conn,instance_name,flavor_name,image_name,network_id)

print('Instancia com nome {0} criada com sucesso'.format(instance.name))
print("Aguardando 10 segundos para deletar a instancia...")
time.sleep(10)

conn.delete_server(instance.id)
