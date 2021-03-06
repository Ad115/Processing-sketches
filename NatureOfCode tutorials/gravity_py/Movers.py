from Mover import Mover

class Movers(object):
    
    # CONSTRUCTOR...................................
    def __init__(self, n_movers, maxMass, maxVelocity):
        self.n_movers = n_movers
        self.movers = [ Mover(maxMass, maxVelocity) for i in range(n_movers) ]
            
    #................................................
    def draw(self):
        for mover in self.movers:
            mover.draw()
            
    #................................................
    def update(self):
        # Feel attraction
        for attracted in self.movers:
            for attractor in self.movers:
                if attractor != attracted:
                    attracted.applyForce( attractor.attractMover(attracted) )
        self.move()
        
    #................................................
    def move(self):
        for mover in self.movers:
            mover.move()
        
    #................................................
    def randomizePosition(self, width, height):
        for mover in self.movers:
            mover.randomizePosition(width, height)
            
    #................................................
    def temperature(self):
        # < v^2 >
        temperature = 0.0
        for mover in self.movers:
            temperature = temperature + mover.velocity.magSq()
        temperature = temperature/len(self.movers)
        return temperature
        
    #................................................
    def energy(self):
        # < 1/m * v^2 >
        energy = 0.0
        for mover in self.movers:
            energy = energy + mover.velocity.magSq()/mover.mass
        energy = energy/len(self.movers)
        return energy
        