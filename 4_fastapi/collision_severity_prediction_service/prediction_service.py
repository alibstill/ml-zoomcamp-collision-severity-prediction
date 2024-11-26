import pickle
from pathlib import Path
import xgboost as xgb


class PredictionService:

    def __init__(self, model_file_name: str) -> None:
        self.model_file_name = model_file_name
        base_path = Path(__file__).parent
        self.dv = None
        self.model = None
        self.model_file_path = base_path / "collision_severity_models" / model_file_name
        self.load_file()

    def load_file(self) -> None:
        if self.model_file_path.exists() and self.model_file_path.is_file():
            with open(self.model_file_path, mode="rb") as model_file:
                dv, model = pickle.load(model_file)
                self.dv = dv
                self.model = model
        else:
            raise FileNotFoundError(f"Filepath: {self.model_file_path}")

    def predict_severity(self, collision: dict) -> tuple[float, str]:
        X_new = self.dv.transform([collision])
        dx = xgb.DMatrix(X_new, feature_names=list(self.dv.get_feature_names_out()))

        severity_pred = self.model.predict(dx)
        is_severe_collision = "Yes" if severity_pred >= 0.5 else "No"
        return severity_pred, is_severe_collision
