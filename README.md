OrchIDE
=======

Objective Robotics Coding Has an IDE. Easy to understand, easy to use, easy to extend.

为面向对象编程而生的机器人编程集成开发环境。易于理解，易于使用，易于扩展。

## The Idea 项目简介

I have been building robots using the VEX Robotics product for nearly 3 years. Since the building process is finished, building a program for it, and the debugging process after that has been a big problem. VEX forces easyC, which is not only hard to learn, but rather inefficient for professional C programmers, to be the only IDE available for coding a VEX V4 Controller. 

Once I came across an idea that if we use abstract ideas (or objects, more exactly) to represent every part of an robot (either a physical part or a logical part), then we build connections among these parts, and use mutiple layers of indirections to organize the code, things will be clearer for newbies, and more extensible for professionals.

Also, as a programmer, I always want to have an online debug system which can change variables or even execute programs over the air in real time, so debugging can be much more convenient. Also, setting a break point and printing out stack trace information will be made possible.

So I am starting this project to replace easyC in some degrees (not completely, since I don't know the protocol to download a program to the controller, and hack it is too time-consuming), to make things easy and understandable for everyone.

我使用 VEX 机器人公司的产品来制造机器人已经有三年左右了。我发现，制造一台机器人时，最复杂的部分不是把各个部件连接起来，而是随后的编程和调试工作。VEX 公司强迫我们使用 easyC 来为 VEX V4 主控器编写程序，但是这个 IDE 不仅难以理解，而且效率极低，扩展性也不强。

有一天我突然想到，如果我们在制造机器人时就对每个部分（事实存在的或者逻辑上的）编写抽象模型，然后在各个模型之间建立特定的联系，使用多重“间接”（indirections）组织代码，那么新手会更容易理解它，高手也能更容易地扩展其特性。

此外，作为一个程序员，我总想在机器人上面做一个在线调试系统，通过无线连接改变参数值，甚至远程执行代码块。这样一来，调试过程就不再有编程-编译-下载程序-测试这四大步的麻烦，只需要在计算机上完成代码编写，点击运行，机器人就会自动执行这一段程序，甚至可以设定断点和堆栈跟踪，那该有多方便！

所以我决定启动这个项目，目的在于在一定程度上取代 easyC（完全取代短期内是不可能的：VEX 公司并未公开机器人程序的传输协议，破解协议太花时间了），让机器人编程变得更简单。

## The Implementation 项目实现

IDE and code generator: mbeddr, together with some python scripts
Online debugger: two Arduino UNO boards for both PC and robot, nRF24L01+ modules for wireless connection (I will make communication APIs open for using different wireless modules)

IDE 和代码生成器：mbeddr 和手写的 Python 脚本
在线调试器：两块 Arduino UNO 分别用于计算机端和机器人端，使用 nRF24L01+ 来完成无线通信（通信 API 将会开放，以便使用不同的无线模块）

## The Problems 目前的问题

I only have one and a half months to finish the project kernel, then I will be leaving this lab due to my graduation. After that, I will have no devices to continue developing, since I cannot afford a controller.

我只有一个半月左右的时间来完成这个项目的核心代码，然后我将离开机器人实验室。此后由于缺少资金，我将没有用于调试的硬件设备（主控器太贵了）。

## Donation Needed! 求捐助！

Devices I needed: 
* Arduino UNO Boards (Other types of Arduino compatible boards is welcomed) and different wireless models
* VEX V4 Controllers, Joysticks, motors, sensors, screens (nearly everything is badly needed)
* Money is also acceptable

需要的设备：
* Arduino UNO（别的 Arduino 兼容板也可以），以及各种无线模块
* VEX V4 主控器，手柄，马达，传感器，屏幕（我需要几乎任何东西）
* 同样欢迎现金捐赠

Besides, if you have these things and you are interested in this project, please join us.

此外，如果你有上述设备且对本项目有兴趣，欢迎参与开发。

## Contact Us 联系方式

Any questions, donations, or you want to be a contibutor of this project, please send an email to:

如有任何问题，想要捐赠或者想共同开发，请发邮件到：

jamesswineson[#]gmail.com

Note: Please replace "[#]" with "@".

注：请把“[#]”替换成“@”。
