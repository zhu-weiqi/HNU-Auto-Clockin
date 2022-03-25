# HNU-Auto-Clockin（目前可用）

HNU疫情防控和健康监测系统每日自动打卡

**2021.6.4 更新：使用百度云公开OCRapi，不再需要百度账号，此处感谢GGP老哥的提醒，[这个是他打卡脚本的链接](https://github.com/ercha-action/HNU-AutoClockIn)。**

**2022.1.12 更新：还是需要百度云自身的OCRapi，公开的api已经不能使用。精简了代码，不需要设置打卡地址，默认为湖南省长沙市岳麓区，详细地址为宿舍**

**2022.2.22 更新：access_token有效期存在一个月，必须通过实时请求获取**

**2022.3.25 更新：由于疫情变化，学校把打卡系统发生了些许变化，提交字段有些改变，目前完成了更新**


**使用前须知：本项目仅用于学习交流Python语言的学习与相关库的使用，不得用于获利 (NON FOR PROFIT)！如有体温异常等请如实上报！**

参考开源仓库：[中南大学nCov健康打卡定时自动脚本](https://github.com/lxy764139720/Auto_Attendance)

## 食用方法

本品通过GitHub Actions实现自动化，~~具有美容养颜、改善睡眠、舒肝理气、应该不会再被辅导员电话轰炸或被喝茶等功效。~~ 需要你做的前期工作有：

1. **创建一个GitHub账号，将本项目fork到你自己的账号下**
   ![QQ20210316-0.png](https://i.loli.net/2021/03/16/1krc8KwVATBUWCl.png)

2. **配置学号与个人中心密码**

    进入刚刚你fork过去到自己名下的项目，再进入Settings -> Secrets页面，点击New repository Secret，在Name栏输入**USERNAME**，Value栏输入你的学号。然后再添加一个Secret，Name栏为**PASSWORD**，Value栏填写你登录个人中心的密码。
    ![QQ20210316-2.png](https://i.loli.net/2021/03/16/4vqF6bsBPfSUDZc.png)


3. **开始自动化运行**

    进入到**Actions**界面，点击该工作流，然后Run workflow，即可开启自动化运行，你可以在设置里绑定邮箱以接收运行失败的通知，防止未来哪天打卡系统升级了你还蒙在鼓里。
    ![Snipaste_2021-03-15_21-56-15.png](https://i.loli.net/2021/03/16/oxSp8VYlfskWq53.png)
    ![Snipaste_2021-03-15_21-56-34.png](https://i.loli.net/2021/03/16/xETNukAF8hVS1nw.png)
    ![Snipaste_2021-03-15_21-57-11.png](https://i.loli.net/2021/03/16/XtR6lphCxLQg3an.png)

    你可以在如下界面中检查自动化运行情况：
    ![Snipaste_2021-03-15_21-57-49.png](https://i.loli.net/2021/03/16/8RwnFvq1ZBTuMxe.png)
    ![Snipaste_2021-03-15_21-58-06.png](https://i.loli.net/2021/03/16/MSok2D9VYJOBRK7.png)
    ![image.png](https://i.loli.net/2021/03/16/vnaiPEmyx5ugNlW.png)

    我设定为每天早晨6：10自动运行，你可以在/.github/workflows/python-app.yml文件里修改，请注意cron语法下的时间为零时区时间，需要将北京时间减8个小时，且分钟在前小时在后。详情参见[POSIX cron 语法](https://crontab.guru/)和[官方文档](https://docs.github.com/cn/actions/reference/events-that-trigger-workflows#)。

6. **如果一切顺利的话，应该没有第六步。若不是那样，可以在Discussion里面说。**

## 觉得有用的话给👴点个Star呗~
