from stocksurferbd import PriceData
loader = PriceData()

loader.save_history_csv('ACI', file_name='ACI_history.csv')

from stocksurferbd import CandlestickPlot

cd_plot = CandlestickPlot(csv_path='ACI_history.csv', symbol='ACI')
cd_plot.show_plot(
    xtick_count=120, 
    resample=True, 
    step='3D'
)