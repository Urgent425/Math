import argparse
from io import StringIO
import sys

import pandas as pd
import matplotlib.pyplot as plt
import requests

FRED_CSV_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXHTUS"

def fetch_exchange_rate_csv(url: str) -> pd.DataFrame:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = pd.read_csv(StringIO(response.text))
    data["DATE"] = pd.to_datetime(data["DATE"], errors="coerce")
    data["DEXHTUS"] = pd.to_numeric(data["DEXHTUS"], errors="coerce")
    return data.dropna(subset=["DATE", "DEXHTUS"]).rename(
        columns={"DATE": "date", "DEXHTUS": "gourdes_per_usd"}
    )


def plot_devaluation(data: pd.DataFrame, output_path: str | None) -> None:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data["date"], data["gourdes_per_usd"], color="tab:blue")
    ax.set_title("Dévaluation de la gourde haïtienne face au dollar (USD)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Gourdes par dollar (USD)")
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()
    if output_path:
        fig.savefig(output_path, dpi=300)
    else:
        plt.show()


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Télécharge la série DEXHTUS depuis FRED et trace la courbe de dévaluation."
        )
    )
    parser.add_argument(
        "--output",
        help="Chemin du fichier image à enregistrer (ex: courbe_gourde.png).",
    )
    args = parser.parse_args()

    try:
        data = fetch_exchange_rate_csv(FRED_CSV_URL)
    except requests.RequestException as exc:
        print(
            "Erreur lors du téléchargement des données. Vérifiez votre connexion Internet.",
            file=sys.stderr,
        )
        raise SystemExit(1) from exc

    if data.empty:
        print("Aucune donnée trouvée dans la série FRED.", file=sys.stderr)
        raise SystemExit(1)

    plot_devaluation(data, args.output)


if __name__ == "__main__":
    main()