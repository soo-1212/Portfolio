import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class GoRobot(Node):
    def __init__(self):
        super().__init__('go_robot')
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def publish_twist_1(self):
        twist = Twist()
        twist.linear.x = 0.1
        self.cmd_vel_pub.publish(twist)

    
    def publish_twist_2(self):
        twist = Twist()
        twist.linear.x = 0.0
        self.cmd_vel_pub.publish(twist)
            
def main():

    # ROS 실행을 위한 rclpy 초기화
    rclpy.init()
    node = GoRobot()

    # rclpy.spin()을 통해 ROS 이벤트 루프 실행
    rclpy.spin(node)

if __name__ == "__main__":
    main()