from utils.all_utils import prepare_data,save_plot
import pandas as pd
from utils.model import Perceptron
import logging
import os

gate = "or"
log_dir = "logs"
os.mkdir(log_dir)
logging.basicConfig(
    filename=os.path.join(log_dir,"running_logs.log"),
    level=logging.INFO,
    format='[%(asctime)s: %(levelname)s: %(module)s]:%(message)s',
    filemode='a'


)

def main(data,modelName,plotName,eta,epochs):
    df_OR = pd.DataFrame(OR)
    gate 
    logging.info(f"this is the raw dataset:{df_OR}")
    X, y = prepare_data(df_OR)

    

    model_or = Perceptron(eta=eta, epochs=epochs)
    model_or.fit(X, y)

    _ = model_or.total_loss()

    model_or.save(filename="or.model", model_dir="model_or")
    save_plot(df_OR,model_or,filename= plotName)



if __name__ == "__main__":
    OR = {
    "x1": [0,0,1,1],
    "x2": [0,1,0,1],
    "y" : [0,1,1,1]
}
    ETA = 0.3
    EPOCHS = 10
    try:
        logging.info(f">>>>starting trainin>>>>> for {gate}")
        main(data=OR,modelName="or.model",plotName="or.png",eta=ETA,epochs=EPOCHS)
        logging.info(f"<<<<done training>>>>>>>> for {gate}")
    except Exception as e:
        logging.exception(e)
        raise e










