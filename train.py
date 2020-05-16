import argparse
import random
import mlflow

def main(alpha, beta):
    params = {'alpha': alpha, 'beta': beta}
    loss = random.random()
    print(f"loss: {loss}")
    with open("output.txt", 'w') as f:
        f.write("Finished!")
    with mlflow.start_run():
        mlflow.log_params(params)
        mlflow.log_metric("loss", loss)
        mlflow.log_artifact("output.txt")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('alpha', type=float)
    parser.add_argument('beta', type=float)

    args = parser.parse_args()
    main(args.alpha, args.beta)
