### 过程 ###

发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

程序：
- 编写MUA把邮件发到MTA；

- 编写MUA从MDA上收邮件。

发邮件：MUA与MTA使用SMTP协议

收邮件：MUA与MDA使用POP3、IMAP4协议

发邮件与收邮件时都需要填写相应的服务器地址和口令，放置冒认。