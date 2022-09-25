import sys

class Solution:
    def generateParenthesis(self, n: int):# -> List[str]:
        output = []
        
        # only add ) if ( is open/valid
        
        def helper(opened, closed, p):
            if len(p) == n * 2:
                output.append(p)
                return
            #checks if the opened/left curl is less than n specificed
            if opened < n:
                helper(opened + 1, closed, p + '(')
                
            # checks if less closes curls than opened meaning we can add )    
            if closed < opened:
                helper(opened, closed + 1, p + ')')
        
        helper(0,0,'')
        return output


    generateParenthesis(5,5)
    

"""
n = 2
                                    (0, 0, '')
								 	    |	
									(1, 0, '(')  
								   /           \
							(2, 0, '((')      (1, 1, '()')
							   /                 \
						(2, 1, '(()')           (2, 1, '()(')
						   /                       \
					(2, 2, '(())')                (2, 2, '()()')
						      |	                             |
					output.append('(())')             output.append('()()')
"""