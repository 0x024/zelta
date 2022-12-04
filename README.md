# 0x01 项目背景
Zelta注册以进入候补名单并获得免费保证的 NFT。
邮箱+钱包地址：
[zelta.io](url)
# 0x02 环境准备

`mac os ventura Pycharm 
`

`pip3 install web3
`

`pip3 install requests
`

`pip3 install selenium
`

# 0x03 目录结构

```
main.py----运行程序
zelta.db----存放钱包地址及邮箱地址
```
# 0x04 运行方式

## step1: 创建钱包，

1:需要取消`creat_wallet()`前面的注视，

2:需要在creat_db传入钱包数量，例如要创建1000个钱包及`creat_wallet(1000)`

3:`最后运行 python3 main.py`

4:运行过程中会直接写入到sqlite数据库中

```
id -钱包序号
address -钱包地址
private_key -钱包密钥
phrases -钱包助记词
Gmail -邮箱，需要写入自己的邮箱
status -状态值
```

## step2: 通过selenium方式进行注册

1:需要取消`regist_selenium()`前面的注视，

2:`最后运行 python3 main.py`

