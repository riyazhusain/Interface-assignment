import json
import requests
from texttable import Texttable

environment = {
    'local': 'http://localhost:5000',
    'server': 'http://dummyapi.interface.com'
}
interfaces = ['all', 'GigabitEthernet0/0', 'GigabitEthernet0/1', 'GigabitEthernet0/0', 'Loopback0', 'Loopba']


class ApiClient:
    def __init__(self, interfaces, env):
        self.interfaces = interfaces
        self.headers = {'Content-Type': 'json'}
        self.interface_url = '{}/interface/'.format(environment[env])

    def get_data(self, interface_name):
        '''
        This method hits to the end point given manually in the list of interfaces
        and fetches the response from those end-points and returns it.

        '''
        view_url = self.interface_url + interface_name
        print("Printing table for : " + interface_name)

        response = requests.get(view_url, headers=self.headers)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

    def ascii_table(self):
        """
        This method created a ascii table out of data which is recieved from get_data()
        by show_data in list of diictionaries format i.e. in json format
        """
        try:
            for data in self.interfaces:
                show_data = self.get_data(data)
                t = Texttable()
                t.header(show_data[0].keys())
                t.add_rows([x.values() for x in show_data], header=False)
                print(t.draw())
        except TypeError:
            print("The name of the interface is not Available : {}".format(data))


client_object = ApiClient(interfaces, 'local')
client_object.ascii_table()
