# import omni.ext
# import omni.ui as ui
# import omni.kit.commands
# from datetime import datetime as dt
# # from pxr import Sdf, Gf

# from omni.kit.widget.viewport import ViewportWidget

# # Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# # instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# # on_shutdown() is called.


# class MyExtension(omni.ext.IExt):
#     # ext_id is current extension id. It can be used with extension manager to query additional information, like where
#     # this extension is located on filesystem.

#     # c=1
#     #spawns
#     def on_click_cube(self):
#         omni.kit.commands.execute('CreatePrimWithDefaultXform',
#         prim_type ='Cube',
#         attributes = {'size': 100, 'extent': [(-50, -50, -50), (50, 50, 50)]})
#         print("clicked! And made a cube")

#     def on_click_sphere(self):
#         omni.kit.commands.execute('CreatePrimWithDefaultXform',
#         prim_type='Sphere',
#         attributes={'radius': 50, 'extent': [(-50, -50, -50), (50, 50, 50)]})

#     def on_click_cylinder(self):
#         omni.kit.commands.execute('CreatePrimWithDefaultXform',
#         prim_type='Cylinder',
#         attributes={'radius': 50, 'height': 100, 'extent': [(-50, -50, -50), (50, 50, 50)]})

#     def on_click_camera(self):
#         omni.kit.commands.execute(
#             'CreatePrimWithDefaultXform',
#             prim_type='Camera',
#             attributes={'focusDistance': 400, 'focalLength': 24})



#     #selections
#     def helper_selected(self):
#         context = self.helper_context()
#         stage = self.helper_stage()
#         prims = [stage.GetPrimAtPath(m) for m in context.get_selection().get_selected_prim_paths()]
#         return prims

#     def helper_selected_path(self):
#         context= self.helper_context()
#         prims=[m for m in context.get_selection().get_selected_prim_paths()]
#         return prims

#     #all
#     def helper_all_path(self):
#         context= self.helper_context()
#         # prims=[m for m in context.AllPrims()]
#         # print(dir(self.helper_stage()))
#         # print("HIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
#         prims=self.helper_stage().GetDefaultPrim().GetChildren()
#         # print(dir(self.helper_stage().GetDefaultPrim()))
#         return prims
        
#     #helpers
#     def helper_context(self):
#         context= omni.usd.get_context()
#         return context

#     def helper_stage(self):
#         context= self.helper_context()
#         stage=context.get_stage()
#         return stage

#     #others
#     def on_click_get(self):
#         for p in self.helper_selected():
#             strp=str(p)
#             print("GET THE PRIM:" + strp)

#     def on_click_dup(self):
#         duprim = self.helper_selected_path()
#         for p in duprim:
#             ct = dt.now()
#             newpath = str(p)+str(ct.year)+str(ct.month)+str(ct.day)+str(ct.hour)+str(ct.minute)+str(ct.second)+str(ct.microsecond)
#             omni.usd.duplicate_prim(self.helper_stage(), p, newpath, True)
       
# #camera switching
#     def switch_helper0(self):
#         self.viewport_api.camera_path = '/World/Camera'
#         print("0 trggered")

#     def switch_helper1(self):
#         #get stage
#         #get cpntext
#         # self.helper_selected()
#         self.viewport_api.camera_path = '/World/Camera_01'
#         print("1 trggered")

#     def switch_helper2(self):
#         self.viewport_api.camera_path = '/World/Camera_02'
#         print("2 trggered")

#     def helper_ret(self):
#         pass

#     def cam_loop(self):
#         print("in progress")
        
#         self.cams=[]
#         print(self.helper_all_path(),'HOLA')
#         for p in self.helper_all_path():
#             cam = "Camera"
#             print(self.helper_all_path())
#             if cam in p.GetPath():
#                 self.cams.append(p)

#     def default(self):
#         self.on_click_camera()
#         self.on_click_camera()
#         self.on_click_camera()
           
#     def on_click_view(self):
#         self.default()
#         self._window2 = ui.Window('Alt Viewport', width=480, height=270+20+30) # Add 20 for the title-bar
#         with self._window2.frame:
#             with ui.VStack():
#                 viewport_widget = ViewportWidget(resolution=(1280, 720))
#                 # Control of the ViewportTexture happens through the object held in the viewport_api property
#                 self.viewport_api = viewport_widget.viewport_api
#                 # We can reduce the resolution of the render easily
#                 self.viewport_api.resolution = (640, 360)
#                 self.viewport_api.camera_path = '/World/Camera'
#                 with ui.CollapsableFrame("Cams"):                      
#                     with ui.VStack(height=0):
#                         ui.Label("Get Avaible Cameras", height=30, width=426)
#                         ui.Button("Camera0", height=30, width=426, clicked_fn=lambda: self.switch_helper0())
#                         ui.Button("Camera_01", height=30, width=426, clicked_fn=lambda: self.switch_helper1())
#                         ui.Button("Camera_02", height=30, width=426, clicked_fn=lambda: self.switch_helper2())

