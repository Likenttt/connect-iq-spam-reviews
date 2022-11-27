# Connect IQ 中的虚假评论 Spam Reviews In Connect IQ

让我们看看 Connect IQ Store 里某个应用下有多少虚假评价? 看见水军都有谁
Let‘s calculate the amount of spam reviews of certain app in connect iq store?This repo will scan the trending apps to get the amount and contents of reviews under some app.

- [English Version](./README-en.md)

## 为什么做这个仓库?

我个人早期开发 Connect IQ 应用是为了娱乐, 全世界用户都能使用我创作的软件, 偶尔有人请我喝杯咖啡, 这已然令我很快乐.

现在我为了生存以盈利为目的开发 Connect IQ 应用, 我向来不耻于谈钱, 付费意味着对应用有更高的要求, 对产品售后有更大的责任, 意味着要摆脱之前“爱用用,不用卸载就是了,我没有过多时间来完善”这样的业余想法.

但是, 在经济利益的驱使下, 代理国外开发者的应用的两个人(佳明运动营、佳明宝典)开始兴风作浪, 他们不仅伤害了我的公平竞争的权利, 更是破坏了应用市场这个公平公正的竞争规则. 我个人表示要坚决与他们斗争到底, 辛勤创作、公平竞争的中国开发者必定会支持我, 享受 Connect IQ 应用市场的广大消费者必定支持我

欢迎来围观他们的恶劣行径 https://li2niu.com/spamreviews

## 这个仓库做了什么?

欢迎提交 pr

- 统计某个应用下的评论数量、评论的用户名和他们的评论次数.
- todo: 监控 Trend Apps 的评论数量和评论内容
- todo: 监控高频出现的广告词

## 如何使用

```
git clone https://github.com/Likenttt/connect-iq-spam-reviews

pip install -r requirements.txt

python scripts/main.py https://apps.garmin.cn/en-US/apps/02d16e10-84dc-46aa-8edb-c42834c9b907
```

## 输出示例

### JumpJump 跳绳

```
python scripts/main.py https://apps.garmin.cn/zh-CN/apps/dc6ceca8-6ec6-49f2-b711-4ebc0d347177

```

------------------------应用:「JumpJump 跳绳」日期产生评价次数排名----------------------------
------------------------APP:「JumpJump 跳绳」Reviews Generated on Date Order by Ammount----------------------------
2022 年 11 月 16 日 产生了:7 条评论
2022 年 11 月 21 日 产生了:6 条评论
2022 年 11 月 15 日 产生了:5 条评论
2022 年 11 月 13 日 产生了:5 条评论
2022 年 11 月 12 日 产生了:5 条评论
2022 年 11 月 25 日 产生了:4 条评论
2022 年 11 月 24 日 产生了:4 条评论
2022 年 11 月 22 日 产生了:4 条评论
2022 年 11 月 10 日 产生了:4 条评论
2022 年 11 月 23 日 产生了:3 条评论
2022 年 11 月 20 日 产生了:3 条评论
2022 年 11 月 19 日 产生了:3 条评论
2022 年 11 月 14 日 产生了:3 条评论
2022 年 11 月 11 日 产生了:3 条评论
2022 年 10 月 31 日 产生了:3 条评论
2022 年 10 月 23 日 产生了:3 条评论
2022 年 10 月 22 日 产生了:3 条评论
2022 年 5 月 27 日 产生了:3 条评论
---------------------“应用:「JumpJump 跳绳」狂热粉丝”排行榜, 单个用户评价次数排行------------------------------
---------------------“APP:「JumpJump 跳绳」Big Fans” Single User Reviews Order By Times-------------------------------
应用:「JumpJump 跳绳」没有一位粉丝评论超过 3 次
APP:「JumpJump 跳绳」No User Reviews more than 3 Times
-----------------------应用:「JumpJump 跳绳」重复垃圾评论出现次数排行榜,真有你的-----------------------------
-----------------------APP:「JumpJump 跳绳」Duplicated Reviews Order by Times Shown-----------------------------
出现「4」次的评论为:「好用」

### GRun 中文版

```
python scripts/main.py https://apps.garmin.cn/en-US/apps/02d16e10-84dc-46aa-8edb-c42834c9b907
```

六万下载的免费应用, 几乎不主动运营评价体系, 全靠自觉, 一年多只有区区 200 自然评价

------------------------日期评论次数排名----------------------------
November 24, 2022 产生了:4 条评论
August 19, 2022 产生了:3 条评论
June 12, 2022 产生了:3 条评论
March 8, 2022 产生了:3 条评论
January 20, 2022 产生了:3 条评论
January 11, 2022 产生了:3 条评论
November 18, 2021 产生了:3 条评论
---------------------“狂热粉丝”排行榜 这得多爱你才能浪费生命写这么多评价-------------------------------
竟然没有一位粉丝评论超过 3 次
-----------------------重复垃圾评论,真有你的-----------------------------
竟然没有重复垃圾评论

