import yfinance as yf
import pandas as pd

ticker = 'GOOGL'
data = yf.download(ticker, start="2020-01-01", end="2022-03-06")
print(data.head())  # Check if data is being fetched correctly

# Part 2: Load model and predict
def catch_data():
    #model = load_model("LSTM_GRU_model.keras")
   # data = prepare_data()
  #  predictions = sc.inverse_transform(model.predict(x_train) )
   # predictions = model.predict(data)
    if data.empty:
      raise ValueError(f"Failed to fetch data for ticker {ticker}")
    else:
      pd.DataFrame(data).to_csv("data.csv", index=False)


if __name__ == "__main__":
    catch_data()
