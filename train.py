import argparse
import random
import mlflow

def main(alpha):
    with mlflow.start_run():
        mlflow.log_param("alpha", alpha)

        loss = random.random()
        print(f"loss: {loss}")
        mlflow.log_metric("loss", loss)

        with open("output.txt", 'w') as f:
            f.write("Finished!")
        mlflow.log_artifact("output.txt")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('alpha', type=float)

    args = parser.parse_args()
    main(args.alpha)
