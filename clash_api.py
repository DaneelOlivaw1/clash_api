import yaml
import json
import requests


class ClashController:
    def __init__(self, config_path: str) -> None:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            self.secret = config.get('secret')
            self.external_controller = config.get('external-controller')


    def get_node_list(self):
        url = f"http://{self.external_controller}/proxies"

        payload = {}
        headers = {
        'Authorization': f'Bearer {self.secret}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()

    def switch_node(self, group_name, node_name):
        url = f"http://{self.external_controller}/proxies/{group_name}"

        payload = json.dumps({
            "name": f"{node_name}"
        })
        headers = {
            'Authorization': f'Bearer {self.secret}',
            'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        return response.json()   

    def get_providers_proxies(self):
        url = f"http://{self.external_controller}/providers/proxies"

        payload = {}
        headers = {
        'Authorization': f'Bearer {self.secret}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()

    def get_node_delay(self, node_name):
        url = f"http://{self.external_controller}/proxies/{node_name}"

        payload = {}
        headers = {
        'Authorization': f'Bearer {self.secret}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response_json = response.json()
        delay_history = response_json["history"]
        delay = delay_history[-1]["delay"]
        return delay

    def is_node_alive(self, node_name):
        url = f"http://{self.external_controller}/proxies/{node_name}"

        payload = {}
        headers = {
        'Authorization': f'Bearer {self.secret}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response_json = response.json()
        node_state = response_json["alive"]
        return node_state


if __name__ == "__main__":
    config_path = r"C:\Users\bjtc\.config\clash\config.yaml"
    clash_controller = ClashController(config_path)
    res = clash_controller.is_node_alive("美国-大流量801,723752")
    print(res)