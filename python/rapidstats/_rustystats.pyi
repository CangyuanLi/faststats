from typing import Optional

import polars as pl

ConfidenceInterval = tuple[float, float, float]

def _confusion_matrix(df: pl.DataFrame) -> list[float]: ...
def _bootstrap_confusion_matrix(
    df: pl.DataFrame, iterations: int, z: float, seed: Optional[int]
) -> list[ConfidenceInterval]: ...
def _roc_auc(df: pl.DataFrame) -> float: ...
def _bootstrap_roc_auc(
    df: pl.DataFrame, iterations: int, z: float, seed: Optional[int]
) -> ConfidenceInterval: ...
def _max_ks(df: pl.DataFrame) -> float: ...
def _bootstrap_max_ks(
    df: pl.DataFrame, iterations: int, z: float, seed: Optional[int]
) -> ConfidenceInterval: ...
def _brier_loss(df: pl.DataFrame) -> float: ...
def _bootstrap_brier_loss(
    df: pl.DataFrame, iterations: int, z: float, seed: Optional[int]
) -> ConfidenceInterval: ...
def _positive_ratio(df: pl.DataFrame) -> float: ...
def _bootstrap_positive_ratio(
    df: pl.DataFrame, iterations: int, z: float, seed: Optional[int]
) -> ConfidenceInterval: ...
