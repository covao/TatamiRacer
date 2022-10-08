[日本語 Japanese](https://github.com/covao/TatamiRacer/blob/master/README_JP.md) / [English](https://github.com/covao/TatamiRacer/blob/master/README.md)  

![TatamiRacerLogo](img/TatamiRacer_LogoM.png)    
TatamiRacer は、小さな自動運転車です。
[TAMIYA ミニ四駆キット](https://www.tamiya.com/japan/mini4wd/index.html)をベースにしています。  
[畳](https://en.wikipedia.org/wiki/Tatami)一畳(約1.8m×0.9m)で運転できます。  
["DonkeyCar"](http://docs.donkeycar.com/)ソフトウエアを、深層学習と自動運転制御に利用できます。  

### YouTube  
TatamiRacer  
[![](https://img.youtube.com/vi/b-pkVy8e3DA/0.jpg)](https://www.youtube.com/watch?v=b-pkVy8e3DA)  
TatamiRacer at Maker Faire Tokyo 2022  
[![](https://img.youtube.com/vi/s3ll8Y1OPn8/0.jpg)](https://www.youtube.com/watch?v=s3ll8Y1OPn8)  

# 部品表(BOM)
|部品名 |備考 |最小構成|推奨構成|Amazon-JP|Amazon-US|
|:---|:---|:---:|:---:|:---:|:---:|
| Raspberry Pi 3 モデル B+ | |+|| [リンク](https://www.amazon.co.jp/dp/B01NAHBSUD/) | [リンク](https://www.amazon.com/dp/B07P4LSDYV) |
| Raspberry Pi 4 |2、4または8 GB RAM を選択||+| [リンク](https://www.amazon.co.jp/dp/B09GRVDPCX/) | [リンク](https://www.amazon.com/dp/B07TC2BK1X) |
| Raspberry Pi カメラ モジュール V1 | OV5647(オムニビジョン) |+|| [リンク](https://www.amazon.co.jp/dp/B073RCXGQS/) | [リンク](https://www.amazon.com/dp/B07QNSJ32M/) |
| Raspberry Pi カメラモジュール V2 | IMX219PQ(SONY) ||+| [リンク](https://www.amazon.co.jp/dp/B01F1SWTZE/) | [リンク](https://www.amazon.com/dp/B083BHJZ16/) |
|マイクロ SD カード | 16GB以上|+|+| [リンク](https://www.amazon.co.jp/dp/B088TYHF8V/) | [リンク](https://www.amazon.com/dp//B00M55BS8G) |
|モバイルバッテリー |サイズ:6.2x9.15x1.15cm 電圧:5V 電流:最大2A |+|+|[リンク](https://www.amazon.co.jp/dp/B07SN2R3S2/) | [リンク](https://www.amazon.com/dp/B082X53VDL/) |
|モータードライバーモジュール| DCモーター/H-Bridge用|+|+| [リンク](https://www.amazon.co.jp/dp/B078X88R27/) |[リンク](https://www.amazon.com/dp/B07Y1QJZK3/) |
| ピンヘッダー | オス 90度 / モータードライバ用|+|+| [リンク](https://www.amazon.co.jp/dp/B00V4V703O/) |[リンク](https://www.amazon.com/dp/B0979568B3/) |
| 130 DC モーター |低速 (<8000 RPM) および低電流 (<500m A)|+|+| [TAMIYA](https://www.amazon.co.jp/dp/B005AFBLIA/),[uxcell](https://www.amazon.co.jp/dp/B07CWLWRYJ/) | [uxcell](https://www.amazon.com/dp/B01ERLPVJW) |
|マイクロサーボ | TowerPro SG90 |+|+| [リンク](https://www.amazon.co.jp/dp/B016FKJJ8M/) | [リンク](https://www.amazon.com/dp/B07MLR1498/) |
|タミヤ ミニ四駆キット |VZシャーシとお好みのボディ。(5：1ギアをお勧めします）|+|+| [TOYOTA Yaris](https://www.amazon.co.jp/dp/B08C5FM9HM/),[Honda e](https://www.amazon.co.jp/dp/B08HK7HWCM/) , [Dual Ridge Jr](https://www.amazon.co.jp/dp/B088FK3NC2/), [Elephant](https://www.amazon.co.jp/dp/B08VX3W3Q6/), [Penguin](https://www.amazon.co.jp/dp/B0043RYKPW/)|[TOYOTA Yaris](https://www.amazon.co.jp/dp/B08C5FM9HM/),[Neo-VQS](https://www.amazon.com/dp/B005GJCC9C/) |
|タミヤ ギアセット |5:1が必要な場合||| [リンク](https://www.amazon.co.jp/dp/B009WJG2ES/)| [リンク](https://www.amazon.com/dp//B0043RN7W4/)|
|タミヤ ミニ四駆 ローラーパーツ | スペーサーと M2x10 ネジ が必要です。 |+|+| [15381](https://www.amazon.co.jp/dp/B001E40PXI/), [95391](https://www.amazon.co.jp/dp/B07F8RLJBQ/),[15435](https://www.amazon.co.jp/dp/B005GJCC9C/)| [リンク](https://www.amazon.com/dp/B005GJCC9C/) |
| M2x15 または M2x16 mm ボルト |前輪シャフト用 |+|+| [15508](https://www.amazon.co.jp/dp/B01MXVKDOM/),  [15233](https://www.amazon.co.jp/dp/B001VZE9MS/)| [リンク](https://www.amazon.com/dp/B07YS5ZSZH/) |
|タミヤ ミニ四駆 72mm シャフト |延長リヤシャフト用|+|+| [リンク](https://www.amazon.co.jp/dp/B003GALRS0/) | [リンク](https://www.amazon.com/dp/B002CAO2IC/) |
|ジャンパーケーブル |メスコネクタからメスコネクタ 10cm|+|+| [リンク](https://www.amazon.co.jp/dp/B07MR1SVVR/) | [リンク](https://www.amazon.com/dp/B0742RS6YL) |
|マイクロ USB ケーブル |ショートケーブル 約15cm |+|+| [リンク](https://www.amazon.co.jp/dp/B07PTZ6VGV/) | [リンク](https://www.amazon.com/dp/B01FA4JXN0/) |
|マイクロ USB から Type-C へのアダプター | Raspberry pi 4 の場合 | |+| [リンク](https://www.amazon.co.jp/dp/B06XFL6159/) | [リンク](https://www.amazon.com/dp/B07G54XXZZ/) |
|ゲームパッド| USBまたはBluetooth | |+| [F710](https://www.amazon.co.jp/dp/B00475S13W/), [PS4 ゲームパッド](https://www.amazon.co.jp/dp/B08TR67991/)  | [F710](https://www.amazon.com/dp/B0041RR0TW/), [PS4 ゲームパッド](https://www.amazon.co.jp/dp/B00475S13W/) |
||  || |  |  |
| 概算費用 (Raspberry PiとマイクロSDカードなし) |  |6,000 yen |13,000 yen |  |  |


# 3Dプリントパーツ

## [アセンブリー (STL Viewer)](3d/tatamiracer_assembly.stl)  
<img src="img/TatamiRacer_3D_Assembly.png" alt="" title="" width="640" height="">  
  
## [3Dプリント用キット(STL Viewer)](3d/tatamiracer_kit.stl)  
<img src="img/TatamiRacer_3D_Kit.png" alt="" title="" width="640" height="">  
  
# 回路図  
<img src="img/TatamiRacer_Circuit.png" alt="" title="" width="640" height="">

# ボディ 
様々なタイプのミニ四駆ボディを装着可能。 
例 [Amazon JP](https://www.amazon.co.jp/s?k=%E3%83%9F%E3%83%8B%E5%9B%9B%E9%A7%86+and+%E3%83%97%E3%83%A9%E3%83%A2%E3%83%87%E3%83%AB+and+%E3%82%B7%E3%83%A3%E3%83%BC%E3%82%B7&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss), [Amazon US](https://www.amazon.com/s?k=tamiya+1%2F32+mini4wd&ref=nb_sb_noss)  
<img src="img/Body_Selection.jpg" alt="" title="" width="640" height="">

# Tatamiサーキットコース  
<img src="img/Tatami Circuit.png" alt="" title="" width="640" height="">

# [TatamiRacerの組み立て方法](doc/Assembly_Instructions.md)  
[TatamiRacerの組み立て方法](doc/Assembly_Instructions.md)を参照してください  
<img src="img/TatamiRacerBuild.jpg" alt="" title="" width="640" height="">

# [ソフトウェアのセットアップ方法](doc/HowToSetupSoftware.md)
[ソフトウェアのセットアップ方法](doc/HowToSetupSoftware.md)を参照してください
<img src="img/TatamiRacer_Shortcut.jpg" alt="" title="" width="640" height="">

# [TatamiRacer のキャリブレーション方法](doc/HowToCalibrateTatamiRacer.md)
[TatamiRacerのキャリブレーション方法](doc/HowToCalibrateTatamiRacer.md)を参照してください 
<img src="img/tatamiracer_test.jpg" alt="" title="" width="640" height="">

# [TatamiRacerの運転方法](doc/HowToGetDriving.md)
[TatamiRacerの運転方法](doc/HowToGetDriving.md)を参照してください   
<img src="img/browser_control.jpg" alt="" title="" width="640" height="">

