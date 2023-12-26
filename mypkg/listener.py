import os
import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.count = 20  # ここを希望のカウント数に変更する
        self.pub = self.create_subscription(Int16, "countup", self.cb, 10)

    def cb(self, msg):
        self.get_logger().info("Listen: %d" % msg.data)
        self.count -= 1
        if self.count < 0:
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = Listener()
    time.sleep(1.0)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    print("successfully ended.")  # 終了メッセージを追加

if __name__ == "__main__":
    main()

