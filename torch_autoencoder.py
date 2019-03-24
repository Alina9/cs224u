import pandas as pd
import torch
import torch.nn as nn
import torch.utils.data
from torch_model_base import TorchModelBase
from utils import progress_bar

__author__ = "Christopher Potts"
__version__ = "CS224u, Stanford, Spring 2019"


class TorchAutoencoder(TorchModelBase):
    def __init__(self, **kwargs):
        super(TorchAutoencoder, self).__init__(**kwargs)

    def define_graph(self):
        return nn.Sequential(
            nn.Linear(self.input_dim_, self.hidden_dim),
            self.hidden_activation,
            nn.Linear(self.hidden_dim, self.output_dim_))

    def fit(self, X):
        # Data prep:
        self.input_dim_ = X.shape[1]
        self.output_dim_ = X.shape[1]
        # Dataset:
        X_tensor = self.convert_input_to_tensor(X)
        dataset = torch.utils.data.TensorDataset(X_tensor, X_tensor)
        dataloader = torch.utils.data.DataLoader(
            dataset, batch_size=self.batch_size, shuffle=True)
        # Graph
        self.model = self.define_graph()
        self.model.to(self.device)
        # Optimization:
        loss = nn.MSELoss()
        optimizer = self.optimizer(self.model.parameters(), lr=self.eta)
        # Train:
        for iteration in range(1, self.max_iter+1):
            epoch_error = 0.0
            for X_batch, y_batch in dataloader:
                X_batch = X_batch.to(self.device)
                y_batch = y_batch.to(self.device)
                batch_preds = self.model(X_batch)
                err = loss(batch_preds, y_batch)
                epoch_error += err.item()
                optimizer.zero_grad()
                err.backward()
                optimizer.step()
            self.errors.append(epoch_error)
            progress_bar(
                "Finished epoch {} of {}; error is {}".format(
                    iteration, self.max_iter, err))
        # Hidden representations:
        with torch.no_grad():
            H = self.model[1](self.model[0](X_tensor))
            return self.convert_output(H, X)

    def predict(self, X):
        with torch.no_grad():
            X_tensor = self.convert_input_to_tensor(X)
            X_pred = self.model(X_tensor)
            return self.convert_output(X_pred, X)

    def convert_input_to_tensor(self, X):
        if isinstance(X, pd.DataFrame):
            X = X.values
        X = torch.tensor(X, dtype=torch.float)
        X = X.to(self.device)
        return X

    @staticmethod
    def convert_output(X_pred, X):
        X_pred = X_pred.cpu().numpy()
        if isinstance(X, pd.DataFrame):
            X_pred = pd.DataFrame(X_pred, index=X.index)
        return X_pred


def simple_example():
    import numpy as np

    np.random.seed(seed=42)

    def randmatrix(m, n, sigma=0.1, mu=0):
        return sigma * np.random.randn(m, n) + mu

    rank = 20
    nrow = 1000
    ncol = 100

    X = randmatrix(nrow, rank).dot(randmatrix(rank, ncol))
    ae = TorchAutoencoder(hidden_dim=rank, max_iter=200)
    H = ae.fit(X)
    X_pred = ae.predict(X)
    mse = (0.5*(X_pred - X)**2).mean()
    print("\nMSE between actual and reconstructed: {0:0.06f}".format(mse))
    print("Hidden representations")
    print(H)
    return mse


if __name__ == '__main__':
   simple_example()
