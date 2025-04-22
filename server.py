import flwr as fl
from flwr.server.strategy import FedAvg
from flwr.server.server import ServerConfig
import matplotlib.pyplot as plt

accuracies = []

class LoggingFedAvg(FedAvg):
    def aggregate_evaluate(self, rnd, results, failures):
        # Run base aggregation logic
        loss, metrics_agg = super().aggregate_evaluate(rnd, results, failures)

        # Aggregate accuracy manually from client metrics
        accuracies_this_round = [
            res.metrics["accuracy"] for _, res in results if "accuracy" in res.metrics
        ]

        if accuracies_this_round:
            avg_acc = sum(accuracies_this_round) / len(accuracies_this_round)
            print(f"[Round {rnd}] Avg Accuracy: {avg_acc:.4f}")
            accuracies.append((rnd, avg_acc))
        else:
            print(f"[Round {rnd}] No accuracy data.")

        return loss, metrics_agg

def plot_accuracy():
    if not accuracies:
        print("No accuracy data to plot.")
        return
    rounds, accs = zip(*accuracies)
    plt.figure(figsize=(6, 4))
    plt.plot(rounds, accs, marker='o')
    plt.title("Federated Model Accuracy per Round")
    plt.xlabel("Round")
    plt.ylabel("Accuracy")
    plt.ylim(0, 1)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("federated_accuracy.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    strategy = LoggingFedAvg(
        min_fit_clients=5,
        min_evaluate_clients=5,
        min_available_clients=5,
    )
    try:
        fl.server.start_server(
            server_address="localhost:8080",
            config=ServerConfig(num_rounds=5),
            strategy=strategy,
        )
    finally:
        plot_accuracy()
