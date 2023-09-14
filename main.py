from clash_api import ClashController

group_name = "🚀 节点选择"
config_path = r"C:\Users\bjtc\.config\clash\config.yaml"
clash_controller = ClashController(config_path)



providers_proxies = clash_controller.get_providers_proxies()
nodes = providers_proxies["providers"][group_name]
for node in nodes["proxies"]:
    node_satate = clash_controller.is_node_alive(node["name"])
    print(node["name"], node_satate)