### Quatro 中文版

```
python scripts/main.py https://apps.garmin.cn/en-US/apps/a24870e3-b1ea-40a4-aea9-655cdf1d3ee2
```

一个两万多下载的付费应用被刷出来了 1850 条评论;其中近百条是引流广告, 十几个小号枪手轮番上阵, 真有你的. 尸位素餐, 不干你干谁

------------------------日期评论次数排名----------------------------
August 10, 2022 产生了:44 条评论
August 11, 2022 产生了:35 条评论
August 15, 2022 产生了:28 条评论
August 12, 2022 产生了:27 条评论
August 5, 2022 产生了:27 条评论
August 3, 2022 产生了:27 条评论
October 5, 2022 产生了:26 条评论
September 29, 2022 产生了:26 条评论
August 1, 2022 产生了:26 条评论
October 13, 2022 产生了:25 条评论
August 17, 2022 产生了:25 条评论
July 29, 2022 产生了:24 条评论
August 13, 2022 产生了:23 条评论
September 15, 2022 产生了:22 条评论
September 27, 2022 产生了:21 条评论
November 18, 2022 产生了:20 条评论
July 30, 2022 产生了:20 条评论
August 14, 2022 产生了:19 条评论
August 8, 2022 产生了:19 条评论
July 31, 2022 产生了:19 条评论
September 22, 2022 产生了:18 条评论
August 19, 2022 产生了:18 条评论
August 18, 2022 产生了:18 条评论
August 7, 2022 产生了:18 条评论
August 1, 2022 产生了:18 条评论
September 25, 2022 产生了:17 条评论
July 30, 2022 产生了:17 条评论
August 22, 2022 产生了:16 条评论
August 19, 2022 产生了:16 条评论
August 16, 2022 产生了:16 条评论
August 4, 2022 产生了:16 条评论
August 8, 2022 产生了:15 条评论
September 26, 2022 产生了:14 条评论
September 21, 2022 产生了:14 条评论
August 6, 2022 产生了:14 条评论
October 9, 2022 产生了:13 条评论
September 3, 2022 产生了:13 条评论
August 30, 2022 产生了:13 条评论
August 23, 2022 产生了:13 条评论
August 20, 2022 产生了:13 条评论
July 31, 2022 产生了:13 条评论
November 15, 2022 产生了:12 条评论
October 4, 2022 产生了:12 条评论
September 28, 2022 产生了:12 条评论
September 13, 2022 产生了:12 条评论
August 21, 2022 产生了:12 条评论
August 9, 2022 产生了:12 条评论
July 27, 2022 产生了:12 条评论
November 13, 2022 产生了:11 条评论
October 18, 2022 产生了:11 条评论
October 12, 2022 产生了:11 条评论
October 1, 2022 产生了:11 条评论
September 12, 2022 产生了:11 条评论
August 22, 2022 产生了:11 条评论
November 22, 2022 产生了:10 条评论
October 19, 2022 产生了:10 条评论
October 11, 2022 产生了:10 条评论
October 10, 2022 产生了:10 条评论
October 8, 2022 产生了:10 条评论
October 2, 2022 产生了:10 条评论
September 16, 2022 产生了:10 条评论
September 14, 2022 产生了:10 条评论
September 4, 2022 产生了:10 条评论
November 14, 2022 产生了:9 条评论
October 22, 2022 产生了:9 条评论
September 26, 2022 产生了:9 条评论
September 24, 2022 产生了:9 条评论
September 2, 2022 产生了:9 条评论
April 27, 2022 产生了:9 条评论
November 15, 2022 产生了:8 条评论
November 11, 2022 产生了:8 条评论
October 6, 2022 产生了:8 条评论
September 23, 2022 产生了:8 条评论
September 19, 2022 产生了:8 条评论
September 17, 2022 产生了:8 条评论
September 10, 2022 产生了:8 条评论
August 28, 2022 产生了:8 条评论
August 24, 2022 产生了:8 条评论
August 7, 2022 产生了:8 条评论
August 4, 2022 产生了:8 条评论
November 19, 2022 产生了:7 条评论
November 12, 2022 产生了:7 条评论
October 30, 2022 产生了:7 条评论
September 6, 2022 产生了:7 条评论
September 5, 2022 产生了:7 条评论
September 1, 2022 产生了:7 条评论
August 31, 2022 产生了:7 条评论
August 29, 2022 产生了:7 条评论
August 27, 2022 产生了:7 条评论
August 26, 2022 产生了:7 条评论
August 2, 2022 产生了:7 条评论
July 28, 2022 产生了:7 条评论
November 20, 2022 产生了:6 条评论
November 16, 2022 产生了:6 条评论
October 24, 2022 产生了:6 条评论
October 16, 2022 产生了:6 条评论
October 14, 2022 产生了:6 条评论
September 20, 2022 产生了:6 条评论
September 11, 2022 产生了:6 条评论
August 25, 2022 产生了:6 条评论
August 6, 2022 产生了:6 条评论
July 25, 2022 产生了:6 条评论
April 29, 2022 产生了:6 条评论
October 23, 2022 产生了:5 条评论
October 21, 2022 产生了:5 条评论
October 17, 2022 产生了:5 条评论
October 3, 2022 产生了:5 条评论
September 30, 2022 产生了:5 条评论
September 9, 2022 产生了:5 条评论
September 8, 2022 产生了:5 条评论
September 6, 2022 产生了:5 条评论
August 2, 2022 产生了:5 条评论
July 26, 2022 产生了:5 条评论
July 26, 2022 产生了:5 条评论
November 2, 2022 产生了:4 条评论
October 9, 2022 产生了:4 条评论
October 7, 2022 产生了:4 条评论
September 27, 2022 产生了:4 条评论
September 18, 2022 产生了:4 条评论
August 24, 2022 产生了:4 条评论
November 4, 2022 产生了:3 条评论
October 20, 2022 产生了:3 条评论
October 15, 2022 产生了:3 条评论
September 30, 2022 产生了:3 条评论
September 8, 2022 产生了:3 条评论
September 7, 2022 产生了:3 条评论
July 1, 2022 产生了:3 条评论
May 11, 2022 产生了:3 条评论
May 10, 2022 产生了:3 条评论
May 7, 2022 产生了:3 条评论
May 5, 2022 产生了:3 条评论
May 3, 2022 产生了:3 条评论
May 1, 2022 产生了:3 条评论
April 28, 2022 产生了:3 条评论
---------------------“狂热粉丝”排行榜 这得多爱你才能浪费生命写这么多评价-------------------------------
「朝溪」 累计评价 「14」次
「言芝」 累计评价 「14」次
「霾」 累计评价 「13」次
「金亮」 累计评价 「13」次
「漫雨」 累计评价 「13」次
「枭飞」 累计评价 「13」次
「春芳」 累计评价 「13」次
「方慧」 累计评价 「11」次
「七七」 累计评价 「11」次
「钱贵文」 累计评价 「10」次
「雅安」 累计评价 「10」次
「醒」 累计评价 「9」次
「永奎」 累计评价 「9」次
「霄芭」 累计评价 「8」次
「咿呀」 累计评价 「8」次
「小宇」 累计评价 「8」次
「宁」 累计评价 「7」次
「A 啾」 累计评价 「7」次
「明媚」 累计评价 「7」次
「壹念」 累计评价 「7」次
「日光」 累计评价 「6」次
「媛儿」 累计评价 「6」次
「昭」 累计评价 「5」次
「Mike」 累计评价 「5」次
「跑步者」 累计评价 「5」次
「陈」 累计评价 「5」次
「筱筱」 累计评价 「5」次
「Geniadk」 累计评价 「4」次
「寇娃」 累计评价 「4」次
「小熊」 累计评价 「4」次
「岳良」 累计评价 「4」次
「瑟瑟」 累计评价 「4」次
「焱焱」 累计评价 「4」次
「Joe9998」 累计评价 「4」次
「潘超）」 累计评价 「4」次
-----------------------重复垃圾评论,真有你的-----------------------------
出现「79」次的评论:「请关注“佳明宝典”微信公众号【1】免费获取天气 key 和教程 【2】最快 5 分钟显天气，100%成功」
出现「27」次的评论:「好评」
出现「19」次的评论:「好用」
出现「12」次的评论:「开发者已 24H 在线,免费解决相关疑难杂症—————————————————— 表盘解锁,天气定位,错误乱码,开发进度等——————————————————☛ 微信 → 添加 → 公众号 → 搜索:佳明运动营——————————————————自助解锁请搜索微信小程序:佳明表盘商场—————————————————— 声明:请认准官方唯一通道,本店正版授权——————————————————如使用盗版解锁码将导致手表被统一锁定——————————————————」
出现「12」次的评论:「非常好」
出现「11」次的评论:「好评！」
出现「9」次的评论:「非常好用」
出现「9」次的评论:「好」
出现「9」次的评论:「请关注“tianqikaifa”微信公众号 【1】免费获取天气 key 和教程【2】最快 5 分钟显天气，100%成功」
出现「7」次的评论:「好看」
出现「6」次的评论:「不错不错」
出现「6」次的评论:「不错」
出现「6」次的评论:「请关注“佳明宝典”微信公众号 【1】免费获取天气 key 和教程【2】最快 5 分钟显天气，100%成功」
出现「5」次的评论:「简洁明了」
出现「5」次的评论:「很喜欢」
出现「5」次的评论:「非常好的表盘」
出现「5」次的评论:「很好用」
出现「4」次的评论:「所有信息都可以显示，佳明表盘中比较靠谱的一款。 」
出现「4」次的评论:「很好」
出现「4」次的评论:「简单实用」
出现「4」次的评论:「非常不错的表盘」
