# コマンドラインで事前に以下を実行
# pip install pillow qrcode
# pip install -U pip


# パッケージをインポート
import qrcode
# QRコードを生成
img  =qrcode.make('https://www.google.com/')
# 画像ファイルとして保存
img.save('qrcode-test.png')

# コマンドラインで実行すること