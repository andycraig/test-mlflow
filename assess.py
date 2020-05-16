import mlflow

if __name__ == '__main__':
    runs = mlflow.search_runs(order_by=['metrics.loss'])
    print(runs.iloc[0])

