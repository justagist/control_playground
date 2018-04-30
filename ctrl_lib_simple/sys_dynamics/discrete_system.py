import utils.utilfuncs as utilfuncs
from dynamics import Dynamics
import numpy as np

class DiscreteSystem(Dynamics):

    def __init__(self, **kwargs):

        # ----- x(k+1) = Ax(k) + Bu

        Dynamics.__init__(self,**kwargs)

    def check_system_stability(self, A = None):

        if A is None:
            A = self.Amat

        self._sanity_check()

        eigvals, _ = utilfuncs.get_eigen(A, eigs_as_mat = False)

        for i in eigvals:
            if isinstance(i,complex):
                if abs(i) > 1:
                    return False
            else:
                if i > 1:
                    return False

        return True

    def state_at(self, timestep):
        '''
            Get state at time t for discrete system    
        # ----- xk = A^(k).x0

        '''
        return np.dot(np.linalg.matrix_power(self.Amat, timestep), self.initial_state)



## ======================== ##
#         TEST CODE          #
## ======================== ##
if __name__ == '__main__':
    
    a = DiscreteSystem(A = np.array([[0,1],[-1,0.01]]), x = (1,2), B = np.array([[0],[1]]))

    # print a.Amat
    # print a.Bmat
    # print a.state

    # print a.get_controllability_matrix()
    # eigvals, _ = utilfuncs.get_eigen(np.array([[0,1],[-1,12]]), eigs_as_mat = False)

    # print eigvals

    # print a.check_controllability()

    # print a.check_system_stability()

    print a.state_at(20)