#                         print("HIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
#                         self.cam_loop()
#                         print(self.cams)
#                         for c in self.cams:
#                             strc = c.strip(">)").split("/")[-1]
#                             #2022-06-20 21:46:00  [Info] [omni.kit.app.impl] [py stdout]: GET THE PRIM:Usd.Prim(</World/Camera_07>)
#                             # strc=c[c.index("Cam"):c.index(">")]
#                             #print(strc)
#                             ui.Button(strc, height = 30, width = 426, clicked_fn=lambda: self.helper_ret())
#                             # ui.Label(strc, height = 30, width = 300)



#     def on_startup(self, ext_id):
#         print("[cornell.warm.ext] MyExtension startup")
#         print("HOLA")
#         self._window = ui.Window("Warm Up", width=500, height=720+20)
#         with self._window.frame:
#             with ui.VStack():
#                 ui.Label("Menu", height=30, width=500, alignment=ui.Alignment.CENTER)
#                 with ui.CollapsableFrame("Spawns"):
#                     with ui.VStack(height=0):
#                         ui.Button("Spawn Cube", height=30, width=426, clicked_fn=lambda: self.on_click_cube())
#                         ui.Button("Spawn Sphere", height=30, width=426, clicked_fn=lambda: self.on_click_sphere())
#                         ui.Button("Spawn Cylinder", height=30, width=426, clicked_fn=lambda: self.on_click_cylinder())
#                         ui.Button("Spawn Camera", height=30, width=426, clicked_fn=lambda: self.on_click_camera())
#                         ui.Button("Spawn Viewport", height=30, width=426, clicked_fn=lambda: self.on_click_view())
#                 with ui.CollapsableFrame("Others"):                       
#                     with ui.VStack(height=0):
#                         ui.Button("Get Selected Prims in Console", height=30, width=426, 
#                                   clicked_fn=lambda: self.on_click_get())
#                         ui.Button("Duplicate Selected Prims", height=30, width=426, 
#                                   clicked_fn=lambda: self.on_click_dup())

#         # viewport stuff
       
        

#         # We can also switch to a different camera if we know the path to one that exists
#         # viewport_api.camera_path = '/World/Camera_01'

#         # # And inspect 
#         # print(viewport_api.projection)
#         # print(viewport_api.transform)
       
#         # self.helper_all_path()
        

#     def on_shutdown(self):
#         # Don't forget to destroy the objects when done with them
#         # self.viewport_widget.destroy()
#         # self._window2.destroy()
#         # self._window2 = None
#         # self.viewport_widget = None

#         self.viewport_widget.destroy()
#         self.viewport_window2.destroy()
#         # viewport_window2, viewport_widget = None, None
#         print("[cornell.warm.ext] MyExtension shutdown")


# # class Cams(MyExtension):
#     # def get_cam(self):
#     #     print("in progress")
#     #     prims=self.helper_selected_path()
#     #     cams=[]
#     #         for p in prims:
#     #             if p.find("Camera")!=-1:
#     #                 cams.append(p)
             

#     # #in progress get cam stuff    
#     #     self._window3 = ui.Window("Avaliable Cams", width=300, height=500)
#     #     with self._window3.frame:
#     #         with ui.VStack():
#     #             for c in cams:
#     #                 strc=str(c)
#     #                 #print(strc)
#     #                 # ui.Button(strc, height = 30, width = 300, clicked_fn=lambda: self.helper_ret())
#     #                 ui.Label(strc, height = 30, width = 300)

    
    
#     # def helper_ret(self):
#     #     print ("in progress")


#     #in progress cams (on start up?)
#         # ui.Button("Get Avaible Cameras", height = 30, width = 426, clicked_fn=lambda: self.get_cam())

#         #in progress cams
#         #viewport_api.camera_path = '/World/'+self.helper_ret()
       

      

# # Don't forget to destroy the objects when done with them
# # viewport_widget.destroy()
# # viewport_window.destroy()
# # viewport_window, viewport_widget = None, None
    
    

    


