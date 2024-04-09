# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/compat.ipynb.

# %% auto 0
__all__ = []

# %% ../nbs/compat.ipynb 1
try:
    from catboost import CatBoostRegressor
except ImportError:

    class CatBoostRegressor:
        def __init__(self, *args, **kwargs):  # noqa: ARG002
            raise ImportError("Please install catboost to use this model.")


try:
    from lightgbm import LGBMRegressor
except ImportError:

    class LGBMRegressor:
        def __init__(self, *args, **kwargs):  # noqa: ARG002
            raise ImportError("Please install lightgbm to use this model.")


try:
    from window_ops.shift import shift_array
except ImportError:

    def shift_array(*_args, **_kwargs):  # noqa: ARG002
        raise Exception


try:
    from xgboost import XGBRegressor
except ImportError:

    class XGBRegressor:
        def __init__(self, *args, **kwargs):  # noqa: ARG002
            raise ImportError("Please install xgboost to use this model.")