import rclpy                     #ROS 2のクライアントのためのライブラリ
import time
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

#クラスでまとめている。
class Talker():
    def __init__(self,nh):
        self.pub = nh.create_publisher(Int16, "countup", 10)   
        self.n = 20 #ここを希望のカウント数に変更する
        nh.create_timer(1.0,self.cb)  #タイマー設定

    def cb(self):       
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n -= 1

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)       #この一行でパブリッシャが動き出す。
    rclpy.spin(node)

if __name__ == '__main__':
    main()

