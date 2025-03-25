import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main_v2 import Ui_Dialog  
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import threading


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


#--------------------------------------------------------------------------
class MyApp(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #버튼 연결
        self.pushButton.clicked.connect(self.on_button_click_1)
        self.pushButton_2.clicked.connect(self.on_button_click_2)
        #/버튼 연결

        # GoRobot 노드를 초기화
        self.robot_node = GoRobot()

    def on_button_click_1(self):
        # 버튼 클릭 시 Twist 메시지를 발행
        self.robot_node.publish_twist_1()

    def on_button_click_2(self):
        # 버튼 클릭 시 Twist 메시지를 발행
        self.robot_node.publish_twist_2()

#------------------------------------------------------------------------------

#ros2 실행 함수
def run_ros():
    rclpy.init()
    node = GoRobot()
    rclpy.spin(node)
#/ros2 실행 함수


def main():
    #ros2 threading
    ros_thread = threading.Thread(target=run_ros)
    ros_thread.start()
    #/ros2 threading

    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()