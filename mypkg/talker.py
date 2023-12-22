import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

#クラスでまとめている。
class Talker():
    def __init__(self,nh):
        self.pub = nh.create_publisher(Int16, "countup", 10)   
        self.n = 0
        nh.create_timer(0.5,self.cb)  #タイマー設定

    def cb(self):       
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

rclpy.init()
node = Node("talker")
talker = Talker(node)       #この一行でパブリッシャが動き出す。
rclpy.spin(node)            #実行（無限ループ）
