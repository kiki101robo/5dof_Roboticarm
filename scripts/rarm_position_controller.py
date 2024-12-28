import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

class RobotControl(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.joint_position_pub = self.create_publisher(Float64MultiArray, '/position_controller/commands', 10)

    def move_robot(self, joint_positions):
        position_command = Float64MultiArray()
        position_command.data = joint_positions
        self.joint_position_pub.publish(position_command)

def main(args=None):
    rclpy.init(args=args)
    robot_control_1 = RobotControl('robot_control_1')
    robot_control_2 = RobotControl('robot_control_2')
    robot_control_3 = RobotControl('robot_control_3')
    robot_control_4 = RobotControl('robot_control_4')
    robot_control_5 = RobotControl('robot_control_5')

    q1_values = [0.00197306213845128, -0.021017637956678, -0.0641479047729379, -0.121913341657977, -0.186933699470577, -0.251276089402479, -0.307736172650685, -0.350197641834088, -0.372949404583206, -0.336727600527502, -0.322022731327981, -0.282448452904189, -0.22354104505249, -0.151699722460842, -0.0744068682250548, 0.000469179990167014, 0.0654362519055818, 0.113985990137576, 0.140911315770299, 0.141829635411051]
    q2_values = [0.0875471518341038, 0.190035022519902, 0.296053432203258, 0.390699171779078, 0.459107645244256, 0.490362521428679, 0.480791970214044, 0.433459937035950, 0.353720858233589, 0.177600394579241, 0.0805305969385709, -0.026963154262325, -0.132187327290824, -0.225367979095565, -0.298267380859839, -0.344503092633128, -0.360022266551684, -0.343371903636059, -0.295478783914856, -0.217897390594167]
    q3_values = [-0.0875471518341036, -0.197083455382983, -0.316689709026639, -0.430183455895801, -0.520796453156243, -0.575518646948729, -0.58884134164898, -0.562473623754931, -0.501350777933927, -0.375784044265647, -0.279670683095163, -0.170016963886861, -0.0583352747225736, 0.044877709740269, 0.129888162946205, 0.188460316982049, 0.214645894347734, 0.205378424010494, 0.160711044852639, 0.0831680937295826]
    q4_values = [0.00102693786154872, 0.0240167774491757, 0.0671405852217215, 0.124888036395079, 0.189878095353574, 0.25418525880282, 0.310616195588301, 0.353061231283257, 0.375808005486844, 0.339589055850693, 0.324884282973635, 0.285310409051628, 0.226406916313275, 0.154575740378728, 0.0772982598307607, 0.00243828176693215, -0.0625169527684686, -0.111061073123693, -0.137985201158759, -0.138903518428117]
    q5_values = [-0.282134724286383, -0.548765896352441, -0.763254033606401, -0.891472796179878, -0.904666019668585, -0.790694764431695, -0.562853952848088, -0.255858057437457, 0.0899467481950192, 0.555910443094556, 0.826499932467902, 1.04786605338466, 1.19774023908238, 1.26602193304473, 1.2508632225163, 1.15746036515859, 0.997040946178732, 0.785636893545128, 0.542349444129678, 0.285469768568629]


    for index in range(len(q1_values)):
        arm_joint_position = [
            q1_values[index],
            q2_values[index],
            q3_values[index],
            q4_values[index],
            q5_values[index]
        ]

        robot_control_1.move_robot(arm_joint_position)
        robot_control_2.move_robot(arm_joint_position)
        robot_control_3.move_robot(arm_joint_position)
        robot_control_4.move_robot(arm_joint_position)
        robot_control_5.move_robot(arm_joint_position)

        rclpy.spin_once(robot_control_1, timeout_sec=1.0)
        rclpy.spin_once(robot_control_2, timeout_sec=1.0)
        rclpy.spin_once(robot_control_3, timeout_sec=1.0)
        rclpy.spin_once(robot_control_4, timeout_sec=1.0)
        rclpy.spin_once(robot_control_5, timeout_sec=1.0)

    robot_control_1.destroy_node()
    robot_control_2.destroy_node()
    robot_control_3.destroy_node()
    robot_control_4.destroy_node()
    robot_control_5.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
