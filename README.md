# ROS 2 Robotics Learning

My hands-on journey into robotics software development using **ROS 2 Humble, Python, and Ubuntu 22.04**.

This repository contains practical exercises and projects developed while learning ROS 2, robot communication, simulation, and autonomous robotics.

## Environment

- **OS:** Ubuntu 22.04.5 LTS
- **ROS 2:** Humble
- **Python:** 3.10
- **Architecture:** x86_64

## Learning Roadmap

### Phase 1 — Python Fundamentals
- [x] Python fundamentals

### Phase 2 — Linux, Git and GitHub
- [x] Linux fundamentals
- [x] Git and GitHub workflow
- [x] Repository setup and version control

### Phase 3 — ROS 2 Fundamentals
- [x] ROS 2 installation and setup
- [x] Understanding ROS 2 nodes
- [x] Understanding ROS 2 topics
- [x] Creating ROS 2 Python packages
- [x] Publisher and subscriber communication
- [x] ROS 2 topic commands
- [x] Services and clients
- [x] ROS 2 parameters
- [x] ROS 2 actions
- [x] Action feedback, results and cancellation
- [x] AswinBot mini-project
- [x] Integration testing

## Phase 3 Project — AswinBot

AswinBot is a ROS 2 Python project combining the fundamental ROS 2 communication mechanisms into one small robot software system.

### Features

- Periodic robot status publishing
- Status message subscription
- Runtime parameter configuration
- Service-based robot status checking
- Action-based Fibonacci sequence execution
- Action feedback and result handling
- Action goal cancellation

### ROS 2 Architecture

| Component | Name |
|---|---|
| Status publisher node | `/aswinbot_status` |
| Subscriber node | `/aswinbot_subscriber` |
| Service server node | `/aswinbot_service_server` |
| Service client node | `/aswinbot_service_client` |
| Action server node | `/aswinbot_action_server` |
| Action client node | `/aswinbot_action_client` |

### Topic

| Topic | Message type | Purpose |
|---|---|---|
| `/aswinbot/status` | `std_msgs/msg/String` | Publishes robot status |

### Service

| Service | Service type | Purpose |
|---|---|---|
| `/aswinbot/check_status` | `std_srvs/srv/Trigger` | Checks robot status |

### Action

| Action | Action type | Purpose |
|---|---|---|
| `/aswinbot/fibonacci` | `example_interfaces/action/Fibonacci` | Executes Fibonacci sequence with feedback, result and cancellation |

### Parameters

| Parameter | Default value | Purpose |
|---|---|---|
| `robot_name` | `AswinBot` | Robot name |
| `speed` | `0.5` | Robot speed value |

## Build Instructions

Navigate to the ROS 2 workspace:

```bash
cd ~/ros2-robotics-learning/phase_03_ros2_fundamentals/ros2_ws
```

Build the package:

```bash
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

## Running AswinBot

Run each node in a separate terminal after sourcing the workspace.

```bash
ros2 run my_robot aswinbot_status
```

```bash
ros2 run my_robot aswinbot_subscriber
```

```bash
ros2 run my_robot aswinbot_service_server
```

```bash
ros2 run my_robot aswinbot_action_server
```

### Test the Service

```bash
ros2 service call /aswinbot/check_status std_srvs/srv/Trigger "{}"
```

### Test the Action

```bash
ros2 run my_robot aswinbot_action_client
```

### Change Parameters

```bash
ros2 param set /aswinbot_status robot_name "MarsBot"
ros2 param set /aswinbot_status speed 2.5
```

### Inspect ROS 2 Communication

```bash
ros2 node list
ros2 topic list
ros2 topic info /aswinbot/status
ros2 service list
ros2 action list
```

## Repository Structure

```text
ros2-robotics-learning/
├── README.md
└── phase_03_ros2_fundamentals/
    └── ros2_ws/
        └── src/
            └── my_robot/
                ├── my_robot/
                │   ├── robot_status.py
                │   ├── robot_publisher.py
                │   ├── robot_subscriber.py
                │   └── final_project/
                │       ├── robot_status.py
                │       ├── robot_subscriber.py
                │       ├── robot_service_server.py
                │       ├── robot_service_client.py
                │       ├── robot_action_server.py
                │       └── robot_action_client.py
                ├── package.xml
                └── setup.py
```

## Upcoming Learning Phases

- Phase 4: URDF, Xacro and TF2
- Phase 5: Gazebo Simulation
- Phase 6: ROS 2 Control and Robot Manipulation
- Phase 7: Navigation2 and SLAM
- Phase 8: Sensors and Hardware Integration
- Phase 9: Advanced ROS 2
- Phase 10: Computer Vision with OpenCV
- Phase 11: AI/ML for Robotics
- Phase 12: Autonomous Robotics Projects
- Phase 13: Portfolio and Job Preparation

---

**This repository documents my practical progress toward becoming a Robotics Software Engineer.**
