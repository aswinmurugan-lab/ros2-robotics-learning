# AswinBot – ROS 2 Mobile Robot Description

A differential-drive mobile robot model developed using **ROS 2 Humble, URDF, Xacro, TF2 and RViz2**.

This project demonstrates how to design a robot description, define links and joints, publish coordinate transforms, and visualize a mobile robot using ROS 2 tools.

---

## Environment

| Component | Version / Details |
|---|---|
| Operating System | Ubuntu 22.04 |
| ROS 2 Distribution | Humble |
| Programming / Description | Python, XML, Xacro |
| Robot Description | URDF / Xacro |
| Visualization | RViz2 |
| Transform System | TF2 |
| Build System | Colcon |
| Package Type | ament_cmake |

---

## Learning Roadmap

This project is part of my ROS 2 Robotics Software Engineering learning journey.

- [x] Phase 1 – Linux and Development Environment
- [x] Phase 2 – Python for Robotics
- [x] Phase 3 – ROS 2 Fundamentals
- [x] Phase 4 – URDF, Xacro and TF2
- [ ] Phase 5 – Gazebo Simulation
- [ ] Phase 6 – Robot Control
- [ ] Phase 7 – Navigation (Nav2)
- [ ] Phase 8 – SLAM
- [ ] Phase 9 – Sensors and Perception
- [ ] Phase 10 – MoveIt 2
- [ ] Phase 11 – Advanced ROS 2
- [ ] Phase 12 – Robotics Projects
- [ ] Phase 13 – Portfolio and Job Preparation

---

# Phase 4 Final Project – AswinBot

## Project Overview

AswinBot is a differential-drive mobile robot model created using URDF and Xacro.

The robot consists of a main chassis, two wheels, a camera and a LiDAR sensor.

The robot description is integrated with ROS 2's `robot_state_publisher`, `joint_state_publisher_gui` and RViz2 to visualize the robot and inspect its coordinate frames.

## Features

- Differential-drive robot structure.
- Five robot links connected through four joints.
- Two continuous wheel joints.
- Fixed camera and LiDAR mounting joints.
- Xacro properties and reusable robot components.
- Visual and collision geometry.
- Inertial properties for robot links.
- TF2 coordinate frame publishing.
- Interactive wheel joint movement.
- RViz2 robot visualization.
- Automatic RViz configuration loading through a launch file.
- TF tree generation and inspection.

---

## Robot Specifications

| Component | Description |
|---|---|
| `base_link` | Main robot chassis |
| `left_wheel_link` | Left wheel |
| `right_wheel_link` | Right wheel |
| `camera_link` | Camera mounted at the front |
| `lidar_link` | LiDAR mounted above the chassis |

### Joints

| Joint | Type | Parent | Child |
|---|---|---|---|
| `left_wheel_joint` | Continuous | base_link | left_wheel_link |
| `right_wheel_joint` | Continuous | base_link | right_wheel_link |
| Camera joint | Fixed | base_link | camera_link |
| LiDAR joint | Fixed | base_link | lidar_link |

---

## ROS 2 Architecture

| ROS 2 Component | Purpose |
|---|---|
| `robot_state_publisher` | Publishes robot link transforms |
| `joint_state_publisher_gui` | Provides interactive joint controls |
| `xacro` | Processes the robot description |
| `tf2` | Manages coordinate transforms |
| `rviz2` | Visualizes the robot model and TF frames |

### Coordinate Frame Structure

The robot has five coordinate frames:

```text
                  base_link
                /     |      \
               /      |       \
       camera_link  lidar_link  left_wheel_link
                               \
                                right_wheel_link
```

`base_link` is the root frame, and the other four frames are its children.

---

## Project Structure

```text
phase_04_urdf_xacro_tf2/
│
├── ros2_ws/
│   └── src/
│       └── my_robot_description/
│           ├── urdf/
│           ├── launch/
│           └── ...
│
└── final_project/
    ├── README.md
    │
    └── ros2_ws/
        └── src/
            └── aswinbot_description/
                │
                ├── CMakeLists.txt
                ├── package.xml
                │
                ├── urdf/
                │   ├── aswinbot.urdf.xacro
                │   └── aswinbot.urdf
                │
                ├── launch/
                │   └── display.launch.py
                │
                ├── rviz/
                │   └── aswinbot.rviz
                │
                ├── AswinBot.gv
                └── AswinBot.pdf
```

---

## Build Instructions

### 1. Source ROS 2 Humble

```bash
source /opt/ros/humble/setup.bash
```

### 2. Navigate to the final project workspace

```bash
cd ~/ros2-robotics-learning/phase_04_urdf_xacro_tf2/final_project/ros2_ws
```

### 3. Build the package

```bash
colcon build
```

### 4. Source the workspace

```bash
source install/setup.bash
```

---

## Running AswinBot

Launch the complete robot visualization:

```bash
ros2 launch aswinbot_description display.launch.py
```

The launch file starts:

1. `robot_state_publisher`
2. `joint_state_publisher_gui`
3. `rviz2`

RViz2 automatically loads the saved configuration from:

```text
aswinbot_description/rviz/aswinbot.rviz
```

---

## Robot Description Validation

Convert the Xacro file into URDF:

```bash
cd ~/ros2-robotics-learning/phase_04_urdf_xacro_tf2/final_project/ros2_ws/src/aswinbot_description

xacro urdf/aswinbot.urdf.xacro -o /tmp/aswinbot.urdf
```

Validate the generated URDF:

```bash
check_urdf /tmp/aswinbot.urdf
```

Expected result:

```text
robot name is: AswinBot
---------- Successfully Parsed XML ---------------
root Link: base_link has 4 child(ren)
```

---

## Testing and Verification

### 1. Check available ROS 2 topics

```bash
ros2 topic list
```

### 2. Inspect joint states

```bash
ros2 topic echo /joint_states
```

### 3. Inspect dynamic transforms

```bash
ros2 topic echo /tf
```

### 4. Inspect static transforms

```bash
ros2 topic echo /tf_static
```

### 5. Generate the TF tree

```bash
ros2 run tf2_tools view_frames
```

This generates:

- `frames.pdf`
- `frames.gv`

The generated TF tree can be opened using:

```bash
xdg-open frames.pdf
```

The project also includes the inspected TF tree as `AswinBot.pdf` and `AswinBot.gv`.

---

## Key Concepts Learned

Through this project, I gained practical experience with:

- Robot links and joints.
- URDF XML structure.
- Visual, collision and inertial properties.
- Fixed and continuous joints.
- Joint origins and rotation axes.
- Xacro properties and macros.
- Coordinate frames and TF trees.
- `robot_state_publisher`.
- `joint_state_publisher_gui`.
- RViz2 visualization.
- ROS 2 launch files.
- Package installation and build configuration.

---

## Future Improvements

- Integrate AswinBot with Gazebo simulation.
- Add a differential-drive controller.
- Integrate camera and LiDAR sensor plugins.
- Implement robot movement using velocity commands.
- Explore SLAM and autonomous navigation using Nav2.

---

## Author

**Aswin**

GitHub: [aswinmurugan-lab](https://github.com/aswinmurugan-lab)

Repository: [ros2-robotics-learning](https://github.com/aswinmurugan-lab/ros2-robotics-learning)

---

This project is part of my hands-on journey toward becoming a Robotics Software Engineer, with a focus on ROS 2, robot modeling, simulation, control and autonomous navigation.
