from pathlib import Path
import pytest

from src.visualization import plot_prices, plot_compare


def test_plot_prices_creates_file(tmp_path: Path):
    result = plot_prices("Gold", [1, 2, 3], output_dir=tmp_path)
    assert result.file_path.exists()
    assert result.file_path.suffix == ".png"


def test_plot_compare_creates_file(tmp_path: Path):
    result = plot_compare([1, 2, 3], [1, 2], output_dir=tmp_path)
    assert result.file_path.exists()
    assert result.file_path.suffix == ".png"


def test_plot_prices_empty_data_raises(tmp_path: Path):
    with pytest.raises(ValueError):
        plot_prices("Gold", [], output_dir=tmp_path)
