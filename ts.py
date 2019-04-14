import tushare as ts
import pandas as pd

pro.query('trade_cal', start_date='20180101', end_date='20190401')

def get_trade_cal(start_date, end_date):
    """
    获取交易日历数据
    :param start_date: 20180101
    :param end_date: 20190401
    :return: 时间序列    """
    #调用交易日历接口
    df = pro.trade_cal(exchange='', start_date=start_date, 
   end_date=end_date, is_open='1')
    #截取交易时间列
    trade_days = df['cal_date']
    return trade_days.values


def get_daily(trade_days):
    """
    获取日线行情数据
    :param trade_days: 交易日期序列
    :return:
    """
    #遍历交易日期序列
    for day in trade_days:
        #调用日线行情接口
        df = pro.daily(trade_date=day)
        #保存日线行情到CSV文件
        df.to_csv('./data/daily/daily_{}.csv'.format(day))

def main():
    """
    程序入口
    :return:
    """
    trade_days = get_trade_cal("20180101", "20181231")
    get_daily(trade_days)

if __name__ == '__main__':
    main()