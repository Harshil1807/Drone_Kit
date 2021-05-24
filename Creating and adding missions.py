# Connect to the Vehicle (in this case a simulated vehicle at 127.0.0.1:14550)
vehicle = connect('127.0.0.1:14550', wait_ready=True)

# Get the set of commands from the vehicle
cmds = vehicle.commands
cmds.download()
cmds.wait_ready()

# Create and add commands
cmd1=Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, 0, 10)
cmd2=Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, 10, 10, 10)
cmds.add(cmd1)
cmds.add(cmd2)
cmds.upload() # Send commands