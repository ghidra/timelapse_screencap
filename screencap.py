import gtk.gdk
import math

def screencap( path, name, e=0 ):
	w = gtk.gdk.get_default_root_window()
	sz = w.get_size()
	if(e): print "The size of the window is %d x %d" % sz
	pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1] )
	pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
	if (pb != None):
		save_to = path+"/"+name+".png"
    		pb.save(save_to,"png")
    		if(e): print "Screenshot saved to:"+save_to
	else:
    		if(e): print "Unable to get the screenshot."

