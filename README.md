# tushare
我们想要实现的最终目标是获取2018年全年的股票交易数据，Tushare提供的两个数据接口可以满足我们的需求，接口分别是交易日历和日线行情。


接口介绍


一、交易日历接口。

接口：trade_cal
描述：获取各大交易所交易日历数据,默认提取的是上交所。

输入参数

名称	类型	必选	描述
exchange	str	N	交易所 SSE上交所 SZSE深交所
start_date	str	N	开始日期
end_date	str	N	结束日期
is_open	int	N	是否交易 0休市 1交易

输出参数

名称	类型	描述
exchange	str	交易所 SSE上交所 SZSE深交所
cal_date	str	日历日期
is_open	int	是否交易 0休市 1交易
pretrade_date	str	上一个交易日

二、日线行情接口。

接口：daily
更新时间：交易日每天15点～16点之间
调取说明：每分钟内最多调取200次，超过5000积分无限制

描述：获取股票行情数据，包含了前后复权数据

输入参数

名称	类型	必选	描述
ts_code	str	N	股票代码（二选一）
trade_date	str	N	交易日期（二选一）
start_date	str	N	开始日期(YYYYMMDD)
end_date	str	N	结束日期(YYYYMMDD)
注：日期都填YYYYMMDD格式，比如20181010

输出参数

名称	类型	描述
ts_code	str	股票代码
trade_date	str	交易日期
open	float	开盘价
high	float	最高价
low	float	最低价
close	float	收盘价
pre_close	float	昨收价
change	float	涨跌额
pct_chg	float	涨跌幅 （未复权）
vol	float	成交量 （手）
amount	float	成交额 （千元）

