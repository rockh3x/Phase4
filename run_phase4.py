from flwr.simulation import start_simulation, SimulationConfig
from client import FlowerClient
from utils import create_non_iid

# Prepare partitions
_ = create_non_iid(num_clients=5)

def client_fn(cid: str):
    import sys
    sys.argv = [sys.argv[0], str(cid)]
    from client import FlowerClient
    return FlowerClient()

if __name__ == "__main__":
    start_simulation(
        client_fn=client_fn,
        num_clients=5,
        config=SimulationConfig(num_rounds=5),
    )
