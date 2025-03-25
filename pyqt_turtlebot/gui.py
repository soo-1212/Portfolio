import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_Dialog  # 변환된 파일에서 가져옴
import rclpy
from rclpy.node import Node
import threading
from geometry_msgs.msg import Twist
from PyQt5.QtCore import QTimer


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
            



# -----------------------------------------------------------------------------------------

class MyApp(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_1.clicked.connect(self.on_button_click_1)
        


        self.pushButton_2.clicked.connect(self.on_button_click_2)
        
        # GoRobot 노드를 초기화
        self.robot_node = GoRobot()


    def on_button_click_1(self):
        # 버튼 클릭 시 Twist 메시지를 발행
        self.robot_node.publish_twist_1()

    def on_button_click_2(self):
        # 버튼 클릭 시 Twist 메시지를 발행
        self.robot_node.publish_twist_2()


# -----------------------------------------------------------------------------------------

def run_ros():
    # ROS 실행을 위한 rclpy 초기화
    rclpy.init()
    node = GoRobot()

    # rclpy.spin()을 통해 ROS 이벤트 루프 실행
    rclpy.spin(node)

def main():

    ros_thread = threading.Thread(target=run_ros)
    ros_thread.start()

    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()