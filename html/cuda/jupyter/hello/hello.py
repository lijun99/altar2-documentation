# import the altar module
import altar

# create an application based on altar.application
class HelloApp(altar.application, family='altar.applications.hello'):
    """
    A specialized AlTar application to say hello 
    """
    
    # user configurable parameters/components
    who = altar.properties.str(default='world')
    who.doc = "the person to say hello to"
    
    times = altar.properties.int(default=1)
    times.validators = altar.constraints.isPositive()
    times.doc = "how many times you want to say hello"
    
    # define methods
    def main(self):
        """
        The main method
        """
        for i in range(self.times):
            print(f"Hello {self.who}!")
        # all done
        return

# bootstrap
if __name__ == "__main__":
    # build an instance of the default app
    app = HelloApp(name="hello")
    # invoke the main entry point
    status = app.main()
    # share
    raise SystemExit(status)
