<h1 align="center">web3兼职:rooster: </h1>
<p align="center">========================================
<p align="center">心有山海，静而不争</p>
<p align="center">There are mountains and seas in the heart 
<p align="center">quiet but without contention 
<p align="center">如果喜欢我，您的支持将给予我无限分享下去的动力
<p align="center">========================================
<p align="center">:dog2: Email | zw97073966@gmail.com</p>
<p align="center">:cow: Github | https://github.com/0x024</p>
<p align="center">:owl: Twitter | https://twitter.com/_0x024</p>
<p align="center">:cat2: Mirror | https://mirror.xyz/1x024.eth</p>
<p align="center">:rabbit2: ERC-20 | 0x14bCa363445462082101164Eff599F83fbBEbab1</p></p>
<p align="center">========================================




## 0x01 项目背景
Zelta NFT免费领取 填写邮箱和马蹄链钱包地址不用gas费（Polygon网络） 总量好像是9999个 过程是手动的，因此 NFT 可能需要 2-3 天才能在您的钱包中显示。 免费的可以撸一撸：

[zelta.io](url)
## 0x02 环境准备

```

mac os ventura Pycharm 
pip3 install web3
pip3 install requests
pip3 install selenium
git clone git@github.com:0x024/zelta.git
```
## 0x03 目录结构

```
main.py----运行程序
zelta.db----存放钱包地址及邮箱地址
```
## 0x04 运行方式

### step1: 创建钱包，

1:取消`creat_wallet()`前面的注视，

2:在creat_db传入钱包数量，例如要创建1000个钱包及`creat_wallet(1000)`

3:最后运行 `python3 main.py`

4:运行过程中会直接写入到sqlite数据库中

```
id -钱包序号
address -钱包地址
private_key -钱包密钥
phrases -钱包助记词
Gmail -邮箱，需要写入自己的邮箱
status -状态值 "ALREADY_EXISTS"和"User signed up successfully"
```

### step2: 通过selenium方式进行注册

1:取消`regist_selenium()`前面的注视，

2:运行 `python3 main.py`  
 
3:运行过程中，会调用起来chrome，然后自动点击注册，自动填写邮箱地址，自动填写钱包地址，自动提交，且注册的结果，会直接写入到数据库中,status=1代表注册成功

PS:需要提前准备好chromedriver环境，可以自行google
同时采用selenium的方式，点击频率过高，会出发google的验证码机制，所以可以通过更换vpn地址或者待会运行的方式

### step3: 通过requests方式进行注册

1:取消`regist_post()`前面的注视，

2:运行 `python3 main.py`  

3:运行结果会直接在终端输出，该方式运行速度快，且经测试不会触发google的验证码机制






































