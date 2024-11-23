import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from geometry_msgs.msg import PoseStamped, Quaternion
from std_msgs.msg import Header
from tf_transformations import quaternion_from_euler

def create_pose(x, y, yaw):
    pose_stamped = PoseStamped()

    pose_stamped.header.stamp = rclpy.clock.Clock().now().to_msg()
    pose_stamped.header.frame_id = 'map'

    pose_stamped.pose.position.x = x
    pose_stamped.pose.position.y = y
    pose_stamped.pose.position.z = 0.0

    q = quaternion_from_euler(0, 0, yaw)
    pose_stamped.pose.orientation = Quaternion(x=q[0], y=q[1], z=q[2], w=q[3])
    return pose_stamped

def move_to_goal(nav, goal):
    nav.goToPose(goal)
    while not nav.isTaskComplete():
        feedback = nav.getFeedback()

    result = nav.getResult()
    if result == TaskResult.SUCCEEDED:
        print('Goal succeeded!')
    elif result == TaskResult.CANCELED:
        print('Goal was canceled!')
    elif result == TaskResult.FAILED:
        print('Goal failed!')

def main():
    rclpy.init()
    nav = BasicNavigator()

    initial = create_pose(1.839628, -9.050033, 3.140261)
    p1 = create_pose(-0.12, -2.35, 3.14)
    p2 = create_pose(1.86, 2.56, 0.97)
    p3 = create_pose(-3.84, 2.64, 2.78)

    nav.waitUntilNav2Active()
    nav.setInitialPose(initial)

    move_to_goal(nav, p1)
    move_to_goal(nav, p2)
    move_to_goal(nav, p3)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
