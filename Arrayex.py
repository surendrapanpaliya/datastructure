#Example: Storing VM Configuration Parameters in Azure
import numpy as np

# 2D array of VM configurations: [VM Name, CPU Cores, Memory (GB)]
vm_configs = np.array([
    ['vm1', 2, 4],
    ['vm2', 4, 8],
    ['vm3', 8, 16]
])

# Iterate over the array to deploy VMs with specified configurations
for config in vm_configs:
    vm_name, cpu_cores, memory_gb = config
    print(f"Deploying {vm_name} with {cpu_cores} CPU cores and {memory_gb} GB memory")

# Code to deploy VM in Azure

