import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Node("listener")
pub = node.create_subscription(Int16, "countup", cb, 10)
for i in range(11):
    rclpy.spin_once(node, timeout_sec=1.0)
    time.sleep(1.0)

