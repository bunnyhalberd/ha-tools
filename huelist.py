
import pyhue


bridge = pyhue.Bridge('192.168.7.39', 'GA9vM13aYHH3HZ5QkWpTWzdwTmTUwP9jmBUYWWD6')

#for light in bridge.lights:
#    print(light.id)
#    print(light.name)
#    print(light.xy)
#    print(light.swversion)

lights = bridge.lights

for group in bridge.groups:
    print(group.name)
    for light in group.lights:
        print(' %s' % lights[int(light)-1].name)
    print('')

