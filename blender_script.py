import json
import bpy
import itertools

data = json.load(open('data.json'))
j = json.load(open('out.json'))
i = 0
verts = []
faces = []
for ons,c in j.items():
    name = ons
    try:
        name, height = data[ons]
    except KeyError:
        height = 0
    print(height)
    for co in c:
        first = i
        topface = []
        bottomface = []
        for [x,y] in co:
            verts.append([x,y,0])
            verts.append([x,y,height/2])
            bottomface.append(i)
            topface.append(i+1)
            if i>first:
                faces.append([i-2,i-1,i+1,i])
            i+=2
        faces.append(topface)
        faces.append(bottomface)
#print(verts,faces)
name = 'all'
# Create mesh and object
origin = (0,0,0)
me = bpy.data.meshes.new(name+'Mesh')
ob = bpy.data.objects.new(name, me)
ob.location = origin
ob.show_name = True
# Link object to scene
bpy.context.scene.objects.link(ob)
 
# Create mesh from given verts, edges, faces. Either edges or
# faces should be [], or you ask for problems
me.from_pydata(verts, [], faces)
 
# Update mesh with new data
me.update(calc_edges=True)