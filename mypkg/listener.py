import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.count = 0  # count属性を追加
        self.pub = self.create_subscription(Int16, "countup", self.cb, 10)

    def cb(self, msg):
        self.get_logger().info("Listen: %d" % msg.data)
        self.count += 1
        if self.count > 20:
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = Listener()
    time.sleep(1.0)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

