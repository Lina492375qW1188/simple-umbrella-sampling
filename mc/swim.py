import numpy as np

class double_well:
    
    def __init__(self):
        """
        param['B'] = B: height of barrier;
        param['x0'] = x0: minima of double well.
        """
        self.param={}
        
    def act(self, x):
        """
        defining an act function taking simulation variable as input argument.
        x: array-like.
        """
        dx = x**2 - self.param['x0']
        return self.param['B']*dx**2
    
    def deriv(self, x):
        """
        derivative.
        """
        return 4 * self.param['B'] * x**3 - 4 * self.param['B'] * self.param['x0'] * x


class harmonic:
    
    def __init__(self):
        self.param={}
        
    def act(self, x):
        """
        defining an act function taking simulation variable as input argument.
        x: array-like.
        """
        dx = x - self.param['x0']
        return self.param['K'] * dx**2
    
    def deriv(self, x):
        """
        derivative.
        """
        return 2 * self.param['K'] * (x - self.param['x0'])

    
        
class simple_mc:
    
    def __init__(self, seed=0):
        self._rng = np.random.default_rng(seed)
        self.external_pe = []
        self.counter = [0, 0]
        
    def set_param(self, movesize, kT=1.0):
        self.movesize = movesize
        self.kT = kT
        
    def set_init_x(self, init_x):
        self.init_x = init_x
        self.i = 0
        self.traj = [[self.i, self.init_x]]
    
    def run(self, nsteps):
        """
        nsteps: number of steps.
        """
        for step in range(int(nsteps)):
            
            _, current_x = self.traj[-1]
            initi_pe = sum([pe.act(self.init_x) for pe in self.external_pe])

            # trial move
            trial_x = current_x + (2 * self._rng.random() - 1) * self.movesize
            trial_pe = sum([pe.act(trial_x) for pe in self.external_pe])

            d_pe = trial_pe - initi_pe

            prob = np.exp( -d_pe / self.kT )
            if self._rng.random() < prob:
                self.traj.append( [self.i, trial_x] )
                self.counter[0] += 1
                self.i += 1
            else:
                self.counter[1] += 1
        
        
