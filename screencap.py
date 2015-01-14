import gtk.gdk
import math

def screencap( path, name,size_multiplier=1.0, e=0 ):
	w = gtk.gdk.get_default_root_window()
	sz = w.get_size()
	if(e): print "The size of the window is %d x %d" % sz
	pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1] )
	pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
	if (pb != None):
		save_to = path+"/"+name+".png"
		if(size_multiplier<1.0):
			width = int(math.floor(sz[0]*size_multiplier))
        		height = int(math.floor(sz[1]*size_multiplier))
			#npb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,width,height )
			npb = pb.scale_simple(width,height,gtk.gdk.INTERP_BILINEAR)
			npb.save(save_to,"png")
		else:
    			pb.save(save_to,"png")
    		if(e): print "Screenshot saved to:"+save_to
	else:
    		if(e): print "Unable to get the screenshot."

