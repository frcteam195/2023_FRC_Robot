from os.path import dirname, abspath
import sys

descriptionText='This is the main robot project. All nodes used in the robot should be defined in ros_projects.txt and all third party libraries should be defined in third_party_projects.txt. \
In order to run this project, you need to have [ros_dev](https://github.com/frcteam195/ros_dev) at the same directory level as this repository. Then you can run `./ros_dev/mkrobot.sh clone` to pull all the node and third party libraries \
and then run `./ros_dev/mkrobot.sh build` to build all the nodes. To deploy to the ROS robot, run `./ros_dev/mkrobot.sh deploy`.'
if len(sys.argv) > 1:
    descriptionText=sys.argv[1]

scriptParentDirName = dirname(abspath(__file__)).split('/').pop()

robotProjects = []
thirdPartyProjects = []
with open('ros_projects.txt', 'r') as f:
    robotProjects = f.readlines()

with open('third_party_projects.txt', 'r') as f:
    thirdPartyProjects = f.readlines()

with open('README.md', 'w') as f:
    f.write(f'# {scriptParentDirName}\n')
    f.write(f'[![x86 Build Status](https://github.com/frcteam195/{scriptParentDirName}/actions/workflows/main.yml/badge.svg)](https://github.com/frcteam195/{scriptParentDirName}/actions/workflows/main.yml)\n\n')
    f.write(f'{descriptionText}\n\n')
    f.write('\n---\n\n')

    f.write('### Robot Nodes\n\n')
    for line in sorted(robotProjects):
        if '#' in line:
            continue
        node_name = line.split('/')[1]
        node_name = node_name.split('.')[0]
        line = line.replace('git@github.com:', 'https://github.com/')
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        f.write(f'[{node_name}]({line})\n\n') 

    f.write('\n\n---\n\n')

    f.write('### Third Party Projects\n\n')
    for line in sorted(thirdPartyProjects):
        if '#' in line:
            continue
        node_name = line.split('/')[1]
        node_name = node_name.split('.')[0]
        line = line.replace('git@github.com:', 'https://github.com/')
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        f.write(f'[{node_name}]({line})\n\n') 

