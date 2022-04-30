# efficiencies

## Motivation

- 為了減緩我 MacBook 的更換頻率、以及電腦本身的衰退速度，我聽信了網路上流傳著的神秘「**40-80 法則**」，顧名思義就是讓電腦電量盡量維持在 40-80%就能延長其電池壽命。因此我需要一款 app 來提醒我充電。
- 我是一位愛邊聽音樂邊使用電腦工作的人，在長期使用 MacBook 下來，我發現我最喜歡的系統音量在 45%，而我不太喜歡讓音量低於 10%、高於 50%，因此我也需要一款 app 來幫我自動調整系統音量。
- 以往，我都不太愛看學校發的信，因為不是 ee-class 還是 ee-class。不過到了最近，中央開始有人確診我常常會在信箱中發現中大學務處**_劉孔群組長_**發的確診人數通知信，搭配著我不愛打開信箱的壞習慣，我也需要一款 app 在平時能定時幫我打開信箱中來自++中央大學++的信，這樣不僅可以做好防疫措施，也能讓我看到 ee-class 的通知。

#### 說了那麼多需求，反正我的 thread 程式會將以上三個我需要的 app 同時處理。而以上三個我需要的 App 在 AppStore 中幾乎沒有免費現成的所以都只能自己來(;´༎ຶД༎ຶ`)

## Concept

### 1. 總共要做 3 個 app

- 第一個要每十分鐘幫我查看電池狀況以及充電狀況，在快沒電的時候通知我充電充飽電的時候拔掉電源
- 第二個要每分鐘幫我查看音量，在高於 50%時將音量調整回 45%在低於 10%時將音量調整回 45%
- 第三個要每一個小時幫我打開沒讀過的而且來自 eeclass 或衛保組的郵件

### 2. 用 Thread 將三個 app 同時整合

## Installation

```zsh
pip3 install psutil
pip3 install osascript
pip3 install threading
```

## About each app

### 1. Battery app

實際上，這是一個用 AppleScript 寫的通知 App，因為我並不是用 AppleScript 來獲取電池資訊的而是用 psync 來獲取的。

### 2. Set_volume App

這是一個用 AppleScript 寫的 App，每次 run 這個 app 都會幫我檢查我的系統音量若超過範圍則將音量調成 45 並通知

### 3. Open_school_messages App

這是一個用 AppleScript 寫的 App，這個 app 會幫我檢查我的 mail 中是否有來自++中央大學++或++衛保組-劉孔群組長++的未讀郵件，如果有則幫我打開並設成已讀

### 4. Python Driver

在我的 Python Driver 中我 import 了 psutil 幫我檢查電池狀況 threading, osascript 幫我同時控制使用以上三個 app

## Execute

```zsh
python3 efficiency.py
```

## 成品

1. 在我的電腦低於 40％的時候，提示我該充電了。

![](https://i.imgur.com/1mqjH3X.png)

2. 在系統音量高於 50%或低於 10%的時後幫我調整音量到 45%。

![](https://i.imgur.com/rTOWIMv.png)

3. 每個小時幫我打開來自“國立中央大學”、"學生事務處衛生保健組-劉孔群"的未讀郵件

![](https://i.imgur.com/XAcBqMe.png)

參考文獻：
python threading:
https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/
Apple Script:
https://stackoverflow.com/questions/48856158/change-icon-of-notification-when-using-osascript-e-display-notification
https://www.796t.com/content/1534308017.html
https://stackoverflow.com/questions/16559947/applescript-open-mail-then-open-most-recent-5-email
https://alvinalexander.com/mac-os-x/how-to-fire-mac-notifications-applescript-scala-java/
Icons:
https://findicons.com/icon/93600/audio_volume_high
