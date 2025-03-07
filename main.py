import yfinance as yf

ticker = 'GOOGL'
data = yf.download(ticker, start="2020-01-01", end="2022-03-06")
print(data.head())  # Check if data is being fetched correctly

# Part 2: Load model and predict
def catch_data():
    #model = load_model("LSTM_GRU_model.keras")
   # data = prepare_data()
  #  predictions = sc.inverse_transform(model.predict(x_train) )
   # predictions = model.predict(data)
    pd.DataFrame(data).to_csv("data.csv", index=False)


if __name__ == "__main__":
    catch_data()