#Libs/modules
from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import *
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd


#Variables
#data = pd.read_csv("temperatures.csv")
#data["Date"] = pd.to_datetime(data["Date"])
#data = data.set_index("Date")
#data = data["Mean"]

data = yf.download("TSLA")['Close']

data = validate_series(data)

volatility_detector = VolatilityShiftAD(c=10.0, side="positive", window=30)
anomalies = volatility_detector.fit_detect(data)
plot(data, anomaly=anomalies, anomaly_color="red")
plt.show()
