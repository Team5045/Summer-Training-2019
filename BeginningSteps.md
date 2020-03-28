## FRC Lab View Setup
download [here](http://www.ni.com/download/first-robotics-software-2017/7904/en/)

tutorial for labview setup [here](https://wpilib.screenstepslive.com/s/currentCS/m/java/l/1027504-installing-the-frc-update-suite-all-languages)

## setting up roboRIO (only needs to be done once per roborio every year to get newest firmware)
imaging new firmware steps [here](https://www.ni.com/en-us/innovations/white-papers/15/imaging-the-roborio-and-common-troubleshooting-techniques.html)

you must download lab view before imaging roborio

labview 2020 download [here](http://www.ni.com/en-us/support/downloads/drivers/download/packaged.frc-game-tools.333285.html)

installing RobotPy on roborio [here](https://robotpy.readthedocs.io/en/stable/install/robot.html#install-robotpy)

## Radio Setup
programming radio [here](https://docs.wpilib.org/en/latest/docs/getting-started/getting-started-frc-control-system/radio-programming.html)

## Electronics Board wiring
[wpilib link](https://wpilib.screenstepslive.com/s/currentCS/m/kop/l/1030226-wiring-the-frc-control-system)

[Best practices for wiring](https://wpilib.screenstepslive.com/s/currentCS/m/cs_hardware/l/826661-wiring-best-practices)

status lights [reference](https://wpilib.screenstepslive.com/s/currentCS/m/cs_hardware/l/144972-status-light-quick-reference)

## Programming guide
read the docs [here](https://robotpy.readthedocs.io/en/stable/getting_started.html)

## Pneumatics wiring
plumbing overview on page 14 [here](https://firstfrc.blob.core.windows.net/frc2017/pneumatics-manual.pdf)

[wiring pneumatics]([wiring pneumatics])

## Mechanical Reference Center
most links dont work but some are pretty good [here](https://first.wpi.edu/FRC/frc-mechanical.html)

## Updating pyfrc on your computer
open terminal and run this command: pip3 install pyfrc, referecne pyfrc docs for 2020 version
MAKE SURE YOU HAVE 64 BIT PYTHON OR SOME LIBRARIES WILL NOT WORK

## Starting to Program
make sure you have updated the roborio and the talon srx firmware

to deploy code to the robot use py -3 robot.py deploy --skip-tests

use "ctrl ~" to open powershell in vscode

to open the simulator use python .\robot.py sim

## Starting to send code 
make sure that you have updated both labview on your computer and the roborio image
