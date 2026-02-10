from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt


@dataclass(frozen=True)
class PlotResult:
    """Metadata for a generated plot."""
    file_path: Path
    title: str


def _ensure_output_dir(output_dir: str | Path) -> Path:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    return out


def _to_list(values: Iterable[float]) -> List[float]:
    values_list = list(values)
    if not values_list:
        raise ValueError("No price data provided for plotting.")
    return values_list


def plot_prices(
    metal_name: str,
    prices: Iterable[float],
    *,
    output_dir: str | Path = "output",
    filename: Optional[str] = None,
    show: bool = False,
) -> PlotResult:
    """
    Plot a single metal price series and save it as PNG.
    X-axis: Day index (1..N)
    Y-axis: Price
    """
    data = _to_list(prices)
    out_dir = _ensure_output_dir(output_dir)

    safe_name = metal_name.strip().lower().replace(" ", "_")
    file_name = filename or f"{safe_name}_prices.png"
    file_path = out_dir / file_name

    days = list(range(1, len(data) + 1))

    plt.figure()
    plt.plot(days, data, marker="o")
    plt.title(f"{metal_name} Price Trend")
    plt.xlabel("Day")
    plt.ylabel("Price")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.tight_layout()

    plt.savefig(file_path, dpi=150)

    if show:
        plt.show()

    plt.close()

    return PlotResult(file_path=file_path, title=f"{metal_name} Price Trend")


def plot_compare(
    gold_prices: Iterable[float],
    silver_prices: Iterable[float],
    *,
    output_dir: str | Path = "output",
    filename: str = "gold_vs_silver.png",
    show: bool = False,
) -> PlotResult:
    """
    Plot gold vs silver on the same chart and save as PNG.
    If lengths differ, each series uses its own day index.
    """
    gold = _to_list(gold_prices)
    silver = _to_list(silver_prices)

    out_dir = _ensure_output_dir(output_dir)
    file_path = out_dir / filename

    gold_days = list(range(1, len(gold) + 1))
    silver_days = list(range(1, len(silver) + 1))

    plt.figure()
    plt.plot(gold_days, gold, marker="o", label="Gold")
    plt.plot(silver_days, silver, marker="o", label="Silver")
    plt.title("Gold vs Silver Price Trend")
    plt.xlabel("Day")
    plt.ylabel("Price")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()
    plt.tight_layout()

    plt.savefig(file_path, dpi=150)

    if show:
        plt.show()

    plt.close()

    return PlotResult(file_path=file_path, title="Gold vs Silver Price Trend")

